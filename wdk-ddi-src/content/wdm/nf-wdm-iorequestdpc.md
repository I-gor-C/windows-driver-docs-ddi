---
UID: NF:wdm.IoRequestDpc
title: IoRequestDpc function
author: windows-driver-content
description: The IoRequestDpc routine queues a driver-supplied DpcForIsr routine to complete interrupt-driven I/O processing at a lower IRQL.
old-location: kernel\iorequestdpc.htm
old-project: kernel
ms.assetid: 196555c8-74a6-4dae-ac4d-52654015ffeb
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: IoRequestDpc, IoRequestDpc routine [Kernel-Mode Driver Architecture], k104_37f449eb-de3d-4932-b845-388c73c55d01.xml, kernel.iorequestdpc, wdm/IoRequestDpc
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DIRQL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Wdm.h
api_name:
-	IoRequestDpc
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# IoRequestDpc function
The <b>IoRequestDpc</b> routine queues a driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff544079">DpcForIsr</a> routine to complete interrupt-driven I/O processing at a lower IRQL.

## Syntax

```
void IoRequestDpc(
  PDEVICE_OBJECT         DeviceObject,
  PIRP                   Irp,
  __drv_aliasesMem PVOID Context
);
```

## Parameters

`DeviceObject`

Pointer to the device object for which the request that caused the interrupt is being processed.

`Irp`

Pointer to the current IRP for the specified device.

`Context`

Pointer to a driver-determined context to be passed to the DPC routine.


## Return Value

None

## Remarks

Callers of <b>IoRequestDpc</b> must be running at DIRQL.

Drivers call  <b>IoRequestDpc</b> from an <a href="https://msdn.microsoft.com/library/windows/hardware/ff547958">InterruptService</a> routine. Because of this, <b>IoRequestDpc</b> runs at the DIRQL value that was specified by <i>SynchronizeIrql</i> when the driver called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a>. However, it is also possible to queue a DPC at any IRQL &gt;= DISPATCH_LEVEL by using the <b>Ke<i>Xxx</i>Dpc</b> routines. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565664">Which Type of DPC Should You Use?</a>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Desktop |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **IRQL** | DIRQL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549307">IoInitializeDpcRequest</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552130">KeInitializeDpc</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552185">KeInsertQueueDpc</a>