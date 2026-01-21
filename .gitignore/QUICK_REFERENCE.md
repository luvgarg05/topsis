# TOPSIS - Quick Reference Guide

## Command Syntax

```bash
python topsis.py <input_file> <weights> <impacts> [output_file]
```

## Quick Examples

### Example 1: Mobile Phone Selection
```bash
python topsis.py data.csv 1,1,1,2 +,+,+,-
```

### Example 2: Laptop Comparison
```bash
python topsis.py laptops.csv 2,1,1.5,1 +,-,+,+
```

### Example 3: Employee Evaluation
```bash
python topsis.py employees.csv 1,1,1,2 +,+,+,- results_employees.csv
```

---

## Parameter Guide

| Parameter | Type | Example | Notes |
|-----------|------|---------|-------|
| input_file | string | data.csv | CSV file path |
| weights | string | 1,2,3,2 | Comma-separated numbers |
| impacts | string | +,+,-,+ | + or - for each criterion |
| output_file | string | results.csv | Optional, defaults to output.csv |

---

## Input File Format

### CSV Format
```csv
Name,Criterion1,Criterion2,Criterion3
Option1,10,20,30
Option2,15,25,35
Option3,20,30,40
```

### Requirements
- First column: Non-numeric identifiers
- Other columns: Numeric values only
- All values must be positive
- No missing data

---

## Common Parameter Sets

### Benefit Criteria (Higher is Better)
```
Weights: 1,1,1
Impacts: +,+,+
```

### Mixed Criteria (Some Benefits, Some Costs)
```
Weights: 1,1,1,1
Impacts: +,+,-,+
```

### Weighted Criteria (Different Importance)
```
Weights: 2,1,3
Impacts: +,+,+
```

---

## Output Format

| Column | Description |
|--------|-------------|
| Name | Original alternative name |
| Criterion1..N | Original criteria values |
| Topsis Score | Score between 0-1 (higher better) |
| Rank | Rank (1 = best) |

---

## Using Python API

### Basic Usage
```python
from topsis_lavanya_102313066 import topsis

result = topsis('data.csv', '1,1,1,2', '+,+,+,-')
print(result)
```

### With Output File
```python
result = topsis('data.csv', '1,1,1,2', '+,+,+,-', 'output.csv')
```

### With List Parameters
```python
weights = [1, 1, 1, 2]
impacts = ['+', '+', '+', '-']
result = topsis('data.csv', weights, impacts)
```

---

## Web Service Quick Start

### Setup
```bash
cd web_service
pip install -r requirements.txt
python app.py
```

### Access
Open browser: `http://localhost:5000`

### Upload File
1. Upload CSV/Excel/JSON file
2. Enter email address
3. Set weights and impacts
4. Click Analyze

---

## Common Errors

### Error: "File not found"
```
Solution: Use correct file path or absolute path
python topsis.py /full/path/to/data.csv 1,1,1 +,+,+
```

### Error: "Number of weights (2) does not match criteria (3)"
```
Solution: Ensure weights count matches criteria count
python topsis.py data.csv 1,1,1 +,+,+  # 3 weights, 3 impacts
```

### Error: "All weights must be positive"
```
Solution: Use positive numbers only
python topsis.py data.csv 1,2,3 +,+,+  # Good
python topsis.py data.csv -1,2,3 +,+,+  # Bad
```

### Error: "First column must contain non-numeric identifiers"
```
Solution: Make sure first column has text, not numbers
Good: Name,Price,Quality
Bad: 1,2,3
```

---

## Tips and Tricks

### Tip 1: Relative Weights
Use relative weights to show importance ratio:
```
Price is 2x more important than quality
Weights: 2,1
```

### Tip 2: Normalize Weights
All weights will be normalized automatically:
```
1,1,1 is equivalent to 2,2,2 or 10,10,10
```

### Tip 3: Impact Notation
- Use `+` for benefit criteria (higher is better)
- Use `-` for cost criteria (lower is better)

### Tip 4: Email in Web Service
Set up email for result delivery:
1. Edit `.env` file
2. Add SENDER_EMAIL and SENDER_PASSWORD
3. For Gmail, use App-Specific Password

---

## Integration Examples

### Bash Script
```bash
#!/bin/bash
for file in *.csv; do
  python topsis.py "$file" 1,1,1 +,+,+ "result_$file"
done
```

### Python Loop
```python
from topsis_lavanya_102313066 import topsis

files = ['data1.csv', 'data2.csv', 'data3.csv']
for file in files:
    result = topsis(file, '1,1,1', '+,+,+')
    print(f"\n{file}:")
    print(result)
```

### REST API Call
```bash
curl -X POST http://localhost:5000/api/analyze \
  -F "file=@data.csv" \
  -F "email=user@example.com" \
  -F "weights=1,1,1,2" \
  -F "impacts=+,+,+,-"
```

---

## Best Practices

1. **Validate Data First**
   - Check for missing values
   - Ensure all positive numbers
   - Verify column count

2. **Choose Meaningful Weights**
   - Reflect actual importance
   - Be consistent across analyses
   - Document your choices

3. **Test with Sample Data**
   ```bash
   python topsis.py data.csv 1,1,1 +,+,+
   ```

4. **Save Results**
   ```bash
   python topsis.py data.csv 1,1,1 +,+,+ results.csv
   ```

5. **Verify Output**
   - Check all alternatives are ranked
   - Scores should be between 0-1
   - Rank should be 1 to n

---

## Troubleshooting Checklist

- [ ] Python 3.7+ installed: `python --version`
- [ ] Required packages installed: `pip list`
- [ ] Input file exists and readable
- [ ] File format is CSV
- [ ] First column is non-numeric
- [ ] All other columns are numeric
- [ ] All values are positive
- [ ] Weights count matches criteria
- [ ] Impacts count matches criteria
- [ ] Impacts are only + or -

---

## Performance Tips

### For Large Files
- Use CSV format (faster than Excel)
- Pre-process data if possible
- Consider parallel processing

### For Web Service
- Ensure `.env` file is configured
- Use appropriate file size limits
- Monitor server resources

---

## Getting Help

### Check Documentation
- `COMPLETE_GUIDE.md` - Full documentation
- `DEPLOYMENT_GUIDE.md` - Deployment help
- `VERIFICATION_CHECKLIST.md` - Testing help

### Common Issues
See Common Errors section above

### Contact Support
Email: lgarg_be23@thapar.edu

