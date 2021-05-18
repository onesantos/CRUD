schema_movie = {
    "type": "object",
    "properties": {
        "nome": {"type": "string"},
        "ano": {"type": "integer"},
        "avaliacao": {"type": "number"},
        "genero": {"type": "string"},
    },
    "required": ["nome", "ano", "genero"],
}

schema_movies = {"type": "array", "$ref": schema_movie}
