#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

import threading
import socket
import sys

# 定义静态web服务器类
class http_server(object):
    def __init__(self,port):
        # 初始化，为self创建套接字、绑定端口、设置套接字复用
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.socket.bind(("", port))

    @staticmethod
    def handle_service(handle_socket, handle_ip, maxRecv):
        print("CONNECTED:\n", handle_ip)
        # 接收数据
        recv_data = handle_socket.recv(maxRecv)
        if recv_data:
            # 获取请求的文件目录
            recv_content = recv_data.decode("utf-8")
            request_dir = recv_content.split(" ")[1]
            print("Request file direction:\n", request_dir)
            # 以http协议格式回复
            try:
                if request_dir == "/":
                    request_dir = "/index.html"
                with open("/home/xulingjiang/static"+request_dir, "rb") as file:
                    request_body = file.read()
                request_line = "HTTP/1.1 200 ok\r\n".encode("utf-8")
            except:
                with open("/home/xulingjiang/static/error.html", "rb") as file:
                    request_body = file.read()
                request_line = "HTTP/1.1 404 NotFound\r\n".encode("utf-8")
            finally:
                request_head = "server: PWS/3.6.9\r\n".encode("utf-8")
                request = request_line + request_head + b"\r\n" + request_body
                # 响应报文完成，发送
                handle_socket.send(request)
                print("Reponsed Compelet")
                handle_socket.close()
                return
        else: # 如果接收的数据为空，说明浏览器关闭，则退出套接字
            print("The connect is broke!")
            handle_socket.close()
            return            


    def start(self, maxListen=12, maxRecv=3078):
        # 启动服务器
        self.socket.listen(maxListen) # 设置监听
        while True:
            # 循环等待连接请求，并以子线程处理
            handle_socket, handle_ip = self.socket.accept()
            handle_thread = threading.Thread(target=self.handle_service, args=(handle_socket, handle_ip,maxRecv) )
            handle_thread.setDaemon(True)
            handle_thread.start()

    def close(self):
        # 关闭服务器
        print("server套接字关闭！")
        self.socket.close()


def main():
    # 兼容使用命令行（含额外参数）的方式启动服务器
    print(sys.argv) # 打印命令行参数
    # 判断命令行参数个数是否合法
    if len(sys.argv) != 2 and len(sys.argv) != 1:
        print("执行如下命令：python3 static_http_server_oop.py 8000")
        return
    # 判断字符串是否是数字
    if len(sys.argv) == 2 and not sys.argv[1].isdigit():
        print("执行如下命令：python3 static_http_server_oop.py 8000")
        return
    
    # 赋予正确port值
    if len(sys.argv) == 1:
        port = 8000
    else: # 获取命令行参数
        port = int(sys.argv[1])

    # 实例化静态服务器类并启动
    web_http_server = http_server(port)
    web_http_server.start()

if __name__ == "__main__":
    main()

"""
总结：1. 在static_http_server.py上，进行面向对象封装。
     2. 使用sys.argv获取命令行模式下指定的端口号
"""