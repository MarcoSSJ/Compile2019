# 用于帮助编译器
from llvmlite import ir
import codecs

class LLVMTypes(object):
    int32 = ir.IntType(32)
    int16 = ir.IntType(16)
    int8 = ir.IntType(8)
    int1 = ir.IntType(1)
    float32 = ir.FloatType()
    float64 = ir.DoubleType()
    void = ir.VoidType()
    typeStrMap = {
        "int": int32,
        "short": int16,
        "char": int8,
        "long": int32,
        "bool": int1,
        "float": float32,
        "double": float64,
        "void": void
    }
    char = int8
    int = int32
    short = int16
    bool = int1
    float = float64
    double = float64
    void = void
    ascii_mapping = {
        '\\a': '\a',
        '\\b': '\b',
        '\\f': '\f',
        '\\n': '\n',
        '\\r': '\r',
        '\\t': '\t',
        '\\v': '\v',
        '\\\\': '\\',
        '\\?': '\?',
        "\\'": '\'',
        '\\"': '\"',
        '\\0': '\0',
    }
    @classmethod
    def to_lltype(cls, typeStr):
        return cls.typeStrMap[typeStr]

    @classmethod
    def to_str2lltype(cls, s):
        strlen = len(s)
        return ir.ArrayType(cls.int8, strlen + 1)

    def get_array_type(self, elem_type, count):
        return ir.ArrayType(elem_type, count)

    def get_pointer_type(self, pointee_type):
        return ir.PointerType(pointee_type)

def parse_escape(s):
    return codecs.escape_decode(bytes(s, "ascii"))[0].decode("ascii")

def get_const_from_str(ctype, const_value):
    """
    从字符串获得常数类型
    :param ctype: 类型,接受char,float,double,short,int,ir.ArrayType
    :param const_value: 值，是一个字符串
    :return:
    """
    if type(const_value) is str:
        if ctype == 'string':
            ctype = LLVMTypes.to_str2lltype(const_value)
        else:
            ctype = LLVMTypes.to_lltype(ctype)
        if ctype == LLVMTypes.char:
            if len(const_value) == 3:  # 若const_value形如'3',
                return LLVMTypes.char(ord(str(const_value[1:-1])))  # 则将ASCII字符转成对应的整数存储
            elif len(const_value) == 1:  # 若const_value形如44
                return LLVMTypes.char(int(const_value))  # 则已经是整数了
            else:  # 若const_value是转移字符，例如'\n'
                value = const_value[1:-1]
                if value in LLVMTypes.ascii_mapping:
                    return LLVMTypes.char(LLVMTypes.ascii_mapping[value])
                else:
                    raise Exception(msg="Unknown char value: %s" % value)
        elif ctype in [LLVMTypes.float, LLVMTypes.double]:
            return ctype(float(const_value))
        elif ctype in [LLVMTypes.short, LLVMTypes.int]:
            return ctype(int(const_value))
        elif isinstance(ctype, ir.ArrayType) and ctype.element == LLVMTypes.char:
            # string
            str_val = const_value + '\0'
            return ir.Constant(ctype, bytearray(str_val, 'utf-8'))
        else:
            # TODO
            raise Exception(msg="No known conversion: '%s' to '%s'" % (const_value, ctype))
    else:
        raise SyntaxError(msg="get_const_from_str doesn't support const_value which is a " + str(type(const_value)))

def formatString(s:str):
    """将\n之类的替换"""
    mapping = LLVMTypes.ascii_mapping
    for i in mapping.keys():
        s = s.replace(i, mapping[i])
    return s