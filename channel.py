import config
import os


class Channel:
    def __init__(self, name, url, limit, quality):
        self.name = name
        self.url = url
        self.limit = limit
        self.quality = quality
        self.storage_path = os.path.join(config.media_library_path, self.name) + '/'


def create_channel_list():
    channel_list = []

    # RSD
    channel_list.append(Channel("RSDTyler", "https://www.youtube.com/user/RSDTyler", 0, config.video_quality_default))
    channel_list.append(Channel("RSDJeffy", "https://www.youtube.com/user/RSDJeffy", 0, config.video_quality_default))
    channel_list.append(Channel("JulienHimself", "https://www.youtube.com/channel/UCaN4Pe5JEsWzAByY2WfxxjQ/videos", 0, config.video_quality_default))
    channel_list.append(Channel("RSDMaximilian", "https://www.youtube.com/user/RSDMaximilian", 0, config.video_quality_default))
    channel_list.append(Channel("MontrealRSDCrew", "https://www.youtube.com/user/MontrealRSDCrew", 0, config.video_quality_default))
    channel_list.append(Channel("RSDLuke", "https://www.youtube.com/channel/UC2XMvfBq5w2P4_ZYOsMlxVg", 0, config.video_quality_default))
    channel_list.append(Channel("RSDFreeTour", "https://www.youtube.com/user/rsdfreetour", 0, config.video_quality_default))

    # RedPill / self improvement
    channel_list.append(Channel("FarFromAverage", "https://www.youtube.com/channel/UC6Iaz96RkYE-MOjnq5NPgqw", 0, config.video_quality_default))
    channel_list.append(Channel("CoachRedPill", "https://www.youtube.com/channel/UC5tEELgWBfKbA9fVPRzBzPQ", 0, config.video_quality_default))
    channel_list.append(Channel("AlphaM", "https://www.youtube.com/user/AlphaMconsulting/videos", 0, config.video_quality_default))
    channel_list.append(Channel("21Studios", "https://www.youtube.com/user/Under21convention07/videos", 0, config.video_quality_default))

    # Politics / world view
    #channel_list.append(Channel("BlackPidgeonSpeaks", "https://www.youtube.com/user/TokyoAtomic", 0, config.video_quality_default))

    # Car
    channel_list.append(Channel("ChrisFix", "https://www.youtube.com/user/PaintballOO7/videos", 0, config.video_quality_default))
    channel_list.append(Channel("ScottyKilmer", "https://www.youtube.com/user/scottykilmer/videos", 0, config.video_quality_default))

    # Cooking
    channel_list.append(Channel("SzokyKonyhaja", "https://www.youtube.com/user/MrSzoky68", 0, config.video_quality_default))

    # My lists
    channel_list.append(Channel("LIST_AUTO_DOWNLOAD", "https://www.youtube.com/playlist?list=PLGIBmiqt7aCRdF4V23BvrH32mjk846z1Q", 0, config.video_quality_default))
    channel_list.append(Channel("LIST_RECIPE", "https://www.youtube.com/playlist?list=PLGIBmiqt7aCSkvRhfk6tV47gb5YVV-8L4", 0, config.video_quality_default))
    channel_list.append(Channel("LIST_HOME_PLANNING", "https://www.youtube.com/playlist?list=PLGIBmiqt7aCT2iW5TP6Ae5ACjbDZn369R", 0, config.video_quality_default))

    return channel_list
