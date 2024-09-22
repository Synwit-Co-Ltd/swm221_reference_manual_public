
.. toctree::
  :maxdepth: 2
  
    
FLASH 控制器与 ISP 操作
=========================

概述
----

SWM221系列内置FLASH。可以通过调用IAP函数或寄存器读写的方式进行FLASH操作。

.. important:: 操作FLASH前，需要关闭中断，防止打断造成写入错误。


特性
----
-  支持ISP（在系统编程）更新用户程序

-  支持FLASH编程

-  支持BOOT自定义

-  支持加密


功能描述
--------
.. include:: functions.rst

寄存器映射
----------
.. include:: regs_map.rst


寄存器描述
----------
.. include:: regs_tables.rst

