"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""
class Solution:

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    cache = []
    def read(self, buf, n):
        # Write your code here
        write_pos = 0

        # when acutally read char is smaller that n
        while write_pos < n:

            # if there's cache, read from cache first
            if self.cache:
                for i in range(len(self.cache)):
                    buf[write_pos] = self.cache[i] 
                    write_pos += 1 
                    if write_pos == n:
                        self.cache = self.cache[i + 1: ]
                        return write_pos
                self.cache = []
            
            # read from api
            buf4 = ["", "", "", ""]
            num_read = Reader.read4(buf4)
            if num_read == 0:
                break 

            for i in range(num_read):
                if write_pos < n:
                    buf[write_pos] = buf4[i]
                    write_pos += 1 
                else:
                    self.cache.append(buf4[i])
        return write_pos


"""
"filetestbuffer"
read(6)
read(5)
read(4)
read(3)
read(2)
read(1)
read(10)
"""