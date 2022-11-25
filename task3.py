# напишите программу, которая по заданному номеру
# четверти, показывает диапазон возможных координат точек 
# в этой четверти

qutaer = int(input('введите номер четверти:'))
if qutaer==1:
    print('a > 0, b > 0')
elif qutaer==2:
    print('a < 0, b > 0') 
elif qutaer==3:
   print('a < 0, b < 0')  
elif qutaer==4:
    print('a < 0, b > 0') 
else:
    print('error qutaer not found')
