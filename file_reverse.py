with open("dataset_24465_4.txt", "r") as d, open("111.txt", "w") as r:
    for line in reversed(list(d)):
        r.write(line)

