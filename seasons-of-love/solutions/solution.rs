use std::io;
use std::collections::HashMap;

/// A macro to create a HashMap.
///
/// Example:
///
/// ```
/// let letters = map!{"a" => "b", "c" => "d"};
/// ```
///
/// Trailing commas are allowed.
/// Commas between elements are required (even if the expression is a block).
macro_rules! map {
    ($( $key: expr => $val: expr ),* $(,)*) => {{
        let mut map = HashMap::new();
        $( map.insert($key, $val); )*
        map
    }}
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let dates = map! {
        "s" => 1,
        "m" => 60,
        "h" => 60*60,
        "d" => 60*60*24,
        "w" => 60*60*24*7,
        "mo" => 60*60*24*30,
        "y" => 60*60*24*365,
    };

    let mut inp = String::new();
    let stdin = io::stdin();
    stdin.read_line(&mut inp)?;
    let t: u32 = inp.trim().parse()?;
    for _ in 0..t {
        inp.clear();
        stdin.read_line(&mut inp)?;
        let mut iter = inp.trim().split_whitespace();
        let n: u32 = iter.next().unwrap().parse()?;
        let d = iter.next().unwrap();

        println!("{}", dates[d] * n);
    }

    Ok(())
}
