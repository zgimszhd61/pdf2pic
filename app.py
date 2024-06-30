import camelot

# 读取PDF文件
tables = camelot.read_pdf('2406.19256v1.pdf', pages='1')

# 将表格转换为Markdown格式并保存
for i, table in enumerate(tables):
    markdown = table.df.to_markdown(index=False)
    with open(f'table_{i+1}.md', 'w') as f:
        f.write(markdown)
        print(markdown)