# Fill in credentials
host=''
port=''
database=''
user=''
password=''

# sqlalchemy engine for writing data to a database
from sqlalchemy import create_engine    
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

import psycopg2 as pc
import pandas as pd


# Insert the get_data() function definition below
def get_data(query):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # create a connection to the PostgreSQL server
        conn = pc.connect(host=host,
                        port=port,
                        database=database,
                        user=user,
                        password=password)
		
        fetch = pd.read_sql_query(query, conn)
       
	    # close the connection to the PostgreSQL database
        conn.close()

    # the code below makes the function more robust
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return(fetch);
