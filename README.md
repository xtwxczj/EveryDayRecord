# EveryDayRecord
git 操作方法
Quick setup — if you’ve done this kind of thing before
or

We recommend every repository include a README, LICENSE, and .gitignore.
…or create a new repository on the command line

echo "# EveryDayRecord" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:xtwxczj/EveryDayRecord.git
git push -u origin master

…or push an existing repository from the command line

git remote add origin git@github.com:xtwxczj/EveryDayRecord.git
git push -u origin master

…or import code from another repository

You can initialize this repository with code from a Subversion, Mercurial, or TFS project.


2017/10/16
参考了下面链接中随机森林的写法：
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/learn/random_forest_mnist.py
https://github.com/camrongodbout/TensorFlow-in-a-Nutshell/blob/master/part3/random_forest.py
http://www.jianshu.com/p/67977f1fa535
http://blog.csdn.net/flying_sfeng/article/details/64133822
发现了一个方法：局部敏感哈希（Locality-Sensitive Hashing)方法
用于海量高维数据的近似最近邻快速查找技术
http://blog.csdn.net/icvpr/article/details/12342159

