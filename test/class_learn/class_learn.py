# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: LiuFei
# @createTime: 2017-08-25 15:58:44
# @description: 权限控制相关枚举

from __future__ import division


class Enum(dict):
    """
    枚举类，用来创建一个枚举
    """

    def __getattr__(self, key):
        if key in self:
            return self.get(key)
        raise AttributeError, "{0} is not in enumeration".format(key)

    # 枚举类型应该禁止修改数据
    def __setattr__(self, key, value):
        raise AttributeError, "enumeration type prohibit modification"


class DTEnum(Enum):
    SESSION_KEY = "dist"

    DB_KEY = "dt"

    NAME = "渠道商"

    class TABLE(Enum):
        USER = "dt_user"
        INFO = "dt_inlet_info"


class MchEnum(Enum):
    SESSION_KEY = "mch"

    DB_KEY = "mch"

    NAME = "商户"

    class TABLE(Enum):
        USER = "mch_user"
        INFO = "mch_inlet_info"


class ChainEnum(Enum):
    SESSION_KEY = "chain"

    DB_KEY = "chain"

    NAME = "连锁商户"

    class TABLE(Enum):
        USER = "dt_user"
        INFO = "dt_inlet_info"


class CSEnum(Enum):
    SESSION_KEY = "cs"

    DB_KEY = "cs"

    NAME = "门店"

    class TABLE(Enum):
        USER = "mch_user"
        INFO = "mch_inlet_info"


class OfficialEnum(Enum):
    SESSION_KEY = "official"

    DB_KEY = "official"

    NAME = "官方"

    class TABLE(Enum):
        USER = "ub_user"
        INFO = ""


class BankEnum(Enum):
    SESSION_KEY = "bank"

    DB_KEY = "bank"

    NAME = "银行"

    class TABLE(Enum):
        USER = "bank_user"
        INFO = ""


class EmployeeEnum(Enum):
    SESSION_KEY = "employee"

    DB_KEY = "employee"

    NAME = "员工"

    class TABLE(Enum):
        USER = "employee_user"
        INFO = ""


class BusyManEnum(Enum):
    SESSION_KEY = "busy_man"

    DB_KEY = "employee"

    NAME = "业务员"

    class TABLE(Enum):
        USER = "employee_user"
        INFO = ""


class RoleInfoEnum(Enum):
    # 默认 角色类型
    ROLE_TYPE_DEFAULT = 1

    # 业务员 角色类型
    ROLE_TYPE_BUSY_MAN = 2

    # # 创建用户
    # CREATE_USER = (
    #     UserEnum.BANK_USER, UserEnum.OFFICIAL_USER,
    #     UserEnum.DT_USER, UserEnum.MCH_USER,
    #     UserEnum.CHAIN_USER, UserEnum.CS_USER,
    #     UserEnum.EMPLOYEE_USER
    # )


class UserEnum:
    DT = DTEnum()
    MCH = MchEnum()
    CHAIN = ChainEnum()
    CS = CSEnum()
    UB = OfficialEnum()
    BANK = BankEnum()
    EMPLOYEE = EmployeeEnum()
    BUSY_MAN = BusyManEnum()

    @classmethod
    def get(cls, key):
        if key in ["dt", "dist"]:
            return DTEnum()
        elif key in ["mch"]:
            return MchEnum()
        elif key in ["chain"]:
            return ChainEnum()
        elif key in ["cs"]:
            return CSEnum()
        elif key in ["ub", "official"]:
            return OfficialEnum()
        elif key in ["bank"]:
            return BankEnum()
        elif key in ["employee"]:
            return EmployeeEnum()
        elif key in ["busy_man"]:
            return BusyManEnum()

if __name__ == '__main__':

    print(type(UserEnum.DT))
    print(UserEnum.DT)
    print(UserEnum.DT.items())
    print((UserEnum.DT.TABLE.USER))