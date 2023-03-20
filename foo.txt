main

var a, b, c;

{
    let a <- 0;
    let b <- 0;
    let c<- 0 ;
    while a < 99
    do
        let c <- a + 0;

        let b <- 0;
        while b < 17
        do
            let a <- a + 1;
            let b <- b + 1;
        od;

        let a <- a - 1;
    od;
    let c <- a + 0;
    if a == 0 then
        let a <- a -1;
    else
        let b <- a + 22;
    fi;

    let c <- a + 55;
}.