def defangIPaddr(address):
    count = address.count(".")
    output = address.replace(".", "[.]", count)
    return output

# just one iteration
def defangIPaddrBest(address):
    # when count is not given then all occurances are replced.

    return  address.replace(".", "[.]")


if __name__ == '__main__':
    address = "1.1.1.1"
    print(defangIPaddrBest(address))