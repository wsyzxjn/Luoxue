import os.path
import yaml
from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost

"""
在收到私聊或群聊消息"hello"时，回复"hello, <发送者id>!"或"hello, everyone!"
"""


# 注册插件
@register(name="Luoxue", description="hello world", version="0.1", author="Amatsuka")
class HelloPlugin(Plugin):

    # 插件加载时触发
    # plugin_host (pkg.plugin.host.PluginHost) 提供了与主程序交互的一些方法，详细请查看其源码
    def __init__(self, plugin_host: PluginHost):
        pass


    # 当收到个人消息时触发
    @on(PersonNormalMessageReceived)
    def person_normal_message_received(self, event: EventContext, **kwargs):
        msg = kwargs['text_message']
        if msg == "jtj":  # 如果消息为jtj
            this_path = os.getcwd()
            DataFile = open(f"{this_path}/plugins/Luoxue/data.json")
            DataText = DataFile.read()
            if not DataText:
                message = "当前无上报数据"
            else:
                message = "True"

            # 输出调试信息
            logging.debug(message+str(kwargs['sender_id']))

            # 回复消息 "hello, <发送者id>!"

            event.add_return("reply", [message])

            # 阻止该事件默认行为（向接口获取回复）
            event.prevent_default()

    # 当收到群消息时触发
    @on(GroupNormalMessageReceived)
    def group_normal_message_received(self, event: EventContext, **kwargs):
        msg = kwargs['text_message']
        this_path = os.getcwd()

        if msg == "jtj":  # 如果消息为jtj

            data = open(f"{this_path}/plugins/Luoxue/data.json").read()
            if not data:
                reply = "当前无上报数据"
            else:
                reply = "True"

        #增添匹配
        yaml_text = open(f"{this_path}/plugins/Luoxue/config.yaml").read()
        config = yaml.load(yaml_text)
        for key,values in config.items():
            if msg == values+"j":
                reply = key
                break



        # 输出调试信息
        logging.debug(reply+str(kwargs['sender_id']))

        # 回复消息 "hello, <发送者id>!"

        event.add_return("reply", [reply])
        # 阻止该事件默认行为（向接口获取回复）
        event.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
