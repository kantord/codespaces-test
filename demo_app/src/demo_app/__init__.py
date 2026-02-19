"""Demo app with CLI using click."""

def hello() -> str:
    """Return a simple hello message."""
    return "Hello from demo-app!"


def process_data(data: str) -> str:
    """Process input data by calling transform functions."""
    result = transform_step_one(data)
    result = transform_step_two(result)
    return finalize_output(result)


def transform_step_one(data: str) -> str:
    """First transformation step."""
    return f"[Step1: {data.upper()}]"


def transform_step_two(data: str) -> str:
    """Second transformation step."""
    return f"[Step2: {data}]"


def finalize_output(data: str) -> str:
    """Finalize the output."""
    return f"Final: {data}"
