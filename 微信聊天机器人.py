from wxpy import Bot

bot = Bot()

# 机器人账号自身
myself = bot.self

# 向文件传输助手发送消息
bot.file_helper.send('Hello from wxpy!')