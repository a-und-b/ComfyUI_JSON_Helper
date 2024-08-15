# ComfyUI JSON Helper

This custom node for ComfyUI provides a simple way to convert JSON strings to JSON objects, bridging the gap between nodes that output JSON as strings and nodes that require JSON object inputs.

## Features

- Converts JSON strings to JSON objects
- Handles JSON parsing errors gracefully
- Easy to integrate into existing ComfyUI workflows

## Installation

1. Navigate to your ComfyUI custom nodes folder:
   ```
   cd /path/to/ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```
   git clone https://github.com/yourusername/ComfyUI-JSONHelper.git
   ```
3. Restart ComfyUI

## Usage

After installation, you'll find a new node called "JSON String to Object" in the node menu. 

1. Connect the output of a node that produces a JSON string to the input of this node.
2. The output of this node will be a JSON object, which can be connected to nodes that expect JSON input.

## Error Handling

If the input string is not valid JSON, the node will print an error message to the console and return None.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# LICENSE

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.