
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

# 链式调用
c = (
        Geo()
        .add_schema(maptype="china")
        # 加入自定义的点，格式为
        .add_coordinate("测试点", 116.39770014211535, 39.90779994986951)
        # 为自定义的点添加属性
        .add("geo", [("测试点", 51)])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="加入自定义的点"))
)
# 在 html(浏览器) 中渲染图表
c.render(r"WordVisual\\PyEcharts_geo.html")
