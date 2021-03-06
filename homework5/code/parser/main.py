import re

def file_count():
    return sum(1 for line in open('./access.log', 'r'))


def file_method_count():
    with open('./access.log', 'r') as file:
        data = [x.split()[5][1:] for x in file]
        return dict([(x, data.count(x)) for x in set(data) if len(x) < 7])


def file_top10():
    with open('./access.log', 'r') as file:
        data = [x.split()[6] for x in file]
        new_data = [re.split(r"[#?]", x)[0] for x in data]
        return sorted([(x, new_data.count(x)) for x in set(new_data)], reverse=True, key=lambda d: d[1])[:10]


def file_top_5xx():
    urls = []
    with open('./access.log', 'r') as file:
        for line in file.readlines():
            l = line.split()
            if l[8][0] == "5":
                if l[0] in [i[0] for i in urls]:
                    for k in range(len(urls)):
                        if urls[k][0] == l[0]:
                            urls[k][1] += 1
                else:
                    urls.append([l[0], 1])
    return sorted(urls, key=lambda i: i[1], reverse=True)[:5]


def file_top_4xx():
    urls = []
    current_urls = set()
    result = []
    with open('./access.log', 'r') as file:
        for line in file.readlines():
            l = line.split()
            if l[8][0] == "4":
                urls.append([re.split(r"[#?]", l[6])[0], l[8], l[9], l[0]])
    sort = sorted(urls, key=lambda i: int(i[2]), reverse=True)
    for item in sort:
        if item[0] not in current_urls:
            current_urls.add(item[0])
            result.append(item)
        if len(current_urls) == 5:
            break
    return result







f = open('result.txt', 'w')
f.write("Total Requests: \n")
f.write(f'{file_count()}\n')
f.write("Total number of requests by type: \n")
f.write(f'{file_method_count()}\n')
f.write("Top 10 most frequent requests: \n")
f.write(f'{file_top10()}\n')
f.write("Top 5 users by the number of requests that ended with a server (5XX) error: \n")
f.write(f'{file_top_5xx()}\n')
f.write("TTop 5 largest requests that failed in a vlient (4XX) error: \n")
f.write(f'{file_top_4xx()}\n')
f.close()
