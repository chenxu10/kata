public class Dog {
    public int weightpounds;
    
    public Dog(int w){
        weightpounds = w;
    }

    public void makenoise() {
        if (weightpounds < 5){
            System.out.println("bar....");
        }
        else {
            System.out.println("wo....");
        }
    }
}