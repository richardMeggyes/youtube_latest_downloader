import os
from config import *


def download_command(channel):
    return ''.join([youtube_dl_beginning, ' ',
                    youtube_dl_quality.format(channel.quality), ' ',
                    youtube_dl_save_data, ' ',
                    youtube_dl_download_archive.format(channel.name), ' ',
                    youtube_dl_other_switches, ' ',
                    youtube_dl_output_file_name.format(channel.storage_path), ' ',
                    youtube_dl_channel_to_download.format(channel.url)])
