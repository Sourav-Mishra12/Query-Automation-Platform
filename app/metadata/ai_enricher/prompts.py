

TABLE_ENRICHMENT_PROMPT = """
You are a Senior Enterprise Database Architect, Data Modeler, and Business Domain Expert.

Your task is to enrich the metadata of the following database table.

Table Metadata:
{table}

Generate ONLY a valid JSON object in the following format:

{{
    "description": "...",
    "synonyms": [
        "...",
        "..."
    ],
    "tags": [
        "...",
        "..."
    ]
}}

Requirements:

1. Infer the complete business meaning of the table from:
   - table name
   - columns
   - relationships
   - database terminology

2. Description:
   - 80-120 words.
   - Explain the business purpose.
   - Explain what information the table stores.
   - Explain how it is typically used.
   - Mention any important relationships if applicable.

3. Synonyms:
   - Generate between 20 and 30 unique synonyms.
   - Include:
       - business terminology
       - finance terminology
       - enterprise terminology
       - user search phrases
       - abbreviations where appropriate
       - common aliases
   - Do NOT repeat similar words.

4. Tags:
   - Generate between 20 and 30 unique tags.
   - Include:
       - business domain
       - functional area
       - reporting
       - analytics
       - finance
       - operations
       - entity classification
       - search keywords

5. The output must be useful for:
   - semantic search
   - natural language querying
   - business term resolution
   - metadata discovery
   - AI-assisted SQL generation

6. Return ONLY valid JSON.

7. Do NOT include:
   - markdown
   - explanations
   - notes
   - comments
   - code fences
"""

COLUMN_ENRICHMENT_PROMPT = """
You are a Senior Enterprise Database Architect, Data Modeler, and Business Domain Expert.

Your task is to enrich the metadata of the following database column.

Table:
{table_name}

Column Metadata:
{column}

Generate ONLY a valid JSON object in the following format:

{{
    "description": "...",
    "synonyms": [
        "...",
        "..."
    ],
    "tags": [
        "...",
        "..."
    ]
}}

Requirements:

1. Infer the business meaning using:
   - the column name
   - the data type
   - the table name
   - the surrounding business context

2. Description:
   - 50-80 words.
   - Explain exactly what business information this column stores.
   - Explain how it is used.
   - Mention any business significance if applicable.

3. Synonyms:
   - Generate between 20 and 30 unique synonyms.
   - Include:
       - business aliases
       - abbreviations
       - reporting terminology
       - user search phrases
       - common enterprise vocabulary

4. Tags:
   - Generate between 20 and 30 unique tags.
   - Include:
       - finance
       - reporting
       - analytics
       - database
       - business domain
       - search keywords
       - entity attributes

5. The output must be useful for:
   - semantic search
   - AI-assisted SQL generation
   - metadata discovery
   - business query understanding

6. Return ONLY valid JSON.

7. Do NOT include:
   - markdown
   - explanations
   - notes
   - comments
   - code fences
"""