import pymysql
import pandas as pd

def export_mariadb_to_excel(host, user, password, database, queries, port, output_file='data_export.xlsx'):
    """
    Pull data from MariaDB and export to Excel
    
    Parameters:
    - host: MariaDB server hostname
    - user: Database username
    - password: Database password
    - database: Database name
    - query: SQL query to fetch data
    - output_file: Excel file path to save (default: data_export.xlsx)
    """
    try:
        # Establish database connection
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        
        # Read data into pandas DataFrame
    #     df = pd.read_sql(query, connection)
        
    #     # Export to Excel
    #     df.to_excel(output_file, index=False)
        
    #     print(f"Data successfully exported to {output_file}")
    #     print(f"Total rows exported: {len(df)}")
        
    # except Exception as e:
    #     print(f"An error occurred: {e}")
     # Create Excel writer object
        with pd.ExcelWriter(output_file) as writer:
            # Execute each query and write to a separate sheet
            for sheet_name, query in queries.items():
                df = pd.read_sql(query, connection)
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                print(f"{sheet_name} sheet: {len(df)} rows exported")
        print(f"Data successfully exported to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        if 'connection' in locals():
            connection.close()

# Example usage
if __name__ == "__main__":
    export_mariadb_to_excel(
        host='genthrive-wz5bi-mariadb.external.kinsta.app',
        user='gt-admin',
        password='Tx$80$0812900$001', 
        database='genthrive',
        port=31496,
        queries={
            'Organizations':'SELECT * FROM service_providers',
            'Programs':'SELECT * FROM programs'
            },
        output_file='exported_data.xlsx'
    )