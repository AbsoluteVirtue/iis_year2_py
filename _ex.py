

if __name__ == '__main__':
    run = True
    source = ("Непорядок в дебрях школ, под сводами алгебр и геометрий. "
              "Надо школу взять за ушко, промыть и высушить на ветре.")
    words = source.split(" ")
    i = 0
    while run:
        if words[i].startswith("а"):
            print(words[i])
            run = False
        i = i + 1
