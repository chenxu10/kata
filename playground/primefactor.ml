#use "topfind";;



let primefactor x = 
    []

let test_primefactor = 
    assert (primefactor 1 = []);;
    assert (primefactor 2 = []);;


let reverse_string (s: string): string =
  "cba"

let test_reverse_string = 
    assert (reverse_string "abc" = "cba");;
(* can you define a sqaure functions sd *)
let square x = x * x;;
let sol = square 2;;
print_int sol;;
 