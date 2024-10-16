import zipfile

def judge_zip(file_path):
    """
    检查zip文件是否存在伪加密
    """
    with zipfile.ZipFile(file_path) as zf:
        for info in zf.infolist():
            if info.flag_bits & 0x1:
                print(info.flag_bits)
                return True
    return False

def judge_rar(file_path):
    """
    检查rar文件是否存在伪加密
    """
    return True  

if __name__ == "__main__":

    zip_path = './Demo/headcrack-origin-now.zip'
    if judge_zip(zip_path):
        print(f"{zip_path} 可能存在加密")

