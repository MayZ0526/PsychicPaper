def get_directory_contents(directory, recursive=False):
    """
    Gets list of all items in a directory. Gets subdirectory items as well if recursive flag is set to True
    :param directory: Path to look for items
    :param recursive: Flag to look recursively through subdirectories
    :return: List of items in directory
    """

    directory_contents = [os.path.join(directory, item) for item in os.listdir(directory)]

    if not recursive:
        return directory_contents
    else:
        sub_directories = [item for item in directory_contents if os.path.isdir(item)]

        for sub_directory in sub_directories:
            if get_directory_contents(sub_directory):
                directory_contents.extend(get_directory_contents(sub_directory, recursive=recursive))

        return directory_contents
