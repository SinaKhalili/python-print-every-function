"""
This is a simple script that take a file and adds a print log of the function
name and arguments to every function in the file.  For my fellow print debuggers.
"""

import ast
import argparse
import os


def add_log(node, file_name):
    """
    Add a print log of the function name and arguments
    to the function node.
    """
    func_name = node.name

    args = node.args
    arg_names = ["{" + arg.arg + "}" for arg in args.args]

    arg_str = ", ".join(arg_names)
    log_str = f'print(f"{func_name}({arg_str})", "{file_name}" )'

    log_ast = ast.parse(log_str)
    node.body.insert(0, log_ast)

    return node


def add_log_to_file(file_name, output_file_name):
    """
    Add a print log of the function name and arguments
    to every function in the file.
    """
    with open(file_name, "r") as f:
        file_str = f.read()
    file_ast = ast.parse(file_str)

    for node in ast.walk(file_ast):
        if isinstance(node, ast.FunctionDef):
            add_log(node, file_name)

    with open(output_file_name, "w") as f:
        f.write(ast.unparse(file_ast))


def log_files(dir_name, output_dir_name):
    """
    Add a log to all files in the directory.
    """
    for file in os.listdir(dir_name):
        if file.endswith(".py"):
            file_path = os.path.join(dir_name, file)
            output_file_path = os.path.join(output_dir_name, file)
            add_log_to_file(file_path, output_file_path)


def recursively_log_files(dir_name, output_dir_name):
    """
    Write the log to all files in the directory and subdirectories.
    """
    log_files(dir_name, output_dir_name)

    for dir in os.listdir(dir_name):
        dir_path = os.path.join(dir_name, dir)
        if os.path.isdir(dir_path):
            output_dir_path = os.path.join(output_dir_name, dir)
            os.mkdir(output_dir_path)
            recursively_log_files(dir_path, output_dir_path)


def main():
    """
    Add a print log of the function name and arguments
    to every function in the file.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file_or_folder",
        help="The file or folder to add the print statements to. If it's a folder, every python file will be affected.",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        help="Add logs to all files in subfolders",
        action="store_true",
        default=False,
    )

    args = parser.parse_args()
    file_or_folder = args.file_or_folder

    if os.path.isdir(file_or_folder):
        output_folder = f"{file_or_folder}_log"
        os.mkdir(output_folder)
        if args.recursive:
            recursively_log_files(file_or_folder, output_folder)
        else:
            log_files(file_or_folder, output_folder)

    elif os.path.isfile(file_or_folder):
        add_log_to_file(file_or_folder, f"{file_or_folder}.log.py")

    else:
        print("File or folder does not exist")


if __name__ == "__main__":
    main()
