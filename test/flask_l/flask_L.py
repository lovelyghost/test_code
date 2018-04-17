import time
from numba import jit
from flask import Flask
from memory_profiler import profile


app = Flask(__name__)

@profile
def fib_seq_numba(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

@profile
@app.route("/")
def index():
    d = time.time()
    gg = fib_seq_numba(10000)
    print(time.time()-d)
    return str(gg)



if __name__ == "__main__":
    app.run(debug = True)
