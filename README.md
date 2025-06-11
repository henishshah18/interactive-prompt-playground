# OpenAI API Playground

This is an interactive playground for experimenting with OpenAI's GPT models through their API. The playground allows you to test different parameter configurations and see how they affect the model's responses.

## Prerequisites

- Python 3.x
- OpenAI API key

## Setup

1. Install the required packages:
```bash
pip install openai tabulate
```

2. Set up your OpenAI API key as an environment variable:
```bash
# On Windows
set OPENAI_API_KEY=your-api-key-here

# On Unix/MacOS
export OPENAI_API_KEY=your-api-key-here
```

## How to Run

1. Run the script:
```bash
python openai_api_playground.py
```

2. When prompted, enter a product name or description. The playground will generate multiple marketing descriptions using different parameter configurations.

## Features

### Parameter Control
The playground tests various combinations of the following parameters:

- **Temperature**
  - 0.0 (most deterministic)
  - 0.7 (balanced)
  - 1.2 (more creative)

- **Max Tokens**
  - 50 (short responses)
  - 150 (medium responses)
  - 300 (longer responses)

- **Presence Penalty**
  - 0.0 (default)
  - 1.5 (encourages new topics)

- **Frequency Penalty**
  - 0.0 (default)
  - 1.5 (reduces repetition)

### Model Selection
- Currently uses GPT-3.5-turbo model
- System prompt configured for marketing-focused responses

### Output Format
- Results are displayed in a clean, grid-formatted table
- Each response shows the modified parameter and the corresponding generated content
- Uses the `tabulate` library for clear visualization of results

## Example Output
The script will output a grid table showing:
- The parameter that was modified from the base configuration
- The corresponding marketing description generated with those parameters

This allows for easy comparison of how different parameters affect the model's output. 