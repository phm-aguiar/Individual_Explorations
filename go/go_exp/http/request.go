package http


import (
	"fmt"
	"net/http"
)


func RequisitarGoogle(){
	req, err := http.Get("http://www.google.com.br")
	if err != nil {
		fmt.Println(err)
	}
	// res, err := io.ReadAll(req.Body)
	// if err != nil {
	// 	fmt.Println(err)
	// }
	// fmt.Println(string(req))
	req.Body.Close()
}