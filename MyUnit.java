
import java.util.*;

// First  Example Test
// Giai phuong trinh bac nhat .

public class MyUnit{
	//ax+b = 0;
	public String giaiptbac1(float a , float b){
		if ( a != 0  ){
			float result = -b/a ;
			return "" + result;
		} else {
			if ( b == 0 ) return "vo so nghiem";
			else {
				return "vo nghiem";
			}
		}	
	}
	

	public void test1(){
		try
		{
			float f = Float.parseFloat(  giaiptbac1(1,1) );
			if ( f == -1 )
			{
				System.out.println("T1 Succesed");
			}
		}
		catch ( Exception e)
		{
			System.out.println("T1 Failted");
		}
	}

	public void test2(){
		try
		{
			float f = Float.parseFloat(  giaiptbac1(0,0) );
			System.out.println("T2 Failted");
		}
		catch ( Exception e)
		{
			if ( giaiptbac1(0,0).compareTo("vo so nghiem") == 0 )
			{
				System.out.println("T2 Succesed");
			} else System.out.println("T2 Failed");
		}
	}
	
	public void test3(){
		try
		{
			float f = Float.parseFloat(  giaiptbac1(0,1) );
			System.out.println("T3 Failted");
		}
		catch ( Exception e)
		{
			if ( giaiptbac1(0,1).compareTo("vo nghiem") == 0 )
			{
				System.out.println("T3 Succesed");
			} else System.out.println("T3 Failed");
		}
	}
	
	public static void main( String args[]){
		MyUnit test = new MyUnit();
		test.test1();
		test.test2();
		test.test3();
	}

}