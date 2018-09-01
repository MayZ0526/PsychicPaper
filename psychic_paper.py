import os
import random


def send_image_to_display(image):
    print(image)


def get_random_image(directory, recursive=False):
    """
    Will pull a random image from directory based on extension list

    :param directory: Path to look for files.
    :param recursive: Flag to look recursively through subdirectories
    :return: Path to randomly selected image
    """

    supported_image_extensions = ('.png', '.jpg', '.bmp')

    if not os.path.isdir(directory):
        raise IsADirectoryError
    else:
        directory_contents = get_directory_contents(directory=directory, recursive=recursive)
        images = [item for item in directory_contents if item.endswith(supported_image_extensions)]
        return images[int(random.random()*len(images))]


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


def run_psychic_paper():
    image = get_random_image(directory=os.path.join('C:\\', 'temp'), recursive=True)
    send_image_to_display(image=image)


if __name__ == '__main__':
    run_psychic_paper()
