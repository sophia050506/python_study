#coding:utf-8
import  requests
from bs4 import BeautifulSoup
import re

req_head = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': 'td_cookie=18446744070568520460; UM_distinctid=164261a8ab8f9-0c509fd0eaaa6b-5e452019-144000-164261a8aba546; bdshare_firstime=1529647631475; CNZZDATA1273653546=739876611-1529642242-null%7C1529647646',
'Host': 'www.biqugecom.com',
'Referer': 'http://www.biqugecom.com/43/43575/',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'

}

def get_chapter(req_url,title):
    txt_section = "13327658.html"
    # 打开小说文件写入小说相关信息
    fo = open('%s.txt.download'%(title), "ab+")
    # 进入循环，写入每章内容
    while (True):
        try:
            # 请求当前章节页面
            r = requests.get(req_url + str(txt_section), params=req_head)
            r.encoding = 'gb18030'
            # soup转换
            soup = BeautifulSoup(r.text, "html.parser")
            # 获取章节名称
            section_name = soup.select('#wrapper .content_read .box_con .bookname h1')[0]
            section_text = soup.select('#wrapper .content_read .box_con #content')[0]
            for ss in section_text.select("script"):  # 删除无用项
                ss.decompose()
            # 获取章节文本
            section_text = re.sub('\s+', '\r\n\t', section_text.text).strip('\r\n')  #
            # 获取下一章地址
            txt_section = soup.select('#wrapper .content_read .box_con .bottem2 a')[2]['href']
            # 判断是否最后一章，当为最后一章时，会跳转至目录地址，最后一章则跳出循环
            if (txt_section == './'):
                print("小说名：《" + title + "》 下载完成")
                break
            # 以二进制写入章节题目
            fo.write(('\r' + section_name.text + '\r\n').encode('UTF-8'))
            # 以二进制写入章节内容
            fo.write((section_text).encode('UTF-8'))
            print(title + ' 章节：' + section_name.text + '     已下载')
            # print(section_text.text.encode('UTF-8'))
        except:
            print("小说名：《" + title + "》 章节下载失败，正在重新下载。")
    fo.close()

get_chapter('http://www.biqugecom.com/43/43575/','不伤悲')