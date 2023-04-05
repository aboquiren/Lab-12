def main():
    ##################################################
    # Comlete your code here
    ##################################################

    import random 

    n1 = random.randint(0,100)
    n2 = random.randint(0,100)
    n3 = random.randint(0,100)
    print (n1, n2, n3)

    if n1 < n2 and n1 < n3:
        print (f'{n1} is the smallest number')
    elif n2 < n1 and n2 < n3:
        print (f'{n2} is the smallest number')
    else:
        print (f'{n3} is the smallest number')


if __name__ == '__main__':
    main()
