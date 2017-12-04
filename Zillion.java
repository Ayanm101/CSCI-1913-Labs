class Zillion 
{
  private int[] digits; //private array digits
  
  public Zillion(int size)
  {
     digits = new int[size]; 
  }

  
  ////////////////////////////////////////////
  
  public void increment()
  {
	int length = digits.length ; //length of the array
    int initial = length-1;
    int counter = 0;
    
    
    while (counter < length) //if condition is false it continues
    {
        if (digits[initial] == 9)
        {
          digits[initial] = 0;
          initial-=1;
          counter+=1;
        }

        else
        {
          digits[initial]+=1;
          counter+=1;
          break;
        }

    }


  }
  
  //////////////////////////////////////////////////

  public String toString()
  { 
    String newString = "";
    int length = digits.length;
    for(int i=0; i < length ;i++ )
    {
    newString = newString + digits[i]; //newString += str(self.lists[i]) 
    }

    return newString;

  }

}

class IssaDriver
{
  public static void main(String[] args)
  {
    Zillion z = new Zillion(2);
    System.out.println(z);  //  00  2 points

    z.increment();
    System.out.println(z);  //  01  2 points

    z.increment();
    System.out.println(z);  //  02  2 points

    z.increment();
    z.increment();
    z.increment();
    z.increment();
    z.increment();
    z.increment();
    z.increment();
    z.increment();

    System.out.println(z);  //  10  2 points
    z.increment();
    System.out.println(z);  //  11  2 points

    z = new Zillion(4);
    System.out.println(z);  //  0000  2 points

    for (int j = 1; j <= 999; j += 1)
    {
      z.increment();
    }
    System.out.println(z);  //  0999  2 points

    z.increment();
    System.out.println(z);  //  1000  2 points

    for (int j = 1; j <= 999; j += 1)
    {
      z.increment();
    }
    System.out.println(z);  //  1999  2 points

    z.increment();
    System.out.println(z);  //  2000  2 points

    for (int j = 1; j <= 7999; j += 1)
    {
      z.increment();
    }
    System.out.println(z);  //  9999  2 points

    z.increment();
    System.out.println(z);  //  0000  2 points

    z.increment();
    System.out.println(z);  //  0001  1 point
  }
}