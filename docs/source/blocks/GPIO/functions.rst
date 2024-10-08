
数据控制
^^^^^^^^^^

除 SWD 引脚与 ISP 引脚外，所有引脚上电后默认状态均为 GPIO 浮空输入（DIR = 0）。

.. note:: SWD 引脚可在加密章节进行修改 ，ISP 引脚默认下拉使能，保证浮空状态不会进入 ISP 模式。

GPIO方向寄存器（DIRx）用来将每个独立的管脚配置为输入模式或者输出模式：

-  当数据方向设为0时，GPIO对应引脚配置为输入

   通过读取相应数据寄存器（IDRx）对应位或对应 DATAPINx 寄存器获取指定GPIO端口当前状态值

-  当数据方向设为1时，GPIO对应引脚配置为输出

   通过向对应端口数据寄存器（ODRx）对应位或对应DATAPINx寄存器写入值改变指定引脚输出，0输出低电平，1输出高电平。
   DATAPINx 寄存器可以直接控制对应端口，对其他端口无影响，无需经过读后写。

GPIOA/GPIOB/GPIOC 端口为 AHB IO，挂载于AHB总线，对于读取和写入操作，均为命令发出后的1个周期完成。


中断控制与清除
^^^^^^^^^^^^^^

可根据需求将 GPIO 端口对应引脚配置为中断模式，并通过相关寄存器配置中断极性及触发方式。触发方式分为边沿触发和电平触发两种模式。

-  对于边沿触发中断，可以设置为上升沿触发，下降沿触发或双边沿触发。中断发生后，标志位具备保持特性，必须通过软件对中断标志位进行清除。

-  对于电平触发中断，当外部引脚输入为指定电平时，中断发生。当电平翻转后，中断信号消失，无需软件进行清除。
   使用电平触发中断，需保证外部信号源保持电平稳定，以便有效中断电平能被端口识别。

使用以下寄存器来对产生中断触发方式和极性进行定义：

-  GPIO中断触发条件寄存器（INTLVLTRG），用于配置电平触发或边沿触发

-  GPIO中断触发极性寄存器（INTRISEEN），用于配置电平或边沿触发极性

-  GPIO中断边沿触发配置寄存器（INTBE），选择为边沿触发后，用于配置单边沿触发或双边沿触发

通过GPIO中断使能寄存器（INTEN）可以使能或者禁止相应端口对应位中断，GPIO原始中断状态（INTRAWSTAUS）不受使能位影响。

当产生中断时，可以在GPIO原始中断状态（RAWINTSTAUS）获取中断信号的状态。
当中断使能寄存器（INTEN）对应位为1时，中断状态（INTSTAUS）寄存器可读取到对应中断信号，且中断信号会进入中断配置模块及NVIC模块，执行中断程序。

通过写1到GPIO中断清除寄存器（INTCLR）指定位可以清除相应位中断。
