import unittest
import config
from channel import Channel
import downloader

class TestSum(unittest.TestCase):

    def test_youtube_dl_cmd(self):
        channel = Channel("RSDTyler", "https://www.youtube.com/user/RSDTyler", 0, config.video_quality_best)
        cmd = downloader.download_command(channel)
        expected = 'youtube-dl -f \'bestvideo[width<=640]+bestaudio/best[width<=640]\' --write-description --write-info-json --download-archive downloaded_RSDTyler.txt --no-post-overwrites --no-post-overwrites --restrict-filenames -ciw -o "/media/readdeo/maindata/Videos/RSDTyler/%(upload_date)s_%(title)s_%()s_%(display_id)s.%(ext)s" -v https://www.youtube.com/user/RSDTyler'

        self.assertEqual(cmd, expected, "Should match")


if __name__ == "__main__":
    unittest.main()