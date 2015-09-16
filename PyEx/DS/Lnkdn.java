import java.util.StringTokenizer;

class LinkedList {
    private LinkedList next = null;
    private int node = 0;

    public LinkedList(int val) { this.node = val; this.next = null; }

    public LinkedList addNode(int val) { 
        LinkedList curr = this;
        while(curr.next != null) { curr = curr.next; }
        LinkedList newNode = new LinkedList(val);
        curr.next = newNode;

        return this;
    }

    public LinkedList findMid() {
        LinkedList slP = this;
        LinkedList dblP = slP.next.next;
        while(slP != null && dblP != null && dblP.next != null) {
            slP = slP.next;
            dblP = dblP.next;
            System.out.println("slp: "+slP.getNode()+" dblP: "+ dblP.getNode());
        }
        return slP;
    }
    public int getNode() { return this.node; }
}

class Lnkdn {

    private int testval = 1001;
    private int num = 2;

    public int getTestVal() { return testval; }
    public double powLoop(int a, int b) {
        if(b == 0) return 1;
        if(b == 1) return a;

        double res = 1;
        while(b > 0) {
            res = a*res;
            b--;
        }
        return res;
    }
    public double powRec(int a, int b) {
        if(b == 0) return 1;
        if(b == 1) return a;
        
        double res = powRec(a, b/2);
        res *= res;

        return ((b%2 == 0) ? res : a * res);

    }

    public int findMax(int[] arr) {
        int max = arr[0];
        for(int i=0; i < arr.length; i++) {
            if(max < arr[i]) max = arr[i];
        } 
        return max;
    }

    public double sqrt(double number) {
        double num = number/2;
        do {
            num = (num + number/num)/2;
            System.out.println("num is: "+num);

        } while((num*num - number)> 0.00001);

        return num;
    }

    public String maxSumSubseq(int[] arr) {
        int currMax = 0;
        int totMax = arr[0];
        int start=0, end=0;
        for(int i=0; i < arr.length; i++) {
            currMax += arr[i];
            if(currMax < 0) { currMax = 0; start = i; }
            //totMax = Math.max(totMax, currMax);
            if(totMax < currMax) { totMax = currMax; end = i; }
        } 
        StringBuffer sb = new StringBuffer();
        sb.append(totMax).append("|").append(start).append("|").append(end);
        //return totMax+'-'+start+'-'+end;
        return sb.toString();
    }
    public int wordDistance(String str, String w1, String w2) {

        StringTokenizer st = new StringTokenizer(str, " ");
        int minDist=Integer.MAX_VALUE, dist=0;
        while(st.hasMoreTokens()) {
            String word = st.nextToken();
            if(word.equals(w1)) {
                dist = 0;
            } else if(word.equals(w2)) {
                minDist = Math.min(minDist, dist);
            }
            dist++;
        }

        if(minDist == Integer.MAX_VALUE || minDist == 0) {
            return -1;
        } else {
            return minDist;
        }
    }


    public static void main(String args[]){

        Lnkdn obj = new Lnkdn();
        System.out.println("testval: "+obj.getTestVal());
        System.out.printf("pow of 2, 8: %f\n", Math.pow(2, 8));
        System.out.printf("powRec of 2, 8: %f\n", obj.powRec(2, 8));
        System.out.printf("powLoop of 2, 8: %f\n", obj.powLoop(2, 8));
    
        int[] arr = { 2, 5, -7, 6, 0, -1, 4 };
        System.out.println("max - "+ obj.findMax(arr));
        System.out.println("maxSumSubSeq - "+ obj.maxSumSubseq(arr));
        System.out.printf("sqrt %f = %f\n", 81.0,obj.sqrt(81.0));

        System.out.println("WordDist..."+ obj.wordDistance("hey hello how are you doing you?", "hello", "you"));

        LinkedList ll = new LinkedList(10);
        ll.addNode(21);
        ll.addNode(11);
        ll.addNode(33);
        ll.addNode(45);

        System.out.println("mid of LL : "+ ll.findMid().getNode()); 
    }

}
