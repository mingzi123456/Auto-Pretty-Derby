from PIL import Image
import time
import os
import cv2
import aircv as ac
'''对应分辨率2340x1080，稍微有几像素出入应该没问题吧'''
def shitu(tofind):#查找对应图片并点击
    imsrc = ac.imread(img_path)  # 原始图像
    imsch1 = ac.imread(tofind)  # 带查找的部分
    match_result = ac.find_template(imsrc, imsch1, minMatch)#查找
    print('match :  %s' % (match_result))
    global waitTime
    if match_result != None:
        x1, y1 = match_result['result']
        print("\033[1;33m  %s \033[0m" % (match_result['confidence']))
        time.sleep(0.5)
        os.system("adb -s %s shell input tap %s %s" % (devices,x1, y1))
        time.sleep(0.5)
        return True
    else:
        return False

def caigou():
    time.sleep(2)
    jietu()
    print("逛淘宝")
    shitu(shangdian)
    time.sleep(3)
    jietu()#购买属性书和比赛蹄铁并且立刻使用，+7的道具得一个个查看，而另外两种似乎不用
    if(goumai(sudu3) == True):
        print("time.sleep(3)")
        time.sleep(3)
        jietu()
    if (goumai(sudu7) == True):
        print("time.sleep(3)")
        time.sleep(3)
        jietu()
    if (goumai(naili7) == True):
        print("time.sleep(3)")
        time.sleep(3)
        jietu()
    if (goumai(liliang7) == True):
        print("time.sleep(3)")
        time.sleep(3)
        jietu()
    if (goumai(genxing7) == True):
        print("time.sleep(3)")
        time.sleep(3)
        jietu()
    if (goumai(zhili7) == True):
        print("time.sleep(3)")
        time.sleep(3)
        jietu()
    if (goumai(sudu15) == True):
        print("time.sleep(3)")
        time.sleep(3)
        jietu()
    if (goumai(titie) == True):
        print("time.sleep(3)")
        time.sleep(3)
        jietu()
    if (goumai(genxing3) == True):
        print("time.sleep(3)")
        time.sleep(3)
        jietu()
    if (goumai(genxing15) == True):
        print("time.sleep(3)")
        time.sleep(3)
        jietu()
    print("time.sleep(2)")
    time.sleep(1)
    jietu()
    print("停止采购")
    while(shitu(likaishangdian) == False):
        time.sleep(1)
        jietu()
        print("停止采购")

def jietu():#手机截图，一开始没有定义，后面用太多了才定义的
    os.system("adb -s %s shell screencap -p sdcard/screen.png"% devices)  # 截取屏幕，图片命名为screen.png
    os.system("adb -s %s pull sdcard/screen.png  d:\\a\\xn.png"% devices)  # 保存到D盘a文件夹
    img = cv2.imread(img_path)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(r"d:/a/xn.png", gray_image)
    print(img.shape)

def dabisai():
    time.sleep(3)
    jietu()
    while(shitu(bisai) == False):
        time.sleep(1)
        jietu()
        print("找比赛")
    i = 0
    while(i<2):
        time.sleep(0.5)
        jietu()
        print("查看是否有ok")
        if(shitu(ok)==True):
            break
        i += 1
    while (shitu(chuzou) == False):
        time.sleep(1)
        jietu()
        print("出走")
    time.sleep(1.5)
    jietu()
    while (shitu(chuzou) == False):
        time.sleep(1)
        jietu()
        print("出走2")
    while (shitu(jieguo) == False):
        time.sleep(1)
        jietu()
        print("比赛结果")
    while (shitu(ci) == False):
        os.system("adb -s %s shell input tap 553 1892"% devices)
        time.sleep(1)
        jietu()
        print("次")
    time.sleep(3)
    jietu()
    while (shitu(ci2) == False):
        time.sleep(1)
        jietu()
        print("次2")

def zouzhixian():
    time.sleep(2)
    jietu()
    while(shitu(yuyue) == False):
        shitu(zhix)
        shitu(yinzi)
        shitu(ci)
        time.sleep(1)
        jietu()
        print("走支线中")
    time.sleep(1)
    shitu(guanbi)
    print("关掉弹出1")
    time.sleep(2)
    jietu()
    i = 0
    while (i < 2):
        time.sleep(0.5)
        jietu()
        if(shitu(tanchu)==True):
            print("关掉弹出2")
            break
        i += 1


def goumai(tobuy):
    img = Image.open(img_path)  # 原始图像
    imsrc = ac.imread(img_path)
    imsch1 = ac.imread(tobuy)# 带查找的部分
    imsch3 = ac.imread(huanwan)
    match_result = ac.find_template(imsrc, imsch1, minMatch)
    print('match :  %s' %(match_result))
    global waitTime
    if match_result != None:
        x1, y1 = match_result['result']
        x2, y2, x3, y3 =match_result['rectangle']
        print("\033[1;33m  %s \033[0m" % ( match_result['confidence']))
        cropped = img.crop((0, x2[1], 1080, y2[1]))  # (左，上，右，下 )
        cropped.save(r"D:/python project/ppc/huanwan.png")
        chakan=r"D:/python project/ppc/huanwan.png"
        imsch2=ac.imread(chakan)
        match_result2 = ac.find_template(imsch2, imsch3, minMatch)
        print('match :  %s' % (match_result2))
        if match_result2 == None:
            print("可以交换")
            os.system("adb -s %s shell input tap %s %s"%(devices,x1+790 ,y1))
            while(shitu(shiyong) == False):
                jietu()
            while (shitu(shiyong2) == False):
                jietu()
            return True
        else:
            print("不可交换")
            return False


#商店购买物
shangdian = r"D:/python project/ppc/shuc/shangdian.png"#打开商店
tili20 = r"D:/python project/ppc/shuc/tili20.png"#体力药+20
sudu3 = r"D:/python project/ppc/shuc/sudu3.png"#速度书+3
sudu7 = r"D:/python project/ppc/shuc/sudu7.png"#速度书+7
sudu15 = r"D:/python project/ppc/shuc/sudu15.png"#速度书+15

naili3 = r"D:/python project/ppc/shuc/naili3.png"#耐力书+3
naili7 = r"D:/python project/ppc/shuc/naili7.png"#耐力书+7
naili15 = r"D:/python project/ppc/shuc/naili15.png"#耐力书+15

liliang3 = r"D:/python project/ppc/shuc/liliang3.png"#力量书+3
liliang7 = r"D:/python project/ppc/shuc/liliang7.png"#力量书+7
liliang15 = r"D:/python project/ppc/shuc/liliang15.png"#力量书+15

genxing3 = r"D:/python project/ppc/shuc/genxing3.png"#根性书+3
genxing7 = r"D:/python project/ppc/shuc/genxing7.png"#根性书+7
genxing15 = r"D:/python project/ppc/shuc/genxing15.png"#根性书+15

zhili3 = r"D:/python project/ppc/shuc/zhili3.png"#智力书+3
zhili7 = r"D:/python project/ppc/shuc/zhili7.png"#智力书+7
zhili15 = r"D:/python project/ppc/shuc/zhili3.png"#智力书+15

titie = r"D:/python project/ppc/shuc/titie.png"#比赛加成

shiyong = r"D:/python project/ppc/shuc/shiyong.png"#使用
shiyong2 = r"D:/python project/ppc/shuc/shiyong2.png"#使用2
likaishangdian = r"D:/python project/ppc/shuc/likaishangdian.png"#离开商店
huanwan = r"D:/python project/ppc/shuc/huanwan.png"#交换完

bisai = r"D:/python project/ppc/shuc/bisai.png"#比赛
ok = r"D:/python project/ppc/shuc/ok.png"#ok
chuzou = r"D:/python project/ppc/shuc/chuzou.png"#出走
jieguo = r"D:/python project/ppc/shuc/jieguo.png"#比赛结果
ci = r"D:/python project/ppc/shuc/ci.png"#次
ci2 = r"D:/python project/ppc/shuc/ci2.png"#次2

zhix = r"D:/python project/ppc/shuc/zhix.png"#支线
yinzi = r"D:/python project/ppc/shuc/yinzi.png"#因子继承
yuyue = r"D:/python project/ppc/shuc/yuyue.png"#预约
guanbi = r"D:/python project/ppc/shuc/guanbi.png"#关闭
tanchu = r"D:/python project/ppc/shuc/tanchu.png"#弹出
img_path = r"d:/a/xn.png"#截图保存位置
minMatch = 0.9 #最小相似度
devices = "9FK5T19430020327" #adb设备名
os.system("adb devices")
while(True):
    dabisai()
    zouzhixian()
    caigou()
