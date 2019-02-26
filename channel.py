class Channel:
    def __init__(self, name, url, limit):
        self.name = name
        self.url = url
        self.limit = limit


def create_channel_list():
    channel_list = []
    channel_list.append(Channel("BlackPidgeonSpeaks", "https://www.youtube.com/user/TokyoAtomic", 3))
    channel_list.append(Channel("FarFromAverage", "https://www.youtube.com/channel/UC6Iaz96RkYE-MOjnq5NPgqw", 0))
    channel_list.append(Channel("RSDFreeTour", "https://www.youtube.com/user/rsdfreetour", 0))
    channel_list.append(Channel("CoachRedPill", "https://www.youtube.com/channel/UC5tEELgWBfKbA9fVPRzBzPQ", 0))

    return channel_list
