package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
    "github.com/gorilla/mux"
    "os"
    "strings"
)

func main() {
    BACKEND := os.Getenv("BACKEND_SVC")
    HOSTNAME := os.Getenv("HOSTNAME")
    POD_IP := os.Getenv("POD_IP")
    HOST_IP := os.Getenv("HOST_IP")
    r := mux.NewRouter()
    r.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
	    response, err := http.Get(BACKEND)
            if err != nil {
               fmt.Printf("The HTTP request failed with error %s\n", err)
            } else {
               data, _ := ioutil.ReadAll(response.Body)
               fmt.Fprintf(w, string(data))
            }
    })
    s := []string{"I Am from GO Middleware Application",  "          ", "My HostName is ", HOSTNAME, "         ", "My Pod IP is ", POD_IP, "         ","My Host IP is ",  HOST_IP}
    r.HandleFunc("/goapp", func(w http.ResponseWriter, r *http.Request) {
            fmt.Fprintf(w, string(strings.Join(s, " ")))
    })
    http.ListenAndServe(":80", r)
}
