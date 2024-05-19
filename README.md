# _Google Cloud Storage Asset Library_


  </a>
  <a href="https://www.python.org/downloads/release/python-311">
    <img src="https://img.shields.io/badge/python-3.11-lightgreen.svg" lazyload />
  </a>
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/GoogleCloud lib-0.34.0-lightblue.svg" lazyload />
  </a>
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/CloudStorage lib-2.16.0-blue.svg" lazyload />
  </a>

####

## References

[Poetry Doc](https://python-poetry.org/docs/)

[Cloud Storage Doc](https://cloud.google.com/storage/docs?hl=i)

## Introduction

The Google Cloud Storage (GCS) Python library provides a simple yet powerful interface
for interacting with Google Cloud Storage buckets and objects directly from your Python code.
With this library, you can easily manage and manipulate objects and buckets in GCS using just 
a few lines of Python code.
Whether you're building a web application, a mobile application, or a data analytics application, 
the Google Cloud Storage Python library allows you to easily integrate the power and scalability 
of GCS into your Python applications.


## Main Architecture

The structure of the project is based on the Object Oriented Paradigm.
####
The first class implemented in the **cloudClientConnector.py**:
    
    class CloudStorageClient(CloudClient)
    -> Variables: client
    -> Methods:
        - def connect()
        - def get_client()

is used to encapsulate the Cloud Storage client connection operations.
####
In the **storageGetter.py** other two classes are defined:
    
    class BucketGetter
    -> Variables: bucket_name, __storage_client
    -> Methods:
        - def declare_bucket()
        - def get_bucket()
        - def list_buckets()
        - def list_files()

    class FileGetter
    -> Variables: file_name, bucket_name, __bucket_getter
    -> Methods:
        - def declare_file()
        - def get_file()
        - def get_file_size()

that consent to instantiate a Bucket object and a File object 
containing the get methods in order to have access to the storage object desired. 

####

This classes are used in the "Manager" layer which represents the basic modules 
on which to build an application. 
It is composed by two main classes:
(EXTEND WITH THE MANAGER CLASSES)
Finally all the logs generated are customized in the **logger.py**.

## Code Flow

<p align="center">
  <img src="doc\img\GCS_ASSET_CODE_FLOW.png" />
</p>
<br>