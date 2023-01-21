import matplotlib.pyplot as mpt
import numpy as np

R = 0.06
y = 0.55


def get_f(x):
    return (x ** 3) - 3 * R * (x ** 2) + 4 * (R ** 3) * y
    # define the given function of x In this case f(x) = x^3-3Rx^2+4R^3y
    # we want to solve f(x)=0


def get_dif(x):
    return 3 * (x ** 2) - 6 * R * x
    # return the differential of f(x)


def graph():
    x = np.linspace(-0.05, 0.2, 100)
    f = get_f(x)
    mpt.plot(x, f, '-r', label='Assignment-1')
    mpt.legend(loc='best')
    mpt.xlabel('x')
    mpt.ylabel('f(x)')
    mpt.grid()
    mpt.show()


def bisec(st, ed, max_err, max_itr):
    global n_mid
    mid = 0
    if np.sign(get_f(st)) == np.sign(get_f(ed)):
        print("No root in this part")

    itr_nbr = 1
    flg = 1
    condition = True
    while condition:
        n_mid = (st + ed) * 0.5

        if itr_nbr > max_itr:
            flg = 0
            break

        if np.sign(get_f(st)) != np.sign(get_f(n_mid)):
            ed = n_mid
        else:
            st = n_mid

        error = abs(mid - n_mid) / n_mid
        mid = n_mid
        condition = abs(error) > max_err
        if itr_nbr != 1:
            print(f'Iteration-{itr_nbr - 1}, error = {abs(error) * 100}%')
        itr_nbr += 1

    if flg == 1:
        print(f'\nRequired root is: {n_mid}\n')
    else:
        print('\nNot Convergent.')


def newtonRaphson(x, max_err, max_itr):
    global n_x

    while x >= 0.1 or x <= 0:
        x = float(input("Enter a guess between 0 to 0.1  : "))

    itr_nbr = 1
    flg = 1
    condition = True
    while condition:
        if get_dif(x) == 0.0:
            print('Divide by zero error!')
            break

        n_x = x - get_f(x) / get_dif(x)
        error = (n_x - x) / n_x
        print(f'Iteration-{itr_nbr}, error = {abs(error) * 100}%')
        x = n_x
        itr_nbr += 1

        if itr_nbr > max_itr:
            flg = 0
            break

        condition = abs(error) > max_err

    if flg == 1:
        print(f'\nRequired root is: {n_x}\n')
    else:
        print('\nNot Convergent.')


def main():
    print("Bisection: \n")
    s = float(input('Enter lower bound of bracket: '))
    e = float(input('Enter upper bound of bracket: '))
    t_e1 = float(input('Tolerable Error: '))
    max_stp1 = int(input('Maximum Step: '))
    bisec(s, e, t_e1, max_stp1)

    print("NewtonRaphson : \n")
    x = float(input('Enter Guess: '))
    t_e = float(input('Tolerable Error: '))
    max_stp = int(input('Maximum Step: '))
    newtonRaphson(x, t_e, max_stp)


graph()
main()
