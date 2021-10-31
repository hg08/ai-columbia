# week 1. lecture 2  Applications of AI

Let us now talk about some of the state of the art applications in artificial intelligence.

So you could think of many of them, AI is not only compelling,

it actually touches many aspects of our lives.



The first application one can think of is speech recognition,

in which we have Virtual assistants such as **Siri from Apple**, **Echo from Amazon**,

Google Now, or **Cortana** from Microsoft.

They kind of help get things done such as sending an email,

making a doctor appointment, finding a restaurant,

order pizza, or an Uber car, tell you the weather, and many more.

So this kind of technology leverages (利用) deep neural networks to handle natural language

understanding as speech recognition.

We are making good progress in this area of research, it's not top yet but

we can still use them for simple queries.

They are doing performing pretty well.

But this remains in the research area for now.



A second popular application of artificial intelligence is hand writing recognition.

For the history, in the mid 90s, the USPS, US Postal Services got very interested

in automatically sorting handwritten addresses and zip codes on envelope.　

By the end of the 80s, Yann LeCun, who is an eminent researchers doing deep learning

and neural networks, has published a solution using neural networks to

recognize hand written digits on an envelope.

The same approach was adopted to

automatically recognize the digits on a check in ATM machines.

And hence the whole process of recognizing zip codes and

amounts of dollars on the check.

Checks were completely automated and

actually saved hundreds of millions of dollars to society.



A popular and　successful application of artificial intelligence is machine translation.

Machine translation actually existed since the beginning of artificial intelligence.

And the historical motivation is the US government actually wanting to translate

Russian text to English.

Unfortunately the first system using what we call mechanical translation or

one to one correspondence completely failed.

Here's an example drawn from the history of AI.

In which we have "out of sight,　out of mind" expression that got translated into French as "invisible,

imbecile" that actually completely changes the meaning of the expression.

Machine translation has gone through ups and downs in the literature and

many funding got cut after this kind of incidents that completely

mistranslated what you wanted, mistranslated the text.

Historically, machine translation has gone through lots of ups and

downs, cutting funding and so on and so forth.

Especially after this kind of mistranslations in　the Russian text specifically.

But today, machine translation became statistical, and　we talk about statistical machine translation

that leverages the vast amount of available translated corpuses.

So let's say online, we have access to a lot of texts from official governments and

also from let's say embassies, and

United Nations that publish texts both in English and other languages.

And this is a good quality text.

Translate that a text that could be, and was,　leveraged by machine translation systems.

While there is room for improvement,　machine translation has made significant progress and

we all use at some times online such as machine translation from Google translate.

That can handle today over 100 languages.

So if you plug in "out of sight, out of mind" one more time into the system,

you can see that the translation to French is much, much better and

is more faithful to the true meaning, true semantics of out of sight out of mind.

So huge progress has been made in machine translation today.



So another obvious application of artificial intelligence is **robotics**.

We know today of some robots such as **Nao**, and **Asimo**, you could here Asimo dancing,

but robotics has made a really important contributions and

important progress in the last years.

Robots can be important in may applications such as robotic surgery and

household keeping, and also navigation etc., etc.

So, there's a lot of progress on that front as well.



Another, and maybe unsuspected application of AI is **recommender Systems**.

So you know **Netflix recommendation systems**, **Amazon recommendation system**,

that leverages collaborative filtering, to look into the history

of your purchases and the history of other customers to make recommendations.

For example, if you buy this video game, then Amazon would suggest other

kinds of items such as customers who buy this item.

Item also bought may be a microphone or other kinds of games.

So this is actually at the core of recommender systems

to use another data and learn from it to make such recommendations.



Your **email system** is also enhanced with AI capabilities.

There's a spam filter in your email that actually helps

sort your emails as spam or non spam.

And **this AI system is actually learning from your own actions**,

when you **interact** with your emails you're teaching this system how to behave and

how to sort your emails.

So it leverages some techniques such as **naive Bayes' classifiers**.

And other kinds of classifiers to be able to classify your text or

your email text as a spam or non spam.

It could also leverage your existing emails to propose maybe some ads so

your email is also having some intelligence and

is using it to make your experience browsing your emails much better.



Another widely used and outstanding successful application

of artificial intelligence, is **face detection**.

So you'll all use some kind of smartphone to take pictures of our kids or

our family and friends.

Whenever we do that, we could see that, quickly, we have some things being detected here which are rectangles around the faces.

Doesn't go through the shirts or through the background.

There is an accurate and fast way to detect those faces on

the picture that is done by a method called the **Viola Johns**, named after

its inventors Paul Viola and Michael Johns who wrote the paper about this methodology

in a conference on computer vision and pattern recognition in 2001.

This has been of the most successful applications of AI.

The Viola Jones method detects and classifies images as having a face or

not based on a different features rather than pixels.

Instead of using pixels, the algorithm will use windows of 24x24 pixels.

to recognize whether there are different rectangle features in them.

So for example this is an example of a kind of rectangle feature

that actually can help identify the area of the eyes separated by

the area of the nose which is lighter in the middle.

Another possible feature could be the area of the eyes.

On the top and the area of the cheeks on the bottom.

So, we're going to have a sliding window of 24 by 24 pixels going through the image

and try to see whether these these features are exhibited this kind of,

what we call rectangle features are exhibited in this area in order

to be able to classify the images.

So the algorithm uses also **AdaBoost**, which is a machine learning algorithm that helps

to do classification in a boosting which we'll see in the next lectures.



Besides this presentation,

the algorithm also uses **boosting algorithms** and specifically the **Ada boost**

machine algorithm that allows to focus on the area of interest.

In which there is likely a face rather than the background, for example,

of the image.

It has been very successful to do that.

This method is very successful.

it fails sometimes when we have some problem with luminosity or orientation.

For example, this person here has a hat which covers most of the eyes and

part of the nose.

So the feature patterns that actually tries to identify different rectangles in the face fail.

And same thing for this person here that has his head little bit on the right side.

So but in general it's doing a great job, it is accurate and

fast and it's embarked in many face detection systems.



另一个领域：人脸识别(**face recognition**)AI取得了很好的进展.

人脸识别目前尚未完全解决,但已经有了非常大的进步．在人脸识别中， 我们的目标不只是探测出一张照片中是否有人脸，有多少人脸，更要识别出是谁的脸！　这很容易出错，因为光照不同，人的姿势(面部的表情，方位)不同等等！例如，有些时候他在笑，有些时候在哭！有时戴了眼镜，有时又没戴．有时转向左侧，有时候又转向右侧．有时照片上有雨点！　等等等．

变化因素太多了，极具挑战的领域．



Remaining in the vision topic of AI, there has been significant progress

in medical imaging such as **detection of breast cancer** and mammography images.

And many, many more applications that require.

Imaging of the body, the brain, and the bones.

Adversarial search or games represent an important part of AI.

Because it is challenging and because human has always wanted to create computer

programs or intelligent machines that play against humans.

An example is the chess game.

在1997年， **Gary Kasparov**, 国际象棋冠军被**Deep Blue**打败了．它是一台IBM 机器that was able to use and

leverage powerful search algorithms to win the game against Kasparov.

Another example is **Jeopardy**!

in 2011 in which a human plays against IBM Watson in Jeopardy!

And IBM Watson was the winner of the game and leveraged natural language

understanding and information extraction to answer the questions.

This is the first time where the machine that only used search algorithms and

used its computational powers against human.

It also used some natural language understanding of the questions and

digging into the resources online to get information and answer the questions.

And last remarkable event this year regarding AI and games is when **Lee Sedol**,

the world champion in "Go" which is in an ancient game,

was defeated by **Google AlphaGo**.

In the match in which Google AlphaGo won 4-1.

It leverages **deep learning**, **reinforcement learning**, and **search algorithms**

 to complete the search for the best moves, assuming that

here we have actually a complicated search problem because the branching factors, or

the number of possible moves exceeds 300.

So it's a complicated search problem for AI.

And yet AlphaGo leveraging a combination of these techniques,

was able to defeat the world champion in this area.



Last but not least in the series of AI applications, is **autonomous driving** or

self driving cars. 它成了长久以来的梦想．它现在正在变成现实．

It's personally my dream to get into a car, not worry about the commute time and

driving.

And just relax, have a cup of tea and read.

So the area is flourishing.

thanks to the advances in technology, in sensors, etc.

And it's also flourishing thanks to different challenges that were

done by DARPA.

It was the DARPA Grand Challenge in which a self driving cars has to drive

132 miles in 2005.

The winner was Stanford.

2007 it launched also the urban challenge which was even more challenging for

cars and it ended up with winners from CMU and

最终 Google自动驾驶车在2009年实现.

Where Google started Getting interested in self-driving cars and designing those.

So the dream is not far really,

I don't know how many decades we need to wait because there is a big change and

shift in our mindset and our thinking about how we interact with cars.

There is a lot of logistics and policy that needs to be looked at in order to

make this really happen, and switching to the self driving cars era.



I just went through a large number of AI applications.

They're actually, AI is all over the place, they're also other application that

actually I didn't talk about such as **fraud detection web search engine**,

社交网络分析, 蛋白质设计, 搜索路线，文档总结,交通调度，信息提取等等.

还有更多其他应用能提升AI的能力，从而使得我们的生活变得更好.

搜索引擎中的信息提取利用现存的数以亿计的网页，将那些查询者可能感兴趣的结果在一眨眼时间以一个排序呈现出来．　谷歌排序算法和其变体有广泛的应用.　它们构成了我们日常的基础，这是又一类AI应用．
