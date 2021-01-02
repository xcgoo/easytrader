# -*- coding: utf-8 -*-
def create(broker):
    if broker == "yh":
        return YH
    if broker == "ht":
        return HT
    if broker == "gj":
        return GJ
    if broker == "gf":
        return GF
    if broker == "ths":
        return CommonConfig
    if broker == "wk":
        return WK
    if broker == "htzq":
        return HTZQ
    if broker == "zx":
        return ZX
    if broker == "cj":
        return CJ
    raise NotImplementedError


class CommonConfig:
    DEFAULT_EXE_PATH: str = ""
    TITLE = "网上股票交易系统5.0"

    # 交易所类型。 深圳A股、上海A股
    TRADE_STOCK_EXCHANGE_CONTROL_ID = 1003

    # 撤销界面上， 全部撤销按钮
    TRADE_CANCEL_ALL_ENTRUST_CONTROL_ID = 30001

    TRADE_SECURITY_CONTROL_ID = 1032
    TRADE_PRICE_CONTROL_ID = 1033
    TRADE_AMOUNT_CONTROL_ID = 1034

    TRADE_SUBMIT_CONTROL_ID = 1006

    TRADE_MARKET_TYPE_CONTROL_ID = 1541

    COMMON_GRID_CONTROL_ID = 1047

    COMMON_GRID_LEFT_MARGIN = 10
    COMMON_GRID_FIRST_ROW_HEIGHT = 30
    COMMON_GRID_ROW_HEIGHT = 16

    BALANCE_MENU_PATH = ["查询[F4]", "资金股票"]
    POSITION_MENU_PATH = ["查询[F4]", "资金股票"]
    TODAY_ENTRUSTS_MENU_PATH = ["查询[F4]", "当日委托"]
    TODAY_TRADES_MENU_PATH = ["查询[F4]", "当日成交"]

    BALANCE_CONTROL_ID_GROUP = {
        "资金余额": 1012,
        "可用金额": 1016,
        "可取金额": 1017,
        "股票市值": 1014,
        "总资产": 1015,
    }

    POP_DIALOD_TITLE_CONTROL_ID = 1365

    GRID_DTYPE = {
        "操作日期": str,
        "委托编号": str,
        "申请编号": str,
        "合同编号": str,
        "证券代码": str,
        "股东代码": str,
        "资金帐号": str,
        "资金帐户": str,
        "发生日期": str,
    }

    CANCEL_ENTRUST_ENTRUST_FIELD = "合同编号"
    CANCEL_ENTRUST_GRID_LEFT_MARGIN = 50
    CANCEL_ENTRUST_GRID_FIRST_ROW_HEIGHT = 30
    CANCEL_ENTRUST_GRID_ROW_HEIGHT = 16

    AUTO_IPO_SELECT_ALL_BUTTON_CONTROL_ID = 1098
    AUTO_IPO_BUTTON_CONTROL_ID = 1006
    AUTO_IPO_MENU_PATH = ["新股申购", "批量新股申购"]
    AUTO_IPO_NUMBER = '申购数量'

    POSITION_COMPARE_ITEMS = ["股票余额", "可用余额", "冻结数量", "成本价"]


class YH(CommonConfig):
    DEFAULT_EXE_PATH = r"C:\双子星-中国银河证券\Binarystar.exe"

    BALANCE_GRID_CONTROL_ID = 1308

    GRID_DTYPE = {
        "操作日期": str,
        "委托编号": str,
        "申请编号": str,
        "合同编号": str,
        "证券代码": str,
        "股东代码": str,
        "资金帐号": str,
        "资金帐户": str,
        "发生日期": str,
    }

    AUTO_IPO_MENU_PATH = ["新股申购", "一键打新"]


class HT(CommonConfig):
    DEFAULT_EXE_PATH = r"C:\htzqzyb2\xiadan.exe"

    BALANCE_CONTROL_ID_GROUP = {
        "资金余额": 1012,
        "冻结金额": 1013,
        "可用金额": 1016,
        "可取金额": 1017,
        "股票市值": 1014,
        "现金资产": 1483,
        "总资产": 1015,
    }

    GRID_DTYPE = {
        "操作日期": str,
        "委托编号": str,
        "申请编号": str,
        "合同编号": str,
        "证券代码": str,
        "股东代码": str,
        "资金帐号": str,
        "资金帐户": str,
        "发生日期": str,
    }

    AUTO_IPO_MENU_PATH = ["新股申购", "批量新股申购"]
    AUTO_IPO_NUMBER = '可申购数量'



class GJ(CommonConfig):
    DEFAULT_EXE_PATH = "C:\\全能行证券交易终端\\xiadan.exe"

    GRID_DTYPE = {
        "操作日期": str,
        "委托编号": str,
        "申请编号": str,
        "合同编号": str,
        "证券代码": str,
        "股东代码": str,
        "资金帐号": str,
        "资金帐户": str,
        "发生日期": str,
    }

    AUTO_IPO_MENU_PATH = ["新股申购", "新股批量申购"]

class GF(CommonConfig):
    DEFAULT_EXE_PATH = "C:\\gfzqrzrq\\xiadan.exe"
    TITLE = "核新网上交易系统"

    GRID_DTYPE = {
        "操作日期": str,
        "委托编号": str,
        "申请编号": str,
        "合同编号": str,
        "证券代码": str,
        "股东代码": str,
        "资金帐号": str,
        "资金帐户": str,
        "发生日期": str,
    }

    AUTO_IPO_MENU_PATH = ["新股申购", "批量新股申购"]

class WK(HT):
    pass


class HTZQ(CommonConfig):
    DEFAULT_EXE_PATH = r"c:\\海通证券委托\\xiadan.exe"

    BALANCE_CONTROL_ID_GROUP = {
        "资金余额": 1012,
        "可用金额": 1016,
        "可取金额": 1017,
        "总资产": 1015,
    }

    AUTO_IPO_NUMBER = '可申购数量'

class ZX(CommonConfig):
    DEFAULT_EXE_PATH = r"C:\Program Files (x86)\中信证券(山东)至胜全能版网上交易\xiadan.exe"

    GRID_DTYPE = {
        "操作日期": str,
        "委托编号": str,
        "申请编号": str,
        "合同编号": str,
        "证券代码": str,
        "股东代码": str,
        "资金帐号": str,
        "资金帐户": str,
        "发生日期": str,
    }

    BALANCE_CONTROL_ID_GROUP = {
        "资金余额": 1012,
        "可用金额": 1016,
        "可取金额": 1017,
        "总资产": 1015,
        "股票市值": 1014,
        "冻结金额": 1013
    }

    TITLE = "中信证券"
    BALANCE_MENU_PATH = ["查询[F4]", "资金股份"]
    POSITION_COMPARE_ITEMS = ["参考持股", "可用股份", "成本价", "冻结数量"]

class CJ(CommonConfig):
    DEFAULT_EXE_PATH = r"C:\Programs\金长江网上交易汇智版\xiadan.exe"

    BALANCE_CONTROL_ID_GROUP = {
        "资金余额": 1012,
        "可用金额": 1016,
        "可取金额": 1017,
        "总资产": 1015,
        "股票市值": 1014,
        "持仓盈亏": 1027
    }

    POSITION_COMPARE_ITEMS = ["股票余额", "可用余额", "成本价"]