from google.cloud import bigquery
import sys
from csv import reader
from csv import writer

# open file in read mode

# Construct a BigQuery client object.
client = bigquery.Client()

with open('write_to.csv', 'w' , newline = '') as write_obj:
    csv_writer = writer(write_obj)
    # next(csv_writer, None)
    csv_writer.writerow(['SOURCE','DESTINATION','EMAIL','ROLE'])
    with open(r'read_from.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        next(csv_reader, None)  # skip the headers
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            source_dataset_id=row[0].replace(':','.').strip()
            destination_dataset_id=row[1].replace(':','.').strip()

            dataset = client.get_dataset(source_dataset_id)  # Make an API request.
            
            entries = list(dataset.access_entries) 

            # Iterate over access entry objects in the list
            for entry in entries:
                
                # If entity_type property of the access entry object is "userByEmail" append the object to the csv
                if entry.entity_type=="userByEmail":
                    csv_writer.writerow([source_dataset_id,destination_dataset_id,entry.entity_id,entry.role])
                

print("EmailIds & Roles updated in the write_to.csv")



        


       