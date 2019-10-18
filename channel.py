import config

class Channel:
    def __init__(self, name, url, limit, quality):
        self.name = name
        self.url = url
        self.limit = limit
        self.quality = quality


def create_channel_list():
    channel_list = []
    # channel_list.append(Channel("BlackPidgeonSpeaks", "https://www.youtube.com/user/TokyoAtomic", 3))
    channel_list.append(Channel("FarFromAverage", "https://www.youtube.com/channel/UC6Iaz96RkYE-MOjnq5NPgqw", 0, config.video_quality_854))
    channel_list.append(Channel("RSDFreeTour", "https://www.youtube.com/user/rsdfreetour", 0, config.video_quality_854))
    channel_list.append(Channel("CoachRedPill", "https://www.youtube.com/channel/UC5tEELgWBfKbA9fVPRzBzPQ", 0, config.video_quality_854))
    channel_list.append(Channel("RSDTyler", "https://www.youtube.com/user/RSDTyler", 0, config.video_quality_854))
    channel_list.append(Channel("RSDJeffy", "https://www.youtube.com/user/RSDJeffy", 0, config.video_quality_854))
    channel_list.append(Channel("JulienHimself", "https://www.youtube.com/channel/UCaN4Pe5JEsWzAByY2WfxxjQ/videos", 0, config.video_quality_854))
    channel_list.append(Channel("RSDMaximilian", "https://www.youtube.com/user/RSDMaximilian", 0, config.video_quality_854))
    channel_list.append(Channel("MontrealRSDCrew", "https://www.youtube.com/user/MontrealRSDCrew", 0, config.video_quality_854))
    channel_list.append(Channel("RSDLuke", "https://www.youtube.com/channel/UC2XMvfBq5w2P4_ZYOsMlxVg", 0, config.video_quality_854))

    return channel_list
