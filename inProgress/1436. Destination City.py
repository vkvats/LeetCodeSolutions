def destCity(paths):
    origin = []
    dest = []
    for pair in paths:
        origin.append(pair[0])
        dest.append(pair[1])
    return list(set(dest) - set(origin))[0]


if __name__ == '__main__':
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    print(destCityHash(paths))