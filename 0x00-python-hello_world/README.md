<h1>0x00.Python-Hello, World</h1>
<code>Python</code>
<h2>Author's Disclaimer</h2>


```
Welcome to the Python world!

The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode.

Enjoy!

- Guillaume
```


<h3>Requirements</h3>
<h4>Python Scripts</h4>
<ul>
<li>Allowed editors: <code>vi, vim, emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A README.md file at the root of the repo, containing a description of the repository</li>
<li>A README.md file, at the root of the folder of this project, is mandatory</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>



<h3>Shell Scripts</h3>
<ul>
<li>Allowed editors: <code>vi, vim, emacs</code></li>
<li>All your scripts will be tested on Ubuntu 20.04 LTS</li>
<li>All your scripts should be exactly two lines long <code>(wc -l</code> file should print 2)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/bin/bash</code></li>
<li>All your files must be executable</li>
</ul>


<h3>More Info</h3>
<h4>Zen</h4>


```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```


<h1>Tasks</h1>
<ul>
<li><code>0-run></code>  -  Shell script that runs a Python script.The Python file name will be saved in the environment variable <code>$PYFILE</code></li>
<li><code>1-run_inline</code>  -   Shell script that runs Python code.The Python code will be saved in the environment variable <code>$PYCODE</code></li>
<li><code>2-print.py</code>   -  Write a Python script that prints exactly <code>"Programming is like building a multilingual puzzle</code>, followed by a new line.</li>
<li><code>3-print_number.py</code>  -  Complete this source code in order to print the integer stored in the variable number, followed by <code>Battery street</code>, followed by a new line.</li>
<li><code>4-print_float.py<code>   -  Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.</li>
<li><code>5-print_string.py</code>  - prints string three times followed by its first nine characters</li>
<li><code>6-concat.py</code>  -  use two variables to print a conatenated string</li>
<li><code>7-edges.py</code>   -  prints a first three characters of a word, last two characters of a word and the middle characters</li>
<li><code>8-concat_edges.py</code>   -   conatenates edges of a string</li>
<li><code>9-easter_egg.py</code>  -  Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.Your script should be maximum 98 characters long (please check with <code>wc -m 9-easter_egg.py)</code></li>
<li><code>10-check_cycle.c</code>and<code>lists.h</code</li>  -  a <code>C</code> that checks if a singly linked list has a cycle in it.
<li><code>100-write.py</code>    -   Write a Python script that prints exactly and <code>that piece of art is useful - Dora Korpar, 2015-10-19</code>, followed by a new line.</li>
<li><code>101-compile</code>  -  Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be <code>$PYFILEc</code> (ex: <code>export PYFILE=my_main.py</code> => output filename: <code>my_main.pyc)</code></li>
<li><code>102-magic_calculation.py</code>  -  Write the Python function <code>def magic_calculation(a, b)</code>: that does exactly the same as the following Python bytecode:


```bash
 3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```


</li>
</ul>
