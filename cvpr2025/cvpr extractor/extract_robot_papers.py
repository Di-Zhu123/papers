print(1)
from bs4 import BeautifulSoup
import re
import sys
import subprocess
import pkg_resources

try:
    # 检查是否安装了lxml
    try:
        pkg_resources.require('lxml')
    except pkg_resources.DistributionNotFound:
        print('正在安装lxml包...')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'lxml'])
        print('lxml包安装完成')

    print('开始执行脚本...')
    
    # 读取HTML文件
    with open('CVPR 2025 Accepted Papers.html', 'r', encoding='utf-8', errors='ignore') as file:
        html_content = file.read()
        print(f'成功读取HTML文件，文件大小：{len(html_content)}字节')
        if len(html_content) == 0:
            raise Exception('HTML文件内容为空')

    # 使用BeautifulSoup解析HTML，使用lxml解析器
    soup = BeautifulSoup(html_content, 'lxml')
    print('成功解析HTML内容')

    # 找到所有包含论文标题的td标签
    paper_entries = soup.select('td strong')
    print(f'找到{len(paper_entries)}个论文标题')

    if len(paper_entries) == 0:
        raise Exception('未找到任何论文条目')

    # 存储包含'robot'的标题
    robot_papers = []

    for title_element in paper_entries:
        # 获取标题文本
        title = title_element.get_text().strip()
        print(f'处理标题: {title}')
        
        # 检查标题是否包含'robot'（不区分大小写）
        if 'robot' in title.lower():
            robot_papers.append(title)
            print(f'找到包含robot的论文：{title}')

    print(f'总共处理了{len(paper_entries)}个论文标题')

    # 将结果写入txt文件
    with open('robot_papers.txt', 'w', encoding='utf-8') as file:
        for title in robot_papers:
            file.write(title + '\n')

    print(f'找到{len(robot_papers)}篇包含"robot"的论文，已保存到robot_papers.txt')

except Exception as e:
    print(f'发生错误：{str(e)}', file=sys.stderr)
    sys.exit(1)