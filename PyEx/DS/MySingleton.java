public class MySingleton {

    private static MySingleton obj ;

    private MySingleton() {}
    static {
        obj = new MySingleton();
    }
    public static MySingleton getInstance() { return obj; }
    public void show() { System.out.println("hello world"); }
    public static void main(String args[]) {
        MySingleton ms = new MySingleton();
        ms.show();
        MySingleton ms2 = new MySingleton();
        ms2.show();
    }
}
