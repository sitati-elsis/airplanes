from typing import Any

from rest_framework.schemas.openapi import SchemaGenerator
from rest_framework.schemas.openapi import DRFOpenAPISchema

class PlanesInputSchema(SchemaGenerator):
    """
    Defines expected Schema structure when adding planes from the interactive
    documentation
    """
    def get_schema(self, *args: Any, **kwargs: Any) -> DRFOpenAPISchema:
        schema = super().get_schema(*args, **kwargs)
        schema_structure = {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'integer',
                    'format': 'int32',
                    'description': 'The Plane id',
                },
                'passengers': {
                    'type': 'integer',
                    'format': 'int32',
                    'description': 'The number of passengers',
                }
            },
        }
        schema['paths']['/api/planes/']['post']['requestBody']['content']\
            ['application/json']['schema'] = schema_structure
        return schema