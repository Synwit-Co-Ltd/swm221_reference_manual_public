
模块结构框图
^^^^^^^^^^^^^^^^^

PGA 模块结构如 :numref:`PGA模块结构框图` 所示。

.. _PGA模块结构框图:
.. figure:: ./images/PGA模块结构框图.svg
   :align: center
   :scale: 100%


   PGA模块结构框图


功能描述
^^^^^^^^^^

本芯片拥有PGA0、PGA1、PGA2共3个可编程增益运放（PGA），PGA的内部参考电压可设为1.2V、1.8V、2.25V和VREF_ADC/2（可配置PGAREF寄存器），PGA的放大倍数（x1、x5、x10、x20）可通过配置PGACR寄存器的GAIN位决定，可经开关输出到OPAxOUT，开关可选100ohm/1kohm/10kohm。

**ADC采样**


PGA输出可通过使能PGACR的BUFEN位驱动内部ADC的采样通道，此时需正常配置ADC对应通道，对应关系如下表所示：

.. list-table::
   :widths: 36 36
   :header-rows: 1

   - 

      - PGA输出
      - ADC通道
   - 

      - PGA0OUT
      - ADC0_CH3
   - 

      - PGA1OUT
      - ADC0_CH4
   - 

      - PGA1OUT
      - ADC1_CH4
   - 

      - PGA2OUT
      - ADC1_CH5

**OPA功能**

当PGAx设置为运放模式的时候，连接到PGA_VREF的电阻和反馈电阻都会断开，可以作为差分输入单端输出运放使用。

