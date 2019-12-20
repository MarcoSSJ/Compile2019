; ModuleID = ""
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"helloworld"() 
{
.entry:
  %".2" = getelementptr inbounds [20 x i8], [20 x i8]* @".str0", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  ret i32 0
}

@".str0" = constant [20 x i8] c"helloworld, again.\0a\00"
define i32 @"main"() 
{
.entry:
  %".2" = getelementptr inbounds [14 x i8], [14 x i8]* @".str1", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %".4" = call i32 @"helloworld"()
  ret i32 0
}

@".str1" = constant [14 x i8] c"hello world.\0a\00"