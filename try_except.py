def trying(fileName):
    try:
        f = open(fileName)
        s = f.readline()
        i = int(s.strip())
        print(i)
    except IOError as rr:
        print('IOError:', rr)
    except OSError as rr:
        print('OSError: ', rr)
    except Exception as rr:
        print('Error:', rr)
    finally:
        print('Well done!')

f = input('Enter the file name: ')
trying(f)
print('Well done anytime ;)')



# Come up with an example (or examples) and write a program try_except.py that uses   
# try... except... statement to handle three different exceptions 
# [except the following: ZeroDivisionError, NameError, TypeError, ValueError, StopIteration, AssertionError].

