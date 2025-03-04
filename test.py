import pandas

M = [7,8,5,6,7,7]
add = [2,3,0,1,2,2]
lower = [5,5,5,5,5,5]
scheme = ["a","b","c","d","e","f"]


if __name__ == "__main__":
    M2 = dict(zip(scheme,M))
    add2 = dict(zip(scheme,add))
    lower2 = dict(zip(scheme,lower))
    u = pandas.read_csv("/home/giacomo/projects/automarker/CSC3232_N.txt.csv")
    for entry in u.to_dict('records'):
        name = entry.pop("name")
        number = entry.pop("number")
        total = 0
        for x in scheme:
            if entry[x]<=lower2[x]:
                total += add2[x]
            else:
                val = M2[x] - entry[x]
                assert val<=add2[x]
                if val>=0:
                    total += val
        print(f"{name} = +{total} with {entry['n']} = {entry['n']+total}")