# BigQuery - Copy Delta permissions from Dataset to Dataset

This tutorial describes how to copy the delta permissions from one BigQuery Dataset to another BigQuery Dataset.

# Prerequisites
## Configuration file
* List of BigQuery Dataset source and destination in the read_from.csv file with following format:
    *   Contains Source & Destination column
    *   (Source - DatasetId who's permission is to be read) 
    *   (Destination - DatasetId to which the permission is to be applied ) 
```
Source,Destination
<project_id>:<dataset_id>,<project_id>:<dataset_id>
```
## GCP Permissions
Following permissions are required for the Python scripts to execute properly. [More details here](https://cloud.google.com/bigquery/docs/access-control#bigquery)
* BigQuery Data Owner (roles/bigquery.dataOwner)
* BigQuuery Admin (roles/bigquery.admin)

## Environment
* Install python3 
* Install Python Google Cloud Library
``` pip3 install google-cloud-bigquery ```
* Install gcloud sdk
* Configure gcloud environment. [More details here](https://cloud.google.com/sdk/docs/initializing)
``` 
gcloud init
gcloud auth application-default login
gcloud config configurations list
```


# Execution
Two steps process to read the permissions from the source, then review it manually and update the permissions in the destination. For that purpose, there are two Python scripts:
1. **bq_read_permissions_from_source.py**: this python script read each row of the read_from.csv and fetches the permissions from the source dataset_id and further writes the necessary data into the write_to.csv
2. **bq_update_permissions_destination.py**: this python script read each row of the write_to.csv and updates the permissions on the destination dataset_id


*  Read the BigQuery Dataset permissions from the source:
```
    python3 bq_read_permissions_from_source.py
```
* Review manually the generated file write_to.csv to adjust the permissions (manual step)
    * Contains Source, Destination, Email, Role column
    *   (Source - DatasetId who's permission is to be read) 
    *   (Destination - DatasetId to which the permission is to be applied ) 
    *   (Email - Entity_ID to which we need to provide permission )
    *   (Role - Role we need to provide to the Entity_ID)
* Update the BigQuery Dataset permissions to add the delta permissions to the destination
```
    python3 bq_update_permissions_destination.py 
```
