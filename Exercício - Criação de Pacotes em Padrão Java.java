package br.estacio.objetos.programas;

import br.estacio.objetos.exemplos.ContaCorrente;

public class ProgramaContaCorrente 
{
 public static void main(String[] args) 
 {
 System.out.println("Oi, iniciando...");
 
 ContaCorrente c1;
 c1 = new ContaCorrente();
 
 c1.cadastrarConta(500178,"BBrasil","Anderson Silva");
 
 System.out.println("Saldo: " + c1.obterSaldo());
 
 c1.depositar(3000);

 System.out.println("Saldo: " + c1.obterSaldo());

 c1.sacar(80);
 
 System.out.println("Saldo: " + c1.obterSaldo());
 
 if (! c1.sacar(1000))
 System.out.println("Saldo Insuficiente.");

 System.out.println("Saldo: " + c1.obterSaldo());

 }

}