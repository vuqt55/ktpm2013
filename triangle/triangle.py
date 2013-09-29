import math
   
def detect_triangle(b , c, d):
# -1 : nhap sai
# -2 : khong lam tam giac
# 0 : tam giac deu
# 1 : tam giac vuong can
# 2 : tam giac can
# 3 : tam giac vuong
# 4 : tam giac thuong .
    a = [0]*3
    a[0] = b;
    a[1] = c;
    a[2] = d;
    
    try :
        a[1] = float(a[1])
        a[2] = float(a[2])
        a[0] = float(a[0])
    except ValueError:
        print "Nhap sai"
        return -1
    if a[0] <= 0 or a[1]<= 0 or a[2] <= 0 or a[0] >= 2**32 -1 or a[1] >= 2**32 -1 or a[2] >= 2**32 -1:
        print "Canh phai lon hon khong "
        return -1
    elif a[0] + a[1] <= a[2] or a[1] + a[2] <= a[0] or a[0] + a[2] <= a[1] :
        print "Khong phai tam giac"
        return -2
    elif a[0] == a[1] and a[1] == a[2] :
        print "La tam giac deu"
        return 0
    elif a[0] == a[1] or a[1] == a[2] or a[0] == a[2] :
         if math.fabs(a[0]*a[0] + a[1]*a[1] -(a[2]*a[2])) < 10**-9 or math.fabs(a[2]*a[2] + a[1]*a[1] - a[0]*a[0]) < 10**-9 or  math.fabs(a[2]*a[2] + a[0]*a[0] - a[1]*a[1]) < 10**-9 :
             print "La tam giac vuong can "
             return 1
         else :
             print "La tam giac can"
             return 2   
    elif math.fabs(a[0]*a[0] + a[1]*a[1] - a[2]*a[2]) < 10**-9 or math.fabs(a[2]*a[2] + a[1]*a[1] - a[0]*a[0]) < 10**-9 or  math.fabs(a[2]*a[2] + a[0]*a[0] - a[1]*a[1])< 10**-9 :
        print "La tam giac vuong"
        return 3
    else :
        print "La tam giac"
        return 4

