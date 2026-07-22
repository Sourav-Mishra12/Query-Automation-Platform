"""
Compares two metadata documents and identifies schema changes
such as added, removed, and modified tables and columns.

"""


class MetadataDiffer:

    COLUMN_PROPERTIES = (

      "data_type",
      "nullable",
      "primary_key",
      "foreign_key",
      "default",
    )


    def compare(
            self,
            old_metadata: dict,
            new_metadata: dict,
           ) -> dict:
     
     """
     Compares two metadata documents.

     """

     return self._compare_tables(old_metadata,new_metadata)
    

    def _compare_tables(
        self,
        old_metadata: dict,
        new_metadata: dict,
            ) -> list:
     """
     Compares tables between two metadata documents.

     """


     old_tables = {
       table["name"] : table 
       for table in old_metadata.get("tables" , [])
     }


     new_tables = {
       table["name"] : table 
       for table in new_metadata.get("tables" , [])
     }


     added_tables = []
     removed_tables = []
     modified_tables = []
     
     # find added tables

     for table_name in new_tables:
       if table_name not in old_tables:
         added_tables.append(table_name)

     # find removed tables

     for table_name in old_tables:
       if table_name not in new_tables:
         removed_tables.append(table_name)

     for table_name in old_tables:
      if table_name in new_tables:
         
         changes = self._compare_columns(
           old_tables[table_name],
           new_tables[table_name],
         )

         if (
           changes["added_columns"]
           or changes["removed_columns"]
           or changes["modified_columns"]
         ) :
           
           modified_tables.append(
             {
               "table" : table_name,
               **changes,
             }
           )


     return {
       
        "added_tables": added_tables,
        "removed_tables": removed_tables,
        "modified_tables": modified_tables,

         }
    

    def _compare_columns(
          self,
          old_table: dict,
          new_table: dict,
        ) -> dict:
     
     """
     Compare the columns of two tables.

     """

     old_columns = {
        column["name"]: column
        for column in old_table.get("columns", [])
     }

     new_columns = {
        column["name"]: column
        for column in new_table.get("columns", [])
     }

     added_columns = []
     removed_columns = []
     modified_columns = []

    # Added columns
     for column_name in new_columns:
        if column_name not in old_columns:
            added_columns.append(column_name)

    # Removed columns
     for column_name in old_columns:
        if column_name not in new_columns:
            removed_columns.append(column_name)

    # Compare common columns
     for column_name in old_columns:

        if column_name not in new_columns:
            continue

        changes = self._compare_column_properties(
            old_columns[column_name],
            new_columns[column_name],
        )

        if changes:
            modified_columns.append(
                {
                    "column": column_name,
                    "changes": changes,
                }
            )

     return {
        "added_columns": added_columns,
        "removed_columns": removed_columns,
        "modified_columns": modified_columns,
    }
    

    def _compare_column_properties(
        self,
        old_column : dict,
        new_column : dict,
    ) -> dict :
      

      changes = {}

      for property_name in self.COLUMN_PROPERTIES :

        old_value = old_column.get(property_name)
        new_value = new_column.get(property_name)

        if old_value != new_value :
          changes[property_name] = {
            "old" : old_value,
            "new" : new_value,
          }

      return changes 