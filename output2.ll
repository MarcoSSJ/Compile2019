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
define void @"calNext"(i8* %".1", i32* %".2") 
{
.entrycalNext:
  %".4" = alloca i32
  store i32 0, i32* %".4"
  %".6" = alloca i32
  %".7" = sub i32 0, 1
  store i32 %".7", i32* %".6"
  %".9" = alloca i32
  %".10" = load i32, i32* %".9"
  %".11" = call i32 @"strLen"(i8* %".1")
  store i32 %".11", i32* %".9"
  %".13" = getelementptr i32, i32* %".2", i32 0
  %".14" = load i32, i32* %".13"
  %".15" = sub i32 0, 1
  store i32 %".15", i32* %".13"
  br label %".entrycalNext.loop_cond"
.entrycalNext.loop_cond:
  %".18" = load i32, i32* %".4"
  %".19" = load i32, i32* %".9"
  %".20" = sub i32 %".19", 1
  %".21" = icmp slt i32 %".18", %".20"
  %".22" = icmp ne i1 %".21", 0
  br i1 %".22", label %".entrycalNext.loop_body", label %".entrycalNext.loop_end"
.entrycalNext.loop_body:
  %".25" = load i32, i32* %".6"
  %".26" = sub i32 0, 1
  %".27" = icmp eq i32 %".25", %".26"
  %".28" = load i32, i32* %".4"
  %".29" = getelementptr i8, i8* %".1", i32 %".28"
  %".30" = load i8, i8* %".29"
  %".31" = load i32, i32* %".6"
  %".32" = getelementptr i8, i8* %".1", i32 %".31"
  %".33" = load i8, i8* %".32"
  %".34" = icmp eq i8 %".30", %".33"
  %".35" = alloca i1
  %".36" = icmp ne i1 %".27", 0
  br i1 %".36", label %".entrycalNext.loop_body.if", label %".entrycalNext.loop_body.else"
.entrycalNext.loop_update:
  br label %".entrycalNext.loop_cond"
.entrycalNext.loop_end:
  ret void
.entrycalNext.loop_body.if:
  store i1 0, i1* %".35"
  br label %".entrycalNext.loop_body.endif"
.entrycalNext.loop_body.else:
  store i1 %".34", i1* %".35"
  br label %".entrycalNext.loop_body.endif"
.entrycalNext.loop_body.endif:
  %".42" = load i1, i1* %".35"
  %".43" = icmp ne i1 %".42", 0
  br i1 %".43", label %".entrycalNext.loop_body.endif.if", label %".entrycalNext.loop_body.endif.else"
.entrycalNext.loop_body.endif.if:
  %".45" = load i32, i32* %".4"
  %".46" = add i32 %".45", 1
  store i32 %".46", i32* %".4"
  %".48" = load i32, i32* %".6"
  %".49" = add i32 %".48", 1
  store i32 %".49", i32* %".6"
  %".51" = load i32, i32* %".4"
  %".52" = getelementptr i8, i8* %".1", i32 %".51"
  %".53" = load i8, i8* %".52"
  %".54" = load i32, i32* %".6"
  %".55" = getelementptr i8, i8* %".1", i32 %".54"
  %".56" = load i8, i8* %".55"
  %".57" = icmp ne i8 %".53", %".56"
  %".58" = icmp ne i1 %".57", 0
  br i1 %".58", label %".entrycalNext.loop_body.endif.if.if", label %".entrycalNext.loop_body.endif.if.else"
.entrycalNext.loop_body.endif.else:
  %".75" = load i32, i32* %".4"
  %".76" = load i32, i32* %".4"
  %".77" = getelementptr i32, i32* %".2", i32 %".76"
  %".78" = load i32, i32* %".77"
  store i32 %".78", i32* %".4"
  br label %".entrycalNext.loop_body.endif.endif"
.entrycalNext.loop_body.endif.endif:
  br label %".entrycalNext.loop_update"
.entrycalNext.loop_body.endif.if.if:
  %".60" = load i32, i32* %".4"
  %".61" = getelementptr i32, i32* %".2", i32 %".60"
  %".62" = load i32, i32* %".61"
  %".63" = load i32, i32* %".6"
  store i32 %".63", i32* %".61"
  br label %".entrycalNext.loop_body.endif.if.endif"
.entrycalNext.loop_body.endif.if.else:
  %".66" = load i32, i32* %".4"
  %".67" = getelementptr i32, i32* %".2", i32 %".66"
  %".68" = load i32, i32* %".67"
  %".69" = load i32, i32* %".6"
  %".70" = getelementptr i32, i32* %".2", i32 %".69"
  %".71" = load i32, i32* %".70"
  store i32 %".71", i32* %".67"
  br label %".entrycalNext.loop_body.endif.if.endif"
.entrycalNext.loop_body.endif.if.endif:
  br label %".entrycalNext.loop_body.endif.endif"
}

define i32 @"firstIndexOf"(i8* %".1", i8* %".2") 
{
.entryfirstIndexOf:
  %".4" = alloca i32
  store i32 0, i32* %".4"
  %".6" = alloca i32
  store i32 0, i32* %".6"
  %".8" = alloca i32
  %".9" = call i32 @"strLen"(i8* %".2")
  store i32 %".9", i32* %".8"
  %".11" = alloca i32
  %".12" = call i32 @"strLen"(i8* %".1")
  store i32 %".12", i32* %".11"
  %".14" = alloca [50 x i32]
  %".15" = alloca i32
  store i32 0, i32* %".15"
  br label %".entryfirstIndexOf.loop_cond"
.entryfirstIndexOf.loop_cond:
  %".18" = load i32, i32* %".15"
  %".19" = load i32, i32* %".8"
  %".20" = icmp slt i32 %".18", %".19"
  %".21" = icmp ne i1 %".20", 0
  br i1 %".21", label %".entryfirstIndexOf.loop_body", label %".entryfirstIndexOf.loop_end"
.entryfirstIndexOf.loop_body:
  %".27" = load [50 x i32], [50 x i32]* %".14"
  %".28" = load i32, i32* %".15"
  %".29" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 %".28"
  %".30" = load i32, i32* %".29"
  store i32 0, i32* %".29"
  br label %".entryfirstIndexOf.loop_update"
.entryfirstIndexOf.loop_update:
  %".23" = load i32, i32* %".15"
  %".24" = add i32 %".23", 1
  store i32 %".24", i32* %".15"
  br label %".entryfirstIndexOf.loop_cond"
.entryfirstIndexOf.loop_end:
  %".33" = load [50 x i32], [50 x i32]* %".14"
  %".34" = alloca [50 x i32]
  store [50 x i32] %".33", [50 x i32]* %".34"
  %".36" = getelementptr [50 x i32], [50 x i32]* %".34", i32 0, i32 0
  call void @"calNext"(i8* %".2", i32* %".36")
  %".38" = alloca i32
  store i32 0, i32* %".38"
  br label %".entryfirstIndexOf.loop_end.loop_cond"
.entryfirstIndexOf.loop_end.loop_cond:
  %".41" = load i32, i32* %".38"
  %".42" = load i32, i32* %".8"
  %".43" = icmp slt i32 %".41", %".42"
  %".44" = icmp ne i1 %".43", 0
  br i1 %".44", label %".entryfirstIndexOf.loop_end.loop_body", label %".entryfirstIndexOf.loop_end.loop_end"
.entryfirstIndexOf.loop_end.loop_body:
  %".50" = getelementptr inbounds [18 x i8], [18 x i8]* @".str2", i32 0, i32 0
  %".51" = load i32, i32* %".38"
  %".52" = load [50 x i32], [50 x i32]* %".14"
  %".53" = load i32, i32* %".38"
  %".54" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 %".53"
  %".55" = load i32, i32* %".54"
  %".56" = call i32 (i8*, ...) @"printf"(i8* %".50", i32 %".51", i32 %".55")
  br label %".entryfirstIndexOf.loop_end.loop_update"
.entryfirstIndexOf.loop_end.loop_update:
  %".46" = load i32, i32* %".38"
  %".47" = add i32 %".46", 1
  store i32 %".47", i32* %".38"
  br label %".entryfirstIndexOf.loop_end.loop_cond"
.entryfirstIndexOf.loop_end.loop_end:
  br label %".entryfirstIndexOf.loop_end.loop_end.loop_cond"
.entryfirstIndexOf.loop_end.loop_end.loop_cond:
  %".59" = load i32, i32* %".6"
  %".60" = load i32, i32* %".11"
  %".61" = icmp slt i32 %".59", %".60"
  %".62" = icmp ne i1 %".61", 0
  br i1 %".62", label %".entryfirstIndexOf.loop_end.loop_end.loop_body", label %".entryfirstIndexOf.loop_end.loop_end.loop_end"
.entryfirstIndexOf.loop_end.loop_end.loop_body:
  %".65" = load i32, i32* %".4"
  %".66" = getelementptr i8, i8* %".2", i32 %".65"
  %".67" = load i8, i8* %".66"
  %".68" = load i32, i32* %".6"
  %".69" = getelementptr i8, i8* %".1", i32 %".68"
  %".70" = load i8, i8* %".69"
  %".71" = icmp eq i8 %".67", %".70"
  %".72" = icmp ne i1 %".71", 0
  br i1 %".72", label %".entryfirstIndexOf.loop_end.loop_end.loop_body.if", label %".entryfirstIndexOf.loop_end.loop_end.loop_body.else"
.entryfirstIndexOf.loop_end.loop_end.loop_update:
  br label %".entryfirstIndexOf.loop_end.loop_end.loop_cond"
.entryfirstIndexOf.loop_end.loop_end.loop_end:
  %".111" = sub i32 0, 1
  ret i32 %".111"
.entryfirstIndexOf.loop_end.loop_end.loop_body.if:
  %".74" = load i32, i32* %".4"
  %".75" = add i32 %".74", 1
  store i32 %".75", i32* %".4"
  %".77" = load i32, i32* %".6"
  %".78" = add i32 %".77", 1
  store i32 %".78", i32* %".6"
  br label %".entryfirstIndexOf.loop_end.loop_end.loop_body.endif"
.entryfirstIndexOf.loop_end.loop_end.loop_body.else:
  %".81" = load [50 x i32], [50 x i32]* %".14"
  %".82" = load i32, i32* %".4"
  %".83" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 %".82"
  %".84" = load i32, i32* %".83"
  %".85" = sub i32 0, 1
  %".86" = icmp ne i32 %".84", %".85"
  %".87" = icmp ne i1 %".86", 0
  br i1 %".87", label %".entryfirstIndexOf.loop_end.loop_end.loop_body.else.if", label %".entryfirstIndexOf.loop_end.loop_end.loop_body.else.endif"
.entryfirstIndexOf.loop_end.loop_end.loop_body.endif:
  %".100" = load i32, i32* %".4"
  %".101" = getelementptr i8, i8* %".2", i32 %".100"
  %".102" = load i8, i8* %".101"
  %".103" = icmp eq i8 %".102", 0
  %".104" = icmp ne i1 %".103", 0
  br i1 %".104", label %".entryfirstIndexOf.loop_end.loop_end.loop_body.endif.if", label %".entryfirstIndexOf.loop_end.loop_end.loop_body.endif.endif"
.entryfirstIndexOf.loop_end.loop_end.loop_body.else.if:
  %".89" = load i32, i32* %".4"
  %".90" = load [50 x i32], [50 x i32]* %".14"
  %".91" = load i32, i32* %".4"
  %".92" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 %".91"
  %".93" = load i32, i32* %".92"
  store i32 %".93", i32* %".4"
  br label %".entryfirstIndexOf.loop_end.loop_end.loop_body.else.endif"
.entryfirstIndexOf.loop_end.loop_end.loop_body.else.endif:
  %".96" = load i32, i32* %".6"
  %".97" = add i32 %".96", 1
  store i32 %".97", i32* %".6"
  br label %".entryfirstIndexOf.loop_end.loop_end.loop_body.endif"
.entryfirstIndexOf.loop_end.loop_end.loop_body.endif.if:
  %".106" = load i32, i32* %".6"
  %".107" = load i32, i32* %".8"
  %".108" = sub i32 %".106", %".107"
  ret i32 %".108"
.entryfirstIndexOf.loop_end.loop_end.loop_body.endif.endif:
  br label %".entryfirstIndexOf.loop_end.loop_end.loop_update"
}

@".str2" = constant [18 x i8] c"next [] %d  = %d\0a\00"
define void @"testKmp"(i8* %".1", i8* %".2", i32 %".3") 
{
.entrytestKmp:
  %".5" = getelementptr inbounds [23 x i8], [23 x i8]* @".str3", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5")
  %".7" = alloca i32
  %".8" = call i32 @"firstIndexOf"(i8* %".1", i8* %".2")
  store i32 %".8", i32* %".7"
  %".10" = load i32, i32* %".7"
  call void @"assertTest"(i32 %".10", i32 %".3")
  ret void
}

@".str3" = constant [23 x i8] c"--new kmp test start:\0a\00"
define void @"unittest"() 
{
.entryunittest:
  %".2" = getelementptr inbounds [26 x i8], [26 x i8]* @".str4", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %".4" = getelementptr inbounds [8 x i8], [8 x i8]* @".str5", i32 0, i32 0
  %".5" = getelementptr inbounds [5 x i8], [5 x i8]* @".str6", i32 0, i32 0
  call void @"testKmp"(i8* %".4", i8* %".5", i32 3)
  %".7" = getelementptr inbounds [2 x i8], [2 x i8]* @".str7", i32 0, i32 0
  %".8" = getelementptr inbounds [3 x i8], [3 x i8]* @".str8", i32 0, i32 0
  %".9" = sub i32 0, 1
  call void @"testKmp"(i8* %".7", i8* %".8", i32 %".9")
  %".11" = getelementptr inbounds [2 x i8], [2 x i8]* @".str9", i32 0, i32 0
  %".12" = getelementptr inbounds [2 x i8], [2 x i8]* @".str10", i32 0, i32 0
  %".13" = sub i32 0, 1
  call void @"testKmp"(i8* %".11", i8* %".12", i32 %".13")
  %".15" = getelementptr inbounds [5 x i8], [5 x i8]* @".str11", i32 0, i32 0
  %".16" = getelementptr inbounds [2 x i8], [2 x i8]* @".str12", i32 0, i32 0
  %".17" = sub i32 0, 1
  call void @"testKmp"(i8* %".15", i8* %".16", i32 %".17")
  %".19" = getelementptr inbounds [5 x i8], [5 x i8]* @".str13", i32 0, i32 0
  %".20" = getelementptr inbounds [3 x i8], [3 x i8]* @".str14", i32 0, i32 0
  call void @"testKmp"(i8* %".19", i8* %".20", i32 0)
  ret void
}

@".str4" = constant [26 x i8] c"*******kmp test*********\0a\00"
@".str5" = constant [8 x i8] c"aaabaaa\00"
@".str6" = constant [5 x i8] c"baaa\00"
@".str7" = constant [2 x i8] c"a\00"
@".str8" = constant [3 x i8] c"aa\00"
@".str9" = constant [2 x i8] c"b\00"
@".str10" = constant [2 x i8] c"a\00"
@".str11" = constant [5 x i8] c"aaaa\00"
@".str12" = constant [2 x i8] c"b\00"
@".str13" = constant [5 x i8] c"aaaa\00"
@".str14" = constant [3 x i8] c"aa\00"
define i32 @"main"() 
{
.entrymain:
  call void @"unittest"()
  ret i32 0
}
