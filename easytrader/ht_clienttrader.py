# -*- coding: utf-8 -*-

import pywinauto
import pywinauto.clipboard

from easytrader import grid_strategies
from . import clienttrader
import time


class HTClientTrader(clienttrader.BaseLoginClientTrader):
    grid_strategy = grid_strategies.Xls

    @property
    def broker_type(self):
        return "ht"

    def login(self, user, password, exe_path, comm_password=None, **kwargs):
        """
        :param user: 用户名
        :param password: 密码
        :param exe_path: 客户端路径, 类似
        :param comm_password:
        :param kwargs:
        :return:
        """
        self._editor_need_type_keys = False
        if comm_password is None:
            raise ValueError("华泰必须设置通讯密码")

        try:
            self._app = pywinauto.Application().connect(path=self._run_exe_path(exe_path), timeout=1)
        # pylint: disable=broad-except
        except Exception:
            self._app = pywinauto.Application().start(exe_path)

            dlg_login = self._app.window(title_re=u"用户登录", class_name="#32770")
            dlg_login.wait("ready", 100)
            # 帐号
            edit_account = dlg_login['Edit1']
            # 密码
            edit_password = dlg_login['Edit2']
            # 通讯密码
            edit_commpsw = dlg_login['Edit3']

            # 确定
            while dlg_login.exists():
                try:
                    edit_account.set_text(user)
                    edit_password.set_text(password)
                    edit_commpsw.set_text(comm_password)

                    bt_confirm = dlg_login.child_window(title_re=u'确定', class_name="Button")
                    bt_confirm.wait("ready", 2)
                    bt_confirm.click()
                except:
                    break
                time.sleep(0.5)

        while True:
            try:
                self._app.active()
                self._app.top_window().set_focus()
                tmp_txt = self._app.top_window().window_text()
                if tmp_txt is None or self._config.TITLE not in tmp_txt:
                    dlg = self._app.top_window()
                    info = dlg.child_window(title_re="请输入您的交易密码", class_name="Static")
                    if info.exists():
                        pass_edit = dlg.child_window(control_id=1039, class_name="Edit")
                        pass_edit.type_keys(password)  # 输入密码
                        dlg.child_window(class_name="Button", control_id=1).click()
                    else:
                        logger.info("最顶层窗口非主窗口，程序终止运行！")
                        return
                else:
                    self._main = self._app.window(title_re=self._config.TITLE)
                    self._main.wait("ready", timeout=100)
                    break
            except:
                time.sleep(0.5)

        # 关闭弹出窗口
        self.close_pop_dialog()

    @property
    def balance(self):
        self._switch_left_menus(self._config.BALANCE_MENU_PATH)

        return self._get_balance_from_statics()

    def _get_balance_from_statics(self):
        result = {}
        for key, control_id in self._config.BALANCE_CONTROL_ID_GROUP.items():
            result[key] = float(
                self._main.child_window(
                    control_id=control_id, class_name="Static"
                ).window_text()
            )
        return result


