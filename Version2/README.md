工程设计学-学习与实践手册（版本2）
===================================

内容上没有做太多的修改，只是为了生成pdf图书时，删除了每章中序号。下面介绍下在Ubuntu下如何生成pdf文档的。

### Ubuntu下安装Sphinx

		$ easy_install sphinx

还需要安装需要安装Python中文分词组件jieba：
		
		$ easy_install jieba

为了生成pdf需要安装：
		
		$ apt-get install make python-sphinx texlive-full

上面安装 LaTeX 套件的时候也安装了CJK字体。其中有 4 种中文字体：gbsn(简体宋体)、gkai(简体楷体)、bsmi(繁体明体)和 bkai(繁体楷体)。选择字体的时候一定要简体选简体的字体，繁体选繁体的字体，否则生成的 pdf 文档会出现文字缺失。选择好字体就可以在 conf.py 的 latex_elements 选项中添加相关的配置内容：

		latex_elements = {
		
		'preamble': '''
		\\hypersetup{unicode=true}
		\\usepackage{CJKutf8}
		\\AtBeginDocument{\\begin{CJK}{UTF8}{gbsn}}
		\\AtEndDocument{\\end{CJK}}
		'''
		}

其中 \hypersetup 是用于设置生成的 pdf 的书签使用 Unicode 字符，否则会出现乱码。

修改完 conf.py 后，就可以执行 Sphinx 项目的 make latexpdf 命令生成 pdf 文档了。

如果在 conf.py 的 latex_document 选项中文档标题的内容或作者的内容里包含有 Unicode 字符，可能会出现下面这些莫名其妙的错误。

这是由于 Sphinx 在生成 LaTeX 文档时会用 CJK 字符直接替换掉相应的占位符。用 \unexpanded 将 Unicode 字符括起来：

		latex_documents = [
  			('index', 'AnIntroductiontolibuv.tex', u'title \\unexpanded{中文内容}',
   			u'\\unexpanded{中文作者}', 'manual'),
		]

这样就可以生成带有 Unicode 字符的标题和作者了。

参考：[用Sphinx制作中文pdf](http://gutspot.com/2013/06/21/%E7%94%A8sphinx%E5%88%B6%E4%BD%9C%E4%B8%AD%E6%96%87pdf/)