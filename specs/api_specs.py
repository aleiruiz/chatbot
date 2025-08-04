inbound_chat_specs = {
    "parameters": [
        {
            "name": "From",
            "in": "formData",
            "type": "string",
            "required": "true",
            "default": "",
            "example": "whatsapp:+1234567890",
        },
        {
            "name": "Body",
            "in": "formData",
            "type": "string",
            "required": "true",
            "default": "",
            "example": "Hello, I need help with my vehicle purchase.",
        },
    ],
    "responses": {
        "200": {
            "description": "A list of colors (may be filtered by palette)",
            "examples": {"application/json": {"value": {"message": "ok"}}},
        }
    },
}
