media_library_path = "/media/readdeo/maindata/Videos/"
sync_latest_video_path = "/media/readdeo/maindata/SYNCH/LatestYoutube/"

# channels = {"FarFromAverage":"https://www.youtube.com/channel/UC6Iaz96RkYE-MOjnq5NPgqw",
#             "RSDFreeTour":"https://www.youtube.com/user/rsdfreetour",
#             "CoachRedPill":"https://www.youtube.com/channel/UC5tEELgWBfKbA9fVPRzBzPQ"}

# channel name, storage path, channel link
youtube_dl_link = 'youtube-dl -f {} --write-description --write-info-json --download-archive downloaded_{}.txt --no-post-overwrites --restrict-filenames -ciw -o "{}%(upload_date)s_%(title)s_%()s_%(display_id)s.%(ext)s" -v {}'
# number of videos to download, channel name, storage path, channel link
youtube_dl_link_limited = 'youtube-dl --playlist-items 1-{} -f {} --download-archive downloaded_{}.txt --no-post-overwrites --restrict-filenames -ciw -o "{}%(upload_date)s_%(title)s_%()s_%(display_id)s.%(ext)s" -v {}'

video_quality_default = "\'bestvideo[width<=854]+bestaudio/best[width<=854]\'"
video_quality_1920 = "\'bestvideo[width<=1920]+bestaudio/best[width<=1920]\'"
video_quality_1280 = "\'bestvideo[width<=1280]+bestaudio/best[width<=1280]\'"
video_quality_854 = "\'bestvideo[width<=854]+bestaudio/best[width<=854]\'"
video_quality_640 = "\'bestvideo[width<=640]+bestaudio/best[width<=640]\'"
video_quality_426 = "\'bestvideo[width<=426]+bestaudio/best[width<=426]\'"
video_quality_256 = "\'bestvideo[width<=256]+bestaudio/best[width<=256]\'"