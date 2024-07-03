package main


// type endereco struct {
// 	rua string
// 	numero int
// }

// type Cliente struct {
	// 	nome string
	// 	idade int
	// 	ativo bool
	// 	endereco
	// }
	
// type empresa struct {
// 	nome string
// 	ativo bool
// }

// type pessoa interface {
// 	desativarCliente()
// }

// func ativarCliente(p pessoa){
	// 	p.desativarCliente()
	// }
	
// func (c Cliente)desativarCliente(){
// 	c.ativo = false
// }

// func (e empresa)desativarCliente(){
	// 	e.ativo = false
	// }
	
	
	// func main() {
		// 	var err error
		// 	pedro := Cliente{"Pedro", 27, true, endereco{"Rua das Flores", 123}}
		// 	empresa := empresa{"Empresa", true}
		// 	var lista *LikedList
		
		// 	x := -1
		
		// 	x, err = menorQueZero(x)
		// 	if err != nil {
			// 		fmt.Println(err)
			// 	}
			// 	fmt.Println(x)
			// 	fmt.Println(somaInfinita(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
			// 	total:= func() int { return somaInfinita(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) *2 }() // funcao anonima
			// 	fmt.Println(total)
			// 	pedro.ativo = false
			// 	fmt.Printf("o cliente %s tem %d anos e está ativo? %t\n", pedro.nome, pedro.idade, pedro.ativo)
			// 	pedro.endereco = endereco{"Rua das Flores", 123}
			// 	pedro.rua = "Rua das Flores 2"
// 	pedro.desativarCliente()
// 	fmt.Println(pedro)
// 	ativarCliente(pedro) // passando uma estrutura para uma interface sem precisar modificar o tipo da estrutura
// 	ativarCliente(empresa) // passando uma estrutura para uma interface sem precisar modificar o tipo da estrutura
// 	fmt.Printf(" a empres está ativa? %v\n", empresa.ativo)

// 	lista.newLikedList(1)

// }

import (
	"fmt"
	"github.com/google/uuid"
	"aprendendoGo/arquivos"
	"aprendendoGo/http"
	"aprendendoGo/json"
)


func main(){

	var x interface{} = "10"
	lista:= newLikedList(1)
	defer fmt.Println("essa linha só vai ser executada no final")
	fmt.Println(lista.value)
	lista.push(2)
	fmt.Println(lista.next)
	fmt.Println(lista.next.value)
	lista.push(3)
	lista.print()
	num:= lista.pop()
	fmt.Println(num)
	lista.print()
	lista.push(4)
	fmt.Println("rotate")
	lista.rotate()
	lista.rotate()
	lista.rotate()
	lista.print()
	lista.swap()
	lista.print()
	fmt.Println(x.(string))
	res, ok := x.(int)
	fmt.Printf("o valor é %v e o tipo é %T\n deu certo? %v\n", res, res, ok)
	fmt.Println(uuid.New().String())
	arquivos.CriarArquivo()
	arquivos.LerArquivo()
	arquivos.RemoverArquivo()
	http.RequisitarGoogle()
	json.ConverteEmJson()
}

//  comando para criar um modulo
// go mod init nomeDoModulo
// go mod tidy
// caso eu queira usar um pacote que não está no modulo, eu posso usar o comando go get nomeDoPacote, esse comando so vai funcionar se existir um go.mod no projeto
// se eu tiver um go.mod no projeto, para compilar o projeto eu posso usar o comando go build, que vai compilar o projeto e criar um executavel