
.. toctree::
  :maxdepth: 2
  
    
I2C 总线控制器 (I2C)
=========================

概述
----
SWM221 系列所有型号 I2C 操作均相同，不同型号 I2C 模块数量可能不同。使用前需使能对应 I2C 模块时钟。

I2C 模块提供了 Master 模式及 Slave 模式，基本操作及配置详见功能描述章节。

特性
----

-  支持通过 APB 总线进行配置

-  支持 Master, Slave 两种模式

-  支持 I2C 输入信号数字滤波

-  支持 Standard-mode（100kbps）、Fast-mode（400kbps）、Fast-mode Plus（1Mbps）、High-speed mode（3.4Mbps）

-  SCL/SDA 线上数据可读

-  Master 模式特性：

   -  支持 Clock Synchronization

   -  支持多 Master 总线仲裁

   -  支持 Clock Stretching，Slave 器件可通过拉低 SCL 延长时钟来占据总线

   -  支持 SCL LOW 超时报警

   -  支持读、写操作

   -  支持发出的SCL时钟周期最大为（2\ :sup:`17`） x PCLK

   -  SCL 时钟占空比可配置

-  Slave 模式特性：

   -  支持多 Slave

   -  支持7位、10位两种地址模式

   -  支持地址 Mask，一个 Slave 器件可以占用多个地址

      -  7位地址模式，一个 Slave 器件最多可占用128个地址

      -  10位地址模式，一个 Slave 器件最多可占用256个地址

   -  支持 Clock Stretching，通过拉低 SCL 延长时钟占据总线

   -  支持读、写操作


功能描述
--------
.. include:: functions.rst


寄存器映射
----------
.. include:: regs_map.rst


寄存器描述
----------
.. include:: regs_tables.rst

