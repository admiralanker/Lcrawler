### Python的工程结构

#### python规范目录结构
假设项目名称为Foo
```
Foo/
|-- bin/ #存放项目的一些可执行文件
|   |-- foo
|-- foo/ # 所有模块、包都应该放在此目录，程序的入口最好命名为main.py
|   |-- tests/ # 存放单元测试代码；
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |-- __init__.py
|   |-- main.py
|-- docs/ # 用于存放文档
|   |-- conf.py
|   |-- abc.rst
|-- setup.py # 来管理代码的打包、安装、部署问题
|-- requirements.txt # 存放软件依赖的外部Python包列表
|-- README # 项目说明文件
```  

---

#### Python通用目录结构
```
ProjectName 
│ readme 项目说明文档 
│ requirements.txt 存放依赖的外部Python包列表 
│ setup.py 安装、部署、打包的脚本 
├─ bin 存放脚本，执行文件等 
│ └─ projectname 
├─ docs 文档和配置 
│ └─ abc.rst 
│ └─ conf.py 配置文件 
└─ projectname 工程源码（包括源码、测试代码等） 
│ main.py 程序入口 
│ init.py 
└─ tests 测试代码 
└─ test_main.py 
└─ init.py
```


```python
print('1')
```
