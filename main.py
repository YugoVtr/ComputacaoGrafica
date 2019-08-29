import os, subprocess, signal, hashlib, time

def my_hash():
    with open("draw_square.py", "r") as f:
        c = f.read().encode('utf-8')
    return hashlib.md5(c).digest()

def my_open(): 
    return subprocess.Popen('python draw_square.py', shell=True, preexec_fn=os.setsid)

def my_close( pid ): 
    return os.kill(pid, signal.SIGKILL)

def my_grep( ):
    ps = subprocess.Popen(['ps', 'ax'], stdout=subprocess.PIPE)
    
    grep1 = subprocess.Popen(
            ['grep', 'draw_square.py$'],
            stdin=ps.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
    )
    
    grep2 = subprocess.Popen(
            ['grep', 'Rl'],
            stdin=grep1.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
    )
    
    awk = subprocess.Popen(
            ['awk', '{print $1}'],
            stdin=grep2.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
    )
            
    out, err = awk.communicate()
    return int(out)

def my_loop():
    var_hash = my_hash()
    pid = my_open()
    while True :
        time.sleep(2)
        new_var_hash = my_hash()
        if new_var_hash != var_hash :
            var_hash = new_var_hash
            window_pid = my_grep()
            my_close( window_pid )
            pid = my_open()

def main():
    my_loop()
    
if __name__ == "__main__":
    main()