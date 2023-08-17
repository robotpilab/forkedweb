import os

# 获取当前工作目录的路径
directory_path = os.getcwd()

# 要搜索和删除的文本
text_to_delete = '''{{% callout note %}}
Click the _Cite_ button above to import publication metadata.
{{% /callout %}}
'''

# 遍历所有子目录
for root, dirs, files in os.walk(directory_path):
  for file_name in files:
    if file_name == 'index.md':
      file_path = os.path.join(root, file_name)

      # 读取文件内容
      with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

      # 检查文本是否存在
      if text_to_delete in content:
        # 删除文本并将修改后的内容写回文件
        content = content.replace(text_to_delete, '')
        with open(file_path, 'w', encoding='utf-8') as file:
          file.write(content)
        print(f"在 {file_path} 中删除了指定的文本")
