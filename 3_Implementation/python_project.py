"""summary

    Returns:
        type: description
    """
num_limit = int(input("Enter limit to largest number.\n"))
try:
    if num_limit < 0:
        print("\n Please enter positive number.\n")
except ValueError:
    pass

try:
    if num_limit == 0:
        print("\n 0,Not acceptable.\n")
except ValueError:
    pass

try:
    if num_limit == 10:
        print("\n  10, Not acceptable\n")
except ValueError:
    pass

try:
    if num_limit < 10:
        print("\n Please enter number greater than 10.\n")
except ValueError:
    pass
finally:
    print("Limit is", num_limit)
    encode_num = int(input("Enter a number to be encoded using Number series algorithm\n"))
    store_num = [0 for i in range(num_limit)]

    def checkseries(_self, encode_num):
        """summary

        Args:
            n (type): description

        Returns:
            type: description
        """
        store_num[0] = 1
        # stores 2nd Number
        store_num[1] = 2
        #  stores 3rd  Number
        i = 2
        while store_num[i - 1] <= encode_num:
            store_num[i] = store_num[i - 1] + store_num[i - 2]
            i += 1
        return i - 2

    class Mathalgorithm:
        """summary
        """
        def encode_algo(self, encode_num):
            """summary

            Args:
                n (type): description

            Returns:
                type: description
            """
            index = checkseries(self, encode_num)

            # allocate memory for secret key
            secret_key = ['a' for i in range(index + 2)]

            # index of the largest Fibonacci number
            i = index

            while encode_num:

                # usage of Fibonacci  (1 bit)
                secret_key[i] = '1'
                # Subtract fib from n
                encode_num  = encode_num - store_num[i]
                i = i - 1

                # check  backwards
                while (i >= 0 and store_num[i] > encode_num):
                    secret_key[i] = '0'
                    i = i - 1

            # additional '1' bit
            secret_key[index + 1] = '1'

            # return pointer to secret key
            return "".join(secret_key)


# Driver Code

# create an object for base class

obj_encode = Mathalgorithm()

# print the encoded number

print(" SECRET word for ", encode_num)
print("\n")
print("**********ENCODING**********")
print("\n")
print("",obj_encode.encode_algo(encode_num))
