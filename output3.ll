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
  br label %".entrystrLen.loop_start"
.entrystrLen.loop_start:
  br label %".entrystrLen.loop_cond"
.entrystrLen.loop_cond:
  %".8" = load i32, i32* %".3"
  %".9" = getelementptr i8, i8* %".1", i32 %".8"
  %".10" = load i8, i8* %".9"
  %".11" = icmp ne i8 %".10", 0
  br i1 %".11", label %".entrystrLen.loop_body", label %".entrystrLen.loop_end"
.entrystrLen.loop_body:
  br label %".entrystrLen.loop_update"
.entrystrLen.loop_update:
  %".14" = load i32, i32* %".3"
  %".15" = add i32 %".14", 1
  store i32 %".15", i32* %".3"
  br label %".entrystrLen.loop_cond"
.entrystrLen.loop_end:
  %".18" = load i32, i32* %".3"
  ret i32 %".18"
}

define i32 @"assertTest"(i32 %".1", i32 %".2") 
{
.entryassertTest:
  %".4" = icmp eq i32 %".1", %".2"
  %".5" = icmp ne i1 %".4", 0
  br i1 %".5", label %".entryassertTest.if", label %".entryassertTest.else"
.entryassertTest.if:
  %".7" = alloca [15 x i8]
  store [15 x i8] c"test success!\0a\00", [15 x i8]* %".7"
  %".9" = getelementptr [15 x i8], [15 x i8]* %".7", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9")
  br label %".entryassertTest.endif"
.entryassertTest.else:
  %".12" = alloca [14 x i8]
  store [14 x i8] c"test failed!\0a\00", [14 x i8]* %".12"
  %".14" = getelementptr [14 x i8], [14 x i8]* %".12", i32 0, i32 0
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14")
  br label %".entryassertTest.endif"
.entryassertTest.endif:
  ret i32 0
}

define i32 @"calNext"(i8* %".1", i32* %".2") 
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
  br label %".entrycalNext.loop_start"
.entrycalNext.loop_start:
  br label %".entrycalNext.loop_cond"
.entrycalNext.loop_cond:
  %".19" = load i32, i32* %".4"
  %".20" = load i32, i32* %".9"
  %".21" = icmp slt i32 %".19", %".20"
  %".22" = icmp ne i1 %".21", 0
  br i1 %".22", label %".entrycalNext.loop_body", label %".entrycalNext.loop_end"
.entrycalNext.loop_body:
  %".24" = load i32, i32* %".6"
  %".25" = sub i32 0, 1
  %".26" = icmp eq i32 %".24", %".25"
  %".27" = alloca i1
  %".28" = icmp ne i1 %".26", 0
  br i1 %".28", label %".entrycalNext.loop_body.if", label %".entrycalNext.loop_body.else"
.entrycalNext.loop_update:
  br label %".entrycalNext.loop_cond"
.entrycalNext.loop_end:
  ret i32 0
.entrycalNext.loop_body.if:
  store i1 1, i1* %".27"
  br label %".entrycalNext.loop_body.endif"
.entrycalNext.loop_body.else:
  %".32" = load i32, i32* %".4"
  %".33" = getelementptr i8, i8* %".1", i32 %".32"
  %".34" = load i8, i8* %".33"
  %".35" = load i32, i32* %".6"
  %".36" = getelementptr i8, i8* %".1", i32 %".35"
  %".37" = load i8, i8* %".36"
  %".38" = icmp eq i8 %".34", %".37"
  %".39" = icmp ne i1 %".38", 0
  store i1 %".39", i1* %".27"
  br label %".entrycalNext.loop_body.endif"
.entrycalNext.loop_body.endif:
  %".42" = load i1, i1* %".27"
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
  %".52" = getelementptr i32, i32* %".2", i32 %".51"
  %".53" = load i32, i32* %".52"
  %".54" = load i32, i32* %".6"
  store i32 %".54", i32* %".52"
  br label %".entrycalNext.loop_body.endif.endif"
.entrycalNext.loop_body.endif.else:
  %".57" = load i32, i32* %".6"
  %".58" = load i32, i32* %".6"
  %".59" = getelementptr i32, i32* %".2", i32 %".58"
  %".60" = load i32, i32* %".59"
  store i32 %".60", i32* %".6"
  br label %".entrycalNext.loop_body.endif.endif"
.entrycalNext.loop_body.endif.endif:
  br label %".entrycalNext.loop_update"
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
  br label %".entryfirstIndexOf.loop_start"
.entryfirstIndexOf.loop_start:
  br label %".entryfirstIndexOf.loop_cond"
.entryfirstIndexOf.loop_cond:
  %".19" = load i32, i32* %".15"
  %".20" = load i32, i32* %".8"
  %".21" = icmp slt i32 %".19", %".20"
  %".22" = icmp ne i1 %".21", 0
  br i1 %".22", label %".entryfirstIndexOf.loop_body", label %".entryfirstIndexOf.loop_end"
.entryfirstIndexOf.loop_body:
  %".24" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 0
  %".25" = load i32, i32* %".15"
  %".26" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 %".25"
  %".27" = load i32, i32* %".26"
  store i32 0, i32* %".26"
  br label %".entryfirstIndexOf.loop_update"
.entryfirstIndexOf.loop_update:
  %".30" = load i32, i32* %".15"
  %".31" = add i32 %".30", 1
  store i32 %".31", i32* %".15"
  br label %".entryfirstIndexOf.loop_cond"
.entryfirstIndexOf.loop_end:
  %".34" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 0
  %".35" = call i32 @"calNext"(i8* %".2", i32* %".34")
  %".36" = alloca i32
  store i32 0, i32* %".36"
  br label %".entryfirstIndexOf.loop_end.loop_start"
.entryfirstIndexOf.loop_end.loop_start:
  br label %".entryfirstIndexOf.loop_end.loop_cond"
.entryfirstIndexOf.loop_end.loop_cond:
  %".40" = load i32, i32* %".36"
  %".41" = load i32, i32* %".8"
  %".42" = icmp slt i32 %".40", %".41"
  %".43" = icmp ne i1 %".42", 0
  br i1 %".43", label %".entryfirstIndexOf.loop_end.loop_body", label %".entryfirstIndexOf.loop_end.loop_end"
.entryfirstIndexOf.loop_end.loop_body:
  %".45" = alloca i32
  %".46" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 0
  %".47" = load i32, i32* %".36"
  %".48" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 %".47"
  %".49" = load i32, i32* %".48"
  store i32 %".49", i32* %".45"
  %".51" = load i32, i32* %".36"
  %".52" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 0
  %".53" = load i32, i32* %".36"
  %".54" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 %".53"
  %".55" = load i32, i32* %".54"
  %".56" = alloca [18 x i8]
  store [18 x i8] c"next [] %d  = %d\0a\00", [18 x i8]* %".56"
  %".58" = getelementptr [18 x i8], [18 x i8]* %".56", i32 0, i32 0
  %".59" = call i32 (i8*, ...) @"printf"(i8* %".58", i32 %".51", i32 %".55")
  br label %".entryfirstIndexOf.loop_end.loop_update"
.entryfirstIndexOf.loop_end.loop_update:
  %".61" = load i32, i32* %".36"
  %".62" = add i32 %".61", 1
  store i32 %".62", i32* %".36"
  br label %".entryfirstIndexOf.loop_end.loop_cond"
.entryfirstIndexOf.loop_end.loop_end:
  br label %".entryfirstIndexOf.loop_end.loop_end.loop_start"
.entryfirstIndexOf.loop_end.loop_end.loop_start:
  br label %".entryfirstIndexOf.loop_end.loop_end.loop_cond"
.entryfirstIndexOf.loop_end.loop_end.loop_cond:
  %".67" = load i32, i32* %".6"
  %".68" = load i32, i32* %".11"
  %".69" = icmp slt i32 %".67", %".68"
  %".70" = icmp ne i1 %".69", 0
  br i1 %".70", label %".entryfirstIndexOf.loop_end.loop_end.loop_body", label %".entryfirstIndexOf.loop_end.loop_end.loop_end"
.entryfirstIndexOf.loop_end.loop_end.loop_body:
  %".72" = load i32, i32* %".4"
  %".73" = getelementptr i8, i8* %".2", i32 %".72"
  %".74" = load i8, i8* %".73"
  %".75" = load i32, i32* %".6"
  %".76" = getelementptr i8, i8* %".1", i32 %".75"
  %".77" = load i8, i8* %".76"
  %".78" = icmp eq i8 %".74", %".77"
  %".79" = icmp ne i1 %".78", 0
  br i1 %".79", label %".entryfirstIndexOf.loop_end.loop_end.loop_body.if", label %".entryfirstIndexOf.loop_end.loop_end.loop_body.else"
.entryfirstIndexOf.loop_end.loop_end.loop_update:
  br label %".entryfirstIndexOf.loop_end.loop_end.loop_cond"
.entryfirstIndexOf.loop_end.loop_end.loop_end:
  %".120" = sub i32 0, 1
  ret i32 %".120"
.entryfirstIndexOf.loop_end.loop_end.loop_body.if:
  %".81" = load i32, i32* %".4"
  %".82" = add i32 %".81", 1
  store i32 %".82", i32* %".4"
  %".84" = load i32, i32* %".6"
  %".85" = add i32 %".84", 1
  store i32 %".85", i32* %".6"
  br label %".entryfirstIndexOf.loop_end.loop_end.loop_body.endif"
.entryfirstIndexOf.loop_end.loop_end.loop_body.else:
  %".88" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 0
  %".89" = load i32, i32* %".4"
  %".90" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 %".89"
  %".91" = load i32, i32* %".90"
  %".92" = sub i32 0, 1
  %".93" = icmp ne i32 %".91", %".92"
  %".94" = icmp ne i1 %".93", 0
  br i1 %".94", label %".entryfirstIndexOf.loop_e...if", label %".entryfirstIndexOf.loop_e...else"
.entryfirstIndexOf.loop_end.loop_end.loop_body.endif:
  %".108" = load i32, i32* %".4"
  %".109" = getelementptr i8, i8* %".2", i32 %".108"
  %".110" = load i8, i8* %".109"
  %".111" = icmp eq i8 %".110", 0
  %".112" = icmp ne i1 %".111", 0
  br i1 %".112", label %".entryfirstIndexOf.loop_e...if.1", label %".entryfirstIndexOf.loop_e...endif.1"
.entryfirstIndexOf.loop_e...if:
  %".96" = load i32, i32* %".4"
  %".97" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 0
  %".98" = load i32, i32* %".4"
  %".99" = getelementptr [50 x i32], [50 x i32]* %".14", i32 0, i32 %".98"
  %".100" = load i32, i32* %".99"
  store i32 %".100", i32* %".4"
  br label %".entryfirstIndexOf.loop_e...endif"
.entryfirstIndexOf.loop_e...else:
  %".103" = load i32, i32* %".6"
  %".104" = add i32 %".103", 1
  store i32 %".104", i32* %".6"
  br label %".entryfirstIndexOf.loop_e...endif"
.entryfirstIndexOf.loop_e...endif:
  br label %".entryfirstIndexOf.loop_end.loop_end.loop_body.endif"
.entryfirstIndexOf.loop_e...if.1:
  %".114" = load i32, i32* %".6"
  %".115" = load i32, i32* %".8"
  %".116" = sub i32 %".114", %".115"
  ret i32 %".116"
.entryfirstIndexOf.loop_e...endif.1:
  br label %".entryfirstIndexOf.loop_end.loop_end.loop_update"
}

define i32 @"testKmp"(i8* %".1", i8* %".2", i32 %".3") 
{
.entrytestKmp:
  %".5" = alloca [23 x i8]
  store [23 x i8] c"--new kmp test start:\0a\00", [23 x i8]* %".5"
  %".7" = getelementptr [23 x i8], [23 x i8]* %".5", i32 0, i32 0
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7")
  %".9" = alloca i32
  %".10" = call i32 @"firstIndexOf"(i8* %".1", i8* %".2")
  store i32 %".10", i32* %".9"
  %".12" = load i32, i32* %".9"
  %".13" = call i32 @"assertTest"(i32 %".12", i32 %".3")
  %".14" = load i32, i32* %".9"
  %".15" = alloca [19 x i8]
  store [19 x i8] c"expected %d got %d\00", [19 x i8]* %".15"
  %".17" = getelementptr [19 x i8], [19 x i8]* %".15", i32 0, i32 0
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 %".3", i32 %".14")
  ret i32 0
}

define i32 @"unittest"() 
{
.entryunittest:
  %".2" = alloca [13 x i8]
  store [13 x i8] c"123412341234\00", [13 x i8]* %".2"
  %".4" = alloca i32
  %".5" = getelementptr [13 x i8], [13 x i8]* %".2", i32 0, i32 0
  %".6" = call i32 @"strLen"(i8* %".5")
  store i32 %".6", i32* %".4"
  %".8" = alloca [50 x i32]
  %".9" = getelementptr [13 x i8], [13 x i8]* %".2", i32 0, i32 0
  %".10" = getelementptr [50 x i32], [50 x i32]* %".8", i32 0, i32 0
  %".11" = call i32 @"calNext"(i8* %".9", i32* %".10")
  %".12" = alloca [26 x i8]
  store [26 x i8] c"*******kmp test*********\0a\00", [26 x i8]* %".12"
  %".14" = getelementptr [26 x i8], [26 x i8]* %".12", i32 0, i32 0
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14")
  %".16" = alloca [21 x i8]
  store [21 x i8] c"aaababababababaaaaaa\00", [21 x i8]* %".16"
  %".18" = getelementptr [21 x i8], [21 x i8]* %".16", i32 0, i32 0
  %".19" = alloca [14 x i8]
  store [14 x i8] c"abababababaaa\00", [14 x i8]* %".19"
  %".21" = getelementptr [14 x i8], [14 x i8]* %".19", i32 0, i32 0
  %".22" = call i32 @"testKmp"(i8* %".18", i8* %".21", i32 4)
  %".23" = sub i32 0, 1
  %".24" = alloca [2 x i8]
  store [2 x i8] c"a\00", [2 x i8]* %".24"
  %".26" = getelementptr [2 x i8], [2 x i8]* %".24", i32 0, i32 0
  %".27" = alloca [3 x i8]
  store [3 x i8] c"aa\00", [3 x i8]* %".27"
  %".29" = getelementptr [3 x i8], [3 x i8]* %".27", i32 0, i32 0
  %".30" = call i32 @"testKmp"(i8* %".26", i8* %".29", i32 %".23")
  %".31" = sub i32 0, 1
  %".32" = alloca [2 x i8]
  store [2 x i8] c"b\00", [2 x i8]* %".32"
  %".34" = getelementptr [2 x i8], [2 x i8]* %".32", i32 0, i32 0
  %".35" = alloca [2 x i8]
  store [2 x i8] c"a\00", [2 x i8]* %".35"
  %".37" = getelementptr [2 x i8], [2 x i8]* %".35", i32 0, i32 0
  %".38" = call i32 @"testKmp"(i8* %".34", i8* %".37", i32 %".31")
  %".39" = sub i32 0, 1
  %".40" = alloca [5 x i8]
  store [5 x i8] c"aaaa\00", [5 x i8]* %".40"
  %".42" = getelementptr [5 x i8], [5 x i8]* %".40", i32 0, i32 0
  %".43" = alloca [2 x i8]
  store [2 x i8] c"b\00", [2 x i8]* %".43"
  %".45" = getelementptr [2 x i8], [2 x i8]* %".43", i32 0, i32 0
  %".46" = call i32 @"testKmp"(i8* %".42", i8* %".45", i32 %".39")
  %".47" = alloca [5 x i8]
  store [5 x i8] c"aaaa\00", [5 x i8]* %".47"
  %".49" = getelementptr [5 x i8], [5 x i8]* %".47", i32 0, i32 0
  %".50" = alloca [3 x i8]
  store [3 x i8] c"aa\00", [3 x i8]* %".50"
  %".52" = getelementptr [3 x i8], [3 x i8]* %".50", i32 0, i32 0
  %".53" = call i32 @"testKmp"(i8* %".49", i8* %".52", i32 0)
  ret i32 0
}

define i32 @"main"() 
{
.entrymain:
  %".2" = call i32 @"unittest"()
  ret i32 0
}
