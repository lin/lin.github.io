---
# 这个目录只是 /2021/ 下的图片、CSV 等资源以及子页面的容器。
# 年份正文在 content/archives/2021.md，它的固定链接就是 /2021/，
# 所以这里必须关掉自动生成的 section 列表页，否则会和正文抢同一个地址
# （谁先谁后不确定，2004 和 2007 就是这样被列表页顶掉的）。
# publishResources 保证 /2021/xxx.jpg 这类资源照常输出。
build:
  render: never
  list: never
  publishResources: true
---
