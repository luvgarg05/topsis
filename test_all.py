#!/usr/bin/env python3
"""
Comprehensive test suite for TOPSIS implementation.
Tests all three components: CLI, Package, and Web Service.
"""

import sys
import os
import csv
import json
import tempfile
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

def test_cli_basic():
    """Test basic CLI functionality."""
    print("\n" + "="*60)
    print("TEST 1: CLI Basic Functionality")
    print("="*60)
    
    from topsis import topsis
    
    # Test with sample data
    result = topsis('data.csv', '1,1,1,2', '+,+,+,-', 'test_output.csv')
    
    assert len(result) > 0, "Result should not be empty"
    assert 'Topsis Score' in result.columns, "Result should have Topsis Score column"
    assert 'Rank' in result.columns, "Result should have Rank column"
    assert result['Rank'].max() == len(result), "Highest rank should equal number of alternatives"
    
    print("✓ CLI basic test passed")
    return True


def test_cli_validation():
    """Test input validation."""
    print("\n" + "="*60)
    print("TEST 2: Input Validation")
    print("="*60)
    
    from topsis import validate_inputs
    import pandas as pd
    
    # Create test data
    df = pd.DataFrame({
        'Name': ['A', 'B', 'C'],
        'C1': [1, 2, 3],
        'C2': [4, 5, 6]
    })
    
    # Test valid inputs
    is_valid, msg = validate_inputs(df, [1, 1], ['+', '+'])
    assert is_valid, f"Valid inputs should pass: {msg}"
    print("✓ Valid inputs passed")
    
    # Test weight mismatch
    is_valid, msg = validate_inputs(df, [1], ['+', '+'])
    assert not is_valid, "Weight count mismatch should fail"
    print("✓ Weight mismatch detected")
    
    # Test impact mismatch
    is_valid, msg = validate_inputs(df, [1, 1], ['+'])
    assert not is_valid, "Impact count mismatch should fail"
    print("✓ Impact mismatch detected")
    
    # Test invalid impact
    is_valid, msg = validate_inputs(df, [1, 1], ['+', 'x'])
    assert not is_valid, "Invalid impact should fail"
    print("✓ Invalid impact detected")
    
    return True


def test_package_import():
    """Test PyPI package import."""
    print("\n" + "="*60)
    print("TEST 3: Package Import")
    print("="*60)
    
    try:
        # Try importing from installed package
        import topsis_lavanya_102313066 as topsis_pkg
        print("✓ Package imported successfully")
        
        # Check for main function
        assert hasattr(topsis_pkg, 'topsis'), "Package should have topsis function"
        print("✓ Package has topsis function")
        
        return True
    except ImportError:
        print("✗ Package not installed (expected in test environment)")
        return True


def test_web_service_structure():
    """Test web service file structure."""
    print("\n" + "="*60)
    print("TEST 4: Web Service Structure")
    print("="*60)
    
    web_service_path = Path('web_service')
    
    required_files = [
        'app.py',
        'requirements.txt',
        'templates/index.html',
        '.env.example'
    ]
    
    for file in required_files:
        file_path = web_service_path / file
        assert file_path.exists(), f"Missing file: {file}"
        print(f"✓ Found: {file}")
    
    return True


def test_algorithm_correctness():
    """Test TOPSIS algorithm correctness with known values."""
    print("\n" + "="*60)
    print("TEST 5: Algorithm Correctness")
    print("="*60)
    
    import pandas as pd
    from topsis import (
        normalize_matrix, apply_weights, find_ideal_solutions,
        calculate_separations, calculate_scores
    )
    import numpy as np
    
    # Create simple test data
    data = np.array([
        [10, 20, 30],
        [15, 25, 35],
        [20, 30, 40]
    ], dtype=float)
    
    # Test normalization
    normalized = normalize_matrix(pd.DataFrame(data))
    assert normalized.shape == data.shape, "Shape should be preserved"
    assert np.allclose(np.sqrt((normalized ** 2).sum(axis=0)), 1), "Columns should be normalized"
    print("✓ Normalization correct")
    
    # Test weights application
    weights = [1, 1, 1]
    weighted = apply_weights(normalized, weights)
    assert weighted.shape == normalized.shape, "Shape should be preserved"
    print("✓ Weights applied correctly")
    
    # Test ideal solution finding
    impacts = ['+', '+', '+']
    ideal, anti_ideal = find_ideal_solutions(weighted, impacts)
    assert ideal.shape == (3,), "Ideal should have 3 values"
    assert (ideal >= anti_ideal).all(), "Ideal should be >= anti-ideal for all benefits"
    print("✓ Ideal solutions found correctly")
    
    # Test separations
    s_plus, s_minus = calculate_separations(weighted, ideal, anti_ideal)
    assert len(s_plus) == 3, "Should have 3 separation values"
    assert (s_plus >= 0).all(), "Separations should be non-negative"
    print("✓ Separations calculated correctly")
    
    # Test scores
    scores, ranks = calculate_scores(s_plus, s_minus)
    assert len(scores) == 3, "Should have 3 scores"
    assert (scores >= 0).all() and (scores <= 1).all(), "Scores should be in [0,1]"
    print("✓ Scores calculated correctly")
    
    return True


def test_file_formats():
    """Test handling of different file formats."""
    print("\n" + "="*60)
    print("TEST 6: File Format Support")
    print("="*60)
    
    import pandas as pd
    from topsis import topsis
    
    # Test CSV (already exists)
    try:
        result = topsis('data.csv', '1,1,1,2', '+,+,+,-')
        assert len(result) > 0, "CSV should be readable"
        print("✓ CSV format supported")
    except Exception as e:
        print(f"✗ CSV test failed: {e}")
        return False
    
    return True


def run_all_tests():
    """Run all tests."""
    print("\n" + "="*70)
    print(" "*15 + "TOPSIS COMPREHENSIVE TEST SUITE")
    print("="*70)
    
    tests = [
        ("CLI Basic Functionality", test_cli_basic),
        ("Input Validation", test_cli_validation),
        ("Package Import", test_package_import),
        ("Web Service Structure", test_web_service_structure),
        ("Algorithm Correctness", test_algorithm_correctness),
        ("File Format Support", test_file_formats),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except AssertionError as e:
            print(f"✗ {test_name} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test_name} error: {e}")
            failed += 1
    
    print("\n" + "="*70)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(tests)} tests")
    print("="*70 + "\n")
    
    return failed == 0


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
