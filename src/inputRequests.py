import logger

log = logger.logger()

def input_domain():
    domain_request = int(input(
                            "Hello! Please, select the action you want to execute: \n"
                            " 1 - GET some storage infos\n "
                            "2 - MANAGE storage objects\n "
                            "\n "
    ))
    return domain_request

def input_to_get_info():
    info_request = int(input(
                            "Now select the info you want to retrieve: \n"
                            " 1 - File size\n "
                            "2 - List of files within a bucket\n "
                            "\n "
    ))
    return info_request

def input_operation():
    operation_request = int(input(
                            "Now select the object you want to manage: \n"
                            " 1 - BUCKET\n "
                            "2 - FILE(blob)\n "
                            "\n "
    ))
    return operation_request

def input_bucket_operation():
    operation_request = int(input(
        "Finally select the operation you want to execute: \n"
        " 1 - CREATE BUCKET\n "
        "2 - DELETE BUCKET\n "
        "3 - UPDATE BUCKET STORAGE CLASS \n "
        "\n "
    ))
    return operation_request

def input_file_operation():
    operation_request = int(input(
        "Finally select the operation you want to execute: \n"
        " 1 - UPLOAD FILE\n "
        "2 - DOWNLOAD FILE\n "
        "3 - DELETE FILE\n "
        "4 - WRITE TO FILE\n "
        "5 - READ FROM FILE\n "
        "6 - UPDATE FILE STORAGE CLASS\n "
        "\n "
    ))
    return operation_request


def input_destination_bucket_name():
    return str(input("Input the destination bucket name: "))

def input_destination_file_name():
    return str(input("Input the destination file name: "))

def input_source_file_path():
    return str(input("Input the source file path: "))

def input_storage_class():
    return str(input("Input the new bucket storage class [Standard, Nearline, Coldline]: "))

def input_file_prefix():
    return str(input("Input file prefix: "))

def input_message():
    return str(input("Input message: "))