import unittest
import math
from triangle import detect_triangle
def s_detect_triangle( a , b , c , e):
    return {
        0: detect_triangle(a,b,c),
        1: detect_triangle(a,c,b),
        2: detect_triangle(b,a,c),
        3: detect_triangle(b,c,a),
        4: detect_triangle(c,a,b),
        5: detect_triangle(c,b,a),
    }[e]
 
class TriangleTestCase(unittest.TestCase):
    def setUp(self):
        pass
        
    # Test TH nhap so :
    # Ngoai mien cho phep ben phai: <2^32-1 
    def test_floatvalueoutrangeR(self):
        self.assertEqual(s_detect_triangle(2**32+1,2**32+1,2**32+1,0),-1)
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(1,1,2**32+1,x),-1)
            self.assertEqual(s_detect_triangle(1,2**32+1,2**32+1,x),-1)
            
        
    # Ngoai mien cho phep ben trai: >0
    def test_floatvalueoutrangeL(self):
        self.assertEqual(s_detect_triangle(-1,-1,-1,0),-1)
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(1,1,-1,x),-1)
            self.assertEqual(s_detect_triangle(1,-1,-1,x),-1)
        
    # Hop le : tam giac deu
    def test_Fspecialtriangle1(self):
        self.assertEqual(detect_triangle(5,5,5),0)
    # Hop le : tam giac vuong can
    def test_Fspecialtriangle2(self):
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(1,1,math.sqrt(2),x),1)
            
    # Hop le : tam giac can k vuong :
    def test_Fspecialtriangle3(self):
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(5,5,3,x),2)
    # Hop le : tam giac vuong k can :
    def test_Fspecialtriangle4(self):
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(3,4,5,x),3)
    # Hop le : tam giac thuong :
    def test_Fnormaltriangle(self):
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(3,4,6,x),4)
    # Hop le : k la tam giac :
    def test_Fnottriangle(self):
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(1,1,4,x),-2)
        
    # Test TH co sau trong tham bien :
    # Sau khong hop le :
    def test_stringvaluenotcorrect(self):
        self.assertEqual(s_detect_triangle("abc","asdsad","asdsad",0),-1)
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle("abc",1,2,x),-1)
            self.assertEqual(s_detect_triangle("abc","asdsad",2,x),-1)

        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(-1,"asabc",2,x),-1)
            self.assertEqual(s_detect_triangle(-1,"asabc",-1,x),-1)
            self.assertEqual(s_detect_triangle(-1,"asabc","asabc",x),-1)
            
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(2**32+1,1,"abcsadsa",x),-1)
            self.assertEqual(s_detect_triangle(2**32+1,1,"abcsadsa",x),-1)
            self.assertEqual(s_detect_triangle(2**32+1,"abcsadsa","abcsadsa",x),-1)
                    
    # Sau hop le:
    # Ngoai mien cho phep ben phai: <2^32-1 
    def test_stringvalueoutrangeR(self):
                   
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(1,"2**32+1",1,x),-1)
            self.assertEqual(s_detect_triangle("1",2**32+1,1,x),-1)
            
            self.assertEqual(s_detect_triangle("1","2**32+1",1,x),-1)
            self.assertEqual(s_detect_triangle("1",2**32+1,"1",x),-1)
            
            self.assertEqual(s_detect_triangle("1","2**32+1","1",x),-1)
            
    # Ngoai mien cho phep ben trai: >0
    def test_stringvalueoutrangeL(self):
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(1,"1",-1,x),-1)
            self.assertEqual(s_detect_triangle(1,1,"-1",x),-1)
            
            self.assertEqual(s_detect_triangle(1,"1","-1",x),-1)
            self.assertEqual(s_detect_triangle("1","1",-1,x),-1)
            
            self.assertEqual(s_detect_triangle("1","1","-1",x),-1)
        
    # Hop le : tam giac deu
    def test_Sspecialtriangle1(self):
        self.assertEqual(s_detect_triangle("5","5","5",0),0)
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(5,5,"5",x),0)
            self.assertEqual(s_detect_triangle(5,"5","5",x),0)
            
    # Hop le : tam giac vuong can
    def test_Sspecialtriangle2(self):
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(1,"1",math.sqrt(2),x),1)
            self.assertEqual(s_detect_triangle("1","1",math.sqrt(2),x),1)
    # Hop le : tam giac can k vuong :
    def test_Sspecialtriangle3(self):
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(5,"5",math.sqrt(2),x),2)
            self.assertEqual(s_detect_triangle("5","5",math.sqrt(2),x),2)
    # Hop le : tam giac vuong k can :
    def test_Sspecialtriangle4(self):
        
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(3,"4",5,x),3)
            self.assertEqual(s_detect_triangle(3,4,"5",x),3)
            self.assertEqual(s_detect_triangle("3",4,5,x),3)

            
            self.assertEqual(s_detect_triangle("3","4",5,x),3)
            self.assertEqual(s_detect_triangle("3",4,"5",x),3)
            self.assertEqual(s_detect_triangle(3,"4","5",x),3)
            self.assertEqual(s_detect_triangle("3","4",5,x),3)

            
            self.assertEqual(s_detect_triangle("3","4","5",x),3)
 
    # Hop le : tam giac thuong :
    def test_Snormaltriangle(self):
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle("3",4,6,x),4)
            self.assertEqual(s_detect_triangle(3,"4",6,x),4)
            self.assertEqual(s_detect_triangle(3,4,"6",x),4)

            self.assertEqual(s_detect_triangle("3","4",6,x),4)
            self.assertEqual(s_detect_triangle(3,"4","6",x),4)
            self.assertEqual(s_detect_triangle("3",4,"6",x),4)
            self.assertEqual(s_detect_triangle("3","4",6,x),4)
            
            self.assertEqual(s_detect_triangle("3","4","6",x),4)
    # Hop le : k la tam giac :
    def test_Snottriangle(self):
        for x in range(0, 5):
            self.assertEqual(s_detect_triangle(1,1,"4",x),-2)
            self.assertEqual(s_detect_triangle(1,"1",4,x),-2)
            
            self.assertEqual(s_detect_triangle(1,"1","4",x),-2)
            self.assertEqual(s_detect_triangle("1","1",4,x),-2)
            
            self.assertEqual(s_detect_triangle("1","1","4",x),-2)
        
if __name__ == '__main__':
    unittest.main()
    
         
