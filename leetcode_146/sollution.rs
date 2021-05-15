use std::collections::BTreeMap;

#[derive(Debug)]
struct LRUCache {
    capacity: i32,
    map: BTreeMap<i32, i32>,
}

impl LRUCache {

    fn new(capacity: i32) -> Self {
        let map = BTreeMap::<i32, i32>::new();
        LRUCache {
            capacity: capacity,
            map: map,
        }
    }
    
    // fn get(&mut self, key: i32) -> i32 {
    //     if self.map.contains_key(&key) {
    //         let val = self.map.remove(&key).unwrap();
    //         self.map.insert(key, val);
    //     }
    //     if self.map.contains_key(&key) { *self.map.get(&key).unwrap() } else { -1 }
    // }
    
    // fn put(&self, key: i32, value: i32) {

    // }
}

fn main() {
    let cache = LRUCache::new(2);
    println!("{:?}", cache);
}