package src;

public class TestSort{
    public static void test_sort(){
        String [] input = {"I","Have","An","Egg"};
        String [] expected = {"An","Egg","Have","I"};
        
        Sort.sort(input);
        org.junit.Assert.assertArrayEquals(expected, input);}
    
    public static void test_swap(){
        String [] input = {"I","Have","An","Egg"};
        String [] expected = {"An","Have","I","Egg"};
        Sort.swap(input,0,2);
        org.junit.Assert.assertArrayEquals(expected, input);
    }

    // Test Sort.findSmallest()
    public static void test_findSmallest(){ 
        String [] input = {"I","Have","An","Egg"};
        int expected = 2;
        int actual = Sort.findSmallest(input,2);
        org.junit.Assert.assertEquals(expected, actual);
    }    
    public static void main(String [] args) {
        test_swap();
        test_findSmallest();
        test_sort();}
    }