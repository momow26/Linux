Git操作步骤
一、基本概念
1.	Git: 是目前世界上最最先进的分布式版本控制系统
2.	Git的安装：傻瓜式下一步安装，这里使用的是Git 2.16.2
3.	配置 --- 只需要配置一次即可
1）	配置用户名：git config --global user.name momow26
2）	配置邮箱：git config –global user.email momow26@163.com
4.	版本库：即仓库，可以理解为一个目录，这个目录里面所有的文件都可以被git管理起来，每个文件的修改、删除等git都可以跟踪，以便在任何时候都可以追踪到历史版本，或者在将来某个时候还可以还原。
5.	创建版本库
在自己想要创建的地方，创建一个空目录
Cd进入该目录
使用git init 命令把这个目录变成git可以管理的仓库
6.	添加文件到版本库
在仓库目录中创建一个momo.txt的文件，内容自己选择
把文件添加到仓库 git add momo.txt
把文件提交到仓库 git commit –m “注释信息---第一次添加/提交，实现了哪些功能”
7.	查看仓库状态 --- git status
可以在文件夹中自己手动修改，也可以通过vim进入文件夹编辑，根据自己实际情况来选择
8.	查看修改的内容与之前的内容有什么区别，进行了哪些修改 --- git diff
对修改后的内容再进行重新添加，提交， 
重复  git add momo.txt
git commit –m “注释信息---第二次提交 + 每次修改了哪些内容,实现了哪些功能”
9.	显示提交日志的历史记录---由近及远  git log
简单显示              git log --pretty=oneline
10.	返回到上一个版本      git reset –hard HEAD^
返回到上上一个版本    git reset –hard HEAD^^
返回到上10个版本     git reset –hard HEAD~10
返回到具体版本git reset –hard 20d49b03ba5109106e53040fffdaa18eb555a1e3
11.	记录历史命令 git reflog
12.	撤销刚刚修改的到上一版本（修改后，还没有 git add 和git commit）git checkout -- momo.txt
13.	创建SSH Key 在git bash里输入 ssh-keygen –t rsa –C ‘momow26@163.com
注意在git bash中看.ssh目录的位置 分公钥id_rsa和私钥id_rsa.pub
在id_rsa.pub文件中，将公钥代码拷贝至自己的github账户----setting下的SSH and GPG key目录下，title自己根据实际情况命名
14.	验证密钥是否配置成功
Ssh –T git@github.com
15.	创建远程仓库 在自己的GitHub里建一个repository，名字根据需要命名
关联远程仓库 git remote add origin git@github.com:momow26/Linux.git
删除关联：git remote rm origin
16.	推送本地仓库内容到远程仓库
git push origin master
注意：在推送之前，先要把远程仓库中的内容先拉下来到本地，否在会报错
拉取远程仓库内容到本地仓库
git pull origin master  
如果出现这样的错误，fatal: refusing to merge unrelated histories，需要输入如下代码
git pull origin master --allow-unrelated-histories
二、项目练习
17.	Master主分支 
18.	创建分支 git branch 分支名    git branch momo
19.	切换分支 git checkout 分支名  切换到master分支 git checkout master
20.	创建与切换分支同时进行 git checkout –b 分支名 git checkout –b momo
21.	查看分支 git branch 会列出所有分支， 当前的分支前会绿色显示及有个*号
22.	任何分支都不会相互影响
23.	合并分支：先应到master分支，然后把momo的分支内容合在master分支上，命令如下 git merge momo
在远程仓库创建分支momo： git push --set-upstream origin momo
24.	
