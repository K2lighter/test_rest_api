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
        "name",
      ]
    }
  },
  "required": [

  ]
}
# {'book': {'author': '', 'id': 10, 'isElectronicBook': False, 'name': 'Война и мир', 'year': 'ttt'}}
