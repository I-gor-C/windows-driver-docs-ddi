---
UID : NF:wdm.WRITE_PORT_BUFFER_USHORT
title : WRITE_PORT_BUFFER_USHORT function
author : windows-driver-content
description : The WRITE_PORT_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified port address.
old-location : kernel\write_port_buffer_ushort.htm
old-project : kernel
ms.assetid : e715c0b5-8f72-4642-9a48-2066df0a2650
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : WRITE_PORT_BUFFER_USHORT routine [Kernel-Mode Driver Architecture], kernel.write_port_buffer_ushort, wdm/WRITE_PORT_BUFFER_USHORT, WRITE_PORT_BUFFER_USHORT, k103_c8549446-4478-4c5d-82c2-55e963c81cf3.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdm.h
req.include-header : Wdm.h, Ntddk.h, Ntifs.h
req.target-type : Universal
req.target-min-winverclnt : Available starting with Windows 2000.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Hal.lib
req.dll : 
req.irql : Any level (see Remarks section)
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WORK_QUEUE_TYPE
req.product : Windows 10 or later.
---


# WRITE_PORT_BUFFER_USHORT function
The <b>WRITE_PORT_BUFFER_USHORT</b> routine writes a number of USHORT values from a buffer to the specified port address.

## Syntax

````
 VOID WRITE_PORT_BUFFER_USHORT(
  _In_ PUSHORT Port,
  _In_ PUSHORT Buffer,
  _In_ ULONG   Count
);
````

## Parameters

`Port`

Pointer to the port, which must be a mapped memory range in I/O space.

`Buffer`

Pointer to a buffer from which an array of USHORT values is to be written.

`Count`

Specifies the number of USHORT values to be written to the port.


## Return Value

None

## Remarks

The size of the buffer must be large enough to contain at least the specified number of USHORT values.

Callers of <b>WRITE_PORT_BUFFER_USHORT</b> can be running at any IRQL, assuming the <i>Buffer</i> is resident and the <i>Port</i> is resident, mapped device memory.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** |  |
| **IRQL** | Any level (see Remarks section) |
| **DDI compliance rules** |  |