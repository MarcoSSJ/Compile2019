from llvmlite import ir


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
    def get_pointer_type(self, pointee_type):
        return ir.PointerType(pointee_type)


module = ir.Module()
llvmTypes = LLVMTypes()
printf_type = ir.FunctionType(llvmTypes.int32,
                              (llvmTypes.get_pointer_type(llvmTypes.int8),), var_arg=True)
printf_func = ir.Function(module, printf_type, "printf")