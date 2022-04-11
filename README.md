**Create Virtualenv first**


```python3 -m venv .venv```

**Than activate .venv**


```source .venv/bin/activate```

**After activate .venv, Install python client for the kubernetes API**

```pip install kubernetes```


**Run script**

```python get_resources.py {deployment_name}```
