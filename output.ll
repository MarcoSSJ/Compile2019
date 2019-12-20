; ModuleID = ""
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"main"() 
{
.entry:
  br label %".entry.loop_cond"
.entry.loop_cond:
  br i1 i32 1, label %".entry.loop_body", label %".entry.loop_end"
.entry.loop_body:
  %".5" = getelementptr inbounds [14 x i8], [14 x i8]* @".str0", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5")
  br label %".entry.loop_update"
.entry.loop_update:
  br label %".entry.loop_cond"
.entry.loop_end:
  ret i32 0
}

@".str0" = constant [14 x i8] c"hello world.\0a\00"