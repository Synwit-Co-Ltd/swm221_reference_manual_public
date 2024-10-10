
.. toctree::
  :maxdepth: 2
  
    
嵌套向量中断控制器 (NVIC)
============================

概述
----

Cortex-M0提供了“嵌套向量中断控制器（NVIC）”用以管理中断事件。

中断优先级分为4级，可通过中断优先级配置寄存器（IRQn）进行配置。中断发生时，内核比较中断优先级，并自动获取入口地址，并保护环境，将指定寄存器中数据入栈，无需软件参与。中断服务程序结束后，由硬件完成出栈工作。同时支持“尾链”模式及“迟至”模式，有效的优化了中断发生及背对背中断的执行效率，提高了中断的实时性。

更多细节请参阅 “Cortex®-M0 技术参考手册” 及 “ARM® CoreSight 技术参考手册”。



特性
----

-  支持嵌套及向量中断
-  硬件完成现场的保存和恢复
-  动态改变优先级
-  确定的中断时间



中断向量表
-----------

SWM231提供了32个中断供外设与核交互，其排列如 :numref:`nvic_table` 所示。可以通过中断配置模块，将任意模块或具体IO的中断连接至指定中断编号。具体使用参考中断配置模块。


.. _nvic_table:
.. list-table:: 中断向量表
   :header-rows: 1
   :widths: 28 44
   :class: table-left-align

   - 

      - 中断源
      - 外设中断
   - 

      - 0
      - UART0
   - 

      - 1
      - TIMER0
   - 

      - 2
      - CAN0
   - 

      - 3
      - UART1
   - 

      - 4
      - PWM_CH1
   - 

      - 5
      - TIMER1
   - 

      - 6
      - HALL
   - 

      - 7
      - PWM_CH0
   - 

      - 8
      - QSPI0
   - 

      - 9
      - PWM_HALT
   - 

      - 10
      - USART
   - 

      - 11
      - WDT
   - 

      - 12
      - I2C0
   - 

      - 13
      - XTAL_STOP_DET
   - 

      - 14
      - SARADC0
   - 

      - 15
      - CMP
   - 

      - 16
      - BTIMER0
   - 

      - 17
      - BTIMER1
   - 

      - 18
      - BTIMER2
   - 

      - 19
      - BTIMER3
   - 

      - 20
      - GPIOA
   - 

      - 21
      - GPIOB
   - 

      - 22
      - GPIOC
   - 

      - 23
      - GPIOA0/GPIOC0
   - 

      - 24
      - GPIOA1/GPIOC1/
   - 

      - 25
      - GPIOA2/GPIOC2/MPU
   - 

      - 26
      - GPIOA3/GPIOC3/BOD
   - 

      - 27
      - GPIOB0/GPIOA8/TIMER2
   - 

      - 28
      - GPIOB1/GPIOA9/DMA
   - 

      - 29
      - GPIOB2/GPIOA10/DIV
   - 

      - 30
      - GPIOB3/GPIOA11/SPI0
   - 

      - 31
      - GPIOB4/GPIOB10/QEI
