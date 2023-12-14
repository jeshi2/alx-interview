# Minimum Operations

## Overview

This Python script calculates the minimum number of operations needed to obtain exactly 'n' characters of the letter 'H' in a text file. The script can only perform two operations: Copy All and Paste.

## Method: `minOperations`

```python
def minOperations(n):
    # Implementation details...
    pass
```

## Usage

1. **Run the script:**

   ```bash
   python3 script_name.py
   ```

2. **Modify test cases:**

   Update the values of `n` in the script with your desired input.

   ```python
   n = 4
   print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
   ```

3. **Execute the script:**

   ```bash
   python3 script_name.py
   ```

## Example

```python
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

### Output

```bash
Min # of operations to reach 4 char: 4
Min # of operations to reach 12 char: 7
```

## Notes

- If `n` is impossible to achieve, the script returns 0.

## Requirements

- Python 3.4.3 or later
- Ubuntu 20.04 LTS environment
- Editor: vi, vim, emacs
- PEP 8 coding style
- All files executable

## Author

Antony Evans

---
