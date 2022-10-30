#!/home/xulingjiang/miniconda3/envs/practise/bin/python3
# "__utf-8__"

import socket
import threading

def handle_service(handle_socket, ip_port):
    while True:
        # recive request post
        recv_data = handle_socket.recv(10240)
        if recv_data:
            ## get the request direction
            recv_content = recv_data.decode("utf-8")
            request_dir = recv_content.split(" ")[1]
            print(request_dir)
            # send response post use the diretion
            try:
                ## if the direction is right 
                if request_dir == "/":
                    request_dir = "/index.html"
                with open("/home/xulingjiang/static"+request_dir, "rb") as f:
                    response_body = f.read()
                response_line = "HTTP/1.1 200 OK\r\n".encode("utf-8")
            except:
                ## if the direction is wrong
                print("the request dir is wrong! RETURN 404!!")
                with open("/home/xulingjiang/static/error.html", "rb") as f:
                    response_body = f.read()
                response_line = "HTTP/1.1 404 NotFound\r\n".encode("utf-8")
            finally:
                ## use the finally direction to send response post
                response_head = "server: PWS/3.6\nDate: Sun, 30 Oct 2022 02:51:13 GMT\r\n".encode("utf-8")
                response_data = response_line + response_head + b'\r\n' + response_body
                handle_socket.send(response_data)
                print("have responsed, so close the handle\n")
                handle_socket.close()
                break
        else: # if the request is none, close 
            print("client have disconnect, so close the handle\n")
            handle_socket.close()
            break


if __name__ == "__main__":
    # create server socket
    server_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_soket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # bind port
    server_soket.bind(("", 9000))
    # set listen
    server_soket.listen(12)
    while True:
        # waiting for connect
        handle_socket, ip_port = server_soket.accept()
        print("Have Connected : ", ip_port)
        # creat subthread to handle
        handle_thread = threading.Thread(target=handle_service, args=(handle_socket, ip_port))
        handle_thread.setDaemon(True)
        handle_thread.start()
    server_soket.close()

"""
总结：1. tcp_multi_server.py的基础上，使用http协议规范接收和发送报文
     2. 注意请求报文的地址正确与否
     3. 注意报文的格式
"""