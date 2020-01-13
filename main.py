import os
import time

import downloader
from channel import create_channel_list
from config import archive_path, media_library_path


def pre_check():
    if not os.path.isdir(archive_path):
        os.mkdir(archive_path)
    if not os.path.isdir(media_library_path):
        os.mkdir(media_library_path)


if __name__ == "__main__":

    channels = create_channel_list()
    while True:

        for channel in channels:

            if not os.path.isdir(channel.storage_path):
                os.mkdir(channel.storage_path)

            if channel.limit == 0:
                os.system(downloader.download_command(channel))
            else:
                pass

        print("Finished, waiting 2 hours before downloading again")
        time.sleep(7200)
