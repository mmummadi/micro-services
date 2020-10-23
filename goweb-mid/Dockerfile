FROM golang

COPY . ./

RUN go get -u github.com/go-sql-driver/mysql && \
    go get -u github.com/gorilla/mux

RUN go build ./main.go

EXPOSE 80 

CMD ["./main"]
