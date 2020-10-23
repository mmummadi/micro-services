package main

import (
    //"bytes"
    //"encoding/json"
    "fmt"
    //"io/ioutil"
    "net/http"
    "github.com/gorilla/mux"
    //"html/template"
    "os"
    "strings"
)

func main() {
    HOSTNAME := os.Getenv("HOSTNAME")
    POD_IP := os.Getenv("POD_IP")
    HOST_IP := os.Getenv("HOST_IP")
    s := []string{"I Am from GO Application",  "          ", "My HostName is ", HOSTNAME, "         ", "My Pod IP is ", POD_IP, "         ","My Host IP is ",  HOST_IP}
    r := mux.NewRouter()
    r.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
	    fmt.Fprintf(w, string(strings.Join(s, " ")))
	})
	/*
	   // fmt.Fprintf(w, string("I Am from GO Application" +  '        ' +  HOSTNAME + '          ' + POD_IP + '        ' + HOST_IP)
	 //vars := mux.Vars(r)
        //title := vars["title"]
       // page := vars["page"]

        //fmt.Fprintf(w, "You've requested the book: %s on page\n", title)
	response, err := http.Get(url)
	if err != nil {
           fmt.Printf("The HTTP request failed with error %s\n", err)
        } else {
           data, _ := ioutil.ReadAll(response.Body)
           //fmt.Println(string(data))
	   fmt.Fprintf(w, string(data))
        }
    })
    r.HandleFunc("/{version}", func(w http.ResponseWriter, r *http.Request) {
        vars := mux.Vars(r)
        version := vars["version"]
	if version == "v1" || version == "v2"{
		response, err := http.Get(url+version)
        	if err != nil {
           		fmt.Printf("The HTTP request failed with error %s\n", err)
        	} else {
           		data, _ := ioutil.ReadAll(response.Body)
           		fmt.Fprintf(w, string(data))
        	}
	}
    })
    */
    http.ListenAndServe(":5000", r)
}
