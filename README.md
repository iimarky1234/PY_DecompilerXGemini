# PY_DecompilerXGemini

This script helps disassemble python's bytecode (.pyc) and sends the assembly code to GEMINI to analyse it in order to return a python code.

## Description

The script takes a `.pyc` file as input, disassembles it into bytecode, and then uses the Gemini API to decompile the bytecode back into Python code.

The script will first identify the Python version the `.pyc` file was compiled with by reading the magic number. It will then proceed with the disassembly process only if the Python version of the current environment matches the Python version of the `.pyc` file.

The disassembled bytecode is saved in the `Assembled/` directory.

## Usage

```bash
python main.py <filename.pyc> --api <YOUR_GEMINI_API_KEY>
```

### Arguments

*   `filename`: Path to the `.pyc` file to be decompiled.
*   `--api`: Your Gemini API Key.
*   `--model`: (Optional) The Gemini model to use. Defaults to `gemini-3-flash-preview`. For more info visit [https://ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models).

## Dependencies

The script requires the following Python libraries:

*   google-genai
*   python-magic

You can install them using pip:

```bash
pip install -r requirements.txt
```

## `Versions_magicnum.json`

This JSON file contains a mapping of Python magic numbers to their corresponding Python versions. This is used to identify the Python version of the input `.pyc` file.

If you found the JSON file is outdated, you can look through the new python version's magic number in https://github.com/python/cpython/blob/main/Include/internal/pycore_magic_number.h and manually add it in `Versions_magicnum.json`

## Disclaimer

The results from GEMINI are not always correct. Use with caution.
