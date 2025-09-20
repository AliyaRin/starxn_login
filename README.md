# starxn_login
简易模拟登入操作
# 首先安装Python
win键+R键，打开运行窗口，输入CMD，按回车
<img width="663" height="347" alt="image" src="https://github.com/user-attachments/assets/92825e5f-cfb6-4f2a-982b-6591f7bf6375" />
然后输入Python，敲回车
<img width="597" height="239" alt="image" src="https://github.com/user-attachments/assets/f3910cf7-4209-49ef-b06b-517e578aac57" />
然后安装python
<img width="706" height="361" alt="image" src="https://github.com/user-attachments/assets/ffea4173-e437-4f5f-8937-1ca9759d4e8a" />
# 关掉黑框框！！！
重新按下win键+R键，打开运行窗口，输入CMD，按回车
输入  pip install selenium  按回车等待安装库
右键下载的starxn_login.py,使用记事本打开会吧
中文看得懂吧，把要登入的网页URL、用户名输入框ID、用户名、密码输入框ID、以及密码替换成你要的，别忘了后面的登入按钮ID
# 这时候有人要问了，主播主播，输入框ID和按钮ID是什么呀？
浏览器打开你要登入的页面，按下键盘上的F12键（没反应怎么办？，fn键+F2）
这时候你已经打开开发者工具啦，看到这个按钮了吗？点一下
<img width="462" height="215" alt="image" src="https://github.com/user-attachments/assets/d8347fb6-766f-4c2d-823f-c815e1c1aea3" />
非常棒，现在将你的鼠标光标移动到用户名输入框上，点一下鼠标左键，可以看到右边突出显示的代码了
<img width="370" height="71" alt="image" src="https://github.com/user-attachments/assets/62dd8964-56ab-4900-8c8f-3f963d3bac9b" />
看见我标黄的地方了吗？写着ID=“username”，这里面的username就是这个输入框的ID了。
举一反三啊，剩下的密码输入框、登入按钮，都这样找到吧。
# 修改代码
回到代码编辑页面，把你获取到的填上去，都给好位置了，删掉引号内中文，填入内容（不要删掉引号）
按下键盘上的Ctrl键+S键保存代码
回到桌面双击鼠标左键运行！
# 主播已经写的很细了，将就看吧。
# 登入按钮没有ID名怎么办？？
可能会有这种情况，但是有其他属性，比如type，class，如下
<button type="submit" class="login-button">登录</button>
这时候怎么办呢？
不要急，回到代码编辑。找到这一段
<img width="359" height="126" alt="image" src="https://github.com/user-attachments/assets/57e3afc8-f472-47cb-a9ab-3b22196a0e5d" />


如果按钮有name属性（如 <button name="loginBtn">登录</button>
login_button = wait.until(
    EC.element_to_be_clickable((By.NAME, "loginBtn"))  # 替换为实际的name值
)
使用 class 属性定位（如 <button class="login-btn submit">登录</button>）
login_button = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "login-btn"))  # 替换为实际的class
)
