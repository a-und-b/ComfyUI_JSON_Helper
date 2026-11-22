# ComfyUI JSON Helper

This custom node for ComfyUI provides a simple way to convert JSON strings to JSON objects, bridging the gap between nodes that output JSON as strings and nodes that require JSON object inputs.

## Features

- Converts JSON strings to JSON objects
- Handles JSON parsing errors gracefully
- Easy to integrate into existing ComfyUI workflows

## Requirements

- ComfyUI
- Python 3.10+

## Installation

1. Navigate to your ComfyUI custom nodes folder:
   ```
   cd /path/to/ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```
   git clone https://github.com/a-und-b/ComfyUI_JSON_Helper.git
   ```
3. Restart ComfyUI

## Example workflow

![Example workflow](example_workflows/json-helper-preview.png)

Load [`example_workflows/json-helper-example.json`](example_workflows/json-helper-example.json) to see the node under the **utils** category with sample JSON text.

## Usage

After installation, you'll find **JSON String to Object** under **utils**.

1. Connect the output of a node that produces a JSON string to the input of this node (or paste JSON into the widget).
2. The output is a JSON object for nodes that expect structured JSON.

## Error Handling

If the input string is not valid JSON, the node will print an error message to the console and return None.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
