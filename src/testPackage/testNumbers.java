package testPackage;

import static org.junit.Assert.*;

import org.junit.Test;

public class testNumbers {

	@Test
	public void test() {
		testFunctions junit = new testFunctions();
		int result = junit.AddNumbers(100,200);
		assertEquals (300,result);
	}

}
