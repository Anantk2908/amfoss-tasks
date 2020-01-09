extern crate regex;
use regex::Regex;
use std::io;
 
fn main() 
{
    let mut input = String::new();
    println!("Please enter the email to check :");
    let mut user:String = io::stdin().read_line(&mut input).unwrap().to_string();
    let check= Regex::new(r"^([a-z0-9_+]([a-z0-9_+.]*[a-z0-9_+])?)@([a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,6})").unwrap();
    
 
    
    
    println!("{} is valid: {} ", i , check.is_match(input))
    
}
