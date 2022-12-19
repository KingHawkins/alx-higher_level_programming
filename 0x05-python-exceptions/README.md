<h1>0x05. Python - Exceptions</h1>


```
python
```


<h2>Tasks</h2>

1. <h3> Safe list printing</h3>
<p>Write a function that prints <code>x</code> elements of a list</p>


<p>prototype:</p>


```python
def safe_print_list(my_list=[], x=0):
```


```python, bash
guillaume@ubuntu:~/0x05$ cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

guillaume@ubuntu:~/0x05$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
guillaume@ubuntu:~/0x05$
```



