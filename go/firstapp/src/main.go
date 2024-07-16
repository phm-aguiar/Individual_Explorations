/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.go                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/17 18:47:29 by phenriq2          #+#    #+#             */
/*   Updated: 2024/06/24 10:34:34 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

package main

import (
	"io"
	"net/http"
	"os"
	"log"
)

func serveIndex(w http.ResponseWriter, r *http.Request) {
	f, err := os.Open("index.html")
	if err != nil {
		http.Error(w, "file not found", 404)
		log.Println(err)
		return
	}
	defer f.Close()
	io.Copy(w, f)
}

func serveStaticFiles(prefix string, directory string) {
	fs := http.FileServer(http.Dir(directory))
	http.Handle(prefix, http.StripPrefix(prefix, fs))
}

func main() {
	// Servir arquivos estáticos
	serveStaticFiles("/assets/", "assets")

	// Servir o arquivo index.html
	http.HandleFunc("/", serveIndex)

	log.Println("Servidor iniciado na porta 8000")
	http.ListenAndServe(":8000", nil)
}