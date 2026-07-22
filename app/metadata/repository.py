"""
Provides persistent storage for metadata documents.
Handles saving and loading metadata while hiding filesystem operations
from the rest of the application.

"""

import json 
from pathlib import Path
from app.metadata.exceptions import MetadataNotFoundException



class MetadataRepository:
    """
    Handles persistence of metadata documents.
    """

    def __init__(self, metadata_directory: str = "metadata"):
        self.metadata_directory = Path(metadata_directory)
        self.metadata_directory.mkdir(parents=True, exist_ok=True)


    def _metadata_path(self, database_name: str) -> Path:
     """
     Returns the metadata file path for a database.
     """

     return self.metadata_directory / f"{database_name}.json"
    

    def save(
        self,
        database_name: str,
        metadata: dict,
              ) -> Path :
     """
      Saves metadata to disk.

     """

     path = self._metadata_path(database_name)

     with path.open("w", encoding="utf-8") as file:
        json.dump(
            metadata,
            file,
            indent=4,
            ensure_ascii=False,
        )

     return path


    def load(
       self,
       database_name: str,
         ) -> dict:
     
     """
     Loads metadata from disk.

     """

     path = self._metadata_path(database_name)

     if not path.exists():
       raise MetadataNotFoundException(
         f"Metadata for '{database_name}' was not found . "
       )

     with path.open("r", encoding="utf-8") as file:
        return json.load(file)


    