from datetime import datetime

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


def main():
    rpc_user = 'user'
    rpc_password = 'password'
    rpc_host = '127.0.0.1'
    rpc_port = '8332'
    rpc_url = f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}'

    try:
        rpc_connection = AuthServiceProxy(rpc_url)

        while True:
            new_address = rpc_connection.getnewaddress()
            print(f"Yeni adres: {new_address}")
            amount_received = rpc_connection.getreceivedbyaddress(new_address)
            if amount_received <= 1:
                print(f"Adrese henüz hiçbir miktar gönderilmedi.")
            else:
                print(f"Adrese Gönderilen Toplam Miktar: {amount_received} BTC")
                private_key = rpc_connection.dumpprivkey(new_address)
                print(f"Adresin Private Key'i: {private_key}")
                break

    except JSONRPCException as json_exception:
        print(f"RPC hatası: {json_exception.error}")


if __name__ == '__main__':
    main()
