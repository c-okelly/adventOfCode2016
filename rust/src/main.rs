use std::env;
use std::fs::File;
use std::io::prelude::*;

fn main() {
    println!("Hello, world!");

    let mut filename = "../txt/1.txt"; 
    println!("In file {}", filename);

    let mut f = File::open(filename).expect("file not found");

    let mut contents = String::new();
    f.read_to_string(&mut contents)
        .expect("something went wrong reading the file");

    println!("With text:\n{}", contents);
    let vec: Vec<&str> = contents.split(",").collect();

    for s in contents.split(",") {
      println!("{}", s);
    }

    println!("{}", vec[0]);
    
}
