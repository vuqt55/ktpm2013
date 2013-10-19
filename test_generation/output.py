import sys
import random
import unittest
from input import main

def change( x , i , j) :
        c = x[i]
        x[i] = x[j]
        x[j] = c

def randomX_Y( x , y ) :
        return random.randrange(x, y + 1, 1)

def list_value_test( test_list , value_list ) :

        if ( len(test_list) == 0 ) :
                for i in value_list :
                        t_list = []
                        t_list.append(i)
                        test_list.append(t_list)
        else :
                length_test = len(test_list)
                
                for i in range(1,len(value_list)) :
                        for j in range (0,length_test) :
                                temp_list = test_list[j][:]
                                
                                test_list.append(temp_list)

                for i in range(0,len(value_list)) :
                        for j in range (0,length_test) :
                            test_list[i*length_test + j].append(value_list[i])
                           
                
                        
        
def readNumber(line) :
        _Line = '' + line

        firstvalue = ''
        lastvalue = ''

        array_F = []
        array_L = []

        _Suportread = 0 
        
        for letter in _Line :
                if ( letter == ']' ) :
                        _Suportread = 0
                        # Fist always smaller than last .
                        if ( int(firstvalue) <=  int(lastvalue) ) :
                                
                                array_F.append(int(firstvalue))
                                array_L.append(int(lastvalue))
                                firstvalue = ''
                                lastvalue = ''
                                continue
                        else :
                                raise Exception("wrong input")
                                sys.exit(0)
                
                if ( letter == '[') :
                        _Suportread = 1
                        continue
                if ( letter == ';') :
                        _Suportread = 2
                        continue
                
                if ( _Suportread == 1 and "-0123456789".find(letter) != - 1 ) :
                        firstvalue += letter
                if ( _Suportread == 2 and "-0123456789".find(letter) != - 1 ) :
                        lastvalue += letter

  
        #sorting and check exception :
        for i in range(0,len(array_F) ):
                        
                for j in range(i+1,len(array_F) ):
                        # i have fist always smaller than last 
                        # it must be change index when :
                        if ( array_F[i] > array_F[j] ) :
                                if ( array_F[i] > array_L[j] ) :
                                        change( array_F , i , j)
                                        change( array_L , i , j)
                                else :
                                        #Exception when : Fist i <= Last j and Fist i > Fist j .
					
                                        raise Exception("wrong input")
                                        sys.exit(0)
                        
                        else :
				# continue .
                                if ( array_F[i] < array_F[j] and array_L[i] < array_F[j]  ) :
                                        continue
                                else :
                                        #other : Exception
                                        raise Exception("wrong input")
                                        sys.exit(0)
                                        
        # List value result :
        result = []
        for i in range(0,len(array_F) ):
                result.append(randomX_Y(array_F[i],array_L[i]))
        return result
                
                
                        
                                
        
def readfile(input) :
       
        
        
        t_Find_def = -1
        t_Find_main = -1

        t_Boolean_main = 0
        t_String_main = []

        t_Line_main = ''
               
        for line in input:
                if  ( t_Boolean_main == 1 ) :
                        t_String_main.append(line)   
                else :
                        t_Find_def = line.find("def")
                        if ( t_Find_def == -1 ) :
                                continue
                        else :
                                t_Find_main = line.find("main")

                        if ( t_Find_main == -1 ) :
                                t_Find_def = -1
                                continue
                        else :
                              
                                t_Boolean_main = 1
                                t_Line_main = line

        # this is number of Variable Input :
        t_countVariable = t_Line_main.count(',')
        t_countVariable += 1

        #two array store value 
        t_Firstvalue = []
        t_Lastvalue = []
        
        t_Suportread = 0
        
        t_Listvariable_value = []
        
        for line in t_String_main:
                
                if ( t_Suportread == 0 and line.find("'''") != -1) :
                         t_Suportread += 1
                         continue
                else :
                        if ( t_Suportread == 1 and line.find("'''") != -1 ) :
                                break
                        else :
                                t_Listvariable_value.append(readNumber(line))
                        
        
        s_result = []
        for i in t_Listvariable_value :
                list_value_test(s_result , i)
        return s_result


class TestSequence(unittest.TestCase):
        pass
def test_generator(a):
        def test(self):
		x = main(*a)
                self.assertEqual(main(*a),x);
        return test

if __name__ == "__main__":

	ins = open( "input.py", "r" )
	list_testcase =  readfile(ins)
        
        i = 0
        
	for i_testcase in list_testcase :
                test_name = 'test_%s' % i
                test = test_generator(i_testcase)
                setattr( TestSequence , test_name, test)
                i += 1
        unittest.main()
	
	ins.close()

	
