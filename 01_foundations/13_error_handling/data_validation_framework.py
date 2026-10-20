class ValidationError(Exception):
    """Base class for validation errors."""
    pass

class MissingFieldError(ValidationError):
    """Raised when a required field is missing."""
    pass

class TypeMismatchError(ValidationError):
    """Raised when a value has the wrong type."""
    pass

def validate(data, schema):
    errors = []

    for field, rules in schema.items():
        if field not in data:
            if rules.get("required", False):
                try:
                    raise MissingFieldError(
                        f"Missing required field: {field}"
                    )
                except MissingFieldError as e:
                    errors.append(str(e))
            continue

        value = data[field]
        expected_type = rules.get("type")
        if expected_type is not None:
            valid_type = (
                type(value) is expected_type
                if expected_type in (int, bool)
                else isinstance(value, expected_type)
            )

            if not valid_type:
                try:
                    raise TypeMismatchError(
                        f"{field} must be of type "
                        f"{expected_type.__name__}"
                    )
                except TypeMismatchError as e:
                    errors.append(str(e))
                continue
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            if "min" in rules and value < rules["min"]:
                errors.append(
                    f"{field} must be >= {rules['min']}"
                )

            if "max" in rules and value > rules["max"]:
                errors.append(
                    f"{field} must be <= {rules['max']}"
                )
        if isinstance(value, (str, list)):
            if (
                "min_length" in rules
                and len(value) < rules["min_length"]
            ):
                errors.append(
                    f"{field} must have at least "
                    f"{rules['min_length']} items/characters"
                )
        if "contains" in rules:
            try:
                if rules["contains"] not in value:
                    errors.append(
                        f"{field} must contain {rules['contains']!r}"
                    )
            except TypeError:
                errors.append(
                    f"{field} does not support the contains check"
                )

    return errors
schema = {
    "age": {
        "type": int,
        "required": True,
        "min": 0,
        "max": 120
    },
    "name": {
        "type": str,
        "required": True,
        "min_length": 2
    },
    "email": {
        "type": str,
        "required": False,
        "contains": "@"
    },
    "hobbies": {
        "type": list,
        "required": False,
        "min_length": 1
    }
}
data = {
    "age": 200,
    "email": "invalid-email",
    "hobbies": []
}
errors = validate(data, schema)
if errors:
    print("Validation failed:")
    for error in errors:
        print("-", error)
else:
    print("Validation successful!")