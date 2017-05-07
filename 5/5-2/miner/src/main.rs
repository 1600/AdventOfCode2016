#![feature(range_contains)]

use std::char;
extern crate md5;
use std::io;
use std::io::prelude::*;


fn has_5_consec_zeroes(s: &str) -> bool {
    // remember the "-> bool" part,otherwise it returns default ();

    let zero = char::from_digit(0, 10).unwrap(); // convert digit to char. https://doc.rust-lang.org/std/char/fn.from_digit.html

    if (s.chars().nth(0).unwrap() == zero) && (s.chars().nth(1).unwrap() == zero) &&
       (s.chars().nth(2).unwrap() == zero) && (s.chars().nth(3).unwrap() == zero) &&
       (s.chars().nth(4).unwrap() == zero) 
       {
        return true;
        }
    return false;
}


fn main() {

    fn mining() {
        let seed = String::from("ffykfhsq");
        let mut index: u32 = 844744;                        // start from 515837 because this is nearer to first 5 zeroes
        let mut result_string = String::with_capacity(8);   //create a string with target 8 bytes capacity.
        let mut temp_vector = Vec::new();                   // temporary vector to place character to push like [(pos1, char1), (pos2, char2)]
        let mut times_added : i32 = 1;                      
        let mut inserted_indices : Vec<u32> = Vec::new();

        while times_added <= 8 {                            // only adds 8 chars
            let a = format!("{}{}", seed, index);           //concatenate strings to be calculated by md5
            //println!("Index >> {}", &index);
            index += 1;
            let digest = format!("{:x}", md5::compute(a));  // type(digest)>> &str
            //println!("hash >> {}", digest);
            if has_5_consec_zeroes(&digest) {
                let mut chars = digest.chars();
                let pos = chars.nth(5).unwrap();
                if pos.is_digit(10) {
                    let valid_pos : u32 = pos.to_digit(10).unwrap();
                    if (0..8).contains(valid_pos) && !(inserted_indices.iter().find(|&&x| x == valid_pos) == Some(&valid_pos)) {
                        inserted_indices.push(valid_pos);
                        println!("[i] current filled {} chars.", times_added);
                        let char_to_insert : char= chars.nth(0).unwrap();                   // because digest already has first 5+1 elements sliced by nth(5)
                        println!("[i] inserting \"{}\" at index[{}] to temp_vector.", char_to_insert.clone(), valid_pos);
                        temp_vector.push((valid_pos, char_to_insert));
                        times_added +=1;
                        }
                    }
                }
            }
        println!("temp vec >> {:?}",temp_vector);
        let mut pos = 0;
        while pos < temp_vector.len() {
            println!("round {}",pos);
            for i in &temp_vector {
                if i.0 as usize == pos {
                    result_string.insert(pos , i.1);
                    println!("inserting {}, now vec is {:?}",i.1, result_string);
                    pos += 1;
                    break
                }
            }
        }

        println!("end result >> {:?}",result_string );
    }
    
    mining()
}

// Program Output:
// [i] current filled 1 chars.
// [i] inserting "a" at index[6] to temp_vector.
// [i] current filled 2 chars.
// [i] inserting "b" at index[7] to temp_vector.
// [i] current filled 3 chars.
// [i] inserting "1" at index[5] to temp_vector.
// [i] current filled 4 chars.
// [i] inserting "8" at index[0] to temp_vector.
// [i] current filled 5 chars.
// [i] inserting "5" at index[3] to temp_vector.
// [i] current filled 6 chars.
// [i] inserting "c" at index[1] to temp_vector.
// [i] current filled 7 chars.
// [i] inserting "d" at index[4] to temp_vector.
// [i] current filled 8 chars.
// [i] inserting "3" at index[2] to temp_vector.
// temp vec >> [(6, 'a'), (7, 'b'), (5, '1'), (0, '8'), (3, '5'), (1, 'c'), (4, 'd'), (2, '3')]
// round 0
// inserting 8, now vec is "8"
// round 1
// inserting c, now vec is "8c"
// round 2
// inserting 3, now vec is "8c3"
// round 3
// inserting 5, now vec is "8c35"
// round 4
// inserting d, now vec is "8c35d"
// round 5
// inserting 1, now vec is "8c35d1"
// round 6
// inserting a, now vec is "8c35d1a"
// round 7
// inserting b, now vec is "8c35d1ab"
// end result >> "8c35d1ab"