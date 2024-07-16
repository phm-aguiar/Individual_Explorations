/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.go                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/13 09:01:54 by phenriq2          #+#    #+#             */
/*   Updated: 2024/06/17 15:40:15 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

package main

import "fmt"

type Pessoa struct {
	Nome string
	Idade int
	teste map[string]int
}

type listaLigada struct {
	valor int
	proximo *listaLigada
}


func construtor() Pessoa {
	p := Pessoa{}
	p.Nome = ""
	p.Idade = 0
	p.teste = make(map[string]int)
	return p
}

func main() {
	p := Pessoa{} 
	p.Nome = "Pedro"
	p.Idade = 20
	fmt.Println(p)
	trocaDeIdentidade(&p)
	fmt.Println(p)
	outraPessoa := construtor()
	outraPessoa.Nome = "Maria"
	outraPessoa.Idade = 25
	outraPessoa.teste["teste"] = 1
	fmt.Println(outraPessoa)

	head := list()
	head.valor = 1
	head.proximo = list()
	head.proximo.valor = 2
	head.proximo.proximo = list()
	head.proximo.proximo.valor = 3
	for head != nil{
		fmt.Println(head.valor)
		head = head.proximo
	}
	
	msg := message{"Hello World"}
	msg.send()
}

func trocaDeIdentidade(p *Pessoa) {
	p.Nome = "João"
	p.Idade = 30
}


func list() *listaLigada{
	lista := listaLigada{}
	lista.valor = 0
	lista.proximo = nil
	return &lista
}

type message struct {
	Msg string
}

func (mp *message) send() {
	fmt.Println(mp.Msg)
}