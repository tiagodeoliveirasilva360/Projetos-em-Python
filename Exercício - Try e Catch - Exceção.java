import java.util.Scanner;

public class Exercicio27Softex {
    public static void main(String[] args){
        try{
            System.out.println("Digite um número: ");
            Scanner opc = new Scanner(System.in);
            int num1 = opc.nextInt();
            System.out.println("Digite outro número: ");
            int num2 = opc.nextInt();
            System.out.println(num1/num2);
            
        } catch(Exception e){
            System.out.println("Ocorreu um erro: "+e.getMessage());
        }
        System.out.println("Fim");

    }

    
}
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy