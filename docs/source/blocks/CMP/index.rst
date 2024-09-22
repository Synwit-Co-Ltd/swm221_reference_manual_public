
.. toctree::
  :maxdepth: 2
  
    
比较器 (CMP)
=====================

概述
----
SWM221内置2个模拟比较器。电气特性一样，输入和输出可灵活配置，很好覆盖电机驱动应用需求。

特性
----
-  迟滞设置：无，10mV，20mV或50mV

-  内置1路8位DAC，负端可直接使用DAC参考输出

-  内置DAC参考电压可配置：1.2V，3.6V或VDD

-  输出作为PWM刹车输入使能

-  比较器翻转中断

-  输出数字滤波


功能描述
--------
.. include:: functions.rst

寄存器映射
----------
.. include:: regs_map.rst


寄存器描述
----------
.. include:: regs_tables.rst

