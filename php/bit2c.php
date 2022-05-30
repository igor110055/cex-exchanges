<?php

namespace ccxt;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

use Exception; // a common import
use \ccxt\ExchangeError;
use \ccxt\ArgumentsRequired;
use \ccxt\NotSupported;

class bit2c extends Exchange {

    public function describe() {
        return $this->deep_extend(parent::describe (), array(
            'id' => 'bit2c',
            'name' => 'Bit2C',
            'countries' => array( 'IL' ), // Israel
            'rateLimit' => 3000,
            'has' => array(
                'CORS' => null,
                'spot' => true,
                'margin' => false,
                'swap' => false,
                'future' => false,
                'option' => false,
                'addMargin' => false,
                'cancelOrder' => true,
                'createOrder' => true,
                'createReduceOnlyOrder' => false,
                'fetchBalance' => true,
                'fetchBorrowRate' => false,
                'fetchBorrowRateHistories' => false,
                'fetchBorrowRateHistory' => false,
                'fetchBorrowRates' => false,
                'fetchBorrowRatesPerSymbol' => false,
                'fetchDepositAddress' => true,
                'fetchFundingHistory' => false,
                'fetchFundingRate' => false,
                'fetchFundingRateHistory' => false,
                'fetchFundingRates' => false,
                'fetchIndexOHLCV' => false,
                'fetchLeverage' => false,
                'fetchLeverageTiers' => false,
                'fetchMarkOHLCV' => false,
                'fetchMyTrades' => true,
                'fetchOpenInterestHistory' => false,
                'fetchOpenOrders' => true,
                'fetchOrderBook' => true,
                'fetchPosition' => false,
                'fetchPositions' => false,
                'fetchPositionsRisk' => false,
                'fetchPremiumIndexOHLCV' => false,
                'fetchTicker' => true,
                'fetchTrades' => true,
                'fetchTradingFee' => false,
                'fetchTradingFees' => true,
                'fetchTransfer' => false,
                'fetchTransfers' => false,
                'reduceMargin' => false,
                'setLeverage' => false,
                'setMarginMode' => false,
                'setPositionMode' => false,
                'transfer' => false,
            ),
            'urls' => array(
                'logo' => 'https://user-images.githubusercontent.com/1294454/27766119-3593220e-5ece-11e7-8b3a-5a041f6bcc3f.jpg',
                'api' => 'https://bit2c.co.il',
                'www' => 'https://www.bit2c.co.il',
                'referral' => 'https://bit2c.co.il/Aff/63bfed10-e359-420c-ab5a-ad368dab0baf',
                'doc' => array(
                    'https://www.bit2c.co.il/home/api',
                    'https://github.com/OferE/bit2c',
                ),
            ),
            'api' => array(
                'public' => array(
                    'get' => array(
                        'Exchanges/{pair}/Ticker',
                        'Exchanges/{pair}/orderbook',
                        'Exchanges/{pair}/trades',
                        'Exchanges/{pair}/lasttrades',
                    ),
                ),
                'private' => array(
                    'post' => array(
                        'Merchant/CreateCheckout',
                        'Funds/AddCoinFundsRequest',
                        'Order/AddFund',
                        'Order/AddOrder',
                        'Order/AddOrderMarketPriceBuy',
                        'Order/AddOrderMarketPriceSell',
                        'Order/CancelOrder',
                        'Order/AddCoinFundsRequest',
                        'Order/AddStopOrder',
                        'Payment/GetMyId',
                        'Payment/Send',
                        'Payment/Pay',
                    ),
                    'get' => array(
                        'Account/Balance',
                        'Account/Balance/v2',
                        'Order/MyOrders',
                        'Order/GetById',
                        'Order/AccountHistory',
                        'Order/OrderHistory',
                    ),
                ),
            ),
            'markets' => array(
                'BTC/NIS' => array( 'id' => 'BtcNis', 'symbol' => 'BTC/NIS', 'base' => 'BTC', 'quote' => 'NIS', 'baseId' => 'Btc', 'quoteId' => 'Nis', 'type' => 'spot', 'spot' => true ),
                'ETH/NIS' => array( 'id' => 'EthNis', 'symbol' => 'ETH/NIS', 'base' => 'ETH', 'quote' => 'NIS', 'baseId' => 'Eth', 'quoteId' => 'Nis', 'type' => 'spot', 'spot' => true ),
                'BCH/NIS' => array( 'id' => 'BchabcNis', 'symbol' => 'BCH/NIS', 'base' => 'BCH', 'quote' => 'NIS', 'baseId' => 'Bchabc', 'quoteId' => 'Nis', 'type' => 'spot', 'spot' => true ),
                'LTC/NIS' => array( 'id' => 'LtcNis', 'symbol' => 'LTC/NIS', 'base' => 'LTC', 'quote' => 'NIS', 'baseId' => 'Ltc', 'quoteId' => 'Nis', 'type' => 'spot', 'spot' => true ),
                'ETC/NIS' => array( 'id' => 'EtcNis', 'symbol' => 'ETC/NIS', 'base' => 'ETC', 'quote' => 'NIS', 'baseId' => 'Etc', 'quoteId' => 'Nis', 'type' => 'spot', 'spot' => true ),
                'BTG/NIS' => array( 'id' => 'BtgNis', 'symbol' => 'BTG/NIS', 'base' => 'BTG', 'quote' => 'NIS', 'baseId' => 'Btg', 'quoteId' => 'Nis', 'type' => 'spot', 'spot' => true ),
                'BSV/NIS' => array( 'id' => 'BchsvNis', 'symbol' => 'BSV/NIS', 'base' => 'BSV', 'quote' => 'NIS', 'baseId' => 'Bchsv', 'quoteId' => 'Nis', 'type' => 'spot', 'spot' => true ),
                'GRIN/NIS' => array( 'id' => 'GrinNis', 'symbol' => 'GRIN/NIS', 'base' => 'GRIN', 'quote' => 'NIS', 'baseId' => 'Grin', 'quoteId' => 'Nis', 'type' => 'spot', 'spot' => true ),
            ),
            'fees' => array(
                'trading' => array(
                    'maker' => $this->parse_number('0.005'),
                    'taker' => $this->parse_number('0.005'),
                ),
            ),
            'options' => array(
                'fetchTradesMethod' => 'public_get_exchanges_pair_trades',
            ),
            'exceptions' => array(
                'exact' => array(
                    'Please provide valid APIkey' => '\\ccxt\\AuthenticationError', // array( "error" : "Please provide valid APIkey" )
                ),
                'broad' => array(
                    // array( "error" => "Please provide valid nonce in Request Nonce (1598218490) is not bigger than last nonce (1598218490).")
                    // array( "error" => "Please provide valid nonce in Request UInt64.TryParse failed for nonce :" )
                    'Please provide valid nonce' => '\\ccxt\\InvalidNonce',
                    'please approve new terms of use on site' => '\\ccxt\\PermissionDenied', // array( "error" : "please approve new terms of use on site." )
                ),
            ),
        ));
    }

    public function parse_balance($response) {
        $result = array(
            'info' => $response,
            'timestamp' => null,
            'datetime' => null,
        );
        $codes = is_array($this->currencies) ? array_keys($this->currencies) : array();
        for ($i = 0; $i < count($codes); $i++) {
            $code = $codes[$i];
            $account = $this->account();
            $currency = $this->currency($code);
            $uppercase = strtoupper($currency['id']);
            if (is_array($response) && array_key_exists($uppercase, $response)) {
                $account['free'] = $this->safe_string($response, 'AVAILABLE_' . $uppercase);
                $account['total'] = $this->safe_string($response, $uppercase);
            }
            $result[$code] = $account;
        }
        return $this->safe_balance($result);
    }

    public function fetch_balance($params = array ()) {
        /**
         * query for balance and get the amount of funds available for trading or funds locked in orders
         * @param {dict} $params extra parameters specific to the bit2c api endpoint
         * @return {dict} a ~@link https://docs.ccxt.com/en/latest/manual.html?#balance-structure balance structure~
         */
        $this->load_markets();
        $response = $this->privateGetAccountBalanceV2 ($params);
        //
        //     {
        //         "AVAILABLE_NIS" => 0.0,
        //         "NIS" => 0.0,
        //         "LOCKED_NIS" => 0.0,
        //         "AVAILABLE_BTC" => 0.0,
        //         "BTC" => 0.0,
        //         "LOCKED_BTC" => 0.0,
        //         "AVAILABLE_ETH" => 0.0,
        //         "ETH" => 0.0,
        //         "LOCKED_ETH" => 0.0,
        //         "AVAILABLE_BCHSV" => 0.0,
        //         "BCHSV" => 0.0,
        //         "LOCKED_BCHSV" => 0.0,
        //         "AVAILABLE_BCHABC" => 0.0,
        //         "BCHABC" => 0.0,
        //         "LOCKED_BCHABC" => 0.0,
        //         "AVAILABLE_LTC" => 0.0,
        //         "LTC" => 0.0,
        //         "LOCKED_LTC" => 0.0,
        //         "AVAILABLE_ETC" => 0.0,
        //         "ETC" => 0.0,
        //         "LOCKED_ETC" => 0.0,
        //         "AVAILABLE_BTG" => 0.0,
        //         "BTG" => 0.0,
        //         "LOCKED_BTG" => 0.0,
        //         "AVAILABLE_GRIN" => 0.0,
        //         "GRIN" => 0.0,
        //         "LOCKED_GRIN" => 0.0,
        //         "Fees" => {
        //             "BtcNis" => array( "FeeMaker" => 1.0, "FeeTaker" => 1.0 ),
        //             "EthNis" => array( "FeeMaker" => 1.0, "FeeTaker" => 1.0 ),
        //             "BchabcNis" => array( "FeeMaker" => 1.0, "FeeTaker" => 1.0 ),
        //             "LtcNis" => array( "FeeMaker" => 1.0, "FeeTaker" => 1.0 ),
        //             "EtcNis" => array( "FeeMaker" => 1.0, "FeeTaker" => 1.0 ),
        //             "BtgNis" => array( "FeeMaker" => 1.0, "FeeTaker" => 1.0 ),
        //             "LtcBtc" => array( "FeeMaker" => 1.0, "FeeTaker" => 1.0 ),
        //             "BchsvNis" => array( "FeeMaker" => 1.0, "FeeTaker" => 1.0 ),
        //             "GrinNis" => array( "FeeMaker" => 1.0, "FeeTaker" => 1.0 )
        //         }
        //     }
        //
        return $this->parse_balance($response);
    }

    public function fetch_order_book($symbol, $limit = null, $params = array ()) {
        /**
         * fetches information on open orders with bid (buy) and ask (sell) prices, volumes and other data
         * @param {str} $symbol unified $symbol of the market to fetch the order book for
         * @param {int|null} $limit the maximum amount of order book entries to return
         * @param {dict} $params extra parameters specific to the bit2c api endpoint
         * @return {dict} A dictionary of {@link https://docs.ccxt.com/en/latest/manual.html#order-book-structure order book structures} indexed by market symbols
         */
        $this->load_markets();
        $request = array(
            'pair' => $this->market_id($symbol),
        );
        $orderbook = $this->publicGetExchangesPairOrderbook (array_merge($request, $params));
        return $this->parse_order_book($orderbook, $symbol);
    }

    public function parse_ticker($ticker, $market = null) {
        $symbol = $this->safe_symbol(null, $market);
        $timestamp = $this->milliseconds();
        $averagePrice = $this->safe_string($ticker, 'av');
        $baseVolume = $this->safe_string($ticker, 'a');
        $last = $this->safe_string($ticker, 'll');
        return $this->safe_ticker(array(
            'symbol' => $symbol,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601($timestamp),
            'high' => null,
            'low' => null,
            'bid' => $this->safe_string($ticker, 'h'),
            'bidVolume' => null,
            'ask' => $this->safe_string($ticker, 'l'),
            'askVolume' => null,
            'vwap' => null,
            'open' => null,
            'close' => $last,
            'last' => $last,
            'previousClose' => null,
            'change' => null,
            'percentage' => null,
            'average' => $averagePrice,
            'baseVolume' => $baseVolume,
            'quoteVolume' => null,
            'info' => $ticker,
        ), $market);
    }

    public function fetch_ticker($symbol, $params = array ()) {
        /**
         * fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific $market
         * @param {str} $symbol unified $symbol of the $market to fetch the ticker for
         * @param {dict} $params extra parameters specific to the bit2c api endpoint
         * @return {dict} a {@link https://docs.ccxt.com/en/latest/manual.html#ticker-structure ticker structure}
         */
        $this->load_markets();
        $market = $this->market($symbol);
        $request = array(
            'pair' => $market['id'],
        );
        $response = $this->publicGetExchangesPairTicker (array_merge($request, $params));
        return $this->parse_ticker($response, $market);
    }

    public function fetch_trades($symbol, $since = null, $limit = null, $params = array ()) {
        /**
         * get the list of most recent trades for a particular $symbol
         * @param {str} $symbol unified $symbol of the $market to fetch trades for
         * @param {int|null} $since timestamp in ms of the earliest trade to fetch
         * @param {int|null} $limit the maximum amount of trades to fetch
         * @param {dict} $params extra parameters specific to the bit2c api endpoint
         * @return {[dict]} a list of ~@link https://docs.ccxt.com/en/latest/manual.html?#public-trades trade structures~
         */
        $this->load_markets();
        $market = $this->market($symbol);
        $method = $this->options['fetchTradesMethod']; // public_get_exchanges_pair_trades or public_get_exchanges_pair_lasttrades
        $request = array(
            'pair' => $market['id'],
        );
        if ($since !== null) {
            $request['date'] = intval($since);
        }
        if ($limit !== null) {
            $request['limit'] = $limit; // max 100000
        }
        $response = $this->$method (array_merge($request, $params));
        //
        //     array(
        //         array("date":1651785980,"price":127975.68,"amount":0.3750321,"isBid":true,"tid":1261018),
        //         array("date":1651785980,"price":127987.70,"amount":0.0389527820303982335802581029,"isBid":true,"tid":1261020),
        //         array("date":1651786701,"price":128084.03,"amount":0.0015614749161156156626239821,"isBid":true,"tid":1261022),
        //     )
        //
        if (gettype($response) === 'string') {
            throw new ExchangeError($response);
        }
        return $this->parse_trades($response, $market, $since, $limit);
    }

    public function fetch_trading_fees($params = array ()) {
        $this->load_markets();
        $response = $this->privateGetAccountBalance ($params);
        //
        //     {
        //         "AVAILABLE_NIS" => 0.0,
        //         "NIS" => 0.0,
        //         "LOCKED_NIS" => 0.0,
        //         "AVAILABLE_BTC" => 0.0,
        //         "BTC" => 0.0,
        //         "LOCKED_BTC" => 0.0,
        //         ...
        //         "Fees" => {
        //             "BtcNis" => array( "FeeMaker" => 1.0, "FeeTaker" => 1.0 ),
        //             "EthNis" => array( "FeeMaker" => 1.0, "FeeTaker" => 1.0 ),
        //             ...
        //         }
        //     }
        //
        $fees = $this->safe_value($response, 'Fees', array());
        $keys = is_array($fees) ? array_keys($fees) : array();
        $result = array();
        for ($i = 0; $i < count($keys); $i++) {
            $marketId = $keys[$i];
            $symbol = $this->safe_symbol($marketId);
            $fee = $this->safe_value($fees, $marketId);
            $makerString = $this->safe_string($fee, 'FeeMaker');
            $takerString = $this->safe_string($fee, 'FeeTaker');
            $maker = $this->parse_number(Precise::string_div($makerString, '100'));
            $taker = $this->parse_number(Precise::string_div($takerString, '100'));
            $result[$symbol] = array(
                'info' => $fee,
                'symbol' => $symbol,
                'taker' => $taker,
                'maker' => $maker,
                'percentage' => true,
                'tierBased' => false,
            );
        }
        return $result;
    }

    public function create_order($symbol, $type, $side, $amount, $price = null, $params = array ()) {
        $this->load_markets();
        $method = 'privatePostOrderAddOrder';
        $request = array(
            'Amount' => $amount,
            'Pair' => $this->market_id($symbol),
        );
        if ($type === 'market') {
            $method .= 'MarketPrice' . $this->capitalize($side);
        } else {
            $request['Price'] = $price;
            $request['Total'] = $amount * $price;
            $request['IsBid'] = ($side === 'buy');
        }
        $response = $this->$method (array_merge($request, $params));
        return array(
            'info' => $response,
            'id' => $response['NewOrder']['id'],
        );
    }

    public function cancel_order($id, $symbol = null, $params = array ()) {
        $request = array(
            'id' => $id,
        );
        return $this->privatePostOrderCancelOrder (array_merge($request, $params));
    }

    public function fetch_open_orders($symbol = null, $since = null, $limit = null, $params = array ()) {
        if ($symbol === null) {
            throw new ArgumentsRequired($this->id . ' fetchOpenOrders() requires a $symbol argument');
        }
        $this->load_markets();
        $market = $this->market($symbol);
        $request = array(
            'pair' => $market['id'],
        );
        $response = $this->privateGetOrderMyOrders (array_merge($request, $params));
        $orders = $this->safe_value($response, $market['id'], array());
        $asks = $this->safe_value($orders, 'ask', array());
        $bids = $this->safe_value($orders, 'bid', array());
        return $this->parse_orders($this->array_concat($asks, $bids), $market, $since, $limit);
    }

    public function parse_order($order, $market = null) {
        $timestamp = $this->safe_integer($order, 'created');
        $price = $this->safe_string($order, 'price');
        $amount = $this->safe_string($order, 'amount');
        $market = $this->safe_market(null, $market);
        $side = $this->safe_value($order, 'type');
        if ($side === 0) {
            $side = 'buy';
        } elseif ($side === 1) {
            $side = 'sell';
        }
        $id = $this->safe_string($order, 'id');
        $status = $this->safe_string($order, 'status');
        return $this->safe_order(array(
            'id' => $id,
            'clientOrderId' => null,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601($timestamp),
            'lastTradeTimestamp' => null,
            'status' => $status,
            'symbol' => $market['symbol'],
            'type' => null,
            'timeInForce' => null,
            'postOnly' => null,
            'side' => $side,
            'price' => $price,
            'stopPrice' => null,
            'amount' => $amount,
            'filled' => null,
            'remaining' => null,
            'cost' => null,
            'trades' => null,
            'fee' => null,
            'info' => $order,
            'average' => null,
        ), $market);
    }

    public function fetch_my_trades($symbol = null, $since = null, $limit = null, $params = array ()) {
        $this->load_markets();
        $market = null;
        $request = array();
        if ($limit !== null) {
            $request['take'] = $limit;
        }
        $request['take'] = $limit;
        if ($since !== null) {
            $request['toTime'] = $this->yyyymmdd($this->milliseconds(), '.');
            $request['fromTime'] = $this->yyyymmdd($since, '.');
        }
        if ($symbol !== null) {
            $market = $this->market($symbol);
            $request['pair'] = $market['id'];
        }
        $response = $this->privateGetOrderOrderHistory (array_merge($request, $params));
        //
        //     array(
        //         array(
        //             "ticks":1574767951,
        //             "created":"26/11/19 13:32",
        //             "action":1,
        //             "price":"1000",
        //             "pair":"EthNis",
        //             "reference":"EthNis|10867390|10867377",
        //             "fee":"0.5",
        //             "feeAmount":"0.08",
        //             "feeCoin":"₪",
        //             "firstAmount":"-0.015",
        //             "firstAmountBalance":"9",
        //             "secondAmount":"14.93",
        //             "secondAmountBalance":"130,233.28",
        //             "firstCoin":"ETH",
        //             "secondCoin":"₪"
        //         ),
        //         {
        //             "ticks":1574767951,
        //             "created":"26/11/19 13:32",
        //             "action":0,
        //             "price":"1000",
        //             "pair":"EthNis",
        //             "reference":"EthNis|10867390|10867377",
        //             "fee":"0.5",
        //             "feeAmount":"0.08",
        //             "feeCoin":"₪",
        //             "firstAmount":"0.015",
        //             "firstAmountBalance":"9.015",
        //             "secondAmount":"-15.08",
        //             "secondAmountBalance":"130,218.35",
        //             "firstCoin":"ETH",
        //             "secondCoin":"₪"
        //         }
        //     )
        //
        return $this->parse_trades($response, $market, $since, $limit);
    }

    public function parse_trade($trade, $market = null) {
        //
        // public fetchTrades
        //
        //     {
        //         "date":1651785980,
        //         "price":127975.68,
        //         "amount":0.3750321,
        //         "isBid":true,
        //         "tid":1261018
        //     }
        //
        // private fetchMyTrades
        //
        //     {
        //         "ticks":1574767951,
        //         "created":"26/11/19 13:32",
        //         "action":1,
        //         "price":"1000",
        //         "pair":"EthNis",
        //         "reference":"EthNis|10867390|10867377",
        //         "fee":"0.5",
        //         "feeAmount":"0.08",
        //         "feeCoin":"₪",
        //         "firstAmount":"-0.015",
        //         "firstAmountBalance":"9",
        //         "secondAmount":"14.93",
        //         "secondAmountBalance":"130,233.28",
        //         "firstCoin":"ETH",
        //         "secondCoin":"₪"
        //     }
        //
        $timestamp = null;
        $id = null;
        $price = null;
        $amount = null;
        $orderId = null;
        $fee = null;
        $side = null;
        $reference = $this->safe_string($trade, 'reference');
        if ($reference !== null) {
            $timestamp = $this->safe_timestamp($trade, 'ticks');
            $price = $this->safe_string($trade, 'price');
            $amount = $this->safe_string($trade, 'firstAmount');
            $reference_parts = explode('|', $reference); // $reference contains 'pair|$orderId|tradeId'
            $marketId = $this->safe_string($trade, 'pair');
            $market = $this->safe_market($marketId, $market);
            $market = $this->safe_market($reference_parts[0], $market);
            $orderId = $reference_parts[1];
            $id = $reference_parts[2];
            $side = $this->safe_integer($trade, 'action');
            if ($side === 0) {
                $side = 'buy';
            } elseif ($side === 1) {
                $side = 'sell';
            }
            $feeCost = $this->safe_string($trade, 'feeAmount');
            if ($feeCost !== null) {
                $fee = array(
                    'cost' => $feeCost,
                    'currency' => 'NIS',
                );
            }
        } else {
            $timestamp = $this->safe_timestamp($trade, 'date');
            $id = $this->safe_string($trade, 'tid');
            $price = $this->safe_string($trade, 'price');
            $amount = $this->safe_string($trade, 'amount');
            $side = $this->safe_value($trade, 'isBid');
            if ($side !== null) {
                if ($side) {
                    $side = 'buy';
                } else {
                    $side = 'sell';
                }
            }
        }
        $market = $this->safe_market(null, $market);
        return $this->safe_trade(array(
            'info' => $trade,
            'id' => $id,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601($timestamp),
            'symbol' => $market['symbol'],
            'order' => $orderId,
            'type' => null,
            'side' => $side,
            'takerOrMaker' => null,
            'price' => $price,
            'amount' => $amount,
            'cost' => null,
            'fee' => $fee,
        ), $market);
    }

    public function is_fiat($code) {
        return $code === 'NIS';
    }

    public function fetch_deposit_address($code, $params = array ()) {
        $this->load_markets();
        $currency = $this->currency($code);
        if ($this->is_fiat($code)) {
            throw new NotSupported($this->id . ' fetchDepositAddress() does not support fiat currencies');
        }
        $request = array(
            'Coin' => $currency['id'],
        );
        $response = $this->privatePostFundsAddCoinFundsRequest (array_merge($request, $params));
        //
        //     {
        //         'address' => '0xf14b94518d74aff2b1a6d3429471bcfcd3881d42',
        //         'hasTx' => False
        //     }
        //
        return $this->parse_deposit_address($response, $currency);
    }

    public function parse_deposit_address($depositAddress, $currency = null) {
        //
        //     {
        //         'address' => '0xf14b94518d74aff2b1a6d3429471bcfcd3881d42',
        //         'hasTx' => False
        //     }
        //
        $address = $this->safe_string($depositAddress, 'address');
        $this->check_address($address);
        $code = $this->safe_currency_code(null, $currency);
        return array(
            'currency' => $code,
            'network' => null,
            'address' => $address,
            'tag' => null,
            'info' => $depositAddress,
        );
    }

    public function nonce() {
        return $this->milliseconds();
    }

    public function sign($path, $api = 'public', $method = 'GET', $params = array (), $headers = null, $body = null) {
        $url = $this->urls['api'] . '/' . $this->implode_params($path, $params);
        if ($api === 'public') {
            $url .= '.json';
        } else {
            $this->check_required_credentials();
            $nonce = $this->nonce();
            $query = array_merge(array(
                'nonce' => $nonce,
            ), $params);
            $auth = $this->urlencode($query);
            if ($method === 'GET') {
                if ($query) {
                    $url .= '?' . $auth;
                }
            } else {
                $body = $auth;
            }
            $signature = $this->hmac($this->encode($auth), $this->encode($this->secret), 'sha512', 'base64');
            $headers = array(
                'Content-Type' => 'application/x-www-form-urlencoded',
                'key' => $this->apiKey,
                'sign' => $signature,
            );
        }
        return array( 'url' => $url, 'method' => $method, 'body' => $body, 'headers' => $headers );
    }

    public function handle_errors($httpCode, $reason, $url, $method, $headers, $body, $response, $requestHeaders, $requestBody) {
        if ($response === null) {
            return; // fallback to default $error handler
        }
        //
        //     array( "error" : "please approve new terms of use on site." )
        //     array( "error" => "Please provide valid nonce in Request Nonce (1598218490) is not bigger than last nonce (1598218490).")
        //
        $error = $this->safe_string($response, 'error');
        if ($error !== null) {
            $feedback = $this->id . ' ' . $body;
            $this->throw_exactly_matched_exception($this->exceptions['exact'], $error, $feedback);
            $this->throw_broadly_matched_exception($this->exceptions['broad'], $error, $feedback);
            throw new ExchangeError($feedback); // unknown message
        }
    }
}