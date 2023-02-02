POST_SCHEMA = {
    "type": "object",
    "properties": {
        "book": {
            "type": "object",
            "properties": {
                "author": {
                    "type": "string"
                },
                "id": {
                    "type": "integer"
                },
                "isElectronicBook": {
                    "type": "boolean"
                },
                "name": {
                    "type": "string"
                },
                "year": {
                    "type": "integer"
                }
            },
            "required": [
                "id",
                "name",
                "author",
                "isElectronicBook"

            ]
        }
    },

}
