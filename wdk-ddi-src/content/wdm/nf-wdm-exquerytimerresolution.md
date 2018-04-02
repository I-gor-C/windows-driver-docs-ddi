---
UID: NF:wdm.ExQueryTimerResolution
title: ExQueryTimerResolution function
author: windows-driver-content
description: The ExQueryTimerResolution routine reports the range of timer resolutions that are supported by the system clock.
old-location: kernel\exquerytimerresolution.htm
old-project: kernel
ms.assetid: 2648AD10-B2D7-4F24-A508-239DA6AF551D
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: ExQueryTimerResolution, ExQueryTimerResolution routine [Kernel-Mode Driver Architecture], kernel.exquerytimerresolution, wdm/ExQueryTimerResolution
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
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
req.lib: Ntoskrnl.lib
req.dll: 
req.irql: Any level.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	ntoskrnl.lib
-	ntoskrnl.dll
api_name:
-	ExQueryTimerResolution
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# ExQueryTimerResolution function
The <b>ExQueryTimerResolution</b> routine reports the range of timer resolutions that are supported by the system clock.

## Syntax

```
NTKERNELAPI VOID ExQueryTimerResolution(
  PULONG MaximumTime,
  PULONG MinimumTime,
  PULONG CurrentTime
);
```

## Parameters

`MaximumTime`

A pointer to a location to which the routine writes the maximum time interval, in 100-nanosecond units, between successive ticks of the system clock. A <i>tick</i> is an interrupt caused by the system clock timer.

`MinimumTime`

A pointer to a location to which the routine writes the minimum time interval, in 100-nanosecond units, between successive ticks of the system clock.

`CurrentTime`

A pointer to a location to which the routine writes the current time interval, in 100-nanosecond units, between successive ticks of the system clock.


## Return Value

None.

## Remarks

If your driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545614">ExSetTimerResolution</a> routine to change the time interval between successive system clock interrupts, the driver can first call <b>ExQueryTimerResolution</b> to determine the range of intervals supported by the system clock.

When your driver calls a routine such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff553292">KeSetTimerEx</a> to set a timer, the accuracy of the timer depends on the resolution of the system clock. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/jj602805">Timer Accuracy</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 8.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | Ntoskrnl.lib |
| **IRQL** | Any level. |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff545614">ExSetTimerResolution</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553292">KeSetTimerEx</a>