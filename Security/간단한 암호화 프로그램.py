from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# AES 암호화 및 복호화 클래스
class AESCipher:
    def __init__(self, key):
        self.key = key
    
    def encrypt(self, raw):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(raw.encode(), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return iv, ct

    def decrypt(self, iv, ct):
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8')

# 사용 예
if __name__ == "__main__":
    key = get_random_bytes(16)  # 16바이트 키 생성 (AES-128)
    cipher = AESCipher(key)

    # 암호화
    plaintext = "TEXT" # 복호화 하고 싶은 문자를 입력
    iv, ciphertext = cipher.encrypt(plaintext)
    print("IV:", iv)
    print("Ciphertext:", ciphertext)

    # 복호화
    decrypted = cipher.decrypt(iv, ciphertext)
    print("Decrypted:", decrypted)
