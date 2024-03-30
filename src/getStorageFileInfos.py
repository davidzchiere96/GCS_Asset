
import cloudStorageClient
from google.cloud import storage

# Read from Cloud Storage
def get_files(bucket, prefix):
    # Get the list of files with that prefix
    client = storage.Client()
    bucket = client.get_bucket(bucket)
    blobs = bucket.list_blobs(prefix=prefix, versions=False)

    # Return only the metadata to be used
    metadata = []
    for blob in blobs:
        metadata.append({
            'name': blob.name,
            'size': blob.size,
            'created_time': blob.time_created.strftime("%Y-%m-%dT%H:%M:%S")
        })

    return metadata