# YeScan
BurpSuiteHistorySaveAndScan

> 通过BurpSuite插件将所有BP的请求(包括Re和In模块请求)都保存进数据库，然后通过程序调用，动态取出这些数据，以加载插件的形式检测可能存在的漏洞，目前已完成信息收集和SQL注入检测的插件，其中SQL注入检测通过调用SqlMap完成。

## 文件说明

1. saveRequest.py BurpSuite插件，通过BP加载即可，因为是py插件，BP还行设置jython
2. taskRun.py 主程序，用来数据读取、插件加载和结果显示
3. conf目录 配置文件放置目录，里面的config.py需自行设置，包括：数据库配置信息/不需保存请求的静态文件信息/sqlmap路径信息/temp文件保存路径信息
4. temp目录 用来保存扫描过程的temp文件，目前主要用来保存sqlmap扫描所需的request请求文件
5. plugins目录 用来保存扫描插件
6. libs目录 所有可能用到的第三方库与工具，以及后期可能编写的lib

## 如何使用

首先通过BP加载插件，然后开启需要连接的数据库。之后运行taskrun.py，具体为：
```
usage: taskRun.py [-h] [-t]

Port Scan Ver:1.0

optional arguments:
  -h, --help      show this help message and exit
  -t , --target   scan target
```
使用-t参数，指定需要扫描的目标，可以是完整的域名、主域名或者用`.`来指定扫描所有通过BP的请求

针对SQL注入的检测，插件会判断请求中是否包含关键内容`sqlrun.`，如果有就进行扫描。
我们在测试过程中，如果需要指定请求进行扫描，可以用BP把请求send到Re模块，然后找一处（UA中）位置键入`sqlrun.`即可。
如果需要对所有请求都进行SQL注入扫描，可以使用浏览器插件，直接设置一个包含`sqlrun.`字符串的UA，然后正常访问即可。

## todoList

- [ ] 编扫描结果格式优化及保存
- [x] 优化Sql注入扫描，思考是否需要使用多线程
- [ ] 完善通用插件，目前主要是编写XSS漏洞检测插件
- [ ] 插件调用问题处理，某些漏洞只扫描一次即可，如何实现（匹配扫描结果，如果扫描过就不再扫描？）
- [ ] 整体扫描多线程处理（是否需要？）
- [ ] 编写更多插件

