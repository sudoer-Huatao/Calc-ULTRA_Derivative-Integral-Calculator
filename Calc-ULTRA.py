from sympy import *
import sympy as sp
from math import floor, ceil
import numpy as np
import matplotlib.pyplot as plt
import datetime
from matplotlib.patches import Polygon
import logging
import os
import warnings


# This program requires the Sympy, NumPy, and MatPlotLib modules installed!

def main():

    global print_option, graph_option
    print_option = 'p'
    graph_option = 'f'

    instruct_path = os.path.dirname(os.path.abspath(__file__))+'/texts/main_screen.txt'
    main = open(instruct_path, mode='r')
    for line in main.readlines():
        line = line.rstrip()
        print(line)

    warnings.filterwarnings('ignore')

    while True:

        now = (datetime.datetime.now()).strftime("%Y/%m/%d %H:%M:%S")
        print('\n(Time now is:', now+')')

        print('\n(Current Screen: Main Screen)\n')
        cmd = input('Enter Command: ')

        if cmd == '1':
            derivacalc()

        elif cmd == '2':
            intecalc()
        
        elif cmd == '3':
            limcalc()
        
        elif cmd == 'settings':
            open_settings()
        
        elif cmd == 'exit':
            print('\nExiting Calc-ULTRA ... ... ...\n')
            break
        
        else:
            logging.warn(f'Invalid command:"{cmd}"')

'''
If you find this message, type "hi" in the general discussions - sudoer-Huatao
'''


def derivacalc():

    instruct_path = os.path.dirname(os.path.abspath(__file__))+'/texts/derivacalc_instructs.txt'
    derivacalc = open(instruct_path, mode='r')
    for line in derivacalc.readlines():
        line = line.rstrip()
        print(line)

    while True:

        try:
            print('\n(Current Screen: DerivaCalc Main Screen)\n')
            cmd = input('Enter Command: ')

            if cmd == 'd':
                print('\n(Current Screen: Derivative Screen)\n')
                f = input('Enter a function: ')

                if ('^' in f):
                    f = f.replace('^', '**')

                fnum = input('Enter the order of derivative calculation: ')

                if ('.' in fnum) or (fnum.isnumeric() == False) or (int(fnum) <= 0):
                    logging.error('OrderError: Order of derivative calculation is not a valid number.')

                else:
                    x = symbols('x')
                    df = diff(f, x, fnum)

                    print('\nDerivative of',f,'with order',fnum,'is:\n')
                    print_expr(df)

                    if str(sp.simplify(df, evaluate = False)) != str(df):
                        dsimp = input('\nSimplification of answer found. Simplify? (y/n) ')

                        if dsimp == 'y':
                            print('\nSimplified:', df, 'into:\n')
                            print_expr(sp.simplify(df, evaluate = False))

            elif cmd == 'p':
                f = input('\nEnter a function containing x and y or x and y and z: ')

                if ('z' in f):
                    x,y,z = symbols('x,y,z')

                else:
                    x,y = symbols('x,y')

                if ('^' in f):
                    f = f.replace('^', '**')

                res = input('Enter variable to differentiate in respect to: ')
                fnum = input('Enter the order of partial derivative calculation: ')

                if ('.' in fnum) or (fnum.isnumeric() == False) or (int(fnum) < 0):
                    logging.error('OrderError: Order of derivative calculation is not a valid number.')

                else:
                    df = diff(f, res, fnum)

                    print('\nPartial derivative in respect to',res,'of order',fnum,'is:\n')
                    print_expr(df)
                    
                    if str(sp.simplify(df, evaluate = False)) != str(df):
                        show_simp = input('\nSimplification of answer found. Simplify? (y/n) ')
                        
                        if show_simp == 'y':
                            print('\nSimplified:', df, 'into:\n')
                            print_expr(sp.simplify(df, evaluate = False))

            elif cmd == 'i':

                circ = input('\nEnter an equation containing x and y: ')

                if ('^' in circ):
                    circ = circ.replace('^', '**')

                fnum = input('Enter the order of derivative calculation: ')

                if ('.' in fnum) or (fnum.isnumeric() == False) or (int(fnum) < 0):
                    logging.error('OrderError: Order of derivative calculation is not a valid number.')
                
                else:
                    x,y = symbols('x,y')
                    df = idiff(eval(circ), y, x, int(fnum))

                    print('\nDerivative of order',fnum,'is:\n')
                    print_expr(df)

                    if str(sp.simplify(df, evaluate = False)) != str(df):
                        show_simp = input('\nSimplification of answer found. Simplify? (y/n) ')

                        if show_simp == 'y':
                            print('\nSimplified:', df, 'into:\n')
                            print_expr(sp.simplify(df, evaluate = False))

            elif cmd == 'exit':
                print('\nExiting DerivaCalc ... ... ...')
                break

            else:
                logging.warn(f'Invalid command:"{cmd}"')

        except:
            logging.error('UnknownError: An unknown error occured.')


def intecalc():

    instruct_path = os.path.dirname(os.path.abspath(__file__))+'/texts/intecalc_instructs.txt'
    intecalc = open(instruct_path, mode='r')
    for line in intecalc.readlines():
        line = line.rstrip()
        print(line)

    while True:

        print('\n(Current Screen: InteCalc Main Screen)\n')
        cmd = input('Enter Command: ')

        if cmd == 'a':
            print('\n(Current Screen: Antiderivative Screen)\n')
            f = input('Enter a function: ')

            if ('pi' in f):
                f = f.replace('pi', str(sp.core.numbers.pi))

            if ('^' in f):
                f = f.replace('^', '**')

            else:
                str(f)

            x = Symbol('x')
            F = Integral(f, x)

            if ('Integral' in str(F.doit())):
                logging.warn('Cannot compute integral.')

            else:
                print('\nAntiderivative is:\n')
                print_expr(F.doit())

                if str(sp.simplify(F.doit(), evaluate = False)) != str(F.doit()):
                    show_simp = input('\nThe above answer can be simplified/rewrote. Simplify/rewrite? (y/n) ')
                    
                    if show_simp == 'y':
                        print('\nSimplified/rewrote:', F.doit(), 'into:\n')
                        print_expr(sp.simplify(F.doit(), evaluate = False))

                print("\nDon't forget to add a constant!")

        elif cmd == 'd':
            print('\n(Current Screen: Definite Integral Screen)\n')

            def d_integrate():

                def g(x):
                    final = eval(f)
                    return final

                f = input('Enter the function you want to integrate: ')

                if ('^' in f):
                    f = f.replace('^', '**')

                lbound = input('\nEnter the lower bound: ')

                if (lbound.isnumeric() == False) and ('pi' not in lbound) and ('e' not in lbound) and ('-' not in lbound) and ('.' not in lbound) and ('sqrt' not in lbound) and ('oo' not in lbound):
                    logging.error('TypeError: Lower bound is a not a number.')

                if ('pi' in lbound):
                    lbound = lbound.replace('pi', str(sp.core.numbers.pi))
                if ('e' in lbound):
                    lbound = lbound.replace('e', str(E))

                lbound = float(eval(lbound))

                rbound = input('Enter the upper bound: ')

                if (rbound.isnumeric() == False) and ('pi' not in rbound) and ('e' not in rbound) and ('-' not in rbound) and ('.' not in rbound) and ('sqrt' not in rbound) and ('oo' not in rbound):
                    logging.error('TypeError: Upper bound is a not a number.')

                if ('pi' in rbound):
                    rbound = rbound.replace('pi', str(sp.core.numbers.pi))
                if ('e' in rbound):
                    rbound = rbound.replace('e', str(E))

                rbound = float(eval(rbound))

                x = Symbol('x')
                result = integrate(f, (x, lbound, rbound)).evalf()

                if (('1/x' in f or f == 'x^-1') and (lbound <= 0 or lbound <= lbound + 1)) or (str(result) == 'nan') or ('I' in str(result)):
                    logging.warn('Cannot compute integral because integral does not converge.')

                else:
                    print('\nCalculated integral of', f, 'from', lbound, 'to', rbound, '. Final area is:', result)
                    print('\nShow graph of area? (y/n)')
                    show = input('(Exit the graph window when you are finished to continue) ')

                    if show == 'y':
                        try:
                            print('\nLoading graph. Might take some time on first startup ...')

                            x = np.linspace((-rbound-8), (rbound + 8), 200000)
                            if ('ln' in f or 'log' in f):
                                x = np.linspace(int(floor(lbound)) + 1, int(ceil(rbound)) + 8, 200000)
                            y = [g(a) for a in x]
                            fig, ax = plt.subplots()

                            title = 'Shaded area beneath function'
                            plt.title(title)
                            plt.xlabel('x', weight = 'bold')
                            plt.ylabel('y', rotation = 0, weight = 'bold')
                            plt.plot(x,y, color = 'red')

                            if graph_option == 'f':
                                plt.axis([-7.5, 7.5, -7.5, 7.5])

                            elif graph_option == 'a':
                                if (float(g(lbound)) != 0) and (float(g(rbound)) != 0):
                                    plt.axis([lbound - 5, rbound + 5, float(g(round(lbound)))-(float(g(round(lbound)))+float(g(round(rbound))))/2-1, float(g(round(rbound)))+(float(g(round(lbound)))+float(g(round(rbound))))/2+1])
                                elif (float(g(lbound)) == 0) or (float(g(rbound)) == 0):
                                    plt.axis([lbound - 5, rbound + 5, -(rbound-lbound)/2, (rbound+lbound)/2])

                            plt.grid()

                            ix = np.linspace(lbound, rbound)
                            iy = [g(i) for i in ix]
                            verts = [(lbound, 0)] + list(zip(ix, iy)) + [(rbound, 0)]
                            poly = Polygon(verts, facecolor = 'blue')
                            ax.add_patch(poly)

                            plt.show()
                            return '\nExited graph.'
                        
                        except:
                            logging.warn('Could not graph function.')

                    else:
                        return '\nExiting Definite Integral Screen ...'
                    

            print(d_integrate())

        elif cmd == 'i':
            
            def i_integrate():

                print('\n(Current Screen: Improper Integral Screen)\n')
                f = input('Enter a function: ')

                if ('pi' in f):
                    f = f.replace('pi', str(sp.core.numbers.pi))

                if ('^' in f):
                    f = f.replace('^', '**')

                else:
                    str(f)

                lbound = input('\nEnter the lower bound: ')

                if (lbound.isnumeric() == False) and ('pi' not in lbound) and ('e' not in lbound) and ('-' not in lbound) and ('.' not in lbound) and ('sqrt' not in lbound) and ('oo' not in lbound):
                    logging.error('TypeError: Lower bound is a not a number.')
                    i_integrate()

                if ('pi' in lbound):
                    lbound = lbound.replace('pi', str(sp.core.numbers.pi))
                if ('e' in lbound):
                    lbound = lbound.replace('e', str(E))
                if ('oo' in lbound):
                    lbound = eval(lbound)
                else:
                    lbound = float(eval(lbound))

                rbound = input('Enter the upper bound: ')

                if (rbound.isnumeric() == False) and ('pi' not in rbound) and ('e' not in rbound) and ('-' not in rbound) and ('.' not in rbound) and ('sqrt' not in rbound) and ('oo' not in rbound):
                    logging.error('\nTypeError: Upper bound is a not a number.')
                    i_integrate()

                if ('pi' in rbound):
                    rbound = rbound.replace('pi', str(sp.core.numbers.pi))
                if ('e' in rbound):
                    rbound = rbound.replace('e', str(E))
                if ('oo' in rbound):
                    rbound = eval(rbound)
                else:
                    rbound = float(eval(rbound))

                x = Symbol('x')

                try:
                    improper_area = Integral(f, (x, lbound, rbound)).principal_value()

                    print('\nCalculated improper integral of', f, 'from', lbound, 'to', rbound, '. Final area is:\n')
                    print_expr(improper_area)

                    if str(sp.simplify(improper_area, evaluate = False)) != str(improper_area):
                        isimp = input('\nSimplification of answer found. Simplify? (y/n) ')

                        if isimp == 'y':
                            print('\nSimplified:', improper_area, 'into:\n')
                            print_expr(sp.simplify(improper_area, evaluate = False))

                except ValueError:
                    logging.warn('ValueError: Singularity while computing improper integral.')


            i_integrate()

        elif cmd == 'exit':
            print('\nExiting InteCalc ... ... ...')
            break

        else:
            logging.warn(f'Invalid command:"{cmd}"')


def limcalc():

    instruct_path = os.path.dirname(os.path.abspath(__file__))+'/texts/limcalc_instructs.txt'
    limcalc = open(instruct_path, mode='r')
    for line in limcalc.readlines():
        line = line.rstrip()
        print(line)

    while True:

        try:
            print('\n(Current Screen: LimCalc Main Screen)\n')
            cmd = input('Enter Command: ')

            if cmd == 'n':
                print('\n(Current screen: Limit Screen)\n')
                f = input('Enter a function: ')

                if ('pi' in f):
                    f = f.replace('pi', str(sp.core.numbers.pi))

                if ('^' in f):
                    f = f.replace('^', '**')

                else:
                    str(f)

                num = input('Enter the point of evaluation: ')

                if (num.isnumeric() == False) and ('pi' not in num) and ('e' not in num) and ('-' not in num) and ('.' not in num) and ('oo' not in num) and ('sqrt' not in num):
                    logging.error('TypeError: point of evaluation is a not a number.')

                if ('pi' in num):
                    num = num.replace('pi', str(sp.core.numbers.pi))
                if ('e' in num):
                    num = num.replace('e', str(E))

                num = float(eval(num))

                x = symbols('x')
                l = limit(f, x, num)

                if ('Limit' in str(l)):
                    logging.warn('Cannot compute limit.')

                else:
                    print('\nLimit of',f,'as x approaches',num,'is:\n')
                    print_expr(l)

                    if str(sp.simplify(l, evaluate = False)) != str(l):
                        lsimp = input('\nSimplification of answer found. Simplify? (y/n) ')

                        if lsimp == 'y':
                            print('\nSimplified:', l, 'into:\n')
                            print_expr(sp.simplify(l, evaluate = False))

            elif cmd == 'o':
                print('\n(Current screen: One-sided Limit Screen)\n')
                f = input('Enter a function: ')

                if ('pi' in f):
                    f = f.replace('pi', str(sp.core.numbers.pi))

                if ('^' in f):
                    f = f.replace('^', '**')

                else:
                    str(f)

                num = input('Enter the point of evaluation: ')

                if (num.isnumeric() == False) and ('pi' not in num) and ('e' not in num) and ('-' not in num) and ('.' not in num) and ('oo' not in num) and ('sqrt' not in num):
                    logging.error('TypeError: point of evaluation is a not a number.')

                else:
                    if ('pi' in num):
                        num = num.replace('pi', str(sp.core.numbers.pi))
                        
                    if ('e' in num):
                        num = num.replace('e', str(E))

                    num = float(eval(num))
                    direction = input('Enter direction to compute the limit ("left" or "right"): ')

                    if (direction == 'left') or (direction == 'right'):

                        if direction == 'left':
                            direction_sign = '-'

                        elif direction == 'right':
                            direction_sign = '+'

                        x = symbols('x')
                        l = limit(f, x, num, dir = direction_sign)

                        if ('Limit' in str(l)):
                            print('\nCannot compute limit.')

                        else:
                            print('\nLimit of',f,'as x approaches',num,'from the', direction, 'is:\n')
                            print_expr(l)

                            if str(sp.simplify(l, evaluate = False)) != str(l):
                                lsimp = input('\nSimplification of answer found. Simplify? (y/n) ')
                                
                                if lsimp == 'y':
                                    print('\nSimplified:', l, 'into:\n')
                                    print_expr(sp.simplify(l, evaluate = False))

                    else:
                        print('\nTypeError: Direction is not right or left.')

            elif cmd == 'exit':
                print('\nExiting LimCalc ... ... ...')
                break

            else:
                logging.warn(f'Invalid command:"{cmd}"')
                
        except:
            logging.error('UnknownError: An unknown error occured.')


def open_settings():

    settings_path = os.path.dirname(os.path.abspath(__file__))+'/texts/settings.txt'
    settings = open(settings_path, mode='r')

    for line in settings.readlines():
        line = line.rstrip()
        print(line)
    
    while True:

        print('\n(Current Screen: Settings Screen)\n')
        cmd = input('Enter Command: ')

        if cmd == 'print':
            print('\n(Current Screen: Print Settings Screen)\n')

            print_option = input("Set print mode: 'p' (Sympy Pretty Print) or 'n' (Normal Print): ")
            print(f'\nPrinting mode set to: "{print_option}"')

        elif cmd == 'graph':
            print('\n(Current Screen: Graph Settings Screen)\n')

            graph_option = input("Set graph mode: 'f' (Fixed graph view) or 'a' (Adjusted graph view): ")
            print(f'\nGraph mode set to: "{graph_option}"')

        elif cmd == 'exit':
            print('\nExiting settings ... ... ...')
            break

        else:
            logging.warn(f'Invalid command:"{cmd}"')


def print_expr(text):

    printing_methods = {  
        'p': lambda t: pprint(text),
        'n': lambda t: print(text)
    }

    printing_methods[print_option](text)


main()
