
from google.cloud import spanner

spanner_client = spanner.Client()

instance_id = 'babysteps'
instance = spanner_client.instance(instance_id)

database_id = 'babysteps-db'
database = instance.database(database_id)

with database.snapshot() as snapshot:
    results = snapshot.execute_sql('SELECT 1, 2, 3')

    for row in results:
        print(row)