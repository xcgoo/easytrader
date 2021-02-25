# -*- coding: utf-8 -*-
import re
import tempfile
import time

import pywinauto
import pywinauto.clipboard

from easytrader import grid_strategies
from easytrader import clienttrader
from easytrader.log import logger
from easytrader.utils.captcha import recognize_verify_code, captcha_recognize, aip_recognize


class ZXClientTrader(clienttrader.BaseLoginClientTrader):
    grid_strategy = grid_strategies.Xls
    @property
    def broker_type(self):
        return "zx"

    def login(self, user, password, exe_path, comm_password=None, **kwargs):
        """
        登陆客户端

        :param user: 账号
        :param password: 明文密码
        :param exe_path: 客户端路径类似 'C:\\中国银河证券双子星3.2\\Binarystar.exe',
            默认 'C:\\中国银河证券双子星3.2\\Binarystar.exe'
        :param comm_password: 通讯密码, 华泰需要，可不设
        :return:
        """
        try:
            self._app = pywinauto.Application().connect(path=exe_path, timeout=2)
        # pylint: disable=broad-except
        except Exception:
            self._app = pywinauto.Application().start(exe_path)

            dlg_login = self._app.window(title_re=u"中信证券", class_name="#32770")
            dlg_login.wait("ready", 100)
            # 帐号控件
            edit_account = dlg_login["ComboBox1"].child_window(control_id=1001)
            edit_account.wait("ready", 10)
            # 密码控件
            edit_password = dlg_login.child_window(control_id=0x3F4, class_name="Edit")
            edit_password.wait("ready", 5)
            # 验证码控件
            edit_ocr = dlg_login.child_window(class_name="Edit", control_id=0x3EB)

            # 输入帐号和密码
            edit_account.set_text(user)
            edit_password.type_keys(password)

            # 输入验证码
            file_path = tempfile.mktemp() + ".png"
            while dlg_login.exists():
                try:
                    im = dlg_login.child_window(control_id=0x5db).capture_as_image()
                    im.save(file_path)

                    captcha_num = aip_recognize((file_path))
                    edit_ocr.set_text(captcha_num)  # 输入验证码
                    # 点击确定
                    bt_confirm = dlg_login.child_window(control_id=0x3EE)
                    bt_confirm.wait("ready", 2)
                    bt_confirm.click()
                    time.sleep(1)
                except:
                    break
                time.sleep(0.5)

        while True:
            try:
                # self._app.active()
                # self._app.top_window().set_focus()
                # tmp_txt = self._app.top_window().window_text()
                # if tmp_txt is None or self._config.TITLE not in tmp_txt:
                #     dlg = self._app.top_window()
                #     info = dlg.child_window(title_re="请输入您的交易密码", class_name="Static")
                #     if info.exists():
                #         pass_edit = dlg.child_window(control_id=1039, class_name="Edit")
                #         pass_edit.type_keys(password)  # 输入密码
                #         dlg.child_window(class_name="Button", control_id=1).click()

                self._main = self._app.window(title_re=self._config.TITLE)
                self._main.wait("ready", timeout=100)
                break
            except:
                time.sleep(0.5)
        # 关闭弹出窗口
        self.close_pop_dialog()

    @property
    def position(self):
        self._switch_left_menus(["查询[F4]", "资金股票"])
        tmp_list = self._get_grid_data(self._config.COMMON_GRID_CONTROL_ID)
        for posi in tmp_list:
            posi["证券代码"] = posi["证券代码"][2:8]
            posi["股东代码"] = posi["股东代码"][2:12]
        return tmp_list

