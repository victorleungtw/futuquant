﻿# -*- coding: utf-8 -*-
import pandas as pd
from futuquant.common import RspHandlerBase
from futuquant.quote.quote_query import *
from futuquant.trade.trade_query import *


class StockQuoteHandlerBase(RspHandlerBase):
    """
    异步处理推送的订阅股票的报价。

    .. code:: python

        class StockQuoteTest(StockQuoteHandlerBase):
            def on_recv_rsp(self, rsp_str):
                ret_code, content = super(StockQuoteTest,self).on_recv_rsp(rsp_str)
                if ret_code != RET_OK:
                    print("StockQuoteTest: error, msg: %s" % content)
                    return RET_ERROR, content

                print("StockQuoteTest ", content) # StockQuoteTest自己的处理逻辑

                return RET_OK, content
    """

    def on_recv_rsp(self, rsp_pb):
        """
        在收到实时报价推送后会回调到该函数，使用者需要在派生类中覆盖此方法

        注意该回调是在独立子线程中

        :param rsp_pb: 派生类中不需要直接处理该参数
        :return: 参见get_stock_quote的返回值
        """
        ret_code, msg, quote_list = StockQuoteQuery.unpack_rsp(rsp_pb)
        if ret_code == RET_ERROR:
            return ret_code, msg
        else:
            col_list = [
                'code', 'data_date', 'data_time', 'last_price', 'open_price',
                'high_price', 'low_price', 'prev_close_price', 'volume',
                'turnover', 'turnover_rate', 'amplitude', 'suspension',
                'listing_date', 'price_spread'
            ]

            quote_frame_table = pd.DataFrame(quote_list, columns=col_list)

            return RET_OK, quote_frame_table


class OrderBookHandlerBase(RspHandlerBase):
    """
    异步处理推送的实时摆盘。

    .. code:: python

        class OrderBookTest(OrderBookHandlerBase):
            def on_recv_rsp(self, rsp_str):
                ret_code, data = super(OrderBookTest,self).on_recv_rsp(rsp_str)
                if ret_code != RET_OK:
                    print("OrderBookTest: error, msg: %s" % data)
                    return RET_ERROR, data

                print("OrderBookTest ", data) # OrderBookTest自己的处理逻辑

                return RET_OK, content
    """

    def on_recv_rsp(self, rsp_pb):
        """
        在收到实摆盘数据推送后会回调到该函数，使用者需要在派生类中覆盖此方法

        注意该回调是在独立子线程中

        :param rsp_pb: 派生类中不需要直接处理该参数
        :return: 参见get_order_book的返回值
        """
        ret_code, msg, order_book = OrderBookQuery.unpack_rsp(rsp_pb)
        if ret_code == RET_ERROR:
            return ret_code, msg
        else:
            return ret_code, order_book


class CurKlineHandlerBase(RspHandlerBase):
    """
    异步处理推送的k线数据。

    .. code:: python

        class CurKlineTest(CurKlineHandlerBase):
            def on_recv_rsp(self, rsp_str):
                ret_code, data = super(CurKlineTest,self).on_recv_rsp(rsp_str)
                if ret_code != RET_OK:
                    print("CurKlineTest: error, msg: %s" % data)
                    return RET_ERROR, data

                print("CurKlineTest ", data) # CurKlineTest自己的处理逻辑

                return RET_OK, content
    """

    def on_recv_rsp(self, rsp_pb):
        """
        在收到实时k线数据推送后会回调到该函数，使用者需要在派生类中覆盖此方法

        注意该回调是在独立子线程中

        :param rsp_pb: 派生类中不需要直接处理该参数
        :return: 参见get_cur_kline的返回值
        """
        ret_code, msg, kline_list = CurKlinePush.unpack_rsp(rsp_pb)
        if ret_code == RET_ERROR:
            return ret_code, msg
        else:
            col_list = [
                'code', 'time_key', 'open', 'close', 'high', 'low', 'volume',
                'turnover', 'k_type', 'last_close'
            ]
            kline_frame_table = pd.DataFrame(kline_list, columns=col_list)

            return RET_OK, kline_frame_table


class TickerHandlerBase(RspHandlerBase):
    """
    异步处理推送的逐笔数据。

    .. code:: python

        class TickerTest(TickerHandlerBase):
            def on_recv_rsp(self, rsp_str):
                ret_code, data = super(TickerTest,self).on_recv_rsp(rsp_str)
                if ret_code != RET_OK:
                    print("CurKlineTest: error, msg: %s" % data)
                    return RET_ERROR, data

                print("TickerTest ", data) # TickerTest自己的处理逻辑

                return RET_OK, content
    """

    def on_recv_rsp(self, rsp_pb):
        """
        在收到实时逐笔数据推送后会回调到该函数，使用者需要在派生类中覆盖此方法

        注意该回调是在独立子线程中

        :param rsp_pb: 派生类中不需要直接处理该参数
        :return: 参见get_rt_ticker的返回值
        """
        ret_code, msg, ticker_list = TickerQuery.unpack_rsp(rsp_pb)
        if ret_code == RET_ERROR:
            return ret_code, msg
        else:

            col_list = [
                'code', 'time', 'price', 'volume', 'turnover',
                "ticker_direction", 'sequence'
            ]
            ticker_frame_table = pd.DataFrame(ticker_list, columns=col_list)

            return RET_OK, ticker_frame_table


class RTDataHandlerBase(RspHandlerBase):
    """
    异步处理推送的分时数据。

    .. code:: python

        class RTDataTest(RTDataHandlerBase):
            def on_recv_rsp(self, rsp_str):
                ret_code, data = super(RTDataTest,self).on_recv_rsp(rsp_str)
                if ret_code != RET_OK:
                    print("RTDataTest: error, msg: %s" % data)
                    return RET_ERROR, data

                print("RTDataTest ", data) # RTDataTest自己的处理逻辑

                return RET_OK, content
    """

    def on_recv_rsp(self, rsp_pb):
        """
        在收到实时逐笔数据推送后会回调到该函数，使用者需要在派生类中覆盖此方法

        注意该回调是在独立子线程中

        :param rsp_pb: 派生类中不需要直接处理该参数
        :return: 参见get_rt_data的返回值
        """
        ret_code, msg, rt_data_list = RtDataQuery.unpack_rsp(rsp_pb)
        if ret_code == RET_ERROR:
            return ret_code, msg
        else:

            col_list = [
                'code', 'time', 'is_blank', 'opened_mins', 'cur_price',
                "last_close", 'avg_price', 'turnover', 'volume'
            ]
            rt_data_table = pd.DataFrame(rt_data_list, columns=col_list)

            return RET_OK, rt_data_table


class BrokerHandlerBase(RspHandlerBase):
    """
    异步处理推送的经纪数据。

    .. code:: python

        class BrokerTest(BrokerHandlerBase):
            def on_recv_rsp(self, rsp_str):
                ret_code, data = super(BrokerTest,self).on_recv_rsp(rsp_str)
                if ret_code != RET_OK:
                    print("BrokerTest: error, msg: %s" % data)
                    return RET_ERROR, data

                print("BrokerTest ", data) # BrokerTest自己的处理逻辑

                return RET_OK, content
    """

    def on_recv_rsp(self, rsp_pb):
        """
        在收到实时经纪数据推送后会回调到该函数，使用者需要在派生类中覆盖此方法

        注意该回调是在独立子线程中

        :param rsp_pb: 派生类中不需要直接处理该参数
        :return: 参见get_broker_queue的返回值
        """
        ret_code, msg, (stock_code, bid_content, ask_content) = BrokerQueueQuery.unpack_rsp(
            rsp_pb)
        if ret_code != RET_OK:
            return ret_code, msg, None
        else:
            bid_list = [
                'code', 'bid_broker_id', 'bid_broker_name', 'bid_broker_pos'
            ]
            ask_list = [
                'code', 'ask_broker_id', 'ask_broker_name', 'ask_broker_pos'
            ]
            bid_frame_table = pd.DataFrame(bid_content, columns=bid_list)
            ask_frame_table = pd.DataFrame(ask_content, columns=ask_list)

            return RET_OK, stock_code, [bid_frame_table, ask_frame_table]


class HeartBeatHandlerBase(RspHandlerBase):
    """Base class for handling Heart Beat"""

    def on_recv_rsp(self, rsp_pb):
        """receive response callback function"""
        ret_code, msg, time = HeartBeat.unpack_rsp(rsp_pb)

        return ret_code, time


class SysNotifyHandlerBase(RspHandlerBase):
    """sys notify"""
    def on_recv_rsp(self, rsp_pb):
        """receive response callback function"""
        ret_code, content = SysNotifyPush.unpack_rsp(rsp_pb)

        return ret_code, content


class AsyncHandler_InitConnect(RspHandlerBase):
    """ AsyncHandler_TrdSubAccPush"""
    def __init__(self, notify_obj=None):
        self._notify_obj = notify_obj
        super(AsyncHandler_InitConnect, self).__init__()

    def on_recv_rsp(self, rsp_pb):
        """receive response callback function"""
        ret_code, msg, conn_info_map = InitConnect.unpack_rsp(rsp_pb)

        if self._notify_obj is not None:
            self._notify_obj.on_async_init_connect(ret_code, msg, conn_info_map)

        return ret_code, msg

