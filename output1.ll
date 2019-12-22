; ModuleID = ""
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"strLen"(i8* %".1") 
{
.entrystrLen:
  %".3" = alloca i32
  %".4" = load i32, i32* %".3"
  store i32 0, i32* %".3"
  br label %".entrystrLen.loop_cond"
.entrystrLen.loop_cond:
  %".7" = load i32, i32* %".3"
  %".8" = getelementptr i8, i8* %".1", i32 %".7"
  %".9" = load i8, i8* %".8"
  %".10" = icmp ne i8 %".9", 0
  br i1 %".10", label %".entrystrLen.loop_body", label %".entrystrLen.loop_end"
.entrystrLen.loop_body:
  br label %".entrystrLen.loop_update"
.entrystrLen.loop_update:
  %".12" = load i32, i32* %".3"
  %".13" = add i32 %".12", 1
  store i32 %".13", i32* %".3"
  br label %".entrystrLen.loop_cond"
.entrystrLen.loop_end:
  %".17" = load i32, i32* %".3"
  ret i32 %".17"
}

define i32 @"isPalindrome"(i8* %".1") 
{
.entryisPalindrome:
  %".3" = alloca i32
  %".4" = alloca i32
  %".5" = load i32, i32* %".3"
  %".6" = call i32 @"strLen"(i8* %".1")
  store i32 %".6", i32* %".3"
  %".8" = load i32, i32* %".4"
  store i32 0, i32* %".4"
  br label %".entryisPalindrome.loop_cond"
.entryisPalindrome.loop_cond:
  %".11" = load i32, i32* %".4"
  %".12" = load i32, i32* %".3"
  %".13" = icmp slt i32 %".11", %".12"
  %".14" = icmp ne i1 %".13", 0
  br i1 %".14", label %".entryisPalindrome.loop_body", label %".entryisPalindrome.loop_end"
.entryisPalindrome.loop_body:
  %".20" = load i32, i32* %".4"
  %".21" = getelementptr i8, i8* %".1", i32 %".20"
  %".22" = load i8, i8* %".21"
  %".23" = load i32, i32* %".3"
  %".24" = load i32, i32* %".4"
  %".25" = sub i32 %".23", %".24"
  %".26" = sub i32 %".25", 1
  %".27" = getelementptr i8, i8* %".1", i32 %".26"
  %".28" = load i8, i8* %".27"
  %".29" = icmp ne i8 %".22", %".28"
  %".30" = icmp ne i1 %".29", 0
  br i1 %".30", label %".entryisPalindrome.loop_body.if", label %".entryisPalindrome.loop_body.endif"
.entryisPalindrome.loop_update:
  %".16" = load i32, i32* %".4"
  %".17" = add i32 %".16", 1
  store i32 %".17", i32* %".4"
  br label %".entryisPalindrome.loop_cond"
.entryisPalindrome.loop_end:
  ret i32 1
.entryisPalindrome.loop_body.if:
  ret i32 0
.entryisPalindrome.loop_body.endif:
  br label %".entryisPalindrome.loop_update"
}

define void @"assertTest"(i32 %".1", i32 %".2") 
{
.entryassertTest:
  %".4" = icmp eq i32 %".1", %".2"
  %".5" = icmp ne i1 %".4", 0
  br i1 %".5", label %".entryassertTest.if", label %".entryassertTest.else"
.entryassertTest.if:
  %".7" = getelementptr inbounds [15 x i8], [15 x i8]* @".str0", i32 0, i32 0
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7")
  br label %".entryassertTest.endif"
.entryassertTest.else:
  %".10" = getelementptr inbounds [14 x i8], [14 x i8]* @".str1", i32 0, i32 0
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10")
  br label %".entryassertTest.endif"
.entryassertTest.endif:
  ret void
}

@".str0" = constant [15 x i8] c"test success!\0a\00"
@".str1" = constant [14 x i8] c"test failed!\0a\00"
define void @"testPalindrome"(i8* %".1", i32 %".2") 
{
.entrytestPalindrome:
  %".4" = getelementptr inbounds [30 x i8], [30 x i8]* @".str2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  %".6" = alloca i32
  %".7" = call i32 @"isPalindrome"(i8* %".1")
  store i32 %".7", i32* %".6"
  %".9" = load i32, i32* %".6"
  call void @"assertTest"(i32 %".9", i32 %".2")
  ret void
}

@".str2" = constant [30 x i8] c"--new palindrome test start:\0a\00"
define void @"unittest"() 
{
.entryunittest:
  %".2" = getelementptr inbounds [33 x i8], [33 x i8]* @".str3", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %".4" = getelementptr inbounds [1 x i8], [1 x i8]* @".str4", i32 0, i32 0
  call void @"testPalindrome"(i8* %".4", i32 1)
  %".6" = getelementptr inbounds [2 x i8], [2 x i8]* @".str5", i32 0, i32 0
  call void @"testPalindrome"(i8* %".6", i32 1)
  %".8" = getelementptr inbounds [3 x i8], [3 x i8]* @".str6", i32 0, i32 0
  call void @"testPalindrome"(i8* %".8", i32 1)
  %".10" = getelementptr inbounds [3 x i8], [3 x i8]* @".str7", i32 0, i32 0
  call void @"testPalindrome"(i8* %".10", i32 0)
  %".12" = getelementptr inbounds [10 x i8], [10 x i8]* @".str8", i32 0, i32 0
  call void @"testPalindrome"(i8* %".12", i32 1)
  %".14" = getelementptr inbounds [10 x i8], [10 x i8]* @".str9", i32 0, i32 0
  call void @"testPalindrome"(i8* %".14", i32 1)
  %".16" = getelementptr inbounds [9 x i8], [9 x i8]* @".str10", i32 0, i32 0
  call void @"testPalindrome"(i8* %".16", i32 0)
  ret void
}

@".str3" = constant [33 x i8] c"*******palindrome test*********\0a\00"
@".str4" = constant [1 x i8] c"\00"
@".str5" = constant [2 x i8] c"a\00"
@".str6" = constant [3 x i8] c"aa\00"
@".str7" = constant [3 x i8] c"ab\00"
@".str8" = constant [10 x i8] c"aaaaaaaaa\00"
@".str9" = constant [10 x i8] c"aaaabaaaa\00"
@".str10" = constant [9 x i8] c"aaabaaaa\00"
define i32 @"main"() 
{
.entrymain:
  call void @"unittest"()
  ret i32 0
}
