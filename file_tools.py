import os, shutil
from shutil import copyfile
from config import sync_latest_video_path, media_library_path
from channel import create_channel_list


def get_latest_files_from_path(path, limit):
    if limit == 0:
        limit = 3
    video_list = os.listdir(path)
    video_list.sort()
    latest_video_list = video_list[len(video_list) - limit:len(video_list)]
    latest_video_list.reverse()
    return latest_video_list


def copy_3_latest_files(channel):
    channel_storage_path = media_library_path + channel.name + "/"
    latest_files = get_latest_files_from_path(channel_storage_path, channel.limit)
    for file in latest_files:
        original_file_path = channel_storage_path + file
        new_file_path = sync_latest_video_path + channel.name + "_" + file
        if not os.path.isfile(new_file_path):
            print("Copying file: " + file)
            copyfile(original_file_path, new_file_path)


def get_all_latest_videos():
    channels = create_channel_list()
    latest_videos = []
    for channel in channels:
        channel_videos_path = media_library_path + channel.name
        latest_videos_of_channel = get_latest_files_from_path(channel_videos_path, channel.limit)
        latest_videos += latest_videos_of_channel
    return latest_videos


def remove_older_videos_from_sync():
    latest_videos = get_all_latest_videos()
    all_videos = os.listdir(sync_latest_video_path)
    all_videos_original = os.listdir(sync_latest_video_path)

    for x in range(len(all_videos)):
        file_name = all_videos[x]
        file_name = file_name.split("_")
        file_name.pop(0)
        new_file_name = ""
        for string in file_name:
            new_file_name += string + "_"
        new_file_name = new_file_name[:-1]
        all_videos[x] = new_file_name

    for x in range(len(all_videos)):
        if all_videos_original[x] == ".stfolder": continue
        if all_videos[x] not in latest_videos:
            if os.path.isfile(sync_latest_video_path + all_videos_original[x]):
                print("Removing file: " + all_videos_original[x])
                os.remove(sync_latest_video_path + all_videos_original[x])
            else: print("File to remove not found:", sync_latest_video_path + all_videos_original[x])

    for channel in create_channel_list():
        if channel.limit > 0:
            print("removing folder: " + media_library_path + channel.name)
            shutil.rmtree(media_library_path + channel.name)
