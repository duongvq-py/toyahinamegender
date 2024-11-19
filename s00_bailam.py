#region debai
"""
--- ma debai / id
hi(name,gender)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03hinamegender

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://github.com/namgivu/toya03hinamegender

--- debai / problem
Hay viet ham hi(name, gender) xuat ra cau chao theo mota benduoi

--- vidu mau / testcase
Khi chay voi input    | Ketqua output
--------------------- | ------------
hi('Mom', 'f')        | Hi Ms Mom!
hi('Dad', 'm')        | Hi Mr Dad!
hi('TOYA', None)      | Hi TOYA!
hi(None, None)        | Hi!
"""

#endregion debai


#region bailam
def hi(name, gender):
   if(gender == 'f' and name):
      return f'Hi Ms {name}!'
   elif(gender == 'm' and name):
      return f'Hi Mr {name}!'
   elif name: 
      return f'Hi {name}!'
   else:
      return f'Hi!'
#endregion bailam
