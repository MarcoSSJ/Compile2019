; ModuleID = ""
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"main"() 
{
.entry:
  %".2" = getelementptr inbounds [15 x i8], [15 x i8]* @".str0", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  ret i32 0
}

@".str0" = constant [15 x i8] c"hello world.\5cn\00"