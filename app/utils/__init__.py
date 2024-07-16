

def save_to_excel(dataframe, filename):
    dataframe.to_excel(filename, index=False)
    print(f"数据已成功保存到 {filename} 文件。")
    
def save_to_csv(dataframe, filename):
    dataframe.to_csv(filename, index=False)
    print(f"数据已成功保存到 {filename} 文件。")