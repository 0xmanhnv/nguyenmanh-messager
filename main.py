import json

from nguyen_manh_bot import NguyenManhBot


def main():
    # Load session đăng nhập từ trước nếu có
    with open('session.json') as f:
        session_cookies = json.load(f)

    client = NguyenManhBot('username', 'password', session_cookies=session_cookies)

    # Lấy session và lưu vào file để lần sau dùng cho đăng nhập
    session_cookies_new = client.getSession()
    with open('session.json', 'w') as outfile:
        json.dump(session_cookies_new, outfile)

    # Lắng nghe phản hồi từ messager
    client.listen()


if __name__ == '__main__':
    main()
