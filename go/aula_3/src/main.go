package main

// const (
// 	PI = 3.14159265359
// 	RAIO = 10
// 	DIAMETRO = RAIO * 2
// )


//  iota é uma constante que é incrementada a cada linha
const(
	PI = iota
	RAIO
	DIAMETRO
)


func main() {

	println(PI)
	println(RAIO)
	println(DIAMETRO)


}
