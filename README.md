工程设计学-学习与实践手册
===================================

使用sphinx整理的[《工程设计学》](http://book.douban.com/subject/5335311/)这本书的文档。

模版是参考的：[SAE Python开发者手册](http://python.sinaapp.com/doc/index.html)

clone这个项目后，使用[reStructuredText](http://jwch.sdut.edu.cn/book/rst.html)格式来修改.rst文件，然后使用命令：
    sphinx-build -b html ./ builddir

生成的网页就在builddir这个文件夹中。

上传到SAE上，在线版的文档：[工程设计方法学](http://conanxincv.sinaapp.com/project1/index.html)

这个文档制作的还很粗糙，没有用到太多的reStructuredText格式，也没使用公式、图片，后续还会改进。
