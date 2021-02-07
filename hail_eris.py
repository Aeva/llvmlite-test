
# based on examples from https://llvmlite.readthedocs.io/en/latest/index.html

from ctypes import CFUNCTYPE, c_double
from llvmlite import ir
from llvmlite import binding as llvm


double = ir.DoubleType()
fnty = ir.FunctionType(double, (double, double))
module = ir.Module(name=__file__)
func = ir.Function(module, fnty, name="fpadd")
block = func.append_basic_block(name="entry")
builder = ir.IRBuilder(block)
a, b = func.args
result = builder.fadd(a, b, name="res")
builder.ret(result)


llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()


target = llvm.Target.from_default_triple()
target_machine = target.create_target_machine()
backing_mod = llvm.parse_assembly("")
engine = llvm.create_mcjit_compiler(backing_mod, target_machine)


mod = llvm.parse_assembly(str(module))
mod.verify()
engine.add_module(mod)
engine.finalize_object()
engine.run_static_constructors()


func_ptr = engine.get_function_address("fpadd")
c_fpadd = CFUNCTYPE(c_double, c_double, c_double)(func_ptr)
print(c_fpadd(1.0, 2.0))
