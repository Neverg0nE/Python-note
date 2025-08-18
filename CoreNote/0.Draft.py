import socket

def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False

# 常见的 Clash/FLClash 默认端口
ports = {
    "HTTP/Mixed": 7890,
    "SOCKS5": 7891,
    "Redir": 7892,
    "DNS": 1053
}

ip = "127.0.0.1"

print("🔍 正在检测 FLClash 代理端口...\n")
for name, port in ports.items():
    if check_port(ip, port):
        print(f"✅ {name} 代理运行中: {ip}:{port}")
    else:
        print(f"❌ {name} 代理未监听: {ip}:{port}")
        