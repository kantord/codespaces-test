# Demo App

A slightly complex hello-world demo application managed with `uv` and featuring a CLI built with `click`.

## Features

- Multiple CLI commands with nested function calls
- Data processing pipeline with transformation steps
- Custom greetings with configurable options
- Demonstrates function composition and call chains

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install dependencies
uv sync
```

## Usage

The app provides three main commands:

### 1. Greet
Display a simple greeting:
```bash
uv run demo-app greet
```

### 2. Process
Process text through multiple transformation steps:
```bash
uv run demo-app process "your text here"
```

### 3. Hello Complex
Generate custom greetings with options:
```bash
# Basic usage
uv run demo-app hello-complex

# With custom name
uv run demo-app hello-complex --name Alice

# With repetition count
uv run demo-app hello-complex --name Bob --count 5
```

### Help
View all available commands:
```bash
uv run demo-app --help
```

## Architecture

The application demonstrates a slightly complex structure with functions calling each other:

- **CLI Layer** (`cli.py`): Click-based command-line interface
  - `greet()` → calls `hello()` from core module
  - `process()` → calls `process_data()` which chains multiple transformations
  - `hello_complex()` → calls `generate_greeting()` → `format_greeting()` → `build_greeting_text()`

- **Core Layer** (`__init__.py`): Business logic
  - `process_data()` orchestrates data transformation
  - `transform_step_one()`, `transform_step_two()`, `finalize_output()` form a processing pipeline

## Development

```bash
# Run the CLI in development mode
uv run demo-app [command]

# Or activate the virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
demo-app [command]
```
