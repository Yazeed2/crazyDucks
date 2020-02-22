topLeft = 'top:100px;left:0;'
topRight = 'top:100px;left:100%;'
topCenter = 'top:100px;left:50%;'
left= 'top:50%;left:0;'
right= 'top:50%;left:100%;'
bottomLeft = 'top:100%;left:0;'
bottomRight = 'top:100%;left:100%;'
bottomCenter = 'top:100%;left:50%;'
center = 'top:50%;left:50%;'



arr = [topLeft, topRight, topCenter, left, right, bottomLeft, bottomRight, bottomCenter, center]
num = 0
number = '1'
line = ''
for main in arr:
    for element in arr:
        for elem in arr:

            num = num+1
            number = num.__str__()
            line = '.animation'+ number + '{  animation: animation'+number+' 5s infinite, walk 0.3s infinite ;}  \n'
        # line= '@keyframes animation'+number+'{from{ '+main+'   @include front;} 25%{ top:50%;left:50%;}50%{   '+element+'       @include front;    }    51%{    '+element+'  @include back;} 75%{ top:50%;left:50%; }to{'+x+' @include back;   } } \n'
            # line = '@keyframes animation'+number+'{    from{    '+main+'   @include front;}     33%{    '+element+'}     66% { '+elem+'      @include front;    }           67%{      '+elem+'  @include back;}            to{    '+main+' @include back;   } } \n' 
           
            seg = open("animatio.txt", "a+")
            seg.write(line)
            seg.close()
