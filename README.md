# bypasswaf

2.0：增加优化了部分规则 现在bypass云锁tamper支持所有的注入类型了！<br>
更新了bypass 云锁 数字型注入的tamper<br>

针对最新版云锁和安全狗的sqlmap自动化绕过脚本<br>

包含：<br>
bypass安全狗 延时、布尔、union注入 <br>
bypass云锁tamper （可0警告绕过云锁）<br>

利用知识点：<br>
安全狗：内联注释<br>
blog:https://pureqh.top/?p=1882<br>
云锁：引号包裹注释符绕过检测<br>
blog:https://pureqh.top/?p=4175<br>

注：bypass云锁 使用双引号可以绕过官网检测
http://help.yunsuo.com.cn/guide/install/?id=1' "/*" union select 1,group_concat(schema_name),2,3 from information_schema.schemata -- "*/"

