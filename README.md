### Visualising an Order Book using Python

Visualising order book data can be important for traders to understand the supply and demand of securities in the market in granular depth.

##### Why look at the order book?

The limit order book is the place where all buyers and sellers meet and where the auction takes place. It is basically the entire supply and demand. When we look at the order book, we see all the decisions of all the market participants and the strategies they employ. In contrast to looking at the volume traded, which shows what already happened, the order book provides an insight into the intention of the traders. This information can be used for forecasting short term price action.

Here are few examples of the type of information that can be gained by following and analyzing the order book:

Find price levels with Certain price levels attract large numbers of orders. These clusters can be identified only when looking at the depth of market. In many cases, these levels will act as support and resistance, depending on whether they are above or below the current price.
Watch the spread which can provide clues about what might happen in the immediate future.
Identify intraday shifts in momentum, for example a shift from strong buying to strong selling.
Price changes due to order book activity. Study the relationship between market price movements and the order
When using the depth of market we can also observe strategies in action, for example:

Price triggered strategies. Strategies that automatically change orders positions based on price change.
Validate breaks of key technical analysis levels and better assess if the breakout is real or false.
Identify when big players step
Identify retail

##### Why visualisation is important?

Visualization plays important role in understanding what is really happening and in taking better and more educated decisions. Looking at data in a pictorial or graphical format enables us to grasp difficult concepts with greater ease or identify patterns that are otherwise unobservable. It also helps us to ask questions we did not ask before.

As a result of technological advancement, visualization of big data is now possible. With current CPUs & GPUs visualization that in the past could have only be done offline, can now be achieved in real time. This in turn enables faster more relevant and beneficial decision making. When dealing with market data, I see the use of visualization in the following scenarios:

In early stages when cleaning and ‘checking’ the market data. In many cases wrong decisions are taken because the market data is not accurate, therefore, visualization should be considered at that
When developing a new strategy or refining an existing one. In other words, when ‘teaching the computer’ what to do. Looking at visualized market data can also be beneficial in getting new
When trading live and facing the need to take immediate
When monitoring / watching the market in real time and take decisions like: whether to trade or not in certain market conditions or even see that your strategy is ‘not aligned’ and needs to be

##### Looking at the microstructure

Each macro event is a combination of micro events. In many cases, if you manage to understand the microstructure, than you will be able to better understand the macro. The advantage to study the microstructure is that there are less events, and therefore it is easier to interpret the activity and intentions of market participants. The best way to learn the microstructure is by using visualization tools and zooming  to the basic blocks of the market data.

##### How we visualize the order book

We had to deal with this question when we developed HFT strategies. We wanted to better understand other types of market participants and also see what happens in the market when we send our orders. We decided to visualize the order book using a heatmap, which is updated very frequently (video­like 25­40 FPS). The heat map records and visualises every change in the order book by displaying it on a scale of gray shades. The brighter shades mark price levels with larger number of resting paper while darker shades mark areas of lower liquidity.

The heatmap gave us a clear view of how the entire limit order book and traded volume evolve over time enabling us to get faster and deeper insights into market dynamics. Let me explain it further. Regular charts, such as bar chart, are two dimensional, (price and time). When you use a heatmap you add another dimension so in this case it also let you see the historical sizes at each price/time. In addition, by updating the chart very frequently (40 updates / second) you get a video which lets you view also the frequency of the changes, giving you a ‘feel’ of market accelerations.


##### Below are a few questions that can be investigated with a visualization platform like Bookmap:

How did the size at each price level change over time?
What happened to a certain level when price moved toward it?
Are there additional strong levels below or above that level?
What was the volume traded around these levels?
What is the activity on the other side of the book? Are there areas where the order book is not symmetric?

[Wilmott - Order Book Visualization](https://wilmott.com/order-book-visualization/)

Plan to use the sample data available for free from [Lobster](https://lobsterdata.com/info/DataSamples.php)

##### Data:

The sample files inside [data](../data/ ) contain an 'orderbook' file, a 'message' file and a readme summarizing the data's properties. All sample files are based on the official NASDAQ Historical TotalView-ITCH sample.

| Name | Ticker | Level |
|--------|---------|-----|
|Amazon|AMZN|1|
|||5|
|||10|
|Apple|AAPL|1|
|||5|
|||10|
|Google|GOOG|1|
|||5|
|||10|
|Intel|INTC|1|
|||5|
|||10|
|Microsoft|MSFT|1|
|||5|
|||10|


More experienced researchers might be interested in higher level order books. The files provided below contain the limit order book evolution between 09:30:00 and 10:30:00 on the same day as the files above.

Apple:  AAPL  Levels: [30] [50]
Microsoft:  MSFT  Levels: [30] [50]
SPDR Trust Series I: SPY  Levels: [30] [50]
Please note that if there are unoccupied price levels in the requested price range, LOBSTER's output contains dummy variables to guarantee a symmetric output. Dummy variables are easily identified by a volume of 0.

More details on the sample data can be found here: [Sample Data](https://lobsterdata.com/info/DataSamples.php)


### Level 1 Market Data
Basic market data is known as Level I data. Level I market data provides all of the information needed to trade most chart-based trading systems. If trading using price action or indicator-based strategy, then Level I market data is all that is required. Level I data includes the following information:

1. Bid price: The highest posted price where someone is willing to buy an asset
2. Bid size: The number of shares, forex lots, or contracts that people are trying to buy at the bid price
3. Ask price: The lowest posted price where someone is willing to sell an asset. Also called the "offer price"
4. Ask size: The number of shares, forex lots, or contracts being sold at the ask price
5. Last price: The price at which the last transaction occurred
6. Last size: The number of shares, forex lots, or contracts involved in the last transaction