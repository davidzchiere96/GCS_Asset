import logging

def input_operation_request():
    operation_number = int(input(
                            "Hello! Please, select the operation you want to execute: \n"
                            " 1 - CREATE A BUCKET\n "
                            "2 - UPLOAD A FILE\n "
                            "3 - RETURN AN EXISTENT BUCKET \n "
                            "\n "
    ))
    return operation_number

def input_destination_bucket_name():
    return str(input("Input the destination bucket name: "))

def input_destination_file_name():
    return str(input("Input the destination file name: "))

def input_source_file_path():
    return str(input("Input the source file path: "))