<h1>0x01. Python - Async</h1>
<img src="/img/async.png">
<h1>Resources</h1>


<li><a hfer="https://intranet.alxswe.com/rltoken/zYkXScziW1D5rNdNEvObjQ">Async IO in Python: A Complete Walkthrough</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/aZUO4GiWHbPIrVBIwptFAw">asyncio - Asynchronous I/O</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/72mVf1s8rx2ih_U2WjBmaA">random.uniform</a></li>

<h1>Tasks</h1>
<h3>0. The basics of async</h3>
<p>
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.</p>
<p>
Use the random module.
</p>
<pre>

bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
</pre>
<b>Repo:</b>

<li>GitHub repository: alx-backend-python</li>
<li>Directory: 0x01-python_async_function</li>
<li>File: 0-basic_async_syntax.py</li>
  
<h3>1. Let's execute multiple coroutines at the same time with async</h3>
<p>
Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.</p>
<p>
wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.
</p>
<pre>
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

bob@dylan:~$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
The output for your answers might look a little different and that’s okay.
</pre>
<b>Repo:</b>

<li>GitHub repository: alx-backend-python</li>
<li>Directory: 0x01-python_async_function</li>
<li>File: 1-concurrent_coroutines.py</li>
  
<h3>2. Measure the runtime</h3>
<p>
From the previous file, import wait_n into 2-measure_runtime.py.
</p>
<p>
Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.
</p>
<p>
Use the time module to measure an approximate elapsed time.
</p>
<pre>
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))

bob@dylan:~$ ./2-main.py
1.759705400466919
</pre>
<b>Repo:</b>

<li>GitHub repository: alx-backend-python</li>
<li>Directory: 0x01-python_async_function</li>
<li>File: 2-measure_runtime.py</li>
  
<h3>3. Tasks</h3>
<p>
Import wait_random from 0-basic_async_syntax.
</p>
<p>
Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task.
</p>
<pre>
bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))

bob@dylan:~$ ./3-main.py
<class '_asyncio.Task'>
</pre>
<b>Repo:</b>

<li>GitHub repository: alx-backend-python</li>
<li>Directory: 0x01-python_async_function</li>
<li>File: 3-tasks.py</li>
  
<h3>4. Tasks</h3>
<p>
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.
</p>
<pre>
bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))

bob@dylan:~$ ./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
</pre>
<b>Repo:</b>

<li>GitHub repository: alx-backend-python</li>
<li>Directory: 0x01-python_async_function</li>
<li>File: 4-tasks.py</li>
