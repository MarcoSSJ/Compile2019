# 开发环境

```
llvm ir 运行环境:ubuntu1604，LLVM version 6.0.0

编译器运行依赖环境:python 3.6
库：
ANTLR 可通过pip install antlr4-python3-runtime安装
LLVM lite 可通过pip install llvmlite安装
```

# 代码结构

* parser_/
  * 参考标准[C的BNF文档]([https://cs.wmich.edu/~gupta/teaching/cs4850/sumII06/The%20syntax%20of%20C%20in%20Backus-Naur%20form.htm])使用antlr4语法写的c词法语法文件`tinyc.g4`
  * 文档下的Lexer.py,Parser.py等文件由antlr4生成
* preprocess/
  * 参考该篇[博客]( http://wrice.blogspot.com/2013/12/antlr-grammar-for-cc-preprocessor.html )使用antlr4语法写成的c预编译时的词法语法文件`Cmacros.g4`
  * 文档下的Lexer.py,Parser.py等文件由antlr4生成
* test/
  * 存储了部分进行测试的c代码文件
* SymbolTable.py
  * 存储符号表
* MacroTable.py
  * 存储宏定义变量的表
* macro.py preCompile.py
  * 使用visitor设计模式进行预编译语法树遍历的类
* visitor.py
  * 使用visitor设计模式对c语法树进行遍历的类
* main.py 程序入口 util.py 杂项函数

# 使用说明

```
python main.py <输入的C文件> <输出的C文件名>
```

# 功能实现与难点

## 预编译

本编译器支持对类似于`#define IDENTIFIER(x,y...) INSTRUCTION`这类宏函数的预编译。

我本来以为预编译会比较好写，但实际上预编译阶段需要至少做两件事情，1. 建立宏命令对应的数据结构； 2.遍历c文件替换可能的IDENTIFIER，在反复尝试和搜索资料后，[博客]( http://wrice.blogspot.com/2013/12/antlr-grammar-for-cc-preprocessor.html )中将预编译分两阶段处理的思路启发了我。我实现的编译器中预编译阶段也分成两阶段。

#### 宏表

第一阶段用于根据输入c文本生成宏表，宏表的数据结构如下图所示：（以`#define ADD(A,B) A+B`）

![](D:/课程/大四上/编译原理/黎思宇_2016010695_ 孙士杰_2016011119_ 张小健_2017011434_编译小组作业/preprocessor.png)

一个宏表中含有一个token组成的顺序列表，以及一个从param到参数下标的字典。在第一阶段解析时，需要将#define后紧跟字符串以IDENTIFIER分割，从而建立token的列表，并且需要递归地产生param到下标的字典。使用的是较简单的`Cmacros.g4`语法。

#### 宏替换

在第二阶段用于根据输入c文本输出替换后的c文本，在该阶段对于一般的节点，有判断若子节点为lexer节点，输出lexer值并加上一个空格` `（必要的空格，以防inti）。否则递归地输出子节点的值。

只有当遇到`PostfixExpression`节点时，会根据宏表中是否含有对应的值，若有，遍历宏表内token输出。

## 条件跳转

1. llvm对类型要求非常严格，而llvmlite中常常是INSTRU类型而不是我们所需要的`IR.int(1)`类型，这样在生成语句时容易产生`br %".1" = i1 icmp , %".2", 0,"%.label1","%label2"`这样的非三地址指令导致错误。为此我是这样解决的：如果是INSTRU类型，则用`ir.int(1)(instru.get_reference())`确保其为一个布尔类型而非指令类型。

2. 在llvm-lite中用于跳转的指令有branch,cbranch,if_else,branch可以用在for中，break，continue中进行跳转，if_else可以用在`||` `&&`实现短路特性

   ## 符号表

   我实现的符号表主要用来模仿一个栈结构，其中利用了python的dict类型。

## 运算优先级与冲突

在[C的BNF文档]([https://cs.wmich.edu/~gupta/teaching/cs4850/sumII06/The%20syntax%20of%20C%20in%20Backus-Naur%20form.htm])中定义的语法生成表达式已经解决了运算优先级的问题。

另外我在编写g4文档时经常会遇到[Mismatched Input 'x' expecting 'x'](https://stackoverflow.com/questions/29777778/antlr-4-5-mismatched-input-x-expecting-x)类错误，这是因为antlr4虽然可以将词法语法写在一起，但其词法语法解析是分成两个阶段的。当词法解析发生冲突时，会自动选择最顶层的token，因此如果不慎在lexer开头定义了~[ \t\r\n]+，那么就一定不能得到想要的值了。

解决方法也很简单，就和语法生成表达式解决运算优先级一样，只需要重排词法定义顺序从而确立他们的优先级就行了，一般需要保证上层的词法一定不会包含下层的词法。



# 最后，祝学弟学妹们享受软院的快乐大三