package main

import (
	"bytes"
	"io"
	"net/http"
	"os"
	"time"
)

func main() {
	c := http.Client{Timeout: time.Second}
	jsonVar := bytes.NewBuffer([]byte(`{"nome":"go","cargaHoraria":40}`))

	// resp, err := c.Get("http://www.google.com")
	resp, err := c.Post("http://google.com", "application/json", jsonVar)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	io.CopyBuffer(os.Stdout, resp.Body, nil)
}
