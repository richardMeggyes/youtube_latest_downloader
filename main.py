from config import *
import time, os, sys
from channel import create_channel_list


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    pb_string = '\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix)

    return pb_string


if __name__ == "__main__":
    args = sys.argv

    loop = False

    if len(args) > 1:
        if args[1] == "-l" or args[1] == "--loop":
            loop = True

    channels = create_channel_list()
    while True:

        for channel in channels:
            channel_storage_path = media_library_path + channel.name + "/"
            channel_youtube_link = channel.url

            if not os.path.isdir(channel_storage_path):
                os.mkdir(channel_storage_path)

            youtube_dl_command = ""
            if channel.limit == 0:
                youtube_dl_command = youtube_dl_link.format(channel.quality,
                                                            channel.name,
                                                            channel_storage_path,
                                                            channel_youtube_link)
            else:
                pass
                # youtube_dl_command = youtube_dl_link_limited.format(channel.limit, channel.name,
                #                                                     channel_storage_path, channel_youtube_link)

            # with open("commands.txt", "a+")as f:
            #     f.write(youtube_dl_command + "\n")

            os.system(youtube_dl_command)

            # file_tools.copy_3_latest_files(channel)

        # file_tools.remove_older_videos_from_sync()

        if not loop:
            break
        print("Finished, waiting 30 minutes before downloading again")
        time.sleep(1800)
