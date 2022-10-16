package tictactoe;
import java.util.Scanner;
import java.lang.Math;

public class Main {

    public static boolean xWin(String str) {
        if (str.charAt(0) == 'X' && str.charAt(1) == 'X' && str.charAt(2) == 'X') {
            return true;
        } else if (str.charAt(3) == 'X' && str.charAt(4) == 'X' && str.charAt(5) == 'X') {
            return true;
        } else if (str.charAt(6) == 'X' && str.charAt(7) == 'X' && str.charAt(8) == 'X') {
            return true;
        } else if (str.charAt(0) == 'X' && str.charAt(3) == 'X' && str.charAt(6) == 'X') {
            return true;
        } else if (str.charAt(1) == 'X' && str.charAt(4) == 'X' && str.charAt(7) == 'X') {
            return true;
        } else if (str.charAt(2) == 'X' && str.charAt(5) == 'X' && str.charAt(8) == 'X') {
            return true;
        } else if (str.charAt(0) == 'X' && str.charAt(4) == 'X' && str.charAt(8) == 'X') {
            return true;
        } else if (str.charAt(2) == 'X' && str.charAt(4) == 'X' && str.charAt(6) == 'X') {
            return true;
        } else {
            return false;
        }
    }

    public static boolean oWin(String str) {
        if (str.charAt(0) == 'O' && str.charAt(1) == 'O' && str.charAt(2) == 'O') {
            return true;
        } else if (str.charAt(3) == 'O' && str.charAt(4) == 'O' && str.charAt(5) == 'O') {
            return true;
        } else if (str.charAt(6) == 'O' && str.charAt(7) == 'O' && str.charAt(8) == 'O') {
            return true;
        } else if (str.charAt(0) == 'O' && str.charAt(3) == 'O' && str.charAt(6) == 'O') {
            return true;
        } else if (str.charAt(1) == 'O' && str.charAt(4) == 'O' && str.charAt(7) == 'O') {
            return true;
        } else if (str.charAt(2) == 'O' && str.charAt(5) == 'O' && str.charAt(8) == 'O') {
            return true;
        } else if (str.charAt(0) == 'O' && str.charAt(4) == 'O' && str.charAt(8) == 'O') {
            return true;
        } else if (str.charAt(2) == 'O' && str.charAt(4) == 'O' && str.charAt(6) == 'O') {
            return true;
        } else {
            return false;
        }
    }

    public static boolean hasDash(String str) {

        char[] charArray = str.toCharArray();

        for (char c : charArray) {
            if (c == '_') {
                return true;
            }
        }
        return false;
    }

    public static boolean notEven(String str) {

        int countX = 0;
        int countO = 0;
        char[] charArray = str.toCharArray();

        for (char c : charArray) {
            if (c == 'X') {
                countX++;
            } else if (c == 'O') {
                countO++;
            }
        }

        int difference = Math.abs(countX - countO);

        return difference >= 2;



    }
    public static void printBoard(String current) {

        System.out.println("---------");
        System.out.println("| "+current.charAt(0) +" "+current.charAt(1)+" "+current.charAt(2)+" |");
        System.out.println("| "+current.charAt(3) +" "+current.charAt(4)+" "+current.charAt(5)+" |");
        System.out.println("| "+current.charAt(6) +" "+current.charAt(7)+" "+current.charAt(8)+" |");
        System.out.println("---------");
    }

    public static boolean checkSpace(int row, int col, String current) {

        char[] charArray1 = current.toCharArray();

        if (row == 1 && col == 1) {
            return charArray1[0] != '_';
        } else if (row == 1 &&  col == 2) {
            return charArray1[1] != '_';
        } else if (row == 1 && col == 3) {
            return charArray1[2] != '_';
        } else if (row == 2 && col == 1) {
            return charArray1[3] != '_';
        } else if (row == 2 && col == 2) {
            return charArray1[4] != '_';
        } else if (row == 2 && col == 3) {
            return charArray1[5] != '_';
        } else if (row == 3 && col == 1) {
            return charArray1[6] != '_';
        } else if (row == 3 && col == 2) {
            return charArray1[7] != '_';
        } else if (row == 3 && col == 3) {
            return charArray1[8] != '_';
        }
        return false;
    }

    public static String makeMoveX(int row, int col, String current) {

        char[] charArray1 = current.toCharArray();

        if (row == 1 && col == 1) {
            charArray1[0] = 'X';
        } else if (row == 1 &&  col == 2) {
            charArray1[1] = 'X';
        } else if (row == 1 && col == 3) {
            charArray1[2] = 'X';
        } else if (row == 2 && col == 1) {
            charArray1[3] = 'X';
        } else if (row == 2 && col == 2) {
            charArray1[4] = 'X';
        } else if (row == 2 && col == 3) {
            charArray1[5] = 'X';
        } else if (row == 3 && col == 1) {
            charArray1[6] = 'X';
        } else if (row == 3 && col == 2) {
            charArray1[7] = 'X';
        } else if (row == 3 && col == 3) {
            charArray1[8] = 'X';
        }

        String str = new String(charArray1);
        return str;
    }

    public static String makeMoveO(int row, int col, String current) {

        char[] charArray1 = current.toCharArray();

        if (row == 1 && col == 1) {
            charArray1[0] = 'O';
        } else if (row == 1 &&  col == 2) {
            charArray1[1] = 'O';
        } else if (row == 1 && col == 3) {
            charArray1[2] = 'O';
        } else if (row == 2 && col == 1) {
            charArray1[3] = 'O';
        } else if (row == 2 && col == 2) {
            charArray1[4] = 'O';
        } else if (row == 2 && col == 3) {
            charArray1[5] = 'O';
        } else if (row == 3 && col == 1) {
            charArray1[6] = 'O';
        } else if (row == 3 && col == 2) {
            charArray1[7] = 'O';
        } else if (row == 3 && col == 3) {
            charArray1[8] = 'O';
        }

        String str = new String(charArray1);
        return str;
    }

    public static void printResult(String str) {
        if ((xWin(str) && oWin(str)) || notEven(str)) {
            System.out.println("Impossible");
        } else if (!xWin(str) && !oWin(str) && hasDash(str)) {
            System.out.println("Game not finished");
        } else if (!xWin(str) && !oWin(str)) {
            System.out.println("Draw");
        } else if (xWin(str)) {
            System.out.println("X wins");
        } else if (oWin(str)) {
            System.out.println("O wins");
        } else {
            System.out.println("Game not finished");
        }
    }

    public static boolean isDone(String str) {
        if ((xWin(str) && oWin(str)) || notEven(str)) {
            System.out.println("Impossible");
            return true;
        } else if (!xWin(str) && !oWin(str) && hasDash(str)) {
            System.out.println("Game not finished");
            return false;
        } else if (!xWin(str) && !oWin(str)) {
            System.out.println("Draw");
            return true;
        } else if (xWin(str)) {
            System.out.println("X wins");
            return true;
        } else if (oWin(str)) {
            System.out.println("O wins");
            return true;
        } else {
            System.out.println("Game not finished");
            return false;
        }
    }

    public static boolean boardFull(String str) {

        char[] charArray1 = str.toCharArray();

        int count = 0;

        for (char c : charArray1) {
            if (c != '_') {
                count++;
            }
        }
        return count==9;

    }

    public static void main(String[] args) {
        // write your code here
//        Scanner scanner = new Scanner(System.in);
        String str = "_________";

        printBoard(str);

        //Create new scanner named Input
        Scanner input = new Scanner(System.in);
        //Initialize Number as 0 to reset while loop
        int row = 0;
        int col = 0;
        char player = 0;

        while (!boardFull(str)) {
            try {
                System.out.print("Enter coordinates row & col between 1-3: ");
                row = input.nextInt();
                col = input.nextInt();
                if ((row < 0) || (row > 3) || (col < 0) || (col > 3)) {
                    System.out.println("Coordinates out of bounds.");
                    continue;
                }
                if (checkSpace(row, col, str)) {
                    System.out.println("Space is full. Try again");
                    continue;
                }

                if (isDone(str)) {
                    System.out.println("Game over");
                    break;
                }

                switch (player % 2) {
                    case 0 -> {
                        str = makeMoveX(row, col, str);
                        printBoard(str);
                    }
                    case 1 -> {
                        str = makeMoveO(row, col, str);
                        printBoard(str);
                    }
                }

                player ++;








//                System.out.println("Row: " + col);
//                System.out.println("Col: " + col);
//                break;


            } catch (Exception e) {
                System.out.println("User input was not a number.");
            }
        }

        printResult(str);


    }
}


