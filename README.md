# JSON Verifier

## Description

This Python program verifies the input JSON data against a specific requirement. The input data format is defined as `AWS::IAM::Role Policy`. The program returns `False` if the `Resource` field in any statement within the input JSON data contains a single asterisk (`*`). Otherwise, it returns `True`.

## Usage

To run the program, follow these steps:

1. Navigate to the project's source directory in your terminal or command prompt.
2. Run the following command:
```
python3 main.py <path_to_json>
```
Replace `<path_to_json>` with the actual path to the JSON file you want to verify.

For example:
```
python3 main.py /path/to/policy.json
```

The program will output `True` or `False` based on the verification result.

## Requirements

- Python 3.x
- A valid JSON file in the `AWS::IAM::Role Policy` format
