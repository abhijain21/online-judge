import os, filecmp

codes = {200:'success',404:'file not found',400:'error',408:'timeout'}

def compile(file,lang):
    if lang == 'java':
        class_file = file[:-4]+"class"
    elif lang == 'c':
        class_file = file[:-2]
    elif lang=='cpp':
        class_file = file[:-4]
    elif lang=='ruby':
        return  200
    elif lang=='python':
        return  200

    if (os.path.isfile(class_file)):
        os.remove(class_file)
    if (os.path.isfile(file)):
        if lang == 'java':
            os.system('javac '+file)
        elif lang == 'c' or lang == 'cpp':
            os.system('gcc -o '+class_file+' '+file)
        if (os.path.isfile(class_file)):
            return 200
        else:
            return 400
    else:
        return 404

def run(file,input,timeout,lang):
    if lang == 'java':
        cmd = 'java '+file.split('.')[0]
    elif lang=='c' or lang=='cpp':
        cmd = './'+file.split('.')[0]
    elif lang=='ruby':
        cmd = 'ruby ' + file 
    elif lang=='python':
        cmd = 'python ' + file 
    # elif lang=='javascript':
    #     from pyv8 import PyV8
    #     ctx = PyV8.JSContext()
    #     ctx.enter()
    #     print ctx.eval(input)


    # r = os.system('timeout '+timeout+' '+cmd+' < '+input+' > out.txt')
    r = os.system(cmd+' < '+input+' > out.txt')
    # print("r is " + str(r))
    if lang == 'java':
        os.remove(file.split('.')[0]+'.class')
    elif lang == 'c' or lang == 'cpp':
        os.remove(file.split('.')[0])
    if r==0:
        return 200
    elif r==31744:
        os.remove('out.txt')
        return 408
    else:
        os.remove('out.txt')
        return 400

def match(output):
    if os.path.isfile('out.txt') and os.path.isfile(output):
        b = filecmp.cmp('out.txt',output)
        os.remove('out.txt')
        return b
    else:
        return 404

file = '3n_plus_1.c'
lang = 'c'
testin = 'testin.txt'
testout = 'testout.txt'
timeout = '1' # secs

print(codes[compile(file,lang)])
print (codes[run(file,testin,timeout,lang)])
print (match(testout))  # True implies that code is accepted.