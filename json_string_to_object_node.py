import json

class JSONStringToObjectNode:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"json_string": ("STRING", {"multiline": True})}}
    
    RETURN_TYPES = ("JSON",)
    FUNCTION = "convert_string_to_json"

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