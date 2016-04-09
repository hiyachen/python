# Biopython
## 介绍
Biopython是Python的计算分子生物学和生物信息学工具包，它使得python在生物学数据处理中变得更加强大和高效。

## 安装
Ubuntu(10.04)为例
aptitude search biopython
p   python-biopython                                        - Python library for bioinformatics (implemented in Python 2)       
p   python-biopython-doc                                    - Documentation for the Biopython library                           
p   python-biopython-sql                                    - Biopython support for the BioSQL database schema (Python 2)       
v   python2.7-biopython-sql                                 -                                                                   
p   python3-biopython                                       - Python library for bioinformatics (implemented in Python 3)       
p   python3-biopython-sql                                   - Biopython support for the BioSQL database schema (Python 3) 
### 方法一:使用apt-get install方式安装
sudo apt-get install python-biopython
只有一行命令，可是这种方法安装的不是最新版本，很多新的功能不能用，非常不爽，不建议使用这种方法安装。

### 方法二：使用easy_install安装
（1）安装python-dev，不然会出现Setup script exited with error: command ‘gcc’ failed with exit status 1错误
sudo apt-get install python-dev

（2）安装easy_install工具
sudo apt-get install python-setuptools

（3）安装biopython
sudo easy_install -f http://biopython.org/DIST/ biopython  (DIST/和biopython之间有个空格)

（4） 安装Numpy
从http://numpy.scipy.org/下载numpy，现在的最新版本是numpy-1.6.1.tar.gz
tar -xzvpf numpy-1.6.1.tar.gz
cd numpy-1.6.1/
python setup.py build
sudo python setup.py install
还可以继续安装一些其它的dependencies，如flex，ReportLab等等，暂时不装，需要的时候再装也可以。

（4）改为
Download Numpy1.6.1 and unpack it; using the following commands:
wget http://sourceforge.net/projects/numpy/files/NumPy/1.6.1/numpy-1.6.1.tar.gz
tar -zxvf numpy-1.6.1.tar.gz
If the environment variable PYTHONPATH happens to be set, unset it (you may set it again after installing Numpy):
unset PYTHONPATH
The command that unpacks NumPy1.6.1 will have created a directory called "numpy1.6.1". Enter that directory and build the Numpy package with the help of the fortran compiler:
cd numpy-1.6.1/
python3.2 setup.py build --fcompiler=gnu95



