# SignIn淮阴师范学院自动签到
## 环境

 - 基于Python、Selenium写的，用之前需要安装Python，再pip install selenium
 - 需要浏览器驱动，现提供的是98.0.4758.80版本的谷歌浏览器驱动（chromedriver.exe）以及谷歌浏览器98.0.4758.80。其他或更新版本可自行下载。
 下载地址
 谷歌浏览器驱动：http://chromedriver.storage.googleapis.com/index.html
 谷歌浏览器：https://www.chromedownloads.net/
 
## 运行
安装好环境后需将程序文件夹命名为"SignIn"放入C盘根目录下，随后双击签到.py运行

## 自动化
也可设置windows任务计划，让其每天自动运行

在开始菜单中搜索任务计划，在左侧选择任务计划程序库，点击右侧操作栏下的创建基本任务计划，设置名称，触发频率以及时间，操作选择启动程序，在程序或脚本中选择刚刚的签到.py 要在属性中设置只在用户登录时运行。