class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_index = self._hash_function(key)
        for pair in self.table[hash_index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hash_index].append([key, value])

    def search(self, key):
        hash_index = self._hash_function(key)
        for pair in self.table[hash_index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        hash_index = self._hash_function(key)
        for i, pair in enumerate(self.table[hash_index]):
            if pair[0] == key:
                del self.table[hash_index][i]
                return
        raise KeyError(f"Key '{key}' not found in the hash table")

    def display(self):
        print("HASH TABLE:")
        print("-----------")
        for i, bucket in enumerate(self.table):
            print(f"BUCKET {i}: {bucket}")
        print()

def main():
    HT = HashTable(10)
    HT.insert('LAMBO', 27)
    HT.insert('MERCEDES', 8)
    HT.insert('FERARRI', 63)
    HT.insert('BUGATTI', 10)
    HT.insert('GTR', 7)
    HT.insert('RANGE ROVER', 6)

    print("VALUE OF LAMBO:", HT.search('LAMBO'))
    print("===============")
    print("VALUE OF MERCEDES:", HT.search('MERCEDES'))
    print("===============")
    print("VALUE OF FERARRI:", HT.search('FERARRI'))
    print("=================")
    print("VALUE OF BUGATTI:", HT.search('BUGATTI'))
    print("=================")
    print("VALUE OF GTR:", HT.search('GTR'))
    print("=============")
    print("VALUE OF RANGE ROVER:", HT.search('RANGE ROVER'))
    print("=====================")
    HT.delete('RANGE ROVER')
    print("VALUE OF RANGE ROVER AFTER DELETING:", HT.search('RANGE ROVER'))
    print("====================================")
    print()
    print("----------------------------")
    print("HASH OF LAMBO:", HT._hash_function('LAMBO'))
    print("HASH OF MERCEDES:", HT._hash_function('MERCEDES'))
    print("HASH OF FERARRI:", HT._hash_function('FERARRI'))
    print("HASH OF BUGATTI:", HT._hash_function('BUGATTI'))
    print("HASH OF GTR:", HT._hash_function('GTR'))
    print("HASH OF RANGE ROVER:", HT._hash_function('RANGE ROVER'))
    print("----------------------------")
    print()
    HT.display()

main()
