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

**Python的工程结构**
![](https://lh3.googleusercontent.com/sF-G3pcVe6Txb1ic1Ko_6y-fuRQ2tf-Tmmrf6BwnjuoE5OEd4txZSRPrpiVu9Bab1EzJTzGAI6oUhG9Z0TaalVnrdcRAzmLDSxMsPM2U8HpF8XNr6AisIs-pG-YtQseoQ3a8KiU6yvdW_Y6BgGRmyu9UIx7--dO1zN7JddKE6iVR7RfPwgqIzYEAL4KSL2g-y7g4htYAfTNE3jytxtGa6iV7HvUnHdSIWnuyFi4LNTt2cVN8l4e4oDt3uUiVqxQ9Y8_9MadqsSdKv_zlFwbn_zFLDK_7TAYu4SfE3aP2QDYVGS8MBkD3Ma9j7kN3PcnPl1e06dT7mGLVRkDOdNcr9BTDQ-9Un29oRzW3zE_iu-KKzG5Fl9Ksz1pP8ybsqKVrYsl2M7APlJwVUOrFGIQkzvg9DZPrvGkIEYIu6fsjAN6NffuoeFBdHj2vJ7DbqiYIE4iLClC8l0jUkJ_Tvjd7UC42RhBZx9ph1vKkHvqLos_yFb03eHCzyaHedMjdxrWA7MiH36CT3zZ-XHGIyqpTKMnp5KAdBeQm_0Oe3GshUq2hkyYLdv73tiOa9gpXnqz2-XdZb-6vq45pG2l9IbIEt_0pbWutLukIL0NW-_8UPhkgaWY8OQvbmrh73ZnUDMUEaKhG1UFfZg8uA1dwMZyXooRF2EgWrg=w1228-h667-no)

