tools = [
    {
        "type": "function",
        "function": {
            "name": "check_address",
            "description": "A function to check for the validity and existence of an address, you may call this to retrieve latitude and longitud to the customer",
            "strict": False,
            "parameters": {
                "type": "object",
                "required": ["address"],
                "properties": {
                    "address": {
                        "type": "string",
                        "description": "The address to be checked",
                    },
                    "postal_code": {
                        "type": "string",
                        "description": "The postal code associated with the address, if applicable",
                    },
                    "country": {
                        "type": "string",
                        "description": "The country where the address is located",
                    },
                },
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "verify_client",
            "description": "Verify the user is a valid client, this function should be validated before using any other",
            "strict": True,
            "parameters": {
                "type": "object",
                "required": ["client_email"],
                "properties": {
                    "client_email": {
                        "type": "string",
                        "description": "User's email, we will check if this email exists on our records",
                    }
                },
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "request_trip",
            "description": "Request a trip using the user's physical address, latitude and longitude of origin and all the destinations from the trip, passengers list, email, any note and/or request, and date.",
            "strict": True,
            "parameters": {
                "type": "object",
                "required": [
                    "origin_address",
                    "origin_latitude",
                    "origin_longitude",
                    "destinations",
                    "passengers",
                    "email",
                    "note",
                    "trip_date",
                ],
                "properties": {
                    "origin_address": {
                        "type": "string",
                        "description": "User's physical address where the trip starts",
                    },
                    "origin_latitude": {
                        "type": "number",
                        "description": "Latitude of the origin point",
                    },
                    "origin_longitude": {
                        "type": "number",
                        "description": "Longitude of the origin point",
                    },
                    "destinations": {
                        "type": "array",
                        "description": "List of destinations during the trip",
                        "items": {
                            "type": "object",
                            "properties": {
                                "address": {
                                    "type": "string",
                                    "description": "Physical address of the stop",
                                },
                                "latitude": {
                                    "type": "number",
                                    "description": "Latitude of the stop",
                                },
                                "longitude": {
                                    "type": "number",
                                    "description": "Longitude of the stop",
                                },
                            },
                            "additionalProperties": False,
                            "required": ["address", "latitude", "longitude"],
                        },
                    },
                    "passengers": {
                        "type": "array",
                        "description": "List of passengers for the trip",
                        "items": {
                            "type": "string",
                            "description": "Name of the passenger",
                        },
                    },
                    "email": {
                        "type": "string",
                        "description": "Email address for communication regarding the trip",
                    },
                    "note": {
                        "type": "string",
                        "description": "Any additional notes or requests for the trip",
                    },
                    "trip_date": {
                        "type": "string",
                        "description": "Date of the trip in MM-DD format",
                    },
                },
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "request_quote",
            "description": "Request a trip using the user's physical address, latitude and longitude of origin and all the destinations from the trip, passengers list, email, any note and/or request, and date.",
            "strict": True,
            "parameters": {
                "type": "object",
                "required": [
                    "origin_address",
                    "origin_latitude",
                    "origin_longitude",
                    "destinations",
                    "passengers",
                    "email",
                    "note",
                    "trip_date",
                ],
                "properties": {
                    "origin_address": {
                        "type": "string",
                        "description": "User's physical address where the trip starts",
                    },
                    "origin_latitude": {
                        "type": "number",
                        "description": "Latitude of the origin point",
                    },
                    "origin_longitude": {
                        "type": "number",
                        "description": "Longitude of the origin point",
                    },
                    "destinations": {
                        "type": "array",
                        "description": "List of destinations during the trip",
                        "items": {
                            "type": "object",
                            "properties": {
                                "address": {
                                    "type": "string",
                                    "description": "Physical address of the stop",
                                },
                                "latitude": {
                                    "type": "number",
                                    "description": "Latitude of the stop",
                                },
                                "longitude": {
                                    "type": "number",
                                    "description": "Longitude of the stop",
                                },
                            },
                            "additionalProperties": False,
                            "required": ["address", "latitude", "longitude"],
                        },
                    },
                    "passengers": {
                        "type": "array",
                        "description": "List of passengers for the trip",
                        "items": {
                            "type": "string",
                            "description": "Name of the passenger",
                        },
                    },
                    "email": {
                        "type": "string",
                        "description": "Email address for communication regarding the trip",
                    },
                    "note": {
                        "type": "string",
                        "description": "Any additional notes or requests for the trip",
                    },
                    "trip_date": {
                        "type": "string",
                        "description": "Date of the trip in MM-DD format",
                    },
                },
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "fetch_estimated_fare",
            "description": "Fetch estimated fare for a trip between one origin and multiple destinations, using latitude and longitude for each address",
            "strict": True,
            "parameters": {
                "type": "object",
                "required": ["origin", "destinations"],
                "properties": {
                    "origin": {
                        "type": "object",
                        "required": ["lat", "lng"],
                        "properties": {
                            "lat": {
                                "type": "number",
                                "description": "Latitude of the origin address",
                            },
                            "lng": {
                                "type": "number",
                                "description": "Longitude of the origin address",
                            },
                        },
                        "additionalProperties": False,
                    },
                    "destinations": {
                        "type": "array",
                        "description": "Array of destination coordinates",
                        "items": {
                            "type": "object",
                            "required": ["lat", "lng"],
                            "properties": {
                                "lat": {
                                    "type": "number",
                                    "description": "Latitude of the destination address",
                                },
                                "lng": {
                                    "type": "number",
                                    "description": "Longitude of the destination address",
                                },
                            },
                            "additionalProperties": False,
                        },
                    },
                },
                "additionalProperties": False,
            },
        },
    },
]

prompt = """You are an operator from mowi, a ground transporation company from Uruguay, your task is to help users request quotes and schedule trips through the usage of our APIs, you are not tech support nor a sales agent, if a user wants to get more specialized support, ask them to talk directly to operations department.
When a user starts a conversation, layout clearly the tasks you are able to perform.
Use natural language but be professional and kind, whenever a customer is asking about mowi, refer to it in a first person basis.
Introduce yourself as Mowi and eager to help the customer with any queries.
Deal in Uruguayan pesos
Don't justify your answers. Don't give information not mentioned in the CONTEXT INFORMATION and Don't assist the customer with anything unrelated to Mowi.
"""
