import os

# 查询已连接的设备/模拟器列表
os.system('adb devices')

# 通过同网段而不需要USB连接手机  参数手机ip地址端口
# Connection refused 解决办法
# 1.adb shell   2.setprop service.adb.tcp.port 5555     3.之后去设置里关闭再重新打开"USB调试"选项
os.system('adb connect 192.168.1.237:5555')

# 查看所有应用  【如果多个设备，需要adb -s 设备号 shell pm list packages】
adb shell pm list packages

# 查看系统应用
adb shell pm list packages -s

# 查看第三方应用
adb shell pm list packages -3

# 包名包含某字符串的应用，比如要查看包名包含字符串 huawei 的应用列表
adb shell pm list packages huawei

# 应用安装 adb install apk文件
# 参数 【-r】覆盖安装   【-d】允许降级覆盖安装

#  清除应用数据与缓存, 相当于在设置里的应用信息界面点击了「清除缓存」和「清除数据」
adb shell pm clear com.loyo.elcm

# 查看前台Activity
adb shell dumpsys activity top | grep ACTIVITY

# 查看指定包名正在运行的Activity
 adb shell dumpsys activity activities | grep com.loyo.elcm | grep Activities

# 查看正在运行的Services [<package-name>]非必须，能够配合grep使用
adb shell dumpsys activity services com.loyo.elcm

# 查看apk详细信息，运行次命令的输出中包含很多信息，
# 包括 Activity Resolver Table、Registered ContentProviders、包名、userId、
# 安装后的文件资源代码等路径、版本信息、权限信息和授予状态、签名版本信息等。
adb shell dumpsys package com.loyo.elcm

# 收紧内存，获取pid【adb shell ps | grep com.loyo.elcm】   level【HIDDEN、RUNNING_MODERATE、BACKGROUND、RUNNING_LOW、MODERATE、RUNNING_CRITICAL、COMPLETE】
adb shell am send-trim-memory  <pid> <level>

# 模拟按键，能实现很多手机功能，测试必备
"""
keycode         含义
3               HOME 键
4               返回键
5               打开拨号应用
6               挂断电话
24              增加音量
25              降低音量
26              电源键
27              拍照（需要在相机应用里）
64              打开浏览器
82              菜单键
85              播放/暂停
86              停止播放
87              播放下一首
88              播放上一首
122             移动光标到行首或列表顶部
123             移动光标到行末或列表底部
126             恢复播放
127             暂停播放
164             静音
176             打开系统设置
187             切换应用
207             打开联系人
208             打开日历
209             打开音乐
210             打开计算器
220             降低屏幕亮度
221             提高屏幕亮度
223             系统休眠
224             点亮屏幕
231             打开语音助手
276             如果没有 wakelock 则让系统休眠
"""
adb shell input keyevent 26

#   查看设备屏幕分辨率，输出：Physical size: 720x1520；如果命令修改过，会有Override size
adb shell wm size
#   修改分辨率
adb shell wm size 480x1024
#   恢复原分辨率命令
adb shell wm size reset

#   查看设备屏幕密度，输出：Physical density: 320；如果命令修改过，会有Override density
adb shell wm density
#   修改屏幕密度
adb shell wm density 160
#   恢复原屏幕密度命令
adb shell wm density reset

#   查看设备 android_id
adb shell settings get secure android_id





