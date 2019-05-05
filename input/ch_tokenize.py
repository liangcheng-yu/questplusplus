import jieba


# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))

# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))

# Search mode
text1 = "早晨你在法国坐车一小时到德国了，再坐一小时就到波兰了。\n同一时间点，你在北京朝阳区，坐一小时的车，你在朝阳区，再坐一小时，还是在朝阳区。\n这是网上调侃，北京堵车现象的段子。\n截至2015年六月底，全国机动车保有量达2.7亿余辆，其中汽车163亿辆。\n2015年第三季度，北京出行高峰期，每出行1小时就有30分钟耗费在堵车上，折合时间成本每月808元。\n发展城市公共交通是缓解城市交通拥堵的有效措施。\n以日本东京为例，由于拥有发达的公交网络，人们在出行的时候，即使拥有更多的小汽车，但还是会首选轨道交通。\n买小汽车，用在个人的休闲、度假、旅行等方面。\n这样就形成了小汽车交通和公共交通，良性沟通。"
text2 = "全球性的产能过剩导致企业竞争越来越激烈。\n以往一款产品买三十年的做法已经不行了。\n你跑不快，有的是快的。\n某手机仅仅买上手了几个月，就从一个万众期待的货款成为了乏人问津的过时货。\n产品的生命周期大大缩短了。\n互联网时代的到来，踏入了工业时代的一大基础，信息不对称。\n工业时代里，生产厂家无法低成本地了解客户的每一个需求，所以往往把需求多的产品性能组合到一起，成为一款产品。\n比如买鞋，鞋厂无法知道你脚多大，只有标准码。\n如果你的脚偏肥或偏瘦，对不起，概不伺候。\n互联网改变了这个局面。\n人与人，人与厂商，可以实现低成本的实现连接，从而让每个人的个性需求被放大。\n但是，个性化的东西需求量没有那么大。\n这就需要工业企业，能够实现小批量的，快速生产。"
# seg_list1 = jieba.cut_for_search(text1)
# seg_list2 = jieba.cut_for_search(text2)
# seg_list3 = jieba.cut_for_search(text3)
seg_list1 = jieba.cut(text1)
seg_list2 = jieba.cut(text2)
# seg_list3 = jieba.cut(text3)
print(" ".join(seg_list1))
print(" ".join(seg_list2))
# print(" ".join(seg_list3))
