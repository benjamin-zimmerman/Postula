#!/usr/bin/env python3
import json
import sys
import jsonschema


def validate(file_path, schema_path):
    """Validate a JSON file against a schema"""
    with open(schema_path, 'r') as f:
        schema = json.load(f)
    with open(file_path, 'r') as f:
        data = json.load(f)
    jsonschema.validate(data, schema)
    print("Validation successful.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: validate_json.py <data_file> <schema_file>")
        sys.exit(1)
    validate(sys.argv[1], sys.argv[2])
