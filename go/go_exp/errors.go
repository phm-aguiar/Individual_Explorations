
package main

import (
	"errors"
)


func menorQueZero(n int) (int, error) {
	if n < 0 {
		return 0, errors.New("Número menor que zero")
	}
	return n, nil
}