# pythonLoader
url:/python/load
将某个指定的脚本挂载到管理器内
调用:
| 名称   | 位置 | 类型 | 必选 | 说明                   |
|--------|------|------|------|------------------------|
| pth | pth | string | 是   | python脚本相对位置     |

返回:
{
    "id":脚本全局唯一的id,
    "err":如果是0 则没有错误，如果是1 则是管理器被暂停
    "errText":其他错误内容
}

url:
/python/unload
将某个指定脚本取消挂载
调用:
| 名称   | 位置 | 类型 | 必选 | 说明                   |
|--------|------|------|------|------------------------|
| id | pth | string | 是  | python脚本id     |

返回:
{
    "err":如果是0 则没有错误，如果是1 则是脚本未被挂载或者不存在，如果是2则是脚本被占用，如果是3则是其他错误
    "errText":其他错误内容
}

url:
/python/forceunload
强制将某个指定脚本取消挂载
调用:
| 名称   | 位置 | 类型 | 必选 | 说明                   |
|--------|------|------|------|------------------------|
| id | pth | string | 是  | python脚本id     |

返回:
{
    "err":如果是0 则没有错误，如果是1 则是脚本未被挂载或者不存在，如果是2则是其他错误
}

url:
/python/isRun
某个脚本是否在运行
调用:
| 名称   | 位置 | 类型 | 必选 | 说明                   |
|--------|------|------|------|------------------------|
| id | pth | string | 是  | python脚本id     |

返回:
{
    "err":如果是0 则没有错误，如果是1 则是脚本未被挂载或者不存在
    "errText":其他错误内容
    "isrun":boolean类型，脚本是否在运行
}

url:
/python/isLoaded
某个脚本是否被挂载
调用:
| 名称   | 位置 | 类型 | 必选 | 说明                   |
|--------|------|------|------|------------------------|
| id | pth | string | 是  | python脚本id     |

返回:
{
    "err":如果是0 则没有错误
    "isloaded":boolean类型，是否被挂载
}

url:
/python/stop
终止python管理器运行，再启动需要使用脚本管理器启动
调用:

返回:
{
    "err":如果是0 则没有错误，如果是1 则python管理器被占用，如果是2 则是其他错误
    "errText":其他错误内容
}

url:
/python/pause
暂停python管理器运行，此时python管理器不再接收新的脚本运行指令，以及load脚本指令，并且在运行完成目前的脚本后等待start命令
调用:

返回:
{
    "err":如果是0 则没有错误，如果是1 则是其他错误
    "errText":其他错误内容
}

url:
/python/start
解除python管理器的暂停状态
调用:

返回:
{
    "err":如果是0 则没有错误，如果是1 则是其他错误
    "errText":其他错误内容
}

url:
获取python管理器状态
/python/status
调用:

返回:
{
    "status":runing/pausing/err
    "loadedscripts":所有被加载的脚本的id列表
    "runningscripts":所有正在运行的脚本的id列表
}

url:
根据id获取文件相对位置
/python/getpth
调用:
| 名称   | 位置 | 类型 | 必选 | 说明                   |
|--------|------|------|------|------------------------|
| id | pth | string |  是 | python脚本id     |

返回:
{
    "pth":python脚本相对路径
}

url:
根据pth获取该pth下的一系列被加载脚本的id
/python/getid
调用:
| 名称   | 位置 | 类型 | 必选 | 说明                   |
|--------|------|------|------|------------------------|
| pth | pth | string |  是 | python脚本pth    |

返回:
{
    "id":[id]
}



