# 概述
个人爱好读书，看电影，为自己挑选喜欢的书籍或电影是一件费事费力的"苦差事"，平时如果想看某一类别的书籍，就会上知乎，豆瓣上检索推荐的书籍，找一本评分，评论都很好的书买来看看。不过，作为一个爱好看书的程序猿，这点事情如果还要自己一个个的找，未免有些low了。本文就是解决找书和电影而生的爬虫。
# 功能介绍
- 书籍
  1. 书籍名称，评分，评分人数，作者，出版社，书籍的URL
  2. 数据用数据库保存
  3. 按照tag类型
  4. 为了防止IP被加入黑名单，使用IP代理(注: 豆瓣只会黑当天)
- 电影 
  1. 待续
# 功能分解
## 第一阶段
  1. csv保存数据
## 第二阶段
  1. 数据库保存数据
## 第三阶段
  1. IP代理
# 实现
## csv保存数据
### 方法1：修改配置文件settings.py
```python
# feed exports
# encode
FEED_EXPORT_ENCODING='utf-8'

# format
FEED_URI = 'file:///tmp/export.csv'
FEED_FORMAT='csv'
FEED_EXPORT_FIELDS = ["name", "douban_score", "douban_votes","authors","publisher"]
FEED_STORE_EMPTY = False
```
