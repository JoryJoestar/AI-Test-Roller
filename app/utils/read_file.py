import pandas as pd
import json

def read_txt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return []
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return []

def read_excel_file(file_path, sheet_name=0, header=0):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=header)
        return df
    except Exception as e:
        print(f"读取Excel文件时发生错误: {e}")
        return None
    
def read_csv_file(file_path, header=0):
    try:
        df = pd.read_csv(file_path, header=header)
        return df
    except Exception as e:
        print(f"读取CSV文件时发生错误: {e}")
        return None
    
def read_json_file(file_path):
    """
    读取JSON文件并返回其内容。

    参数:
    file_path (str): JSON文件的路径。

    返回:
    dict: JSON文件的内容。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"文件 {file_path} 不是一个有效的JSON文件")
        return None
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None