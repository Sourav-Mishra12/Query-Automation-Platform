from app.core.database import engine
from app.metadata.generator import MetadataGenerator
from app.metadata.repository import MetadataRepository
from app.metadata.scanner import SchemaScanner


def test_repository():

    scanner = SchemaScanner(engine)
    schema = scanner.scan()

    generator = MetadataGenerator()
    metadata = generator.generate(schema)

    repository = MetadataRepository()

    path = repository.save(
        database_name=schema.database_name,
        metadata=metadata,
    )

    print(f"Saved to: {path}")

    loaded = repository.load(schema.database_name)

    assert loaded == metadata

    print("Repository Test Passed")


if __name__ == "__main__":
    test_repository()