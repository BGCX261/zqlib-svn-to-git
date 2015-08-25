Yongwei Wu <yongwei@zeuux.org>
收件人	"Zoom. Quiet" <zoom.quiet@gmail.com>
副本	Bill Xu <bill@zeuux.org>、
zeuux-member <zeuux-member@zeuux.org>
日期	2008年11月25日 上午 12:17
主旨	Re: [zeuux-member] XHTML标准
寄件人	zeuux.org
	
隱藏詳細資料 00:17 (8 小時以前) [overwrite,sedfile,grepsedfile]
	
	
回覆全部
	
	
刚用grep+sed+脚本搞定了free-software-free-society下的hr和br的问题。其它很多问题可能可以类似炮制。脚本和命令放在这封邮件里。

grepsedfile '<br clear="all">' '<br clear="all" />' *.html
grepsedfile '<hr>' '<hr />' *.html

