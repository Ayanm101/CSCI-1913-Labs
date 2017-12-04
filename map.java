class Map<Key, Value>
{
	private Key[] keys;
	private Value[] values; 
	private int count;
	
	public Map(int length)
	{
		if( length < 0)
		{
			throw new IllegalArgumentException("length is less than 0");
		}
		else
		{
			count = 0;//empty map
			keys = (Key[]) new Object[length];//has L(length) elements 
			values = (Value[]) new Object[length];//has L(length) elements 
			}
			
	}//end of map
		
	public Value get(Key key)
	{
		if (isIn(key))
		{
			return values[where(key)];
		} 
		else
		{
			throw new IllegalArgumentException(" no element equal to key in keys");
		}
	}
	
	private boolean isEqual(Key leftKey, Key rightKey)
	{
		if(leftKey==null || rightKey == null)//shows that both are null
		{
			return (leftKey == rightKey); //leftkey is equal to rightkey 
		}
			
		else
		{
			return leftKey.equals(rightKey); // leftkey does'nt equal rightkey
		}
			
	}//end of isEqual
			
	public boolean isIn(Key key)//Test if there is an element in keys that is equal to key.
	{
			
		for(int i=0; i<count; i++) //count can be any int
		{
			if(isEqual(keys[i], key)) //compare the keys array with the key we pass through
			{
				return true;
			}
		}
			
			return false;
	}//end of isin
			
	public void put(Key key, Value value) 

	{
		for(int i=0; i<keys.length; i++)
		{
			if(isEqual(keys[i],key))
			{
				values[i]=value;
			}
		}
			if(!isIn(key))
			{
				if(count < keys.length)
				{
					keys[count]=key;
					values[count]=value;
					count+=1;		
			}
				
			else
			{
				throw new IllegalStateException("keys and values are full");
			}
					
		}//end of put
		
	}
			
	private int where(Key key)
	{
		for(int i=0; i<keys.length; i++)
		{
			if(isEqual(keys[i],key))
			{
				return i;
			}
		}
			return -1;
	}//end of where
			
}// end of class

//
//Tests for CSci 1913 Lab 7
//James Moen
//07 Mar 17
//
//The TRY-CATCH statements catch exceptions thrown by MAP's methods, so that
//the program can continue to run even if a method fails. We haven't talked
//about TRY-CATCH'es in lecture yet.
//
//Each test has a comment that shows what it should print, and how many
//points it is worth, for a total of 40 points.

//HOGWARTS. The Hogwarts dating service.

class Hogwarts
{

//MAIN. Make an instance of MAP and test it.

public static void main(String [] args)
{
Map<String, String> map;

try
{
  map = new Map<String, String>(-5);
}
catch (IllegalArgumentException ignore)
{
  System.out.println("No negatives");       //  No negatives  2 points.
}

map = new Map<String, String>(5);

map.put("Harry",     "Ginny");
map.put("Ron",       "Lavender");
map.put("Voldemort", null);
map.put(null,        "Wormtail");

System.out.println(map.isIn("Harry"));      //  true          2 points.
System.out.println(map.isIn("Ginny"));      //  false         2 points.
System.out.println(map.isIn("Ron"));        //  true          2 points.
System.out.println(map.isIn("Voldemort"));  //  true          2 points.
System.out.println(map.isIn(null));         //  true          2 points.
System.out.println(map.isIn("Joanne"));     //  false         2 points.

System.out.println(map.get("Harry"));       //  Ginny         2 points.
System.out.println(map.get("Ron"));         //  Lavender      2 points.
System.out.println(map.get("Voldemort"));   //  null          2 points.
System.out.println(map.get(null));          //  Wormtail      2 points.

try
{
  System.out.println(map.get("Joanne"));
}
catch (IllegalArgumentException ignore)
{
  System.out.println("No Joanne");          //  No Joanne     2 points.
}

map.put("Ron",   "Hermione");
map.put("Albus", "Gellert");
map.put(null,    null);

System.out.println(map.isIn(null));         //  true          2 points.
System.out.println(map.isIn("Albus"));      //  true          2 points.

System.out.println(map.get("Albus"));       //  Gellert       2 points.
System.out.println(map.get("Harry"));       //  Ginny         2 points.
System.out.println(map.get("Ron"));         //  Hermione      2 points.
System.out.println(map.get("Voldemort"));   //  null          2 points.
System.out.println(map.get(null));          //  null          2 points.

try
{
  map.put("Draco", "Pansy"); 
}
catch (IllegalStateException minnesota)
{
  System.out.println("No Draco");           //  No Draco      2 points.
}
}
}