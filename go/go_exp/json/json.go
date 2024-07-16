package json

import (
	"encoding/json"
	"fmt"
	"os"
)

type Conta struct {
	Numero int `json:"N"`
	Saldo float64 	`json:"S"`
}

func ConverteEmJson(){
	conta:= Conta{123, 100.0}
	res, err := json.Marshal(conta)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(string(res))

	json.NewEncoder(os.Stdout).Encode(conta)

	// inverso
	jsonPuro := []byte(`{"N":1234,"S":2100}`)
	var conta2 Conta
	err = json.Unmarshal(jsonPuro, &conta2)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(conta2)

}