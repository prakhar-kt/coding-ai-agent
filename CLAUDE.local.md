# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AI coding agent that uses Google's Gemini API to provide interactive assistance for coding tasks. The agent can perform file operations (list, read, write), execute Python files, and operate within a sandboxed working directory.

## Architecture

**Core Components:**
- `main.py`: Entry point and conversation loop with Gemini API
- `call_function.py`: Function dispatch system that maps tool calls to implementations
- `prompts.py`: System prompt that defines the agent's capabilities
- `config.py`: Configuration settings (working directory, file size limits)
- `functions/`: Tool implementations for file operations

**Key Architecture Patterns:**
- Function calling system using Google Genai types and schemas
- Sandboxed execution constrained to WORKING_DIR (currently "./calculator")
- Tool-based architecture where each function has a schema declaration and implementation
- Security model that prevents directory traversal outside working directory

## Development Commands

**Run the AI agent:**
```bash
python main.py 'your prompt here'
python main.py 'your prompt here' --verbose  # for detailed output including token counts
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Environment setup:**
Requires `GEMINI_API_KEY` environment variable (loaded via python-dotenv)

## Function System

The agent provides these core functions to the LLM:
- `get_files_info`: List files and directories with sizes
- `get_file_content`: Read file contents (limited by MAX_CHARS=10000)
- `run_python_file`: Execute Python files within the working directory
- `write_file`: Create or overwrite files

All functions are automatically sandboxed to the WORKING_DIR defined in config.py.

## Working Directory

The agent operates within a sandboxed working directory (currently "./calculator"). All file operations are constrained to this directory for security. The working directory path is automatically injected into function calls.

## Testing

The repository includes a `tests.py` file in the root directory for testing the main functionality.