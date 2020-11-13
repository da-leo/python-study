import asyncio
from multiprocessing import Process

from zf_es_analysis import AsyncESAnalysis


def async_fun(i):
    """
    多协程
    :return:
    """
    query = {
        "size": 20,
        "from": 0,
        "query": {
            "bool": {
                "filter": [
                    {
                        "term": {
                            "site_id": 1
                        }
                    }, {
                        "term": {
                            "amz_asin": 'B0862LLWJT'
                        }
                    }, {
                        "term": {
                            "is_buybox": 1
                        }
                    },
                    {
                        "term": {
                            "is_show": 1
                        }
                    }]
            }
        }
    }
    # data = {"size":10,"from":0}
    filter_data = {}
    # 日志文件名
    log_file_name = 'test'
    loop = asyncio.get_event_loop()
    # async_es = AsyncESAnalysis(es_instance='es_common_us', log_file_name=log_file_name, scene='offline', host_type=1)
    async_es = AsyncESAnalysis(es_instance='es_amazon_us', log_file_name=log_file_name, scene='offline', host_type=1)
    task = []
    for i in range(100):
        get_future = asyncio.ensure_future(async_es.async_query(url='#', body=query, filter_data=filter_data))
        # get_future = asyncio.ensure_future(
        #     async_es.async_query(url='#', body=data, filter_data=filter_data))
        task.append(asyncio.ensure_future(get_future))
    loop.run_until_complete(asyncio.wait(task))
    for ta in task:
        print(ta.result())
    loop.run_until_complete(async_es.close())


def process_fun():
    p_list = []
    for i in range(10):
        p = Process(target=async_fun, args=(i,))
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join()


process_fun()
# async_fun(1)
