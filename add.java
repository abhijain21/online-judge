import java.io.*;

class add {

  public static void main(String [] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // System.out.println("Enter two no.");
    int x=Integer.parseInt(br.readLine());
    int y=Integer.parseInt(br.readLine());
    // int z=x*y;
    int a=x+y;
    System.out.println(a);

  }

}
