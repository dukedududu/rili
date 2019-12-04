import calendar#日历模块
 
# 输入指定年月

m = int(input('输入月份: '))
y = int(input('输入年份: '))
 
# 显示日历
print(calendar.month(y,m))
