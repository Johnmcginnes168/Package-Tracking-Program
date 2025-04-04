


class HashTable:
    # This code builds the Hash Table class with the capacity parameter. Beginning with the constructor.
    # Time Complexity = O(n) to initialize the table, where n is the table capacity.
    def __init__(self, capacity=10):
        self.table = [[] for _ in range(capacity)]

    # Helper method to retrieve chain index for the keys.
    # Time Complexity = O(1)
    def get_chain_index(self, key):
        return hash(key) % len(self.table)

    # This code is to insert/update an item in the table.
    # Time Complexity = O(1) (not accounting for hash collisions, which would be worst case O(n))
    def table_insert(self, key, item):
        chain_index = self.get_chain_index(key) # Calling the helper method
        chain = self.table[chain_index]

        # If Key is present, update instead of insert.
        for key_value_pair in chain:
            if key_value_pair[0] == key:
                key_value_pair[1] = item
                return True

        # Otherwise, insert the new key/value.
        chain.append([key, item])
        return True

    # Search for an item using the key and return either the value, or 'None' if not found.
    # Time Complexity = O(1) (not accounting for hash collisions, which would be worst case O(n))
    def table_search(self, key):
        chain_index = self.get_chain_index(key) # Calling the helper method
        chain = self.table[chain_index]

        # Look a key in the chain
        for key_value_pair in chain:
            if key_value_pair[0] == key:
                return key_value_pair[1]
        return None

    # Remove an item from the hash table using the key
    # Time Complexity = O(1) (not accounting for hash collisions, which would be worst case O(n))
    def table_remove(self, key):
        chain_index = self.get_chain_index(key) # Calling the helper method
        chain = self.table[chain_index]

        # Search for the key to remove.
        for key_value_pair in chain:
            if key_value_pair[0] == key:
                chain.remove(key_value_pair)
                return True # Indicates removal success.
        return False # Returns false if no key was found.