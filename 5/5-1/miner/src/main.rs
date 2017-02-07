use std::char;
extern crate md5;


macro_rules! has_5_consec_zeroes {
    // https://doc.rust-lang.org/beta/book/macros.html
    ($a : expr) => (
        // 以下为宏展开内容.
        ($a.chars().nth(1).unwrap()==char::from_digit(0, 10).unwrap())&&  //
        ($a.chars().nth(2).unwrap()==char::from_digit(0, 10).unwrap())&&
        ($a.chars().nth(3).unwrap()==char::from_digit(0, 10).unwrap())&&
        ($a.chars().nth(4).unwrap()==char::from_digit(0, 10).unwrap())&&
        ($a.chars().nth(0).unwrap()==char::from_digit(0, 10).unwrap());

    )
}


fn has_5_consec_zeroes( s: &str ) -> bool {          // remember the "-> bool" part,otherwise it returns default ();
    let zero = char::from_digit(0, 10).unwrap();     // convert digit to char. https://doc.rust-lang.org/std/char/fn.from_digit.html

    if (s.chars().nth(0).unwrap()==zero)&&
        (s.chars().nth(1).unwrap()==zero)&&
        (s.chars().nth(2).unwrap()==zero)&&
        (s.chars().nth(3).unwrap()==zero)&&
        (s.chars().nth(4).unwrap()==zero) {
        return true;
    }
    return false;
}


fn main() {
        
    println!("fuck miners!");
    fn mining(){
        let seed = String::from("ffykfhsq");
        let mut index :u32 = 0;
        let mut arr = String::from("");
        while true {

            let a = format!("{}{}",seed,index);     //concatenate strings
            println!("Index >> {}", &index);        
            index += 1;
            let digest = format!("{:x}", md5::compute(a));  // type(digest)>> &str
            //let digest = stringify!(md5::compute(a));     //don't use stringify!. 
    
            println!("hash >> {}", digest);
            if has_5_consec_zeroes!(digest)
                {
                arr.push(digest.chars().nth(5).unwrap());
                }
                
            //assert_eq!(format!("{:x}", digest), "c3fcd3d76192e4007dfb496cca67e13b");
            // if index >= 100 {
            //     return
            // }
            if arr.chars().count() == 8 {
                break;
            }
        }
        println!("{}",arr);
    }
    
    mining()
}
