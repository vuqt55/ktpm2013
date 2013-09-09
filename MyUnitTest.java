import org.junit.Test;
import static org.junit.Assert.*;

public class MyUnitTest
{
	@Test
	public void test1(){
		MyUnit test = new MyUnit();
		try
		{
			float f = Float.parseFloat(  test.giaiptbac1(1,1) );
			assertEquals(-1, result);
		}
		catch ( Exception e)
		{
			System.out.println("T1 Failted");
		}
	}

	@Test
	public void test2(){
		MyUnit test = new MyUnit();
		try
		{
			float f = Float.parseFloat(  test.giaiptbac1(0,0) );
			System.out.println("T2 Failted");
		}
		catch ( Exception e)
		{
			assertEquals("vo so nghiem", test.giaiptbac1(0,0) );
		}
	}


	@Test
	public void test3(){
		MyUnit test = new MyUnit();
		try
		{
			float f = Float.parseFloat(  test.giaiptbac1(0,1) );
			System.out.println("T3 Failted");
		}
		catch ( Exception e)
		{
			assertEquals("vo nghiem", test.giaiptbac1(0,0) );
		}
	
	}
	public static void main(String args[]){
	
	}
}