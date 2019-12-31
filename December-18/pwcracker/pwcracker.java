package pwcracker;

import java.util.Iterator;
import java.util.Scanner;

public class pwcracker {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String pw;
        int length;

        System.out.println("Enter a password that is up to 5 chars: ");
        pw = "" + scan.nextLine();
        length = pw.length();

        SequentialPatternGenerator generator = new SequentialPatternGenerator(length);

        generator.forEachRemaining(test -> {if(pw.equals(test)) {
            System.out.println("Your password: " + test );
        }});

    }
}

class SequentialPatternGenerator implements Iterator<String> {

    private static final char[] CHOICES = new char[]{'a', 'b', 'c', 'd', 'e', 'f',
        'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','~','`','@','#','$','%','^','&','*','(',')','-','=','_','+','[',']','{','}',';','\'',':','\"',',','.','<','>','/','?','|','\\',' '};
    // for(int i =32;i<=126;i++) {
    //     CHOICES[i] = (char)i;
    // }
    private static final int MAX_INDEX = CHOICES.length - 1;
    private boolean keepProducing = true;
    private final int[] indexes;

    public SequentialPatternGenerator(final int length) {
        indexes = new int[length];
        initIndexes();
    }

    private void initIndexes() {
        for (int i = 0; i < indexes.length; i++) {
            indexes[i] = 0;
        }
    }

    @Override
    public boolean hasNext() {
        if (!keepProducing) {
            return false;
        }

        for (int i = 0; i < indexes.length; i++) {
            if (indexes[i] < MAX_INDEX) {
                return true;
            }
        }

        return false;
    }

    @Override
    public String next() {
        if (!keepProducing || !hasNext()) {
            return null;
        }

        String next = produceString();
        adjustIndexes();

        return next;
    }

    public void stop() {
        keepProducing = false;
    }

    private String produceString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < indexes.length; i++) {
            sb.append(CHOICES[indexes[i]]);
        }

        return sb.toString();
    }

    private void adjustIndexes() {
        int i;
        for(i = 0 ; i < indexes.length ; i++) {
            if(indexes[i] < MAX_INDEX) {
                indexes[i] = indexes[i] + 1;
                break;
            }
        }

        for(int j=0; j < i; j++) {
            indexes[j] = 0;
        }
    }
}