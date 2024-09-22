
.. toctree::
  :maxdepth: 2
  
    
USART接口控制器 (USART)
=========================

概述
----
USART 除了支持普通UART的功能外，还支持更完善的LIN功能。

特性
----
-  5-9位数据，1、1.5或2位停止位

-  奇偶校验位发送和检测，帧错误检测，溢出错误检测

-  支持先发送高位、或先发送低位可配

-  支持接收超时中断、超时时间可配

-  LIN支持主/从模式，遵循LIN 1.3和LIN 1.2协议规格

-  LIN从机模式支持自同步功能


功能描述
--------
.. include:: functions.rst

寄存器映射
----------
.. include:: regs_map.rst


寄存器描述
----------
.. include:: regs_tables.rst

