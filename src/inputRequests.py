import logger


log = logger.logger()

def input_operation_request_domain():
    operation_domain_number = int(input(
                            "Hello! Please, select the object you want to manage: \n"
                            " 1 - BUCKET\n "
                            "2 - FILE\n "
                            "\n "
    ))
    return operation_domain_number

def input_operation_request_for_bucket():
    operation_number = int(input(
        "Now select the operation you want to execute: \n"
        " 1 - CREATE A BUCKET\n "
        "2 - DELETE A BUCKET\n "
        "3 - RETURN AN EXISTENT BUCKET \n "
        "\n "
    ))
    return operation_number

def input_operation_request_for_file():
    operation_number = int(input(
        "Now select the operation you want to execute: \n"
        " 1 - UPLOAD A FILE\n "
        "2 - DOWNLOAD A FILE\n "
        "3 - DELETE A FILE\n "
        "\n "
    ))
    return operation_number


def input_destination_bucket_name():
    return str(input("Input the destination bucket name: "))

def input_destination_file_name():
    return str(input("Input the destination file name: "))

def input_source_file_path():
    return str(input("Input the source file path: "))