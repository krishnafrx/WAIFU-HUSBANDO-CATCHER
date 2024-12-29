class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5457689317"
    sudo_users = "5457689317"
    GROUP_ID = -1001875294969
    TOKEN = "6707490163:AAHZzqjm3rbEZsObRiNaT7DMtw_i5WPo_0o"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "team_cyclone"
    UPDATE_CHAT = "team_cyclone"
    BOT_USERNAME = "Catch_your_waifu_bot
    CHARA_CHANNEL_ID = "-1001875294969"
    api_id = 24302435
    api_hash = "a814be3b1816d5a7dce5f1f75aa6d28d"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
