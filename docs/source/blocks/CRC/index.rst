
.. toctree::
  :maxdepth: 2
  
    
循环冗余校验器 (CRC)
=====================

概述
----
SWM221系列所有型号CRC模块操作均相同，主要应用于核实数据传输或者数据存储的正确性和完整性，使用前需使能CRC模块时钟。

CRC模块分为CRC-32和CRC-16两个算法。使用CRC-32多项式进行计算时，输入数据有效位宽可选择为32Bit、16Bit、8Bit，使用CRC-16多项式进行计算时，输入数据有效位宽可选择16Bit、8Bit。


特性
----
-  支持CRC-32码多项式

   -  x\ :sup:`32` + x\ :sup:`26` + x\ :sup:`23` + x\ :sup:`22` + x\ :sup:`16` + x\ :sup:`12` + x\ :sup:`11` + x\ :sup:`10` + x\ :sup:`8` + x\ :sup:`7` + x\ :sup:`5` + x\ :sup:`4` + x\ :sup:`2` + x + 1

-  支持CRC-16码多项式

   -  x\ :sup:`16` + x\ :sup:`12` + x\ :sup:`5` + 1 
   -  x\ :sup:`16` + x\ :sup:`15` + x\ :sup:`2` + 1

-  支持CRC-16码多项式

   -  x\ :sup:`8` + x\ :sup:`2` + x + 1

-  支持输出结果设置，包括翻转、取反

-  支持初始值自定义

-  支持输入可选择取反


功能描述
--------
.. include:: functions.rst


寄存器映射
----------
.. include:: regs_map.rst


寄存器描述
----------
.. include:: regs_tables.rst

