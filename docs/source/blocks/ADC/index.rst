
.. toctree::
  :maxdepth: 2
  
    
模拟数字转换器 (ADC)
=====================

概述
----
SWM221内置2个12位高精度SAR ADC，采样率高达1MSPS，每个ADC支持10通道。


特性
----
-  支持单次模式和连续模式

-  灵活的转换启动方式，支持软件、PWM、TIMER启动

-  每个通道都有自己独立的转换结果数据寄存器和转换完成、数据溢出状态寄存器

-  支持DMA传输

-  内嵌1路温度传感器 (TEMPSENSE)


功能描述
--------
.. include:: functions.rst

寄存器映射
----------
.. include:: regs_map.rst


寄存器描述
----------
.. include:: regs_tables.rst

