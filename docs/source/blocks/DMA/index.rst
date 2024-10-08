
.. toctree::
  :maxdepth: 2
  
    
直接内存存取控制器 (DMA)
=========================

概述
----

DMA模块支持特定外设（UART，USART，SPI，QSPI，SARADC，MPU）和存储器（SRAM）之间或总线地址和存储器（SRAM）之间的高速数据传输，无需CPU干涉，数据可以快速的通过DMA传输，从而节省了CPU的资源来做其他操作。


特性
----

-  2个独立的可配置的通道

-  每个通道都直接连接专用的硬件DMA请求，每个通道都同样支持软件触发。这些功能通过软件来配置

-  多个请求间的优先权可以通过软件编程设置，优先权设置相等时由硬件决定(请求0优先于请求1，依此类推)

-  支持传输宽度（字节、半字、全字）可配置。源和目标地址必须按数据传输宽度对齐

-  支持循环的缓冲器管理

-  支持步进 （TIMER触发） 传输

-  每个通道都有3个事件标志（DMA自定义数目传输完成、DMA传输完成和DMA传输出错），这3个事件标志逻辑或成为一个单独的中断请求。

-  支持存储器和存储器间的传输

-  支持外设和存储器、存储器和外设之间的传输

-  可编程的数据传输数目：最大为65535
  


功能描述
--------
.. include:: functions.rst


寄存器映射
----------
.. include:: regs_map.rst


寄存器描述
----------
.. include:: regs_tables.rst

