let term a = 
    1.0 /. (a *. (a +. 2.0))

let () = 
    let a = 2.0 in
    let result = term a in
    print_endline (string_of_float result)

(**)