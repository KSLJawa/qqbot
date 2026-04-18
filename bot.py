import nonebot
from nonebot.adapters.onebot.v11 import Adapter as OneBotV11Adapter
from models.models import init_db

# 初始化数据库
init_db()

# 初始化NoneBot
nonebot.init()

# 获取驱动器
driver = nonebot.get_driver()

# 注册OneBot V11适配器
driver.register_adapter(OneBotV11Adapter)

# 加载插件
nonebot.load_plugins("plugins")

if __name__ == "__main__":
    nonebot.run()