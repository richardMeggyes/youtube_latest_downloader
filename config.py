import os

media_library_path = "/media/readdeo/maindata/Videos/"
sync_latest_video_path = "/media/readdeo/maindata/SYNCH/LatestYoutube/"
archive_path = os.getcwd() + 'archive'

# channel name, storage path, channel link
#youtube_dl_link = 'youtube-dl -f {} --write-description --write-info-json --download-archive downloaded_{}.txt --no-post-overwrites --restrict-filenames -ciw -o "{}%(upload_date)s_%(title)s_%()s_%(display_id)s.%(ext)s" -v {}'
# number of videos to download, channel name, storage path, channel link
#youtube_dl_link_limited = 'youtube-dl --playlist-items 1-{} -f {} --download-archive downloaded_{}.txt --no-post-overwrites --restrict-filenames -ciw -o "{}%(upload_date)s_%(title)s_%()s_%(display_id)s.%(ext)s" -v {}'

youtube_dl_beginning = 'youtube-dl'
youtube_dl_quality = '-f {}'
youtube_dl_save_data = '--write-description --write-thumbnails'
youtube_dl_download_archive = '--download-archive ' + os.path.join(archive_path, 'downloaded_{}.txt')
youtube_dl_other_switches = '--sleep-interval 10 --cookies --no-post-overwrites --restrict-filenames -ciw'
youtube_dl_output_file_name = '-o "{}%(upload_date)s_%(title)s_%()s_%(display_id)s.%(ext)s"'
youtube_dl_channel_to_download = '-v {}'

"""
-ciw is 3 parameter options combined
-c, --continue  [Force resume of partially downloaded files]
-i, --ignore-errors [Continue on download errors, for example to skip unavailable videos in a playlist]
-w, --no-overwrites  [Do not overwrite files]

--restrict-filenames
it makes the file name ascii character only, no white spaces and &
"""

video_quality_default = "\'bestvideo[width<=854]+bestaudio/best[width<=854]\'"
video_quality_best = "\'bestvideo[width<=854]+bestaudio/best[width<=854]\'"
video_quality_1920 = "\'bestvideo[width<=1920]+bestaudio/best[width<=1920]\'"
video_quality_1280 = "\'bestvideo[width<=1280]+bestaudio/best[width<=1280]\'"
video_quality_854 = "\'bestvideo[width<=854]+bestaudio/best[width<=854]\'"
video_quality_640 = "\'bestvideo[width<=640]+bestaudio/best[width<=640]\'"
video_quality_426 = "\'bestvideo[width<=426]+bestaudio/best[width<=426]\'"
video_quality_256 = "\'bestvideo[width<=256]+bestaudio/best[width<=256]\'"
