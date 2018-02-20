import java.util.*;

public class HelloWorld{

    public static int[] coinchange(int[] coinsDenomination, int monetaryValue) {
        
        int[] track = new int[monetaryValue+1]; 
        int[] keep = new int[monetaryValue+1]; //we create two arrays of integers starting from 0 to montaryValue
        //the array 'track' keeps track of the minimum number of coins needed
        //the array 'keep' stores the value of the first coin used
        
        int min;
        int coin = 0;
        
        for (int i=1; i < monetaryValue+1 ; i++)
        {
            min = monetaryValue + 1;
            for (int j=0; j< coinsDenomination.length ; j++)
            {
                if ( (coinsDenomination[j] <= i) && (1 + track[i-coinsDenomination[j]] < min) )
                {
                    min = 1 + track[i-coinsDenomination[j]];
                    coin = j;
                }
            }
            track[i] = min;
            keep[i] = coin;
        }
        int x = monetaryValue;
        ArrayList<Integer> L = new ArrayList<>();
        while (x>0)
        {
            L.add(coinsDenomination[keep[x]]);
            x = x - coinsDenomination[keep[x]];
        }
        
        int[] ret = new int[L.size()];
        for (int k=0; k < ret.length; k++)
        {
            ret[k] = L.get(k).intValue();
        }
        return ret;
    }

    public static void afficherTableau(int[] tableau) {
        for (int i = 0; i < tableau.length; i++) {
            System.out.print(tableau[i] + " ; ");
            
        }
    }


     public static void main(String []args){
        int[] intArray = new int[] {50,30,5};
        int v = 60;
        int[] tab = new int[coinchange(intArray,v).length];
        tab = coinchange(intArray,v);
        afficherTableau(tab);
     }
}