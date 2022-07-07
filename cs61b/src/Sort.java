package src;
public class Sort {   
    public static void sort(String[] x){
        // pick the smallest element
        // swap to the front
        // recursively do the same thing with the remaining list(N -1)
        helpsort(x, 0);
    }

    public static void helpsort(String[] x, int start_index){
        if (start_index == x.length){
            return;
        }
        int smallest = Sort.findSmallest(x, start_index);
        swap(x, start_index, smallest);    
        helpsort(x, start_index + 1);
    }
    
    public static void swap(String[] x, int start_index, int end_index){
       String temp = x[start_index];
       x[start_index] = x[end_index];
       x[end_index] = temp;
    }

    public static int findSmallest(String[] x, int start_index){
        int smallestindex = start_index;
        for (int i = start_index; i < x.length; i+=1){
            int cmp = x[i].compareTo(x[smallestindex]); 
            if (cmp < 0){
                smallestindex = i;
            }
        }
        return smallestindex;
    }
}
