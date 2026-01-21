# TOPSIS - Verification Checklist

## Installation Verification

### CLI Program
- [ ] `topsis.py` file exists
- [ ] `data.csv` sample file exists
- [ ] Python 3.7+ installed
- [ ] pandas and numpy installed
- [ ] Run basic test: `python topsis.py data.csv 1,1,1,2 +,+,+,-`
- [ ] Output file created successfully

### PyPI Package
- [ ] `topsis_package/` directory exists
- [ ] `setup.py` file exists
- [ ] Package structure correct
- [ ] Install locally: `pip install -e topsis_package/`
- [ ] CLI tool available: `topsis-cli`
- [ ] Python import works: `from topsis_lavanya_102313066 import topsis`

### Web Service
- [ ] `web_service/` directory exists
- [ ] `app.py` file exists
- [ ] `requirements.txt` exists
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] `.env` file configured
- [ ] `templates/index.html` exists
- [ ] `uploads/` directory created

---

## Functionality Tests

### CLI Program Tests

#### Test 1: Basic Execution
```bash
python topsis.py data.csv 1,1,1,2 +,+,+,-
```
- [ ] No errors
- [ ] Results displayed
- [ ] All alternatives ranked
- [ ] Scores between 0-1

#### Test 2: File Output
```bash
python topsis.py data.csv 1,1,1,2 +,+,+,- test_output.csv
```
- [ ] Output file created
- [ ] CSV format correct
- [ ] Data matches console output
- [ ] Rank column present

#### Test 3: Input Validation
```bash
python topsis.py data.csv 1,1 +,+,+
```
- [ ] Error displayed
- [ ] Error message clear
- [ ] Program exits cleanly

#### Test 4: Different Weights
```bash
python topsis.py data.csv 2,1,3,1 +,+,+,-
```
- [ ] Results generated
- [ ] Different from previous run
- [ ] Scores still valid

### Web Service Tests

#### Test 5: Access Interface
- [ ] Navigate to `http://localhost:5000`
- [ ] Page loads
- [ ] Form visible
- [ ] All fields present (email, file, weights, impacts)

#### Test 6: File Upload
- [ ] Upload CSV file
- [ ] File accepted
- [ ] No errors
- [ ] Analysis starts

#### Test 7: Results Display
- [ ] Results table appears
- [ ] All alternatives listed
- [ ] Ranks correct (1, 2, 3...)
- [ ] Scores between 0-1

#### Test 8: CSV Download
- [ ] Click Download button
- [ ] File downloaded
- [ ] File format correct
- [ ] Data matches display

### API Tests

#### Test 9: Validation Endpoint
```bash
curl -X POST http://localhost:5000/api/validate \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","weights":"1,1,1","impacts":"+,+,-"}'
```
- [ ] Valid inputs accepted
- [ ] Invalid inputs rejected
- [ ] Error messages provided

#### Test 10: Analysis Endpoint
```bash
curl -X POST http://localhost:5000/api/analyze \
  -F "file=@data.csv" \
  -F "email=test@example.com" \
  -F "weights=1,1,1,2" \
  -F "impacts=+,+,+,-"
```
- [ ] File processed
- [ ] Results returned
- [ ] JSON format correct
- [ ] Email sent (if configured)

---

## Algorithm Correctness Tests

### Test 11: Score Range
- [ ] All scores >= 0
- [ ] All scores <= 1
- [ ] At least one score near 0
- [ ] At least one score near 1

### Test 12: Ranking
- [ ] Rank values: 1, 2, 3, ... n
- [ ] No duplicate ranks
- [ ] Higher score = lower rank number

### Test 13: Normalization
- [ ] Column sums ≈ 1 (after normalization)
- [ ] Results independent of scale
- [ ] Test with scaled input: data.csv vs data*10

### Test 14: Impact Direction
```bash
# Test with opposite impacts
python topsis.py data.csv 1,1,1,2 +,+,+,-
python topsis.py data.csv 1,1,1,2 +,+,-,+
```
- [ ] Results differ
- [ ] Rankings make sense

### Test 15: Weight Effect
```bash
# Test with different weights
python topsis.py data.csv 1,1,1,2 +,+,+,-
python topsis.py data.csv 10,1,1,2 +,+,+,-
```
- [ ] Results differ
- [ ] Heavier weighted criterion dominates

---

## Input Validation Tests

### Test 16: Missing Fields
```bash
python topsis.py data.csv 1,1,1
```
- [ ] Error: "impacts" required
- [ ] Clear error message

### Test 17: Invalid File
```bash
python topsis.py nonexistent.csv 1,1,1 +,+,+
```
- [ ] Error: "File not found"
- [ ] Clear error message

### Test 18: Wrong Weights Count
```bash
python topsis.py data.csv 1,1 +,+,+
```
- [ ] Error: mismatch
- [ ] Expected vs actual shown

### Test 19: Invalid Impacts
```bash
python topsis.py data.csv 1,1,1 +,*,+
```
- [ ] Error: "Invalid impacts"
- [ ] Only + or - accepted

### Test 20: Non-numeric Criteria
- [ ] Create test file with text in criteria
- [ ] Error detected
- [ ] Clear message

---

## Integration Tests

### Test 21: Package Installation
```bash
pip install -e topsis_package/
```
- [ ] No errors
- [ ] Package installed
- [ ] Can import: `from topsis_lavanya_102313066 import topsis`

### Test 22: CLI Entry Point
```bash
topsis-cli data.csv 1,1,1,2 +,+,+,-
```
- [ ] Works correctly
- [ ] Results match direct call

### Test 23: Web Service + Package
- [ ] Web service running
- [ ] Uses correct package code
- [ ] Results consistent

### Test 24: Multiple File Formats (Web Service)
- [ ] CSV upload works
- [ ] Excel upload works
- [ ] JSON upload works
- [ ] All produce similar results

### Test 25: Email Integration (Web Service)
- [ ] Email configured
- [ ] Analysis sent
- [ ] Email received
- [ ] Attachment correct

---

## Performance Tests

### Test 26: Execution Time
```bash
time python topsis.py data.csv 1,1,1,2 +,+,+,-
```
- [ ] Small file (<100 rows): <1 second
- [ ] Medium file (<1000 rows): <5 seconds

### Test 27: Memory Usage
- [ ] Monitor during execution
- [ ] No memory leaks
- [ ] Cleanup after completion

### Test 28: Web Service Response Time
- [ ] API response < 2 seconds
- [ ] File download < 1 second
- [ ] Page load < 2 seconds

---

## Security Tests

### Test 29: Input Sanitization
```bash
python topsis.py "data; rm -rf /" 1,1,1 +,+,+
```
- [ ] No command injection
- [ ] Clear error message

### Test 30: File Upload Security (Web Service)
- [ ] Only allowed file types
- [ ] File size limit enforced
- [ ] Filenames sanitized

### Test 31: Email Validation
```bash
# Web service: enter invalid email
```
- [ ] Validation catches it
- [ ] Clear error message

---

## Documentation Tests

### Test 32: README
- [ ] README.md exists
- [ ] Contains quick start
- [ ] Links to other docs

### Test 33: COMPLETE_GUIDE.md
- [ ] Algorithm explained
- [ ] Examples provided
- [ ] Formulas correct

### Test 34: DEPLOYMENT_GUIDE.md
- [ ] Deployment options clear
- [ ] Instructions complete
- [ ] Troubleshooting included

### Test 35: QUICK_REFERENCE.md
- [ ] Common commands listed
- [ ] Examples work
- [ ] Troubleshooting included

---

## Edge Cases

### Test 36: Single Alternative
```csv
Name,C1,C2,C3
A,1,2,3
```
- [ ] Handles correctly
- [ ] Rank = 1
- [ ] Score valid

### Test 37: Single Criterion
```csv
Name,C1
A,1
B,2
C,3
```
- [ ] Handles correctly
- [ ] Rankings correct

### Test 38: Very Large Numbers
```csv
Name,C1,C2
A,1000000,2000000
B,3000000,4000000
```
- [ ] Handles correctly
- [ ] Scores normalized

### Test 39: Very Small Numbers
```csv
Name,C1,C2
A,0.001,0.002
B,0.003,0.004
```
- [ ] Handles correctly
- [ ] Scores valid

### Test 40: All Equal Values
```csv
Name,C1,C2
A,5,5
B,5,5
```
- [ ] Handles without error
- [ ] Ranks equal

---

## Final Checks

- [ ] All 40 tests passed
- [ ] No console errors
- [ ] No warnings
- [ ] Output files created correctly
- [ ] Documentation complete
- [ ] Code well-commented
- [ ] Performance acceptable
- [ ] Security validated
- [ ] Ready for deployment

---

## Sign-Off

**Tested by:** _______________
**Date:** _______________
**Status:** ☐ PASS ☐ FAIL

**Notes:** 

