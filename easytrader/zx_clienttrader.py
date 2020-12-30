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
                    self._main = self._app.window(title_re=self._config.TITLE)
                    self._main.wait("ready", timeout=100)
                    break
                except:
                    time.sleep(0.5)
            # 关闭弹出窗口
            self.close_pop_dialog()

    # def auto_ipo(self):
    #     self.close_pop_dialog()
    #     logger.info(f"begin to subscribe the IPO stocks.")
    #     time.sleep(0.2)
    #     self._switch_left_menus(self._config.AUTO_IPO_MENU_PATH)
    #     time.sleep(0.5)
    #     control_select_all = self._main.child_window(title_re=u"全部选中", class_name="Button")  # 全部选中按钮
    #     control_sg = self._main.child_window(title_re=u"申购", class_name="Button")  # 申购按钮
    #     dict_new_stk = self._get_grid_data(self._config.COMMON_GRID_CONTROL_ID)
    #     ipo_count = len(dict_new_stk)
    #     if ipo_count > 0:
    #         time.sleep(0.3)
    #         control_select_all.click()
    #         control_sg.click()
    #         # 确认窗口
    #         time.sleep(0.2)
    #         wt_confirm_hwnd = self._main.popup_window()
    #         wt_confirm = self._main.child_window(handle=wt_confirm_hwnd)
    #         okbt = wt_confirm.child_window(class_name="Button", control_id=6)
    #         time.sleep(0.5)
    #         okbt.click_input()
    #         logger.info(f"subscribed the IPO stocks.")
    #         self.close_pop_dialog()
    #     else:
    #         logger.info(f"No IPO today.")
