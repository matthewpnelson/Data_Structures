# Implement a Hash Table with Linear Probing
## Matt Nelson, May 6, 2017

class MyTable:

    def __init__(self, size):

        self.size = size
        self.keys = [None for each in range(int(size))]
        self.values = [None for each in range(int(size))]


    def general_hash(self, key):
        hash_location = 0
        for each in key:
            hash_location += ord(each)
        compressed_hash_index = hash_location % self.size
        return compressed_hash_index


    def __setitem__(self, key, value):
        hash_location = self.general_hash(key)

        # update a value if it exists
        if self.__getitem__(key) != "Key not in table.":

            if self.keys[hash_location] == str(key):
                self.values[hash_location] = value
            else: # begin linear probing

                # Starting at the end of the list? If so, roll back to the start.
                current_location = hash_location
                if current_location == self.size-1:
                    current_location = 0 #roll back to the start of the list
                else:
                    current_location += 1

                while self.keys[current_location] != str(key):
                    if current_location == self.size-1:
                        current_location = 0 #roll back to the start of the list
                    else:
                        current_location += 1
                self.values[current_location] = value


        # add in the new key-value pair
        else:
            # set a new value
            if self.keys[hash_location] == None:
                self.keys[hash_location] = str(key)
                self.values[hash_location] = value

            else: # begin linear probing

                # Starting at the end of the list? If so, roll back to the start.
                current_location = hash_location
                if current_location == self.size-1:
                    current_location = 0 #roll back to the start of the list
                else:
                    current_location += 1

                # are we just updating the value for an existing key?
                if self.keys[current_location] == str(key):
                    self.values[current_location] = value

                else:
                    while self.keys[current_location] is not None and self.keys[current_location] != 'deleted':
                        # are we just updating the value for an existing key?
                        if self.keys[current_location] == str(key):
                            self.values[current_location] = value
                            break
                        elif current_location == self.size-1:
                            current_location = 0 #roll back to the start of the list
                        else:
                            current_location += 1

                    # Set Key and Value @ Current Location
                    self.keys[current_location] = str(key)
                    self.values[current_location] = value


    def __getitem__(self, key):
        hash_location = self.general_hash(key)

        if self.keys[hash_location] == str(key):
            return self.values[hash_location]
        else: # begin linear probing

            # use a count to track how many hash locations have been checked & stop if full table is searched with no result
            index_count = 1

            # Starting at the end of the list? If so, roll back to the start.
            current_location = hash_location
            if current_location == self.size-1:
                current_location = 0 #roll back to the start of the list
                index_count += 1
            else:
                current_location += 1
                index_count += 1

            while self.keys[current_location] != str(key):
                if index_count >= self.size:
                    return "Key not in table."
                if current_location == self.size-1:
                    current_location = 0 #roll back to the start of the list
                    index_count += 1
                else:
                    current_location += 1
                    index_count += 1

            return self.values[current_location]


    def __delitem__(self, key):
        hash_location = self.general_hash(key)

        if self.keys[hash_location] == str(key):
            self.keys[hash_location] = 'deleted'
            self.values[hash_location] = 'deleted'

        else: # begin linear probing

            # Starting at the end of the list? If so, roll back to the start.
            current_location = hash_location
            if current_location == self.size-1:
                current_location = 0 #roll back to the start of the list
            else:
                current_location += 1

            while self.keys[current_location] != str(key):
                if current_location == self.size-1:
                    current_location = 0 #roll back to the start of the list
                else:
                    current_location += 1
            self.keys[current_location] = 'deleted'
            self.values[current_location] = 'deleted'
