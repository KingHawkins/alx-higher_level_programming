<h1>0x02. Python - import & modules</h1>


```
python
```

<img src="https://www.guru99.com/images/2/062620_0700_Importmodul1.png" jsaction="load:XAeZkd;" jsname="HiaYvf" class="n3VNCb KAlRDb" alt="Import module in Python with Examples" data-noaft="1" style="width: 10.7582px; height: 6px; margin: 28.2px 0px;">
<h1>What is a module?</h1>
<p>Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

</p>

<h2>Create a Module</h2>
<p>
To create a module just save the code you want in a file with the file extension <code>.py</code>
</p>


<h3>Example</h3>
<p>Save this code in a file named <code>mymodule.py</code>


```python
def greeting(name):
  print("Hello, " + name)
```


<h3>Use a Module</h3>
<p>Import the module named mymodule, and call the greeting function:</p>


```python
import mymodule

mymodule.greeting("Jonathan")
```


<h3>Variables in Module</h3>
<p>The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):</p>
<h2>Save this code in the file <code>mymodule.py</code></h2>


```python
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```


<h3>Example</h3>
<p>Import the module named mymodule, and access the person1 dictionary:</p>



```python
import mymodule

a = mymodule.person1["age"]
print(a)
```


<h3>Naming a Variable</h3>
<p>You can name the module file whatever you like, but it must have the file extension <code>.py</code></p>
<h4>Example</h4>
<p>You can create an alias when you import a module, by using the <code>as</code> keyword:</p>


```python
import mymodule as mx

a = mx.person1["age"]
print(a)
```


<h3>Built modules</h3>
<p>There are several built-in modules in Python, which you can import whenever you like.</p>
<h4>Example</h4>
<p>Import and use the <code>platform</code> module:


```python
import platform

x = platform.system()
print(x)
```


<h3>Using the dir() Function</h3>
<p>There is a built-in function to list all the function names (or variable names) in a module. The <code>dir()</code> function:</p>
<h4>Example</h4>
<p>List all the defined names belonging to the platform module:</p>


```python
import platform

x = dir(platform)
print(x)
```


