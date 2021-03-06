# nsd1902_devweb_day02

## CSS样式表

样式表的构成：

- 由多个样式规则构成
- 每个样式规则都有两个部分
  - 选择器
  - 样式声明

```html
body {
    font-size: 18px;
	font-weight: bold;
}

h1 {
	color: red;
}
```

## CSS样式表的特征

- 继承性：子元素继承父元素的样式
- 层叠性：多个选择器都选择到了同一元素，所有选择器样式规则都会生效
- 优先性：如果多个选择器用用于同一元素，有冲突的样式，根据相应的优先级生效

## CSS选择器

- 通用选择器：\*
- 元素选择器：html元素
- 类选择器：class，它将一组元素统一进行样式设置，样式表中class名前以英文句点开头。元素可以应用多个类，每个类中的样式都会生效，如果有冲突，样式表中后声明的样式生效。
- id选择器：在样式表中，以#开头
- 群组选择器：将多个选择器用逗号分开，对它们进行统一的样式设置
- 伪类选择器：一般都是为a标签进行设置，设置超链接在访问前、鼠标悬停、访问后时的样式。

## 颜色表示

RGB颜色，每种颜色都由1个字节来表示。某一颜色数值越大，表示越亮，数值越小越暗。

- Red
- Green
- Blue

## 盒子模型

一个元素所占宽度：外边距+边框厚度+内边距+元素宽度

## boostrap

它是twitter公司发布的一个开源前端框架，可以理解为它是一个写好的大样式表文件。样式表文件中预设了非常多的class，如果想要实现某种效果，只要把自己的元素设置相应的class属性即可。

http://bootcss.com  官方中文站

### 应用

将day01中的static目录拷贝到当前路径即可。static中已经有下载好的bootstrap。

bootstrap的颜色可以定义成以下几种：

- primary: 蓝
- info: 蓝
- danger: 红
- warning: 黄
- success: 绿
- muted: 灰

### form表单

- 为了各控件间有良好的间距，需要把它们分别放到form-group中
- 文字都放到label标签中
- 文本类型的input都需要设置form-control

### 栅格系统

- bootstrap把一行最多分成12列
- 每个组件，可以设定占多少列
- 使用时需要一个container容器，其他组件放到container中
- 每一行都用div.row来表示
- 其他的组件放到row中







