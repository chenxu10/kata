package src;
public class TestSort{
    public static void testsort(){
        String [] input = {"I","Have","An","Egg"};
        String [] expected = {"An","Egg","Have","I"};
        
        Sort.sort(input);
        org.junit.Assert.assertArrayEquals(expected, input);}
    public static void main(String [] args) {
        testsort();}
}