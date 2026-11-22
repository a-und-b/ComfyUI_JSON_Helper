import json


class JSONStringToObjectNode:
    """Convert a JSON string into a JSON object for downstream nodes."""

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "json_string": (
                    "STRING",
                    {
                        "multiline": True,
                        "tooltip": "Raw JSON text to parse into an object",
                    },
                )
            }
        }

    RETURN_TYPES = ("JSON",)
    RETURN_NAMES = ("json",)
    FUNCTION = "convert_string_to_json"
    CATEGORY = "utils"
    DESCRIPTION = (
        "Parses a JSON string into a JSON object so it can connect to nodes "
        "that expect structured JSON input."
    )

    def convert_string_to_json(self, json_string):
        try:
            json_object = json.loads(json_string)
            return (json_object,)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return (None,)


NODE_CLASS_MAPPINGS = {
    "JSONStringToObjectNode": JSONStringToObjectNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "JSONStringToObjectNode": "JSON String to Object"
}
