
.. toctree::
  :maxdepth: 2
  
    
MPU接口 (MPU)
=================

概述
----
SWM221系列所有型号MPU模块操作均相同。使用前需使能MPU模块时钟。


特性
----
-  8位 MPU 数据接口位宽

-  半字或字访问时，硬件自动发出两个连续的 MPU 读或写事务。

-  支持MPU接口

   -  接口时序可调

   -  输出时钟可配置为空闲时关闭

   -  通过CPU或者DMA工作


功能描述
--------
.. include:: functions.rst

寄存器映射
----------
.. include:: regs_map.rst


寄存器描述
----------
.. include:: regs_tables.rst

