package arquivos

// arquivo para estudo de manipulacao de arquivos

import (
	"fmt"
	"os"
	"bufio"
)

func LerArquivo() {
	f, err := os.Open("teste.txt")
	if err != nil {
		panic(err)
	}

	// metodo para ler bytes do arquivo
	// b := make([]byte, 100)
	// n, err := f.Read(b)
	// if err != nil {
	// 	panic(err)
	// }
	// fmt.Printf("Foram lidos %d bytes. Conteúdo:\n%s\n", n, string(b))
	reader:= bufio.NewReader(f)
	buffer := make([]byte, 3)
	for {
		n, err := reader.Read(buffer)
		if err != nil {
			if err != nil {
				break
			}
			panic(err)
		}
		fmt.Println(string(buffer[:n]))
	}
	
	f.Close()
}



func CriarArquivo() {
	f, err := os.Create("teste.txt")
	if err != nil {
		panic(err)
		return
	}
	// metodo para escrever string no arquivo
	tamanho, err := f.WriteString("Ola, mundo!")
	if err != nil {
		panic(err)
	}
	// metodo para escrever bytes no arquivo
	tamanho, err = f.Write([]byte("Ola, mundo!2"))
	if err != nil {
		panic(err)
	}
	println(tamanho)
	f.Close()
}

func RemoverArquivo() {
	err := os.Remove("teste.txt")
	if err != nil {
		panic(err)
	}
}