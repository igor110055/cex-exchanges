# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.base.exchange import Exchange
import hashlib
import math
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import PermissionDenied
from ccxt.base.errors import ArgumentsRequired
from ccxt.base.errors import AddressPending
from ccxt.base.errors import NotSupported
from ccxt.base.precise import Precise


class buda(Exchange):

    def describe(self):
        return self.deep_extend(super(buda, self).describe(), {
            'id': 'buda',
            'name': 'Buda',
            'countries': ['AR', 'CL', 'CO', 'PE'],
            'rateLimit': 1000,
            'version': 'v2',
            'has': {
                'CORS': None,
                'spot': True,
                'margin': False,
                'swap': False,
                'future': False,
                'option': False,
                'addMargin': False,
                'cancelOrder': True,
                'createDepositAddress': True,
                'createOrder': True,
                'createReduceOnlyOrder': False,
                'fetchBalance': True,
                'fetchBorrowRate': False,
                'fetchBorrowRateHistories': False,
                'fetchBorrowRateHistory': False,
                'fetchBorrowRates': False,
                'fetchBorrowRatesPerSymbol': False,
                'fetchClosedOrders': True,
                'fetchCurrencies': True,
                'fetchDepositAddress': True,
                'fetchDeposits': True,
                'fetchFundingHistory': False,
                'fetchFundingRate': False,
                'fetchFundingRateHistory': False,
                'fetchFundingRates': False,
                'fetchIndexOHLCV': False,
                'fetchLeverage': False,
                'fetchMarkets': True,
                'fetchMarkOHLCV': False,
                'fetchMyTrades': None,
                'fetchOHLCV': True,
                'fetchOpenInterestHistory': False,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchOrders': True,
                'fetchPosition': False,
                'fetchPositions': False,
                'fetchPositionsRisk': False,
                'fetchPremiumIndexOHLCV': False,
                'fetchTicker': True,
                'fetchTrades': True,
                'fetchTradingFee': False,
                'fetchTradingFees': False,
                'fetchTransactionFees': True,
                'fetchTransfer': False,
                'fetchTransfers': False,
                'fetchWithdrawal': False,
                'fetchWithdrawals': True,
                'reduceMargin': False,
                'setLeverage': False,
                'setMarginMode': False,
                'setPositionMode': False,
                'transfer': False,
                'withdraw': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/47380619-8a029200-d706-11e8-91e0-8a391fe48de3.jpg',
                'api': 'https://www.buda.com/api',
                'www': 'https://www.buda.com',
                'doc': 'https://api.buda.com',
                'fees': 'https://www.buda.com/comisiones',
            },
            'status': {
                'status': 'error',
                'updated': None,
                'eta': None,
                'url': None,
            },
            'api': {
                'public': {
                    'get': [
                        'pairs',
                        'markets',
                        'currencies',
                        'markets/{market}',
                        'markets/{market}/ticker',
                        'markets/{market}/volume',
                        'markets/{market}/order_book',
                        'markets/{market}/trades',
                        'currencies/{currency}/fees/deposit',
                        'currencies/{currency}/fees/withdrawal',
                        'tv/history',
                    ],
                    'post': [
                        'markets/{market}/quotations',
                    ],
                },
                'private': {
                    'get': [
                        'balances',
                        'balances/{currency}',
                        'currencies/{currency}/balances',
                        'orders',
                        'orders/{id}',
                        'markets/{market}/orders',
                        'deposits',
                        'currencies/{currency}/deposits',
                        'withdrawals',
                        'currencies/{currency}/withdrawals',
                        'currencies/{currency}/receive_addresses',
                        'currencies/{currency}/receive_addresses/{id}',
                    ],
                    'post': [
                        'markets/{market}/orders',
                        'currencies/{currency}/deposits',
                        'currencies/{currency}/withdrawals',
                        'currencies/{currency}/simulated_withdrawals',
                        'currencies/{currency}/receive_addresses',
                    ],
                    'put': [
                        'orders/{id}',
                    ],
                },
            },
            'timeframes': {
                '1m': '1',
                '5m': '5',
                '30m': '30',
                '1h': '60',
                '2h': '120',
                '1d': 'D',
                '1w': 'W',
            },
            'fees': {
                'trading': {
                    'tierBased': True,
                    'percentage': True,
                    'taker': 0.008,  # 0.8%
                    'maker': 0.004,  # 0.4%
                    'tiers': {
                        'taker': [
                            [0, 0.008],  # 0.8%
                            [2000, 0.007],  # 0.7%
                            [20000, 0.006],  # 0.6%
                            [100000, 0.005],  # 0.5%
                            [500000, 0.004],  # 0.4%
                            [2500000, 0.003],  # 0.3%
                            [12500000, 0.002],  # 0.2%
                        ],
                        'maker': [
                            [0, 0.004],  # 0.4%
                            [2000, 0.0035],  # 0.35%
                            [20000, 0.003],  # 0.3%
                            [100000, 0.0025],  # 0.25%
                            [500000, 0.002],  # 0.2%
                            [2500000, 0.0015],  # 0.15%
                            [12500000, 0.001],  # 0.1%
                        ],
                    },
                },
            },
            'exceptions': {
                'not_authorized': AuthenticationError,  # {message: 'Invalid credentials', code: 'not_authorized'}
                'forbidden': PermissionDenied,  # {message: 'You dont have access to self resource', code: 'forbidden'}
                'invalid_record': ExchangeError,  # {message: 'Validation Failed', code: 'invalid_record', errors: []}
                'not_found': ExchangeError,  # {message: 'Not found', code: 'not_found'}
                'parameter_missing': ExchangeError,  # {message: 'Parameter missing', code: 'parameter_missing'}
                'bad_parameter': ExchangeError,  # {message: 'Bad Parameter format', code: 'bad_parameter'}
            },
        })

    async def fetch_currency_info(self, currency, currencies=None):
        if not currencies:
            response = await self.publicGetCurrencies()
            #
            #     {
            #         "currencies":[
            #             {
            #                 "id":"BTC",
            #                 "symbol":"฿",
            #                 "managed":true,
            #                 "input_decimals":8,
            #                 "display_decimals":8,
            #                 "timezone":"UTC",
            #                 "deposit_minimum":["0.0","BTC"],
            #                 "withdrawal_minimum":["0.00001","BTC"],
            #                 "max_digits_for_decimals":6,
            #                 "crypto":true,
            #                 "address_explorer":"https://blockchair.com/bitcoin/address/",
            #                 "tx_explorer":"https://blockchair.com/bitcoin/transaction/",
            #                 "amount_to_micro_multiplier":1000000000000
            #             }
            #         ]
            #     }
            #
            currencies = self.safe_value(response, 'currencies')
        for i in range(0, len(currencies)):
            currencyInfo = currencies[i]
            if currencyInfo['id'] == currency:
                return currencyInfo
        return None

    async def fetch_markets(self, params={}):
        """
        retrieves data on all markets for buda
        :param dict params: extra parameters specific to the exchange api endpoint
        :returns [dict]: an array of objects representing market data
        """
        marketsResponse = await self.publicGetMarkets(params)
        markets = self.safe_value(marketsResponse, 'markets', [])
        currenciesResponse = await self.publicGetCurrencies()
        currencies = self.safe_value(currenciesResponse, 'currencies')
        result = []
        for i in range(0, len(markets)):
            market = markets[i]
            baseId = self.safe_string(market, 'base_currency')
            quoteId = self.safe_string(market, 'quote_currency')
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            baseInfo = await self.fetch_currency_info(baseId, currencies)
            quoteInfo = await self.fetch_currency_info(quoteId, currencies)
            pricePrecisionString = self.safe_string(quoteInfo, 'input_decimals')
            minimumOrderAmount = self.safe_value(market, 'minimum_order_amount', [])
            result.append({
                'id': self.safe_string(market, 'id'),
                'symbol': base + '/' + quote,
                'base': base,
                'quote': quote,
                'settle': None,
                'baseId': baseId,
                'quoteId': quoteId,
                'settleId': None,
                'type': 'spot',
                'spot': True,
                'margin': False,
                'swap': False,
                'future': False,
                'option': False,
                'active': True,
                'contract': False,
                'linear': None,
                'inverse': None,
                'contractSize': None,
                'expiry': None,
                'expiryDatetime': None,
                'strike': None,
                'optionType': None,
                'precision': {
                    'amount': self.safe_integer(baseInfo, 'input_decimals'),
                    'price': int(pricePrecisionString),
                },
                'limits': {
                    'leverage': {
                        'min': None,
                        'max': None,
                    },
                    'amount': {
                        'min': self.safe_number(minimumOrderAmount, 0),
                        'max': None,
                    },
                    'price': {
                        'min': None,
                        'max': None,
                    },
                    'cost': {
                        'min': None,
                        'max': None,
                    },
                },
                'info': market,
            })
        return result

    async def fetch_currencies(self, params={}):
        """
        fetches all available currencies on an exchange
        :param dict params: extra parameters specific to the buda api endpoint
        :returns dict: an associative dictionary of currencies
        """
        response = await self.publicGetCurrencies()
        #
        #     {
        #         "currencies":[
        #             {
        #                 "id":"BTC",
        #                 "symbol":"฿",
        #                 "managed":true,
        #                 "input_decimals":8,
        #                 "display_decimals":8,
        #                 "timezone":"UTC",
        #                 "deposit_minimum":["0.0","BTC"],
        #                 "withdrawal_minimum":["0.00001","BTC"],
        #                 "max_digits_for_decimals":6,
        #                 "crypto":true,
        #                 "address_explorer":"https://blockchair.com/bitcoin/address/",
        #                 "tx_explorer":"https://blockchair.com/bitcoin/transaction/",
        #                 "amount_to_micro_multiplier":1000000000000
        #             }
        #         ]
        #     }
        #
        currencies = response['currencies']
        result = {}
        for i in range(0, len(currencies)):
            currency = currencies[i]
            managed = self.safe_value(currency, 'managed', False)
            if not managed:
                continue
            id = self.safe_string(currency, 'id')
            code = self.safe_currency_code(id)
            precision = self.safe_number(currency, 'input_decimals')
            minimum = math.pow(10, -precision)
            depositMinimum = self.safe_value(currency, 'deposit_minimum', [])
            withdrawalMinimum = self.safe_value(currency, 'withdrawal_minimum', [])
            minDeposit = self.safe_number(depositMinimum, 0)
            minWithdraw = self.safe_number(withdrawalMinimum, 0)
            result[code] = {
                'id': id,
                'code': code,
                'info': currency,
                'name': None,
                'active': True,
                'deposit': None,
                'withdraw': None,
                'fee': None,
                'precision': precision,
                'limits': {
                    'amount': {
                        'min': minimum,
                        'max': None,
                    },
                    'deposit': {
                        'min': minDeposit,
                        'max': None,
                    },
                    'withdraw': {
                        'min': minWithdraw,
                    },
                },
            }
        return result

    async def fetch_transaction_fees(self, codes=None, params={}):
        #  by default it will try load withdrawal fees of all currencies(with separate requests)
        #  however if you define codes = ['ETH', 'BTC'] in args it will only load those
        await self.load_markets()
        withdrawFees = {}
        depositFees = {}
        info = {}
        if codes is None:
            codes = list(self.currencies.keys())
        for i in range(0, len(codes)):
            code = codes[i]
            currency = self.currency(code)
            request = {'currency': currency['id']}
            withdrawResponse = await self.publicGetCurrenciesCurrencyFeesWithdrawal(request)
            depositResponse = await self.publicGetCurrenciesCurrencyFeesDeposit(request)
            withdrawFees[code] = self.parse_funding_fee(withdrawResponse['fee'])
            depositFees[code] = self.parse_funding_fee(depositResponse['fee'])
            info[code] = {
                'withdraw': withdrawResponse,
                'deposit': depositResponse,
            }
        return {
            'withdraw': withdrawFees,
            'deposit': depositFees,
            'info': info,
        }

    def parse_funding_fee(self, fee, type=None):
        if type is None:
            type = fee['name']
        if type == 'withdrawal':
            type = 'withdraw'
        return {
            'type': type,
            'currency': fee['base'][1],
            'rate': fee['percent'],
            'cost': float(fee['base'][0]),
        }

    async def fetch_ticker(self, symbol, params={}):
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict params: extra parameters specific to the buda api endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/en/latest/manual.html#ticker-structure>`
        """
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'market': market['id'],
        }
        response = await self.publicGetMarketsMarketTicker(self.extend(request, params))
        #
        #     {
        #         "ticker":{
        #             "market_id":"ETH-BTC",
        #             "last_price":["0.07300001","BTC"],
        #             "min_ask":["0.07716895","BTC"],
        #             "max_bid":["0.0754966","BTC"],
        #             "volume":["0.168965697","ETH"],
        #             "price_variation_24h":"-0.046",
        #             "price_variation_7d":"-0.085"
        #         }
        #     }
        #
        ticker = self.safe_value(response, 'ticker')
        return self.parse_ticker(ticker, market)

    def parse_ticker(self, ticker, market=None):
        #
        # fetchTicker
        #
        #     {
        #         "market_id":"ETH-BTC",
        #         "last_price":["0.07300001","BTC"],
        #         "min_ask":["0.07716895","BTC"],
        #         "max_bid":["0.0754966","BTC"],
        #         "volume":["0.168965697","ETH"],
        #         "price_variation_24h":"-0.046",
        #         "price_variation_7d":"-0.085"
        #     }
        #
        timestamp = self.milliseconds()
        marketId = self.safe_string(ticker, 'market_id')
        symbol = self.safe_symbol(marketId, market, '-')
        lastPrice = self.safe_value(ticker, 'last_price', [])
        last = self.safe_string(lastPrice, 0)
        percentage = self.safe_string(ticker, 'price_variation_24h')
        percentage = Precise.string_mul(percentage, '100')
        maxBid = self.safe_value(ticker, 'max_bid', [])
        minAsk = self.safe_value(ticker, 'min_ask', [])
        baseVolume = self.safe_value(ticker, 'volume', [])
        return self.safe_ticker({
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': None,
            'low': None,
            'bid': self.safe_string(maxBid, 0),
            'bidVolume': None,
            'ask': self.safe_string(minAsk, 0),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': percentage,
            'average': None,
            'baseVolume': self.safe_string(baseVolume, 0),
            'quoteVolume': None,
            'info': ticker,
        }, market)

    async def fetch_trades(self, symbol, since=None, limit=None, params={}):
        """
        get the list of most recent trades for a particular symbol
        :param str symbol: unified symbol of the market to fetch trades for
        :param int|None since: timestamp in ms of the earliest trade to fetch
        :param int|None limit: the maximum amount of trades to fetch
        :param dict params: extra parameters specific to the buda api endpoint
        :returns [dict]: a list of `trade structures <https://docs.ccxt.com/en/latest/manual.html?#public-trades>`
        """
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'market': market['id'],
        }
        # the since argument works backwards – returns trades up to the specified timestamp
        # therefore not implemented here
        # the method is still available for users to be able to traverse backwards in time
        # by using the timestamp from the first received trade upon each iteration
        if limit is not None:
            request['limit'] = limit  # 50 max
        response = await self.publicGetMarketsMarketTrades(self.extend(request, params))
        #
        #     {trades: {     market_id:   "ETH-BTC",
        #                      timestamp:    null,
        #                 last_timestamp:   "1536901277302",
        #                        entries: [["1540077456791", "0.0063767", "0.03", "sell", 479842],
        #                                   ["1539916642772", "0.01888263", "0.03019563", "sell", 479438],
        #                                   ["1539834081787", "0.023718648", "0.031001", "sell", 479069],
        #                                   ...]
        #
        return self.parse_trades(response['trades']['entries'], market, since, limit)

    def parse_trade(self, trade, market=None):
        #
        # fetchTrades(public)
        #  ["1540077456791", "0.0063767", "0.03", "sell", 479842]
        #
        timestamp = None
        side = None
        type = None
        priceString = None
        amountString = None
        id = None
        order = None
        fee = None
        symbol = None
        if market:
            symbol = market['symbol']
        if isinstance(trade, list):
            timestamp = self.safe_integer(trade, 0)
            priceString = self.safe_string(trade, 1)
            amountString = self.safe_string(trade, 2)
            side = self.safe_string(trade, 3)
            id = self.safe_string(trade, 4)
        return self.safe_trade({
            'id': id,
            'order': order,
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': type,
            'side': side,
            'takerOrMaker': None,
            'price': priceString,
            'amount': amountString,
            'cost': None,
            'fee': fee,
        }, market)

    async def fetch_order_book(self, symbol, limit=None, params={}):
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int|None limit: the maximum amount of order book entries to return
        :param dict params: extra parameters specific to the buda api endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/en/latest/manual.html#order-book-structure>` indexed by market symbols
        """
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'market': market['id'],
        }
        response = await self.publicGetMarketsMarketOrderBook(self.extend(request, params))
        orderbook = self.safe_value(response, 'order_book')
        return self.parse_order_book(orderbook, symbol)

    async def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market
        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int|None since: timestamp in ms of the earliest candle to fetch
        :param int|None limit: the maximum amount of candles to fetch
        :param dict params: extra parameters specific to the buda api endpoint
        :returns [[int]]: A list of candles ordered as timestamp, open, high, low, close, volume
        """
        await self.load_markets()
        market = self.market(symbol)
        if since is None:
            since = self.milliseconds() - 86400000
        request = {
            'symbol': market['id'],
            'resolution': self.timeframes[timeframe],
            'from': since / 1000,
            'to': self.seconds(),
        }
        response = await self.publicGetTvHistory(self.extend(request, params))
        return self.parse_trading_view_ohlcv(response, market, timeframe, since, limit)

    def parse_balance(self, response):
        result = {'info': response}
        balances = self.safe_value(response, 'balances', [])
        for i in range(0, len(balances)):
            balance = balances[i]
            currencyId = self.safe_string(balance, 'id')
            code = self.safe_currency_code(currencyId)
            account = self.account()
            account['free'] = self.safe_string(balance['available_amount'], 0)
            account['total'] = self.safe_string(balance['amount'], 0)
            result[code] = account
        return self.safe_balance(result)

    async def fetch_balance(self, params={}):
        """
        query for balance and get the amount of funds available for trading or funds locked in orders
        :param dict params: extra parameters specific to the buda api endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/en/latest/manual.html?#balance-structure>`
        """
        await self.load_markets()
        response = await self.privateGetBalances(params)
        return self.parse_balance(response)

    async def fetch_order(self, id, symbol=None, params={}):
        await self.load_markets()
        request = {
            'id': int(id),
        }
        response = await self.privateGetOrdersId(self.extend(request, params))
        order = self.safe_value(response, 'order')
        return self.parse_order(order)

    async def fetch_orders(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        market = None
        if symbol is not None:
            market = self.market(symbol)
        request = {
            'market': market['id'],
            'per': limit,
        }
        response = await self.privateGetMarketsMarketOrders(self.extend(request, params))
        orders = self.safe_value(response, 'orders')
        return self.parse_orders(orders, market, since, limit)

    async def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        request = {
            'state': 'pending',
        }
        return await self.fetch_orders(symbol, since, limit, self.extend(request, params))

    async def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        request = {
            'state': 'traded',
        }
        return await self.fetch_orders(symbol, since, limit, self.extend(request, params))

    async def create_order(self, symbol, type, side, amount, price=None, params={}):
        await self.load_markets()
        side = 'Bid' if (side == 'buy') else 'Ask'
        request = {
            'market': self.market_id(symbol),
            'price_type': type,
            'type': side,
            'amount': self.amount_to_precision(symbol, amount),
        }
        if type == 'limit':
            request['limit'] = self.price_to_precision(symbol, price)
        response = await self.privatePostMarketsMarketOrders(self.extend(request, params))
        order = self.safe_value(response, 'order')
        return self.parse_order(order)

    async def cancel_order(self, id, symbol=None, params={}):
        await self.load_markets()
        request = {
            'id': int(id),
            'state': 'canceling',
        }
        response = await self.privatePutOrdersId(self.extend(request, params))
        order = self.safe_value(response, 'order')
        return self.parse_order(order)

    def parse_order_status(self, status):
        statuses = {
            'traded': 'closed',
            'received': 'open',
            'canceling': 'canceled',
        }
        return self.safe_string(statuses, status, status)

    def parse_order(self, order, market=None):
        #
        #     {
        #         'id': 63679183,
        #         'uuid': 'f9697bee-627e-4175-983f-0d5a41963fec',
        #         'market_id': 'ETH-CLP',
        #         'account_id': 51590,
        #         'type': 'Ask',
        #         'state': 'received',
        #         'created_at': '2021-01-04T08:29:52.730Z',
        #         'fee_currency': 'CLP',
        #         'price_type': 'limit',
        #         'source': None,
        #         'limit': ['741000.0', 'CLP'],
        #         'amount': ['0.001', 'ETH'],
        #         'original_amount': ['0.001', 'ETH'],
        #         'traded_amount': ['0.0', 'ETH'],
        #         'total_exchanged': ['0.0', 'CLP'],
        #         'paid_fee': ['0.0', 'CLP']
        #     }
        #
        id = self.safe_string(order, 'id')
        timestamp = self.parse8601(self.safe_string(order, 'created_at'))
        datetime = self.iso8601(timestamp)
        marketId = self.safe_string(order, 'market_id')
        symbol = self.safe_symbol(marketId, market, '-')
        type = self.safe_string(order, 'price_type')
        side = self.safe_string_lower(order, 'type')
        status = self.parse_order_status(self.safe_string(order, 'state'))
        originalAmount = self.safe_value(order, 'original_amount', [])
        amount = self.safe_string(originalAmount, 0)
        remainingAmount = self.safe_value(order, 'amount', [])
        remaining = self.safe_string(remainingAmount, 0)
        tradedAmount = self.safe_value(order, 'traded_amount', [])
        filled = self.safe_string(tradedAmount, 0)
        totalExchanged = self.safe_value(order, 'totalExchanged', [])
        cost = self.safe_string(totalExchanged, 0)
        limitPrice = self.safe_value(order, 'limit', [])
        price = self.safe_string(limitPrice, 0)
        if price is None:
            if limitPrice is not None:
                price = limitPrice
        paidFee = self.safe_value(order, 'paid_fee', [])
        feeCost = self.safe_string(paidFee, 0)
        fee = None
        if feeCost is not None:
            feeCurrencyId = self.safe_string(paidFee, 1)
            feeCurrencyCode = self.safe_currency_code(feeCurrencyId)
            fee = {
                'cost': feeCost,
                'code': feeCurrencyCode,
            }
        return self.safe_order({
            'info': order,
            'id': id,
            'clientOrderId': None,
            'datetime': datetime,
            'timestamp': timestamp,
            'lastTradeTimestamp': None,
            'status': status,
            'symbol': symbol,
            'type': type,
            'timeInForce': None,
            'postOnly': None,
            'side': side,
            'price': price,
            'stopPrice': None,
            'average': None,
            'cost': cost,
            'amount': amount,
            'filled': filled,
            'remaining': remaining,
            'trades': None,
            'fee': fee,
        }, market)

    def is_fiat(self, code):
        fiats = {
            'ARS': True,
            'CLP': True,
            'COP': True,
            'PEN': True,
        }
        return self.safe_value(fiats, code, False)

    async def fetch_deposit_address(self, code, params={}):
        await self.load_markets()
        currency = self.currency(code)
        if self.is_fiat(code):
            raise NotSupported(self.id + ' fetchDepositAddress() for fiat ' + code + ' is not supported')
        request = {
            'currency': currency['id'],
        }
        response = await self.privateGetCurrenciesCurrencyReceiveAddresses(self.extend(request, params))
        receiveAddresses = self.safe_value(response, 'receive_addresses')
        addressPool = []
        for i in range(1, len(receiveAddresses)):
            receiveAddress = receiveAddresses[i]
            if receiveAddress['ready']:
                address = receiveAddress['address']
                self.check_address(address)
                addressPool.append(address)
        addressPoolLength = len(addressPool)
        if addressPoolLength < 1:
            raise AddressPending(self.id + ': there are no addresses ready for receiving ' + code + ', retry again later)')
        address = addressPool[0]
        return {
            'currency': code,
            'address': address,
            'tag': None,
            'network': None,
            'info': receiveAddresses,
        }

    async def create_deposit_address(self, code, params={}):
        await self.load_markets()
        currency = self.currency(code)
        if self.is_fiat(code):
            raise NotSupported(self.id + ' createDepositAddress() of fiat for ' + code + ' is not supported')
        request = {
            'currency': currency['id'],
        }
        response = await self.privatePostCurrenciesCurrencyReceiveAddresses(self.extend(request, params))
        address = self.safe_string(response['receive_address'], 'address')  # the creation is async and returns a null address, returns only the id
        return {
            'currency': code,
            'address': address,
            'tag': None,
            'info': response,
        }

    def parse_transaction_status(self, status):
        statuses = {
            'rejected': 'failed',
            'confirmed': 'ok',
            'aNoneed': 'canceled',
            'retained': 'canceled',
            'pending_confirmation': 'pending',
        }
        return self.safe_string(statuses, status, status)

    def parse_transaction(self, transaction, currency=None):
        id = self.safe_string(transaction, 'id')
        timestamp = self.parse8601(self.safe_string(transaction, 'created_at'))
        currencyId = self.safe_string(transaction, 'currency')
        code = self.safe_currency_code(currencyId, currency)
        amount = float(transaction['amount'][0])
        fee = float(transaction['fee'][0])
        feeCurrency = transaction['fee'][1]
        status = self.parse_transaction_status(self.safe_string(transaction, 'state'))
        type = 'deposit' if ('deposit_data' in transaction) else 'withdrawal'
        data = self.safe_value(transaction, type + '_data', {})
        address = self.safe_value(data, 'target_address')
        txid = self.safe_string(data, 'tx_hash')
        updated = self.parse8601(self.safe_string(data, 'updated_at'))
        return {
            'info': transaction,
            'id': id,
            'txid': txid,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'network': None,
            'address': address,
            'addressTo': None,
            'addressFrom': None,
            'tag': None,
            'tagTo': None,
            'tagFrom': None,
            'type': type,
            'amount': amount,
            'currency': code,
            'status': status,
            'updated': updated,
            'fee': {
                'cost': fee,
                'rate': feeCurrency,
            },
        }

    async def fetch_deposits(self, code=None, since=None, limit=None, params={}):
        await self.load_markets()
        if code is None:
            raise ArgumentsRequired(self.id + ' fetchDeposits() requires a currency code argument')
        currency = self.currency(code)
        request = {
            'currency': currency['id'],
            'per': limit,
        }
        response = await self.privateGetCurrenciesCurrencyDeposits(self.extend(request, params))
        deposits = self.safe_value(response, 'deposits')
        return self.parse_transactions(deposits, currency, since, limit)

    async def fetch_withdrawals(self, code=None, since=None, limit=None, params={}):
        await self.load_markets()
        if code is None:
            raise ArgumentsRequired(self.id + ' fetchWithdrawals() requires a currency code argument')
        currency = self.currency(code)
        request = {
            'currency': currency['id'],
            'per': limit,
        }
        response = await self.privateGetCurrenciesCurrencyWithdrawals(self.extend(request, params))
        withdrawals = self.safe_value(response, 'withdrawals')
        return self.parse_transactions(withdrawals, currency, since, limit)

    async def withdraw(self, code, amount, address, tag=None, params={}):
        tag, params = self.handle_withdraw_tag_and_params(tag, params)
        self.check_address(address)
        await self.load_markets()
        currency = self.currency(code)
        request = {
            'currency': currency['id'],
            'amount': amount,
            'withdrawal_data': {
                'target_address': address,
            },
        }
        response = await self.privatePostCurrenciesCurrencyWithdrawals(self.extend(request, params))
        withdrawal = self.safe_value(response, 'withdrawal')
        return self.parse_transaction(withdrawal)

    def nonce(self):
        return self.microseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        request = self.implode_params(path, params)
        query = self.omit(params, self.extract_params(path))
        if query:
            if method == 'GET':
                request += '?' + self.urlencode(query)
            else:
                body = self.json(query)
        url = self.urls['api'] + '/' + self.version + '/' + request
        if api == 'private':
            self.check_required_credentials()
            nonce = str(self.nonce())
            components = [method, '/api/' + self.version + '/' + request]
            if body:
                base64Body = self.string_to_base64(body)
                components.append(self.decode(base64Body))
            components.append(nonce)
            message = ' '.join(components)
            signature = self.hmac(self.encode(message), self.encode(self.secret), hashlib.sha384)
            headers = {
                'X-SBTC-APIKEY': self.apiKey,
                'X-SBTC-SIGNATURE': signature,
                'X-SBTC-NONCE': nonce,
                'Content-Type': 'application/json',
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, code, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return  # fallback to default error handler
        if code >= 400:
            errorCode = self.safe_string(response, 'code')
            message = self.safe_string(response, 'message', body)
            feedback = self.id + ' ' + message
            if errorCode is not None:
                self.throw_exactly_matched_exception(self.exceptions, errorCode, feedback)
                raise ExchangeError(feedback)