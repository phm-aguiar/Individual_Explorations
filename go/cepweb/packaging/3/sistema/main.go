package main

import (
	"fmt"

	"github.com/google/uuid"
	"github.com/phm-aguiar/Individual_Explorations/go/cepweb/packaging/3/math"
)

func main(){
	m:=math.CreateMath(1,2)
	fmt.Println(m.Sum())
	fmt.Println(uuid.New().String())
}