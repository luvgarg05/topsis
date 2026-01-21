#!/usr/bin/env python3
"""
TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) Implementation
Author: Lavanya Garg (Roll: 102313066)
Institution: Thapar Institute of Engineering and Technology
"""

import sys
import pandas as pd
import numpy as np
from pathlib import Path


def validate_inputs(df, weights, impacts):
    """
    Validate input parameters for TOPSIS analysis.
    
    Args:
        df (pd.DataFrame): Input data with first column as identifiers
        weights (list): List of weights
        impacts (list): List of impacts (+ or -)
    
    Returns:
        tuple: (is_valid, error_message)
    """
    # Check if DataFrame has at least 3 columns (requirement: three or more columns)
    if len(df.columns) < 3:
        return False, "Error: Input data must contain three or more columns"
    
    # Check if first column contains non-numeric identifiers
    try:
        pd.to_numeric(df.iloc[:, 0])
        return False, "Error: First column must contain non-numeric identifiers"
    except (ValueError, TypeError):
        pass  # Good - first column is non-numeric
    
    # Get number of criteria (excluding first column)
    num_criteria = len(df.columns) - 1
    
    # Validate weights
    if len(weights) != num_criteria:
        return False, f"Error: Number of weights ({len(weights)}) must match number of criteria ({num_criteria})"
    
    if any(w <= 0 for w in weights):
        return False, "Error: All weights must be positive"
    
    # Validate impacts
    if len(impacts) != num_criteria:
        return False, f"Error: Number of impacts ({len(impacts)}) must match number of criteria ({num_criteria})"
    
    if not all(impact in ['+', '-'] for impact in impacts):
        return False, "Error: Impacts must be '+' (benefit) or '-' (cost)"
    
    # Check all criteria columns are numeric
    criteria_data = df.iloc[:, 1:]
    try:
        numeric_df = criteria_data.apply(pd.to_numeric, errors='raise')
    except (ValueError, TypeError):
        return False, "Error: All criteria columns must contain numeric values"
    
    if (numeric_df <= 0).any().any():
        return False, "Error: All criteria values must be positive"
    
    return True, "OK"


def normalize_matrix(df):
    """
    Step 1: Normalize the criteria matrix using vector normalization.
    
    Formula: n_ij = a_ij / sqrt(sum(a_ij^2))
    
    Args:
        df (pd.DataFrame): Criteria matrix (excluding identifiers)
    
    Returns:
        np.ndarray: Normalized matrix
    """
    matrix = df.values.astype(float)
    # Calculate L2 norm for each column
    norms = np.sqrt((matrix ** 2).sum(axis=0))
    normalized = matrix / norms
    return normalized


def apply_weights(normalized_matrix, weights):
    """
    Step 2: Apply weights to the normalized matrix.
    
    Formula: v_ij = w_j * n_ij
    
    Args:
        normalized_matrix (np.ndarray): Normalized matrix
        weights (list): Weights for each criterion
    
    Returns:
        np.ndarray: Weighted normalized matrix
    """
    return normalized_matrix * np.array(weights)


def find_ideal_solutions(weighted_matrix, impacts):
    """
    Step 3: Find ideal and anti-ideal solutions.
    
    Ideal solution (A+): Maximum for benefit (+), Minimum for cost (-)
    Anti-ideal solution (A-): Minimum for benefit (+), Maximum for cost (-)
    
    Args:
        weighted_matrix (np.ndarray): Weighted normalized matrix
        impacts (list): List of impacts (+ or -)
    
    Returns:
        tuple: (ideal_solution, anti_ideal_solution)
    """
    ideal = np.zeros(weighted_matrix.shape[1])
    anti_ideal = np.zeros(weighted_matrix.shape[1])
    
    for j in range(weighted_matrix.shape[1]):
        if impacts[j] == '+':
            ideal[j] = weighted_matrix[:, j].max()
            anti_ideal[j] = weighted_matrix[:, j].min()
        else:  # '-'
            ideal[j] = weighted_matrix[:, j].min()
            anti_ideal[j] = weighted_matrix[:, j].max()
    
    return ideal, anti_ideal


def calculate_separations(weighted_matrix, ideal, anti_ideal):
    """
    Step 4: Calculate separation measures.
    
    S+ (distance to ideal): sqrt(sum((v_ij - ideal_j)^2))
    S- (distance to anti-ideal): sqrt(sum((v_ij - anti_ideal_j)^2))
    
    Args:
        weighted_matrix (np.ndarray): Weighted normalized matrix
        ideal (np.ndarray): Ideal solution
        anti_ideal (np.ndarray): Anti-ideal solution
    
    Returns:
        tuple: (s_plus, s_minus)
    """
    s_plus = np.sqrt(((weighted_matrix - ideal) ** 2).sum(axis=1))
    s_minus = np.sqrt(((weighted_matrix - anti_ideal) ** 2).sum(axis=1))
    return s_plus, s_minus


def calculate_scores(s_plus, s_minus):
    """
    Step 5: Calculate TOPSIS scores and ranks.
    
    Score: C_i = S- / (S+ + S-)  (Range: 0 to 1)
    
    Args:
        s_plus (np.ndarray): Separation from ideal solution
        s_minus (np.ndarray): Separation from anti-ideal solution
    
    Returns:
        tuple: (scores, ranks)
    """
    # Avoid division by zero
    with np.errstate(divide='ignore', invalid='ignore'):
        scores = np.where(s_plus + s_minus != 0, s_minus / (s_plus + s_minus), 0)
    
    # Calculate ranks (higher score = better = rank 1)
    ranks = pd.Series(scores).rank(method='min', ascending=False).astype(int).values
    
    return scores, ranks


def topsis(input_file, weights, impacts, output_file=None):
    """
    Execute complete TOPSIS analysis.
    
    Args:
        input_file (str): Path to input CSV file
        weights (list or str): List of weights or comma-separated string
        impacts (list or str): List of impacts or comma-separated string
        output_file (str): Path to output file (optional)
    
    Returns:
        pd.DataFrame: Results with original data + score + rank
    """
    # Parse inputs if strings
    if isinstance(weights, str):
        weights = list(map(float, weights.split(',')))
    if isinstance(impacts, str):
        impacts = [i.strip() for i in impacts.split(',')]
    
    # Read input file
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    # Validate inputs
    is_valid, message = validate_inputs(df, weights, impacts)
    if not is_valid:
        print(message)
        sys.exit(1)
    
    # Extract criteria data
    identifiers = df.iloc[:, 0]
    criteria = df.iloc[:, 1:]
    
    # TOPSIS Calculation
    # Step 1: Normalize
    normalized = normalize_matrix(criteria)
    
    # Step 2: Apply weights
    weighted = apply_weights(normalized, weights)
    
    # Step 3: Find ideal solutions
    ideal, anti_ideal = find_ideal_solutions(weighted, impacts)
    
    # Step 4: Calculate separations
    s_plus, s_minus = calculate_separations(weighted, ideal, anti_ideal)
    
    # Step 5: Calculate scores and ranks
    scores, ranks = calculate_scores(s_plus, s_minus)
    
    # Create result DataFrame
    result_df = df.copy()
    result_df['Topsis Score'] = scores
    result_df['Rank'] = ranks
    
    # Sort by rank
    result_df = result_df.sort_values('Rank')
    
    # Save output if specified
    if output_file:
        result_df.to_csv(output_file, index=False)
        print(f"Results saved to '{output_file}'")
    
    return result_df


def main():
    """Command-line interface for TOPSIS."""
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
        print("\nExample:")
        print("  python topsis.py data.csv \"1,1,1,2\" \"+,+,-,+\" output-result.csv")
        print("\nParameters:")
        print("  InputDataFile: CSV file with first column as identifiers")
        print("  Weights: Comma-separated positive numbers (e.g., \"1,1,1,2\")")
        print("  Impacts: Comma-separated + or - (e.g., \"+,+,-,+\")")
        print("  OutputResultFileName: Output file path (required)")
        sys.exit(1)
    
    input_file = sys.argv[1]
    weights_str = sys.argv[2]
    impacts_str = sys.argv[3]
    output_file = sys.argv[4]
    
    # Execute TOPSIS
    result = topsis(input_file, weights_str, impacts_str, output_file)
    print("\n" + "="*60)
    print("TOPSIS ANALYSIS RESULTS")
    print("="*60)
    print(result.to_string(index=False))
    print("="*60)


if __name__ == '__main__':
    main()
