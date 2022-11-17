package testPackage;

import static org.junit.Assert.*;

import org.junit.Test;

public class testAddStr {

	@Test
	public void test() {
		testFunctions junitstring = new testFunctions();
		String result = junitstring.AddString("capstone","project");
		assertEquals("capstoneproject",result);
	}

}
