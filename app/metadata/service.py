"""
Orchestrates the metadata generation workflow by coordinating the
Schema Scanner, Metadata Generator, and Metadata Repository.

"""


from sqlalchemy.engine import Engine

from app.metadata.generator import MetadataGenerator
from app.metadata.repository import MetadataRepository
from app.metadata.scanner import SchemaScanner


class MetadataService:

    """
    Coordinates the metadata generation pipeline.

    """

    def __init__(
            
        self,
        engine: Engine,
        repository: MetadataRepository,

                     ):
     self.scanner = SchemaScanner(engine)
     self.generator = MetadataGenerator()
     self.repository = repository


    def generate_metadata(self) -> dict:
     
     """
     Generates and persists metadata for the connected database.

     """

     schema = self.scanner.scan()

     metadata = self.generator.generate(schema)

     self.repository.save(
        schema.database_name,
        metadata,
     )

     return metadata