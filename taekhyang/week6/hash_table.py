import random


class ChainingHashTable(object):
    def __init__(self, hash_table_len: int):
        self.hash_table_len = hash_table_len
        self.hash_table = [0 for _ in range(hash_table_len)]

    @staticmethod
    def get_key(key):
        return hash(key)

    def hash_key(self, key):
        return key % self.hash_table_len

    def get_hash_address(self, key):
        hashed_key = LinearProbingHashTable.get_key(key)
        hash_address = self.hash_key(hashed_key)
        return hash_address

    def read(self, key):
        hash_address = self.get_hash_address(key)
        if self.hash_table[hash_address] != 0:
            for _key, _data in self.hash_table[hash_address]:
                if _key == key:
                    return _data
            else:
                return False
        else:
            return False

    def write(self, key, value):
        hash_address = self.get_hash_address(key)
        if self.hash_table[hash_address] != 0:
            for i, pair in enumerate(self.hash_table[hash_address]):
                _key, _ = pair
                if _key == key:
                    self.hash_table[hash_address][i] = [key, value]
                    return
            else:
                self.hash_table[hash_address].append([key, value])
        else:
            self.hash_table[hash_address] = [[key, value]]


class LinearProbingHashTable(object):
    def __init__(self, hash_table_len: int):
        self.hash_table_len = hash_table_len
        self.hash_table = [0 for _ in range(hash_table_len)]

    @staticmethod
    def get_key(key):
        return hash(key)

    def hash_key(self, key):
        return key % self.hash_table_len

    def get_hash_address(self, key):
        hashed_key = LinearProbingHashTable.get_key(key)
        hash_address = self.hash_key(hashed_key)
        return hash_address

    def read(self, key):
        hash_address = self.get_hash_address(key)

        for i in range(hash_address, self.hash_table_len):
            if self.hash_table[i] != 0:
                _key, _data = self.hash_table[i]
                if _key == key:
                    return _data
            else:
                return False

    def write(self, key, value):
        hash_address = self.get_hash_address(key)

        for i in range(hash_address, self.hash_table_len):
            if self.hash_table[i] != 0:
                _key, _ = self.hash_table[i]
                if _key == key:
                    self.hash_table[i] = [key, value]
                    return
            else:
                self.hash_table[i] = [key, value]
                return


if __name__ == '__main__':
    write_list = [(0, '???'), (1, '???'), (2, '???'), (3, '???'), (4, '???'), (5, '???'), ('hello', '???????????????')]
    read_list = [0, 1, 2, 3, 4, 5, 'hello']

    # open hashing - chaining ???????????? ??????
    chaining_hash_table = ChainingHashTable(20)
    for key, val in write_list:
        chaining_hash_table.write(key, val)

    print(chaining_hash_table.hash_table)
    for n in read_list:
        val = chaining_hash_table.read(n)
        print(f'{n} ??? ?????? {val if val else "???????????? ????????????"}')

    # close hashing - linear probing ???????????? ??????
    # ?????? ???????????? ??? ??? ???????????? ???????????? ?????? ???????????? ???????????? ????????? ????????? ?
    ln_hash_table = LinearProbingHashTable(20)
    for key, val in write_list:
        ln_hash_table.write(key, val)

    print(ln_hash_table.hash_table)
    for n in read_list:
        val = ln_hash_table.read(n)
        print(f'{n} ??? ?????? {val if val else "???????????? ????????????"}')
