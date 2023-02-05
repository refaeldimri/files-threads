import os
import threading
import time
import shutil

lock = 1


def create_files():
    """
    This function create ten txt files by loop
    and save them in the "./a" path
    :return:
    """
    try:
        for file in range(0, 10):
            f = open("./a/file " + str(file) + ".txt", "w")
            f.flush()
            f.close()
            print("file " + str(file) + ".txt" + " " + "was created")
            time.sleep(2)
    except FileExistsError as e:
        print(e)


def copy_dir(origin, target):
    """
    This function copy all the files form
    directory and move it to target, the files
    will be removed from the origin directory
    :param origin:
    :param target:
    :return:
    """

    while os.listdir(target) != 10:
        # Fetch from origin directory files
        list_files = os.listdir(origin)

        # check if there are files in the directory
        if len(list_files) > 0:
            # loop through files list and copy each
            # to destination folder
            try:
                time.sleep(3)
                for file_name in list_files:
                    shutil.copy(origin + file_name, target + file_name)
                    os.remove(origin + file_name)
                    print(file_name + " " + "was copied")
            except FileNotFoundError as e:
                print(e)


if __name__ == '__main__':
    origin1 = "./a/"
    target1 = "./b/"

    t1 = threading.Thread(target=create_files)
    t2 = threading.Thread(target=copy_dir, args=(origin1, target1))

    t1.start()
    t2.start()
