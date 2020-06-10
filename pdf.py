import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import Color
from reportlab.platypus import Preformatted
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('fangsong', 'simfang.ttf'))
pdfmetrics.registerFont(TTFont('song', 'simsun.ttc'))
pdfmetrics.registerFont(TTFont('hei', 'msyh.ttc'))



# ************************  公共的页面参数  **********************************
PDF_PAGESIZE = (1920,1080)
COVER_BG = "CoverBg.jpg"
CONTENT_BG = "ContentBg.jpg"

# **************************  封面参数   ************************************
COVER_WATERMARKING_CONTENT =  "/ 沃朴物联商流数据统计报告"  # 字体内容   
COVER_WATERMARKING_POSITION = (160,892)
COVER_WATERMARKING_FONTSIZE = 20  # 字体大小
COVER_WATERMARKING_COLOR = (1, 1, 1)  # 字体颜色
COVER_WATERMARKING_OPACITY= 0.4   # 透明度
COVER_WATERMARKING_FONT = "hei"   #  微软雅黑

COVER_EN_CONTENT = "DATA STATISTICS"
COVER_EN_FONTSIZE = 80 # 大英文标题 字体
COVER_EN_POSITION = (160,730)
COVER_EN_COLOR = (1, 1, 1)  # 大英文标题字体颜色
COVER_EN_OPACITY= 0.4   # 透明度
COVER_EN_FONT = 'hei' # 大英文标题  字体大小


COVER_CH_CONTENT = "数据统计模块"
COVER_CH_FONTSIZE = 100 # 大汉语标题  字体
COVER_CH_POSITION = (160,590)
COVER_CH_COLOR = (1, 1, 1)  # 大汉语标题字体颜色
COVER_CH_OPACITY= 1   # 透明度
COVER_CH_FONT = 'hei'  # 大汉语标题  字体大小

COVER_CH_EN_MAPPING = {
    0:{
        "en":"Electronic Warranty Card List Module",  # 模块英文标题
        "ch":"电子质保卡列表模块",  # 模块中文标题
    },
    1:{
        "en":"营销红包参与用户模块",
        "ch":"Marketing Red Pack Participation User Module",
    },
    2:{
        "en":"验伪日志模块",
        "ch":"Pseudo-log Module",
    },
    3:{
        "en":"扫描日志模块",
        "ch":"Scan log Module",
    },
    4:{
        "en":"商品列表模块",
        "ch":"Product List Module",
    },
    5:{
        "en":"出货信息模块",
        "ch":"Shipping Information Module",
    },
    6:{
        "en":"会员列表模块",
        "ch":"Member List Module",
    },
    7:{
        "en":"积分明细模块",
        "ch":"Integral Detail Module",
    },
    8:{
        "en":"积分兑换-实体模块",
        "ch":"Point Redemption-Entity Module",
    },
    9:{
        "en":"积分兑换-红包模块",
        "ch":"Pointredemption-Red Pack Module",
    },
    10:{
        "en":"拼团订单模块",
        "ch":"Slicing Order Module",
    },

}

COVER_TIME_FONTSIZE = 20  # 时间戳字体大小
COVER_TIME_POSITION = (160,160)
COVER_TIME_COLOR = (1, 1, 1)   # 时间戳颜色
COVER_TIME_OPACITY=1   # 透明度
COVER_TIME_FONT = 'hei'  # 时间戳字体



# **************************   内容参数    ********************************
CONTENT_TITLE_CONTENT = '折线图'
CONTENT_TITLE_FONTSIZE = 60   #  图表标题的字体大小
CONTENT_TITLE_POSITION = (80,936)
CONTENT_TITLE_COLOR = (0.6, 0.6, 0.6)  #  图表标题的颜色
CONTENT_TITLE_OPACITY= 1   # 透明度
CONTENT_TITLE_FONT = 'hei'   #   图表标题的字体
 

# # 图表显示的是图片 暂不需要样式
# CONTENT_CHARTS_FONTSIZE = "20px"   # 图表显示的字体大小
# CONTENT_CHARTS_POSITION = ("left","top","425px","174px")
# CONTENT_CHARTS_COLOR =(0.6, 0.6, 0.6)   # 图表显示的颜色
# CONTENT_CHARTS_OPACITY= 1  # 透明度
# CONTENT_CHARTs_FONT = 'hei'  # 图表字体 
CONTENT_CHARTS_POSITION_LATITUDE = (260,352) 
CONTENT_CHARTS_SIZE_LATITUDE= (1660,611)
CONTENT_CHARTS_POSITION_LONGITUDE = (140,108) 
CONTENT_CHARTS_SIZE_LONGITUDE= (1380,816)



CONTENT_DESCRIPTION_BG_POSITION_LATITUDE = (0,128)  # 横向 纬度方向
CONTENT_DESCRIPTION_BG_SIZE_LATITUDE = (1920,197)  # 横向  纬度方向 

CONTENT_DESCRIPTION_BG_POSITION_LONGITUDE = (1520,0)  # 纵向 经度方向
CONTENT_DESCRIPTION_BG_SIZE_LONGITUDE = (400,1080)  # 纵向  经度方向 
CONTENT_DESCRIPTION_BG_COLOR = (0.93,0.93,0.93)  # 图表说明的颜色
CONTENT_DESCRIPTION_BG_OPACITY= 1   # 透明度


CONTENT_DESCRIPTION_CONTENT = '如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；' 
CONTENT_DESCRIPTION_FONTSIZE = 26 # 图表说明的字体大小  
CONTENT_DESCRIPTION_POSITION_LATITUDE = (80,168)
CONTENT_DESCRIPTION_SIZE_LATITUDE = (1760,110)
CONTENT_DESCRIPTION_POSITION_LONGITUDE = (1580,60)
CONTENT_DESCRIPTION_SIZE_LONGITUDE = (280,960)
CONTENT_DESCRIPTION_COLOR = (0.2,0.2,0.2)  # 图表说明的颜色
CONTENT_DESCRIPTION_OPACITY= 1   # 透明度
CONTENT_DESCRIPTION_FONT = "hei" # 图表字体
CONTENT_DESCRIPTION_ROWSPACING_LATITUDE = 36   # 横向行间距 
CONTENT_DESCRIPTION_ROWSPACING_LONGITUDE = 46   # 纵向行间距
CONTENT_DESCRIPTION_MAXLENGTH_LATITUDE = 68  # 横向最大字体行长度 
CONTENT_DESCRIPTION_MAXLENGTH_LONGITUDE = 10  # 最大字体行长度 

CONTENT_PAGE_FONTSIZE = 20  # 页码字体大小
CONTENT_PAGE_POSITION = (80,60)
CONTENT_PAGE_COLOR = (0.12,0,0.86)  # 页码颜色
CONTENT_PAGE_OPACITY= 1   # 透明度
CONTENT_PAGE_FONT = 'hei' # 页码字体
CONTENT_PAGE_PAGE = 2   # 默认页码


CONTENT_FOOTER_MODEL_CONTENT = '拼团订单模块'
CONTENT_FOOTER_MODEL_FONTSIZE = 20  # 页脚模块说明字体大小
CONTENT_FOOTER_MODEL_POSITION = (114,60)
CONTENT_FOOTER_MODEL_COLOR = (0.2,0.2,0.2)   # 页脚模块说明字体颜色
CONTENT_FOOTER_MODEL_OPACITY= 1   # 透明度
CONTENT_FOOTER_MODEL_FONT = 'hei'   # 页脚模块说明字体


CONTENT_FOOTER_WATERMARKING_CONTENT = '/ 沃朴物联商流数据统计报告'
CONTENT_FOOTER_WATERMARKING_FONTSIZE = 20  # 页脚水印说明字体大小
CONTENT_FOOTER_WATERMARKING_POSITION = (0,60)   # 0 表示不确定 是变动的
CONTENT_FOOTER_WATERMARKING_COLOR = (0.6, 0.6, 0.6)  # 页脚水印说明字体颜色
CONTENT_FOOTER_WATERMARKING_OPACITY= 1   # 透明度
CONTENT_FOOTER_WATERMARKING_FONT = 'hei'   # 页脚水印说明字体
CONTENT_FOOTER_WATERMARKING_INTERVAL = 10    # 距离上一个位置的间隔



def cover(c,cover_watermarking,cover_en_title,cover_ch_title,cover_timestamp):
    '''
    pdf封面
    :param c    reportlab convas 对象    object
    :param cover_watermarking  公司水印   str
    :param cover_en_title    英文标题   str
    :param cover_ch_title   中文标题   str
    :param cover_timestamp   生成的时间戳   str
    :return  c
    '''
    # 设置背景
    c.drawImage(COVER_BG,0,0,width=PDF_PAGESIZE[0],height=PDF_PAGESIZE[1],mask=None)
    # ************  设置水印  ***************
    # 设置字体以及大小 
    c.setFont(COVER_WATERMARKING_FONT, COVER_WATERMARKING_FONTSIZE)  
    # 指定填充颜色  
    c.setFillColorRGB(COVER_WATERMARKING_COLOR[0], COVER_WATERMARKING_COLOR[1], COVER_WATERMARKING_COLOR[2])
    # 设置透明度，1为不透明 
    c.setFillAlpha(COVER_WATERMARKING_OPACITY)  
    # 绘制水印
    c.drawString(COVER_WATERMARKING_POSITION[0], COVER_WATERMARKING_POSITION[1], cover_watermarking)
    # *************  设置英文标题  *******************
    # 设置字体以及大小
    c.setFont(COVER_EN_FONT, COVER_EN_FONTSIZE)  
    # 指定填充颜色  
    c.setFillColorRGB(COVER_EN_COLOR[0], COVER_EN_COLOR[1], COVER_EN_COLOR[2])
    # 设置透明度
    c.setFillAlpha(COVER_EN_OPACITY)
    # 绘制英文标题
    c.drawString(COVER_EN_POSITION[0], COVER_EN_POSITION[1], cover_en_title)
    # *************  设置中文标题  *******************
    # 设置字体以及大小
    c.setFont(COVER_CH_FONT, COVER_CH_FONTSIZE)  
    # 指定填充颜色  
    c.setFillColorRGB(COVER_CH_COLOR[0], COVER_CH_COLOR[1], COVER_CH_COLOR[2])
    # 设置透明度
    c.setFillAlpha(COVER_CH_OPACITY)
    # 绘制中文标题
    c.drawString(COVER_CH_POSITION[0], COVER_CH_POSITION[1], cover_ch_title)
    # *************  设置时间戳  *******************
    # 设置字体以及大小
    c.setFont(COVER_TIME_FONT, COVER_TIME_FONTSIZE)  
    # 指定填充颜色  
    c.setFillColorRGB(COVER_TIME_COLOR[0], COVER_TIME_COLOR[1], COVER_TIME_COLOR[2])
    # 设置透明度
    c.setFillAlpha(COVER_TIME_OPACITY)
    # 绘制中文标题
    c.drawString(COVER_TIME_POSITION[0], COVER_TIME_POSITION[1], cover_timestamp)
    return c 
    

def content_latitude(
    c,
    content_title=CONTENT_TITLE_CONTENT,
    content_description=CONTENT_DESCRIPTION_CONTENT,
    content_echart = 'lines.jpg',
    content_page=CONTENT_PAGE_PAGE,
    content_page_subtitle = CONTENT_FOOTER_MODEL_CONTENT,
    content_page_watermarking = CONTENT_FOOTER_WATERMARKING_CONTENT,
):
    '''
    生成pdf内容--横向文本  纬度方向
    :param c  reportlab canvas 对象  object 
    :param content_title   文本标题
    :param content_echart  插入图表的图片路径
    :param content_page     页脚  -- 页码
    :param content_page_subtitle  页脚  -- 副标题 一般与封面的中文名称保持一致
    :param content_page_watermarking  页脚 -- 水印 一般与封面的公司水印保持一致
    '''
    # **************  设置背景  **************
    # 设置图片的背景
    c.drawImage(CONTENT_BG,0,0,width=PDF_PAGESIZE[0],height=PDF_PAGESIZE[1],mask=None)
    # **************  设置标题  ********************
    # 设置标题字体
    c.setFont(CONTENT_TITLE_FONT,CONTENT_TITLE_FONTSIZE)
    # 填充颜色
    c.setFillColorRGB(CONTENT_TITLE_COLOR[0], CONTENT_TITLE_COLOR[1], CONTENT_TITLE_COLOR[2])
    # 设置透明度
    c.setFillAlpha(CONTENT_TITLE_OPACITY)  
    # 标题
    c.drawString(CONTENT_TITLE_POSITION[0],CONTENT_TITLE_POSITION[1],content_title)

    # **************  插入图表  ********************
    c.drawImage(
        content_echart,
        CONTENT_CHARTS_POSITION_LATITUDE[0],
        CONTENT_CHARTS_POSITION_LATITUDE[1],
        width=CONTENT_CHARTS_SIZE_LATITUDE[0],
        height=CONTENT_CHARTS_SIZE_LATITUDE[1],
        mask=None)
    # **************  图表说明背景  ********************
    # 填充颜色
    c.setFillColorRGB(CONTENT_DESCRIPTION_BG_COLOR[0],CONTENT_DESCRIPTION_BG_COLOR[1],CONTENT_DESCRIPTION_BG_COLOR[2])
    # 设置透明度
    c.setFillAlpha(CONTENT_DESCRIPTION_BG_OPACITY)
    # 画矩形框
    c.rect(
        CONTENT_DESCRIPTION_BG_POSITION_LATITUDE[0],
        CONTENT_DESCRIPTION_BG_POSITION_LATITUDE[1], 
        width = CONTENT_DESCRIPTION_BG_SIZE_LATITUDE[0], 
        height=CONTENT_DESCRIPTION_BG_SIZE_LATITUDE[1], 
        stroke=0, 
        fill=1
    )
    # **************  图表说明描述  *******************
    # 获取默认样式的字典对象
    styleSheet = getSampleStyleSheet()
    # 获取文本的样式
    style = styleSheet['BodyText']
    # 设置字体
    style.fontName = CONTENT_DESCRIPTION_FONT   # 字体
    # 设置字体大小
    style.fontSize = CONTENT_DESCRIPTION_FONTSIZE  # 字体大小
    # 设置行间距
    style.leading = CONTENT_DESCRIPTION_ROWSPACING_LATITUDE
    # 设置字体颜色
    style.textColor = CONTENT_DESCRIPTION_COLOR 
    # 官方文档提示 中文要有该参数
    style.wordWrap = 'CJK'    
    # 文本格式化
    p =Preformatted(content_description,style,maxLineLength=CONTENT_DESCRIPTION_MAXLENGTH_LATITUDE, newLineChars='')
    # 指定文本区域大小
    p.wrapOn(c,CONTENT_DESCRIPTION_SIZE_LATITUDE[0], CONTENT_DESCRIPTION_SIZE_LATITUDE[1])
    # 绘画在画布上
    p.drawOn(c, CONTENT_DESCRIPTION_POSITION_LATITUDE[0], CONTENT_DESCRIPTION_POSITION_LATITUDE[1])
    # **************  页脚---页码  *******************
    # 设置标题字体
    c.setFont(CONTENT_PAGE_FONT,CONTENT_PAGE_FONTSIZE)
    # 填充颜色
    c.setFillColorRGB(CONTENT_PAGE_COLOR[0], CONTENT_PAGE_COLOR[1], CONTENT_PAGE_COLOR[2])
    # 设置透明度
    c.setFillAlpha(CONTENT_PAGE_OPACITY)  
    # 标题
    c.drawString(CONTENT_PAGE_POSITION[0],CONTENT_PAGE_POSITION[1],str(content_page).zfill(2))
    # **************  页脚---模块  ******************* 
    # 设置标题字体
    c.setFont(CONTENT_FOOTER_MODEL_FONT,CONTENT_FOOTER_MODEL_FONTSIZE)
    # 填充颜色
    c.setFillColorRGB(CONTENT_FOOTER_MODEL_COLOR[0], CONTENT_FOOTER_MODEL_COLOR[1], CONTENT_FOOTER_MODEL_COLOR[2])
    # 设置透明度
    c.setFillAlpha(CONTENT_FOOTER_MODEL_OPACITY)  
    # 标题
    c.drawString(CONTENT_FOOTER_MODEL_POSITION[0],CONTENT_FOOTER_MODEL_POSITION[1],content_page_subtitle)
    # **************  页脚---水印  *******************
    # 设置标题字体
    c.setFont(CONTENT_FOOTER_WATERMARKING_FONT,CONTENT_FOOTER_WATERMARKING_FONTSIZE)
    # 填充颜色
    c.setFillColorRGB(CONTENT_FOOTER_WATERMARKING_COLOR[0], CONTENT_FOOTER_WATERMARKING_COLOR[1], CONTENT_FOOTER_WATERMARKING_COLOR[2])
    # 设置透明度
    c.setFillAlpha(CONTENT_FOOTER_WATERMARKING_OPACITY)  
    # 标题  前一个的位置+前一个的长度(字体个数*单字的像素点)+二者的间隔
    c.drawString( 
        (CONTENT_FOOTER_MODEL_POSITION[0] + len(content_page_subtitle)*CONTENT_FOOTER_WATERMARKING_FONTSIZE+CONTENT_FOOTER_WATERMARKING_INTERVAL),
        CONTENT_FOOTER_WATERMARKING_POSITION[1],
        content_page_watermarking
    )
    return c 



def content_longitude(
    c, 
    content_title=CONTENT_TITLE_CONTENT,
    content_description=CONTENT_DESCRIPTION_CONTENT,
    content_echart = 'map.jpg',
    content_page=CONTENT_PAGE_PAGE,
    content_page_subtitle = CONTENT_FOOTER_MODEL_CONTENT,
    content_page_watermarking = CONTENT_FOOTER_WATERMARKING_CONTENT,
):
    '''
    生成pdf内容--纵向文本  经度方向
    :param c  reportlab canvas 对象  object 
    :param content_title   文本标题
    :param content_description  文本描述 
    :param content_echart   插入图表的图片路径
    :param content_page     页脚  -- 页码
    :param content_page_subtitle  页脚  -- 副标题 一般与封面的中文名称保持一致
    :param content_page_watermarking  页脚 -- 水印 一般与封面的公司水印保持一致
    '''
    # c = canvas.Canvas("hello.pdf",pagesize=PDF_PAGESIZE)
    # **************  设置背景  **************
    # 设置图片的背景
    c.drawImage(CONTENT_BG,0,0,width=PDF_PAGESIZE[0],height=PDF_PAGESIZE[1],mask=None)
    # **************  设置标题  ********************
    # 设置标题字体
    c.setFont(CONTENT_TITLE_FONT,CONTENT_TITLE_FONTSIZE)
    # 填充颜色
    c.setFillColorRGB(CONTENT_TITLE_COLOR[0], CONTENT_TITLE_COLOR[1], CONTENT_TITLE_COLOR[2])
    # 设置透明度
    c.setFillAlpha(CONTENT_TITLE_OPACITY)  
    # 标题
    c.drawString(CONTENT_TITLE_POSITION[0],CONTENT_TITLE_POSITION[1],content_title)

    # **************  插入图表  ********************
    c.drawImage(
        content_echart,
        CONTENT_CHARTS_POSITION_LONGITUDE[0],
        CONTENT_CHARTS_POSITION_LONGITUDE[1],
        width=CONTENT_CHARTS_SIZE_LONGITUDE[0],
        height=CONTENT_CHARTS_SIZE_LONGITUDE[1],
        mask=None
    )
    # **************  图表说明背景  ********************
    # 填充颜色
    c.setFillColorRGB(CONTENT_DESCRIPTION_BG_COLOR[0],CONTENT_DESCRIPTION_BG_COLOR[1],CONTENT_DESCRIPTION_BG_COLOR[2])
    # 设置透明度
    c.setFillAlpha(CONTENT_DESCRIPTION_BG_OPACITY)
    # 画矩形框
    c.rect(
        CONTENT_DESCRIPTION_BG_POSITION_LONGITUDE[0],
        CONTENT_DESCRIPTION_BG_POSITION_LONGITUDE[1], 
        width = CONTENT_DESCRIPTION_BG_SIZE_LONGITUDE[0], 
        height=CONTENT_DESCRIPTION_BG_SIZE_LONGITUDE[1], 
        stroke=0, 
        fill=1
    )
    # **************  图表说明描述  *******************
    # 获取默认样式的字典对象
    styleSheet = getSampleStyleSheet()
    # 获取文本的样式
    style = styleSheet['BodyText']
    # 设置字体
    style.fontName = CONTENT_DESCRIPTION_FONT   # 字体
    # 设置字体大小
    style.fontSize = CONTENT_DESCRIPTION_FONTSIZE  # 字体大小
    # 设置行间距
    style.leading = CONTENT_DESCRIPTION_ROWSPACING_LONGITUDE
    # 设置字体颜色
    style.textColor = CONTENT_DESCRIPTION_COLOR 
    # 官方文档提示 中文要有该参数
    style.wordWrap = 'CJK'    
    # 文本格式化
    p =Preformatted(content_description,style,maxLineLength=CONTENT_DESCRIPTION_MAXLENGTH_LONGITUDE, newLineChars='')
    # 左下角为(0,0) 原点  所以纵向文本写入画布时会有问题 为了右上角对齐 
    # 纵坐标会根据文本的行数 而发生变动  变动的的纵坐标可以根据计算得出  
    # 文本域距下的像素 + 文本域空余的像素(文本域指定大小 - 根据文本行数计算而得的像素) =  写入文本的坐标位置
    # 行数间隔的像素 = 每行字的像素 + 行与行之间的空格的像素    
    t_px = len(p.lines)  * CONTENT_DESCRIPTION_ROWSPACING_LONGITUDE
    t_px = CONTENT_DESCRIPTION_POSITION_LONGITUDE[1] + 960 - t_px  if t_px <= 960 else CONTENT_DESCRIPTION_POSITION_LONGITUDE[1] 
    # 指定文本区域大小
    p.wrapOn(c,CONTENT_DESCRIPTION_SIZE_LONGITUDE[0], CONTENT_DESCRIPTION_SIZE_LONGITUDE[1])
    # 绘画在画布上
    p.drawOn(c, CONTENT_DESCRIPTION_POSITION_LONGITUDE[0], t_px)
    # **************  页脚---页码  *******************
    # 设置标题字体
    c.setFont(CONTENT_PAGE_FONT,CONTENT_PAGE_FONTSIZE)
    # 填充颜色
    c.setFillColorRGB(CONTENT_PAGE_COLOR[0], CONTENT_PAGE_COLOR[1], CONTENT_PAGE_COLOR[2])
    # 设置透明度
    c.setFillAlpha(CONTENT_PAGE_OPACITY)  
    # 标题
    c.drawString(CONTENT_PAGE_POSITION[0],CONTENT_PAGE_POSITION[1],str(content_page).zfill(2))
    # **************  页脚---模块  ******************* 
    # 设置标题字体
    c.setFont(CONTENT_FOOTER_MODEL_FONT,CONTENT_FOOTER_MODEL_FONTSIZE)
    # 填充颜色
    c.setFillColorRGB(CONTENT_FOOTER_MODEL_COLOR[0], CONTENT_FOOTER_MODEL_COLOR[1], CONTENT_FOOTER_MODEL_COLOR[2])
    # 设置透明度
    c.setFillAlpha(CONTENT_FOOTER_MODEL_OPACITY)  
    # 标题
    c.drawString(CONTENT_FOOTER_MODEL_POSITION[0],CONTENT_FOOTER_MODEL_POSITION[1],content_page_subtitle)
    # **************  页脚---水印  *******************
    # 设置标题字体
    c.setFont(CONTENT_FOOTER_WATERMARKING_FONT,CONTENT_FOOTER_WATERMARKING_FONTSIZE)
    # 填充颜色
    c.setFillColorRGB(CONTENT_FOOTER_WATERMARKING_COLOR[0], CONTENT_FOOTER_WATERMARKING_COLOR[1], CONTENT_FOOTER_WATERMARKING_COLOR[2])
    # 设置透明度
    c.setFillAlpha(CONTENT_FOOTER_WATERMARKING_OPACITY)  
    # 标题  前一个的位置+前一个的长度(字体个数*单字的像素点)+二者的间隔
    c.drawString( 
        (CONTENT_FOOTER_MODEL_POSITION[0] + len(content_page_subtitle)*CONTENT_FOOTER_WATERMARKING_FONTSIZE+CONTENT_FOOTER_WATERMARKING_INTERVAL),
        CONTENT_FOOTER_WATERMARKING_POSITION[1],
        content_page_watermarking
    )
    return c 




def build_pdf(
    path="temp.pdf",
    business_type = -1,
    content_latitudes = None,   
    content_longitudes = None
):
    '''
    生成pdf封面
    :param path   保存的文件路径
    :param business_type   业务类型  与前端配置的业务类型一致  参考数据导出 config.py 配置文件
    :param content_latitudes      图表图片路径以及图表描述说明 纬度  横向文本   类型   列表  [(title1,description1,image_path1),(titile2,description2,image_path2),]
    :param content_longitudes    图表图片路径以及图表描述说明 经度  纵向文本   类型   列表  [(title1,description1,image_path1),(titile2,description2,image_path2),]
    :return 
    '''
    c = canvas.Canvas(path,pagesize=PDF_PAGESIZE)

    business = COVER_CH_EN_MAPPING.get(business_type,None)
    if not business:
        return 
    cover_en_title = business.get('en',None) or COVER_EN_CONTENT
    cover_ch_title= business.get('ch',None) or COVER_CH_CONTENT
    cover_timestamp= datetime.datetime.now().strftime("%Y/%m/%d")
    # 封面
    c = cover(c,COVER_WATERMARKING_CONTENT,cover_en_title,cover_ch_title,cover_timestamp)
    # 画到画布上并翻页
    c.showPage()
    page_num = CONTENT_PAGE_PAGE
    for index,item in enumerate(content_latitudes):
        page_num += index if index == 0 else 1
        c = content_latitude(c,item[0],item[1],item[2],page_num,cover_ch_title,COVER_WATERMARKING_CONTENT)
        c.showPage() 
    if content_latitudes:
        page_num += 1 

    for index,item in enumerate(content_longitudes):
        page_num += index if index == 0 else 1 
        c = content_longitude(c,item[0],item[1],item[2],page_num,cover_ch_title,COVER_WATERMARKING_CONTENT)
        c.showPage() 
    # 保存文件
    c.save()




if __name__ == "__main__":

    content_latitudes = [
        ("折线图",'如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；','lines.jpg'),
        ("柱状图",'如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；','bar.jpg'),
        ("云图",'如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；','cloudword.jpg'),

    ]

    content_longitudes = [
        ("地图",'如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；如果有文字阐述的分析页，就插入这种样式，灰色背景的大小随着文字内容的多寡而不同；','map.jpg'),
    ]

    build_pdf(business_type=0,content_latitudes=content_latitudes,content_longitudes=content_longitudes)   
    pass 
    

    
