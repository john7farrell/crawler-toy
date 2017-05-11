# crawling [Techmeme]
[Techmeme]: https://www.techmeme.com/

Note:
Techmeme is mainly a technology news site.(https://www.techmeme.com/)

This is a small toy of crawling Techmeme website.
Simply doing 2 things:
- crawling the web data (news titles of one day) from: `https://www.techmeme.com/`
- generate a wordcloud based on the news titles.

#-#-#-#-#-#-#-#-#-#
# UPDATE 20170511 #
#-#-#-#-#-#-#-#-#-#
Now updated 3 .py files:
crl_river.py: 
- crawling `https://www.techmeme.com/river` whose structure is simple and easy to crawl.
crl_archive.py: 
- crawling `https://www.techmeme.com/` or plus some suffix accessing the past archives.
crl_test.py: 
- same as crl_archive.py and just put scripts into functions. 
example image of wordcloud:
![img](https://github.com/john7farrell/techmmPrj/blob/master/wc_img/WC-170511-h0000.jpg)