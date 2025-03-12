import subprocess
import sys

def install_package(package_name):
    try:
        # 尝试安装指定的包
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"{package_name} 已成功安装。")
    except subprocess.CalledProcessError:
        print(f"安装 {package_name} 时发生错误。")
    except Exception as e:
        print(f"安装 {package_name} 时发生未知错误: {e}")

if __name__ == "__main__":
    # 调用函数安装 requests 库
    install_package("requests")
