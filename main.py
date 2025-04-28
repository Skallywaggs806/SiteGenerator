from src import *
import os
import shutil
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def copy_static_to_public():
    """
    Copy static files from the static directory to the public directory.
    """
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    public_dir = os.path.join(os.path.dirname(__file__), "public")

    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    
    os.mkdir(public_dir)

    copy_recursive(static_dir, public_dir)


def copy_recursive(src, dst):
    """
    Recursively copy files and directories from src to dst.
    """
    if os.path.isdir(src):
        if not os.path.exists(dst):
            os.mkdir(dst)
            logging.info(f"Created directory: {dst}")
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            logging.info(f"Copying: {s} -> {d}")
            copy_recursive(s, d)
    else:
        shutil.copy2(src, dst)
        logging.info(f"Copied file: {src} -> {dst}")







def main():

    copy_static_to_public()
    print("Static files copied to public directory.")




if __name__ == "__main__":
    main()
