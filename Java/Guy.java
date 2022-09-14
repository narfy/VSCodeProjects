public class Guy {
    String name;

    public Guy(String s) {
      name = s;
    }
  
    public static void main(String[] args) {
      Guy myObj = new Guy("Bob");
      System.out.println(myObj.name);
    }
}