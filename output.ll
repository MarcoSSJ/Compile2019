; ModuleID = ""
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"main"() 
{
.entry:
  %".2" = alloca i32
  store i32 0, i32* %".2"
  %".4" = alloca i32
  store i32 0, i32* %".4"
  br label %".entry.loop_cond"
.entry.loop_cond:
  %".7" = load i32, i32* %".4"
  br i1 %".7" = load i32, i32* %".4", label %".entry.loop_body", label %".entry.loop_end"
.entry.loop_body:
  %".11" = getelementptr inbounds [16 x i8], [16 x i8]* @".str0", i32 0, i32 0
  %".12" = load i32, i32* %".4"
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %".12")
  br label %".entry.loop_update"
.entry.loop_update:
  %".9" = load i32, i32* %".4"
  br label %".entry.loop_cond"
.entry.loop_end:
  ret i32 0
}

@".str0" = constant [16 x i8] c"hello world.%d\0a\00"