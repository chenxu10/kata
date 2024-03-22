let primefactor x = 
    []

let test_primefactor = 
    assert (primefactor 1 = []);;
    assert (primefactor 2 = []);;

(* can you define a sqaure function *)
let square x = x * x;;
let sol = square 2;;
print_int sol;;
