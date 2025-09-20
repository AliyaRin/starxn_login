以下是根据你之前提供的内容整理的.md文件内容：

# starxn_login - 简易模拟登录操作指南

## 1. 首先安装Python
1. 按下键盘上的 **Win键 + R键**，打开Windows“运行”窗口；
2. 在“打开(O)”输入框中输入`cmd`，点击“确定”按钮（或直接按回车键）；  
   ![Windows运行窗口输入CMD](https://github.com/user-attachments/assets/92825e5f-cfb6-4f2a-982b-6591f7bf6375)
3. 打开CMD窗口后，在命令行中输入`python`，按下回车键；  
   ![CMD中输入Python](https://github.com/user-attachments/assets/f3910cf7-4209-49ef-b06b-517e578aac57)
4. 若未安装Python，需先完成安装（已安装则跳过此步），确保系统中存在Python 3.13及以上版本；  
   ![Python 3.13已安装界面](https://github.com/user-attachments/assets/ffea4173-e437-4f5f-8937-1ca9759d4e8a)

## 2. 安装Selenium库（自动化工具）
> ⚠️ **务必关掉之前打开的CMD黑框框！！！**

1. 重新按下**Win键 + R键**，打开“运行”窗口，输入`cmd`并按回车；
2. 在新的CMD窗口中，输入以下命令，按下回车键等待安装完成：  
   ```bash
   pip install selenium
   ```

## 3. 获取登录页面的输入框ID和按钮ID
很多人会问：“主播主播，输入框ID和按钮ID是什么呀？”按以下步骤操作即可获取：
1. 用浏览器打开你需要模拟登录的网页；
2. 按下键盘上的**F12键**（若没反应，尝试**Fn键 + F12键**），打开浏览器“开发者工具”；
3. 在开发者工具界面，点击左上角的“选择元素”按钮（图标通常是“方框内带箭头”样式）；  
   ![浏览器开发者工具选择元素按钮](https://github.com/user-attachments/assets/d8347fb6-766f-4c2d-823f-c815e1c1aea3)
4. 将鼠标光标移动到“用户名输入框”上，点击左键，此时开发者工具右侧会高亮显示该输入框对应的代码；  
   ![用户名输入框代码高亮](https://github.com/user-attachments/assets/62dd8964-56ab-4900-8c8f-3f963d3bac9b)
5. 看见标黄的地方了吗？写着`ID="username"`，这里面的`username`就是这个输入框的ID。举一反三，剩下的密码输入框、登录按钮，都用这样的方法找到。

## 4. 修改代码
1. 右键下载的`starxn_login.py`，使用记事本打开；
2. 把你获取到的登录网页URL、用户名输入框ID、用户名、密码输入框ID、以及密码替换成你需要的内容，别忘了后面的登录按钮ID。注意，删掉引号内中文，填入内容（不要删掉引号）；
3. 按下键盘上的`Ctrl键 + S键`保存代码。

## 5. 运行代码
回到桌面双击鼠标左键运行`starxn_login.py`。

## 6. 登录按钮没有ID名怎么办？
可能会有这种情况，但是有其他属性，比如`type`，`class`，如下：
```html
<button type="submit" class="login - button">登录</button>
```
这时候，回到代码编辑界面。如果按钮有`name`属性（如`<button name="loginBtn">登录</button>`），可以这样修改代码：
```python
login_button = wait.until(
    EC.element_to_be_clickable((By.NAME, "loginBtn"))  # 替换为实际的name值
)
```
如果使用`class`属性定位（如`<button class="login - btn submit">登录</button>`），则修改为：
```python
login_button = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "login - btn"))  # 替换为实际的class
)
```
