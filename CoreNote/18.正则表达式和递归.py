# 正则表达式 字符串验证规则
import re
# match 从头匹配
s1="cry ik gsq ik cry"
result1=re.match("cry",s1)            # match从头匹配“cry”
print(result1)                              # 输出匹配对象的详细信息
print(result1.span())                       # 输出匹配到的位置（元组）
print(result1.group())                      # 输出匹配到的内容
print()
# search 搜索匹配一个
s2="cry very very ik gsq!!!!"
result2=re.search("very",s2)
print(result2)                              # 输出匹配对象的详细信息
print(result2.span())                       # 输出匹配到的位置（元组）
print(result2.group())                      # 输出匹配到的内容
print()
# findall 搜索全部匹配
s3="cry very ik gsq!!!!"
result3=re.findall("!",s3)
print(result3)                              # 输出匹配对象的列表形式
print()



# 元字符匹配
"""
单字符匹配：
.   匹配任意单个字符（除了换行符\n）,\.匹配点本身
[]  匹配[]中列举的字符
\d  匹配任意数字，等同于[0-9]
\D  匹配非数字
\w  匹配任意字母、数字或下划线，等同于[a-z,A-Z, 0-9,_]
\W  匹配非字母数字下划线
\s  匹配任意空白字符（空格、制表符、换行符等）
\S  匹配非空白字符
数量匹配：
*     匹配前一个规则的字符出现零次或多次
+     匹配前一个规则的字符出现一次或多次
?     匹配前一个规则的字符出现零次或一次
{n}   匹配前一个规则的字符出现恰好n次
{m,}  匹配前一个规则的字符出现至少m次
{m,n} 匹配前一个规则的字符出现至少m次，至多n次
字符组：
^   匹配字符串开头
$   匹配字符串结尾
\b  匹配一个单词的边界
\B  匹配非单词边界
|   匹配左右任意一个表达式
()  将括号中字符作为一个分组
"""
s4="a234860sdfw242owhd23452ih1i3o4103#^*&^(*&#)*_ _ ^#)*&_ wofowiej"
result4=re.findall(r"\d",s4)          # 字符串前带r表示转义字符无效，即普通字符的意思
print(result4,'\n')                          # 输出匹配对象的列表形式（全部数字）
result5=re.findall(r"\W",s4)
print(result5,'\n')                          # 输出匹配对象的列表形式（全部符号，非字母、数字、下划线）
result6=re.findall(r"[c1r1y1]",s4)    # 找c,r,y,1四种字符
print(result6,'\n')
result7=re.findall(r"[a-zA-Z]",s4)    # 找所有大小写字母
print(result7,'\n')

p1="20051217"
rule1=r"^[0-9a-zA-Z]{6,10}$"                  # 限定长度6到10位，由数字和字母组成
result8=re.findall(rule1,p1)
print(result8,'\n')

p2="123450"
rule2="^[1-9][0-9]{4,10}$"                    # 第一位不能为零，由数字组成,长度5到11位
print(re.findall(rule2, p2))                  # 如果没有^和$：正则会字符串中任意位置匹配符合规则的子串


import re
p3="1637153678@qq.com"
rule3="(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)"
print(re.findall(rule3, p3))
"""
对rule3的解释：
^   $确定始末
[\w-]+              匹配一个或多个字母数字下划线(\w的作用）或者横杠（手动添加的-）；+表示这样的内容至少一个
(\.[\w-]+)*         匹配零个或多个由点号连接的字母数字下划线或者横杠
@                   匹配@符号
(qq|163|gmail)      匹配qq，163，或者gmail
(\.[\w-]+)+         匹配一个或多个由点号连接的字母数字下划线或者横杠
整体打（）            让findall从整体检索而不是内部括号，在其后加[0][0]更美观
或者将findall改为match
"""


# 递归算法


