
.. toctree::
  :maxdepth: 2
  
    
QSPI总线控制器 (QSPI)
=========================

概述
----
QSPI 专用于和外部存储器通信的接口，支持单线，双线，四线模式。

特性
----
-  AHB Slave接口：CPU Master/DMA通过AHB访问QSPI接口模块

-  QSPI Master接口：可访问外置SPI Flash

-  三种功能模式：间接模式、状态轮询模式、内存映射模式

-  集成 FIFO，用于发送和接收

-  允许 8、16 和 32 位数据访问

-  在达到 FIFO 阈值、超时、操作完成以及发生访问错误时产生中断


功能描述
--------
.. include:: functions.rst


寄存器映射
----------
.. include:: regs_map.rst


寄存器描述
----------
.. include:: regs_tables.rst

