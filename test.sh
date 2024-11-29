#!/bin/bash

# Check if API key is provided
if [ -z "$1" ]; then
    echo "Please provide your OpenAI API key as an argument"
    echo "Usage: ./test.sh YOUR_API_KEY"
    exit 1
fi

# Export API key and run test
export OPENAI_API_KEY=$1
source venv_new/bin/activate
python3 test_processor.py
