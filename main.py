from PyQt5 import uic
from .ClassWidgets.base import PluginBase, SettingsBase  # 导入CW的基类
import tempfile
import os

class Plugin(PluginBase):  # 插件类
    def __init__(self, cw_contexts, method):  # 初始化
        super().__init__(cw_contexts, method)  # 调用父类初始化方法
        self.plugin_dir = self.cw_contexts['PLUGIN_PATH']
        self.temp_dir = tempfile.gettempdir()

    def execute(self):
        pass

    def listen(self):
        if os.path.exists("%s\\unread"%self.temp_dir):
            os.remove("%s\\unread"%self.temp_dir)
            with open("%s\\res.txt"%self.temp_dir,"r",encoding="utf-8") as f:
                msg = f.read()
            self.method.send_notification(
                state=4,
                title='抽选结果',
            subtitle = '被抽中的幸运儿',
            content = str(msg),
            icon = f'{self.plugin_dir}/assets/NamePicker.png',
            duration = 3000  # 通知将显示5秒
            )

    def update(self, cw_contexts):
        super().update(cw_contexts)
        self.listen()