---
title: "一切从简"
date: 2015-07-09
---

> Skinny Everything

最重要的应该是readable，而不是cool或者为了简化而简化,你的目的是减少脑力消耗（思考量）

一切从简的好处:

**工程角度**: 减少程序的复杂度，减轻工作量（这是从数学角度，也就是计算量的缩减）

**商业角度**: 节约时间，降低成本（这是从神经科学角度，也就是工作量的减轻，大脑计算量的缩减）


数学角度：整体复合方式（模块化），抽象的方式。

工作量角度：工具化类比，图像化形象

一切从简的四个方法:

### 1. 避免反复解决那些反复出现的问题

#### 1, Don’t repeat yourself.

把出现多次的重复代码整理起来。

例子:

```ruby
# ==================================================================#
# ========== An example of making codes dry and skinny =============#
# ==================================================================#


# =============================================================== #
# ================== 1, Django's controller ===================== #
# =============================================================== #

def show
  product = Product.find params[:id]
  render 'products/show.html', variables: { product: product }
end

# ================================================================ #
# ================== 2, set default directory ==================== #
# ================================================================ #

# set default folder to 'products/', set default file extension to html
def show
  product = Product.find params[:id]
  render :show, variables: { product: product }
end

# ==================================================================== #
# ================== 3, remove variables argument ==================== #
# ==================================================================== #

# use instance variable instead of passing variables argument
def show
  @product = Product.find params[:id]
  render :show
end

# ======================================================= #
# ================== 4, use callback ==================== #
# ======================================================= #

# use before_action callback to do this repeated task.
before_action :set_product

def show
  # product = Product.find params[:id]
  render :show
end

def index
  # product = Product.find params[:id]
  render :index
end

def edit
  # product = Product.find params[:id]
  render :edit
end

private

def set_product
  @product = Product.find params[:id]
end

# ============================================================ #
# ================== 5, use function name ==================== #
# ============================================================ #

# use function name (show) to call render method
def show
end

# ============================================================ #

# THE END: write nothing
# Note: This is the rails way to deal with normal controller actions.
```

极端的假设：如果一段代码，需要你反复写一千次，你会怎么减轻自己重复敲代码（甚至是重复思考和解决）的痛苦。

更多例子：

1，[Array counting](https://github.com/linyingkui/skinny/blob/master/generalize/count.rb)

2，[jQuery selector](https://github.com/linyingkui/skinny/blob/master/generalize/jquery.coffee)

#### 2, Convention over configuration.

把大多数人在大多数情况下所采取的设置，定为默认设置。

例如，自动生成数据库里table的名字：

```ruby
# ===================================================== #
# ================== Configuration ==================== #
# ===================================================== #

# models/user.rb
User.DATABASE_TABLE_NAME     = "users"

# models/post.rb
Post.DATABASE_TABLE_NAME     = "posts"

# models/product.rb
Product.DATABASE_TABLE_NAME = "products"

# ================================================== #
# ================== Convention ==================== #
# ================================================== #

# models/base.rb
BaseModel.DATABASE_TABLE_NAME= self.class.name.pluralize.lower
```

#### 3, 抽象出一个处理通用逻辑的基类 （特殊的DRY）

例如，[一个RESTful API的基类](https://blog.codelation.com/rails-restful-api-just-add-water/)：

```ruby
class API::BaseController

  def create
    create_resource(params)
    render :show, status: :created
  end

  def read
    @resource = resource_class.find params[:id]
    render :show
  end

  def update
    @resource = resource_class.find params[:id]
    @resource.update params
    render :show
  end

  def destroy
    @resource.destroy
    render :no_content
  end

end
```

### 2. 把问题归类成相互独立的几部分，各司其职

#### 1, 函数要短，最好五行以内，尽量不超过20行

把程序分解成函数主要有三个目的：

1，反复使用相同的逻辑，也就是第一节讨论的话题

2，提高逻辑的抽象等级(raise the level of abstraction)，以便更好的理解

如果一个函数里有多个等级的逻辑混杂在一起，就会使得程序更加难以理解（受到污染，变得不纯净）

3，把复杂的问题切割成更好处理的小块，也就是第三节将要讨论的话题

这样做的好处是，便于程序的理解、测试、debug以及保养

====

在一个函数里，应该：

1，只表述有别于其他任何函数的逻辑

2，只表述同一层面的逻辑

3，只做一件事，并把它做好

====

举例说明，一个要把大象装冰箱的函数

```ruby
# ================================================== #
# ================== Fat Codes ===================== #
# ================================================== #
def put_elephant_into_fridge
  # open
  @user.hand.hold @fridge.door
  @user.hand.pull "10cm"
  @user.hand.clear
  # put
  @user.hand.hold @elephant
  @user.hand.up "30cm"
  @user.body.move "forward", by: "30cm"
  @user.hand.down "30cm"
  @user.hand.clear
  # close
  @user.hand.hold @fridge.door
  @user.hand.push "10cm"
  @user.hand.clear
end

# ======================================================= #
# ================== Polluted Codes ===================== #
# ======================================================= #

def put_elephant_into_fridge
  # open
  @user.hand.hold @fridge.door
  @user.hand.pull "10cm"
  @user.hand.clear
  # put
  @user.put @elephant, into: @fridge
  # close
  @user.hand.hold @fridge.door
  @user.hand.push "10cm"
  @user.hand.clear
end

# ===================================================== #
# ================== Skinny Codes ===================== #
# ===================================================== #
# this is super easy to understand,
# it only has three lines, each line means a clear step
def put_elephant_into_fridge
  @user.open_door @fridge.door
  @user.put @elephant, into: @fridge
  @user.close_door @fridge.door
end

# ===================================================== #
# ================== Better Codes ===================== #
# ===================================================== #

# open/close fridge is a common task.
# this piece of logic is shared by multiple functions.
# so it should have its own function.
# by this way, we reduced 11 lines to one line.

def put_elephant_into_fridge
  operate_fridge { |user, fridge| user.put @elephant, into: fridge }
end

def grab_coke_from_fridge
  operate_fridge { |user, fridge| user.grab @coke, from: fridge }
end

def operate_fridge &block
  @user.open @fridge.door
  block.call @user, @fridge
  @user.close @fridge.door
end
```
#### 2, 一个类要短，并且只做一类事

类所要追从的是[Single Responsibility Principle](https://github.com/linyingkui/skinny/blob/master/split-responsibilities/srp.pdf), 也就是说：

"There should never be more than one reason for a class to change."

更直接的，一个类只做一类事，多了不干。木匠做家具，瓦匠砌墙。

举例说明， 比如在一个卖地皮的网站上，要标注面积和价格信息

```javascript
/*
  # ================================================== #
  # ================== Fat Codes ===================== #
  # ================================================== #
*/
square_sides_length = 20
price_in_cents = 3000

console.log("Area: " + square_sides_length ** 2)
console.log("Price: " + "$" + (price_in_cents / 100).toFixed(2))


/*
  # ===================================================== #
  # ================== Skinny Codes ===================== #
  # ===================================================== #
*/
square_sides_length = 20
price_in_cents = 3000

console.log("Area: "  +  Math.Square.calculate_area(square_sides_length));
console.log("Price: " +  Currency.cents_to_string(price_in_cents));
```

第一个方案的职责是输出数值，但它又承担了计算正方形面积和生成货币字符的任务.

第一个方案虽然比较快，但是污染了类的职责，其主要弊端在于:

不便于理解程序，在这个层面上，程序员只需要知道这是在计算面积，而无需理解计算面积的方式.

#### 3, 宏观的模块化，每一大块负责一个具体的任务

不在一个文件里处理两个模块的问题，彻底把责任分开。例如，在html里：
```html

<!--
  # ================================================== #
  # ================== Fat Codes ===================== #
  # ================================================== #
-->
<!-- it has too much responsibilities, 3 rather than 1 -->
<div class="post" style="background-color: red" onclick="sayHello()"></div>

<!--
  # ===================================================== #
  # ================== Skinny Codes ===================== #
  # ===================================================== #
-->
<!-- post.html  -->
<div class="post"></div>

<!-- post.css  -->
.post {
  background-color: red
}

<!-- post.js  -->
$(".post").click(function(){sayHello()});
```
两个更加具体的例子：

1，[Model-View-Controller](https://github.com/linyingkui/skinny/blob/master/split-responsibilities/mvc.rb)

2，[HTML-CSS-JavaScript](https://github.com/linyingkui/skinny/blob/master/split-responsibilities/hcj.coffee)

#### 4, 任何包含逻辑的文件都应该短，任何文件夹（根目录下）里的文件也应该少

任何手工写的文件，或是要人读的文件都应该非常简短，**最好限制在200行以内**。

这样其他人阅读的时候可以减少压力感(avoid overwhelming feeling)，提高理解程序的效率。

Less is more，写的短，往往意味着写的精简，不罗嗦，不重复。

除了单一文件外，文件夹根目录下的文件数量也要少（不多于10个？）.

只把最核心的文件放在根目录下，其他的文件分类整理到文件夹里，这样便于其他人阅读和查找。

### 3. 把问题细化成较为简单的小问题，逐个突破

这是最简单的一个原则.

#### 1, 把特别长的文件，切割成多个短小的文件。例如，

一个网页的主页有三个部分，把三个部分的逻辑分别放到不同的文件：

```ruby
views/
  ├── home/
  |   ├── hero.html
  |   ├── how-it-works.html
  |   └── press.html
  └── home.html
```

#### 2, 把包含特别多文件的文件夹，整理到少数几个文件夹里，例如

把放字体的文件夹整理起来：

```ruby
# ================================================== #
# ================== Fat Codes ===================== #
# ================================================== #
fonts/
  ├── futurastd-condensed-webfont.woff
  ├── futurastd-condensedbold-webfont.woff
  ├── futurastd-condensedboldobl-webfont.woff
  ├── proximanova-bold-webfont.woff
  ├── proximanova-light-webfont.woff
  ├── proximanova-semibold-webfont.woff
  ├── proximanova-regular-webfont.woff
  ├── raleway-bold.woff
  └── raleway-regular.woff

# ===================================================== #
# ================== Skinny Codes ===================== #
# ===================================================== #
fonts/
  ├── futurastd-condensed/
  |   ├── futurastd-condensed-webfont.woff
  |   ├── futurastd-condensedbold-webfont.woff
  |   └── futurastd-condensedboldobl-webfont.woff
  ├── proximanova/
  |   ├── proximanova-bold-webfont.woff
  |   ├── proximanova-light-webfont.woff
  |   ├── proximanova-semibold-webfont.woff
  |   └── proximanova-regular-webfont.woff
  └── raleway/
      ├── raleway-bold.woff
      └── raleway-regular.woff
```

在写这个文章的过程中，为了更好的放置不同的文件夹，我设计了一个针对GUI的框架(framework)：

#### Scenarios based framework for GUI softwares

### Scenarios based framework for GUI softwares

这个框架方案的理念就是：把写程序当成是按照剧本（设计图稿）拍电影

Scenario指的是场景，Scene指的是场景里的一个画面

为什么会出现scenario？是因为数据的相似性，也就是信息出现的频率，还是计算缩减的一部分。

计算缩减包括了完整信息的缩减，也包括了模糊信息的缩减（所谓模糊就是指的，信息的外延，变形，但是变得不是很大）

接下来举例说明。

这个是程序主目录的列表，（借鉴Rails的设计）

```
twitter/
  ├── app/
  ├── bin/
  ├── config/
  ├── lib/
  ├── log/
  ├── test/
  └── vendor/
```

其中，`app`是和这个软件直接相关的逻辑

在`app`文件夹里：

```
app/
  ├── models/
  ├── controllers/
  ├── helpers/
  └── views/
```

按照MVVMC的设计理念分为四个部分，其中`helpers`就是View Model（把view里重复的逻辑放到helpers里）

在`model`文件夹里：

```
models/
  ├── generic/
  ├── vendor/
  |   ├── stripe.rb
  |   ├── shopify.rb
  |   └── instagram.rb
  ├── user/
  ├── product/
  |   ├── properties.rb
  |   ├── relationships.rb
  |   └── callbacks.rb
  ├── user.rb
  └── product.rb
```

值得注意的是：1，把一个大的class分解成小的部分，2，把相近的model归纳到一个文件夹里

**接下来进入主题**，

对于与views相关的：view，controller和helper，它们都是按照scenarios的不同来建立文件夹。

其中generic就是多个scenarios共用的逻辑。

```
app/
  ├── models/
  ├── controllers/
  |   ├── generic/
  |   ├── auth/
  |   ├── checkout/
  |   └── site/
  ├── helpers/
  |   ├── generic/
  |   ├── auth/
  |   ├── checkout/
  |   └── site/
  └── views/
      ├── generic/
      |   ├── styles/
      |   ├── events/
      |   ├── layouts/
      |   └── scenes/
      ├── auth/
      ├── checkout/
      └── site/
          ├── styles/
          ├── events/
          ├── layouts/
          └── scenes/
              ├── home/
              |   ├── hero.html
              |   ├── how-it-works.html
              |   └── press.html
              ├── home.html
              ├── about-us.html
              └── contact.html
```

这样整理的优点在于：

1，Consistency is king。这样的结构相对比较清晰，便于理解和查找逻辑

2，同一场景里的多个画面，许多设计元素以及需要处理的动作是非常接近的（甚至是一致的）

应该说，正因为这些设计元素和需要处理的动作非常接近，我们才归纳这些画面为一个场景

3，用户操作时，同一场景的多个画面是连续的，有利于将程序切割成相互独立、关联性较小的模块

### 4. 突出重点，消除杂音

====

这个原则的目的是，降低阅读程序的压力，用简短清晰的符号来表达逻辑。

也就是，Reduce learning time, Remove distractions, Avoid stress.

晕头假设：假设你现在比较迷糊，却要在短时间理解一个程序，如何才能让这时的你更好的理解程序

====

#### 1，同一等级的逻辑占用同样行数的代码，最好都是一行，例如:

```ruby
# clear way
checkout: ->
  if order.charge.
    send_order_email.
    success_alert "You are awesome!"
  else
    error_alert "Error!"

# distracting way
checkout: ->
  if order.charge.
    send_order_email.
    AlertViewController.presentAlert
      self,
      title: "Success"
      message: "You are awesome!"
      actions: ["close"]
  else
    AlertViewController.presentAlert
      self,
      title: "Error"
      message: "Error!"
      actions: ["close"]
```

第二个策略的问题在于，喧宾夺主，alert并不是逻辑主要解决的问题，却要抢夺大量的注意力。

===

#### 2，在不引起歧义的前提下，尽量减少字符数（对常用函数，使用4-7个字符的单一单词最佳）

例如:

```ruby
# clean
UserMail.welcome(current_user).deliver

# verbose
MSEmailController.SendEmailMessage(currentUser.emailAddress,
                                   withTemplateNamed: “welcome”,
                                   withLocalVariables: { user:  currentUser })

# ugly
mail = MSMail.new

mail.addTo(currentUser.emailAddress)
mail.setSubject('Welcome to Our Site')

template = MSTemplate.new(locateTemplate('includes/mail/user-welcome.php'))
template.setVar('userName', $currentUser.name)
bodyStr = template.render

mail.setHTMLBody(bodyStr)

mail.send
```

最后一个方案的问题还在于：没有把责任分担给其他的类。

在这个场景下，唯一要表达的信息就是”给用户发一封欢迎邮件“，具体怎么发的（尤其是发邮件的逻辑），那是其他类需要解决的问题。

#### 3，选择或设计一个减少键盘敲击的编程语言

例如：python, ruby，scala, coffeescript

### 结束语

### 结束语

写程序的时候，无需从一开始就严格的按照简洁的方法写，而是先想着实现，然后再整理 (Make it work, then make it better)。也就是，

第一步：Get it to work - 第二步：Make it skinny

第一步的快感是实现目标的成就感，目的是做出雏形。第二步的快感是清晰简洁的美感，目的是成品上市。

#### 2018年更新：

1，笨拙实现。通过穷举的方式，以最为笨拙的方式进行实现，也就是在最底层的方式，混乱的，每一个concern纠缠的形式实现

而且我推荐初学者如此去做（当然也要掌握好分寸，既不能让初学者丧失了解决问题的乐趣，又不能让人失去了解决底层问题的能力）

2，分块整理。把各个concern通过文件或者文件夹的方式割裂开来，让每一个文件尽可能的小一些，所知道的信息少一些，以便于区分职能，各个突破。

3，减少重复。DYI的过程，把重复出现的信息用一个函数也好，把大家约定俗成的用一个函数实现

但是问题是：不要过分的依赖DYI，因为不仅仅是计算量的减少，还要兼顾工作量的减少，也是就说，要考虑到人的因素。

如果DYI不能显著的增加计算量，却使得工作量，无论是新人（自己长时间不看，也算新人）的学习，或者是文档的数量，都变得更加长和抽象，那人理解起来的时间增加，那么在工程上，就增加了工作累，毕竟人是程序员，而不是机器编程，故而，要必要时缩减。

4，避免 magic number。定义一个变量，而不是定义一个奇怪的突兀的数字，这个的好处在于，人的因素，大家思考问题的时间减少了，让人一目了然，清晰明了，也是节约了工作量
