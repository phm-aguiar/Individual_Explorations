package main

import (
	"fmt"

	"github.com/phm-aguiar/Individual_Explorations/go/cepweb/apis/configs"
)

func main() {
	config, _ := configs.LoadConfig(".")
	fmt.Println(config.DBDriver)
}
