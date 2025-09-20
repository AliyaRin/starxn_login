# 自动化登录脚本，使用Selenium模拟浏览器操作
#这里是要求安装selenium和chromedriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def auto_login():
    driver = webdriver.Chrome() 
    try:
        # 打开登录页面
        driver.get("这里是登录页面的URL")
        
        # 等待页面加载完成
        wait = WebDriverWait(driver, 10)
        
        # 输入用户名
        username_field = wait.until(
            EC.presence_of_element_located((By.ID, "这里是用户名输入框的ID"))
        )
        username_field.clear()
        username_field.send_keys("这里是用户名")
        #这里是主播用来测试的
        print("已输入用户名")
        
        # 输入密码
        password_field = wait.until(
            EC.presence_of_element_located((By.ID, "这里是密码输入框的ID"))
        )
        password_field.clear()
        password_field.send_keys("这里是密码")
        #这里是主播用来测试的
        print("已输入密码")
        
        # 点击登录按钮
        login_button = wait.until(
            EC.element_to_be_clickable((By.ID, "这里是登录按钮的ID"))
        )
        login_button.click()
        #这里是主播用来测试的
        print("已点击登录按钮")
        # 等待登录过程完成
        WebDriverWait(driver, 10).until(
            EC.url_changes("这里是登录页面的URL")
        )
        #这里是主播用来测试的
        print("登录完成，正在关闭浏览器...")
        
        #这里是主播用来测试的
    except TimeoutException:
        print("错误：页面元素加载超时")
    except NoSuchElementException:
        print("错误：未找到指定的页面元素")
    except Exception as e:
        print(f"发生错误：{str(e)}")
    finally:
        driver.quit()# 关闭浏览器
        print("浏览器已关闭")
# 这里是主程序入口
if __name__ == "__main__":
    auto_login()
