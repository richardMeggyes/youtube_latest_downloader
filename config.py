media_library_path = "/media/readdeo/ultrabay/Videos/"
sync_latest_video_path = "/media/readdeo/maindata/SYNCH/LatestYoutube/"

# channels = {"FarFromAverage":"https://www.youtube.com/channel/UC6Iaz96RkYE-MOjnq5NPgqw",
#             "RSDFreeTour":"https://www.youtube.com/user/rsdfreetour",
#             "CoachRedPill":"https://www.youtube.com/channel/UC5tEELgWBfKbA9fVPRzBzPQ"}

# channel name, storage path, channel link
youtube_dl_link = 'youtube-dl -f \'bestvideo[height<=480]+bestaudio/best[height<=480]\' --download-archive downloaded_{}.txt --no-post-overwrites --restrict-filenames -ciw -o "{}%(upload_date)s_%(title)s_%()s_%(display_id)s.%(ext)s" -v {}'
# number of videos to download, channel name, storage path, channel link
youtube_dl_link_limited = 'youtube-dl --playlist-items 1-{} -f \'bestvideo[height<=480]+bestaudio/best[height<=480]\' --download-archive downloaded_{}.txt --no-post-overwrites --restrict-filenames -ciw -o "{}%(upload_date)s_%(title)s_%()s_%(display_id)s.%(ext)s" -v {}'
