from google.cloud import bigquery
import sys
from csv import reader

# open file in read mode

# Construct a BigQuery client object.
client = bigquery.Client()
with open(r'write_to.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    next(csv_reader, None)  # skip the headers
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        dataset_id=row[1].strip()
        emailid=row[2].strip()
        role=row[3].strip()
        print(emailid)
        print(dataset_id)
        print(role)

        dataset = client.get_dataset(dataset_id)  # Make an API request.

        entry = bigquery.AccessEntry(
            role=role, #'Reader'
            entity_type="userByEmail",
            entity_id=emailid   #"sample.bigquery.dev@gmail.com",
        )

        entries = list(dataset.access_entries)
        entries.append(entry)
       
        dataset.access_entries = entries
        dataset = client.update_dataset(dataset, ["access_entries"])  # Make an API request.

        full_dataset_id = "{}.{}".format(dataset.project, dataset.dataset_id)
        print(
            "Updated dataset '{}' with modified user permissions.".format(full_dataset_id)
        )
      