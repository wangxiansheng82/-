# print("hello world")
# a=1
# print(a)
# b="小妹"
# print(type(b))
# d=True
# print(type(d))
# c="我爱"
# print(c+b)

# ctrl+/ 多段代码注释
# 元组
# a_tuple=(1,2,3,4,5,6,7,8)#元组
# print(a_tuple)
# print(a_tuple[0])
# print(a_tuple[1:5:3])#切片

#列表
# a_list=[1,2,3,7,4,5,6]#列表
# print(a_list[2:4])
# a_list.append(7)#追加列表值,一次只能追加一个
# a_list.insert(1,"中国")#列表插入值，一次只能插入一个
# a_list.pop(3)#删除列表某个值，根据下标删除
# a_list.remove("中国")#删除列表某个值，根据内容删除
# a_list.clear()#清空列表所有内容
# a_list.reverse()#反转列表数据
# a_list.sort()#正序展示列表数据
# c_list=sorted(a_list)
# print(a_list)
# print(c_list)

#字典
# a_zidian={"name":"汪总","age":18,"addr":"安徽"}     #字典是以键值对的形式创建
# # a_zidian["age"]=8   #修改字典信息
# # x=a_zidian["name"]#字段可以查询，按“键”打印一个值
# # print(x)
# # print(a_zidian.keys())  #只查询键
# # print(a_zidian.items())  #只查询值，但是也会展示键
# # a_zidian.pop("addr") #字典形式的用pop删除可以不用写下标，写键就行
# # a_zidian["like"]="苹果"  #字典增加键值对
# print(a_zidian)


#占位符
# a=0
# b=1
# print('打印a={1}和b={0}'.format(a,b))  #format就是一个占位符，跟据下标来进行占位（a下标为0，b下标为1）

#取余
# x=8
# y=3
# z=x%y
# print(z)

#次方、开平方
# a=4
# b=a * a  #a的平方
# b=a ** 2 #a的2次方，3的话就是a的3次方以此类推
# print(b)

#加等、减等、乘等、除等
# a=1
# b=2
# # a+=b     #等于a=a+b
# # a-=b
# # a*=b
# a/=b
# print('除于后等于',a)

#"与" "或"关系
# a=1
# b=2
# # print(a==1 and b==2)
# print(a==1 or b==2)

#范围内运算以及not的用法(in:在，not：不在)
# a="张三"
# b=["李四","张三"]
# c=["李四","王五"]
# print("张三在b表里面吗？",a in b)
# print("张三在c表里面吗？",a in c)
# print("张三不在c表里面吗？",a not in c)

#两数交换
# a=1
# b=2
# a,b=b,a   #两数交换
# print(a,b)

#输出
# stu_name = input("请输入你的姓名:")
# chinese_score = input("请输入你的语文考试成绩:")
# math_score = input('请输入你的数学考试成绩:')
# english_score = input("请输入你的英语考试成绩:")
# total_01 = chinese_score + math_score + english_score      #未转换类型分数相加错误
# # total_01=int(chinese_score)+int(math_score)+int(english_score)   #强制类型转换
# print("{}同学，你好，你本次期末考试的总成绩是:{}分。".format(stu_name,total_01))

# #单分支语句
# age = int(input('老王，请输入你的年龄:'))
# if age >= 18:
#     print('成年人的世界都不容易，耗子尾汁!')

#双分支语句
# sex=(input("请输入你的性别："))
# if sex == "男":
#     print("小帅哥，你好")
# else:
#     print("小美女，你好")

#多分支
# zheng_01= int(input("请输入正整数限制1-3："))
# if zheng_01 == 1:
#     print("这是1")
# elif zheng_01 == 2:
#     print("这是2")
# elif zheng_01 == 3:
#     print("这是3")
# else:
#     print("你输入的不是正整数")

# #分支嵌套
# print("欢迎来到游戏世界")
# rank=input("请输入最高段位：")
# if rank in("王者","钻石","星耀"):
#     position=input("请输入你报名的位置：")
#     if position in ["上单", "中单","下路"]:
#         print("你所报名的位置已满")
#     elif position == "辅助" or position =="打野":
#         print("报名成功")
#     else:
#         print("你所输入的{}位置错误".format(position))
# else:
#     print("段位不符合")

#while循环语句
# a=1
# while a<=10:
#     print(a)  #python自带回车
#     a=a+1
# print("-"*10)
#while倒叙循环
# a=10
# while a>=1:
#     print(a,end="、")   #end表示不需要换行，中间以顿号隔开
#     a-=1
# print("\n")   #表示回车展示
# print("-"*10)

#作业题：输入三个整数，判断它们是可以构成等边三角形还是等腰三角形还是普通三角形还是不能构成三角形，给出相应的输出。
# a=int(input("请输入第一个数："))
# b=int(input("请输入第二个数："))
# c=int(input("请输入第三个数："))
# if a + b <= c or a + c <= b or b + c <= a:
#     print("这构不成三角形")
# elif a == b or a == c or b == c:
#     print('这是等腰三角形')
# elif a == b and b == c:
#     print("这是等边三角形")
# else:
#     print("这是不规则三角形")

#计算一年有多少天
# year=int(input("请输入你想计算的年份："))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     days = 366
# else:
#     days = 365
# print(days*24*60*60)



