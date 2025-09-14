cont = 0
while True:
    print('-' * 30)
    num = int(input('Digite a tabuada escolhida: '))
    if num >= 0:
        for cont in range(0, 10):
            cont += 1
            print(f' {num} X {cont} = {(num * cont)}')
print('-' * 30)

