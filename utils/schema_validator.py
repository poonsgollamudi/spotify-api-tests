import json
from pathlib import Path

from jsonschema import validate


def validate_schema(response_data, schema_file):

    project_root = Path(__file__).resolve().parent.parent

    schema_path = project_root / "schemas" / schema_file

    with open(schema_path, "r", encoding="utf-8") as file:
        schema = json.load(file)

    validate(
        instance=response_data,
        schema=schema
    )