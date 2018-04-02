---
UID: NC:ks.PFNKSSETTIMER
title: PFNKSSETTIMER
author: windows-driver-content
description: A streaming minidriver's KStrSetTimer routine is called to generate DPC timer callbacks based on presentation time.
old-location: stream\kstrsettimer.htm
old-project: stream
ms.assetid: c9150c02-a53e-4ffc-8cf1-ca668680cdd9
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KStrSetTimer, KStrSetTimer routine [Streaming Media Devices], PFNKSSETTIMER, ks/KStrSetTimer, ksfunc_a1a590b8-ea16-45bd-8517-45e4bfc46ad3.xml, stream.kstrsettimer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: 
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	ks.h
api_name:
-	KStrSetTimer
product:
- Windows
targetos: Windows
req.typenames: SOUNDDETECTOR_PATTERNHEADER
---


# PFNKSSETTIMER callback function
A streaming minidriver's <i>KStrSetTimer</i> routine is called to generate DPC timer callbacks based on presentation time.

## Syntax

```
PFNKSSETTIMER Pfnkssettimer;

BOOLEAN Pfnkssettimer(
  PVOID Context,
  PKTIMER Timer,
  LARGE_INTEGER DueTime,
  PKDPC Dpc
)
{...}
```

## Parameters

`Context`

Pointer to the minidriver-supplied information context. The minidriver passes the information context to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560955">KsAllocateDefaultClockEx</a> in the function's <i>DeferredContext</i> parameter when the minidriver allocates a custom DPC timer object.

`Timer`

Pointer to a timer object allocated by the minidriver.

`DueTime`

Specifies the absolute or relative time at which the timer is to expire. If the value of the <i>DueTime</i> parameter is negative, the expiration time is relative to the current system time. Otherwise, the expiration time is absolute. The expiration time is expressed in system time units (100-nanosecond intervals). Absolute expiration times track any changes in the system time; relative expiration times are not affected by system time changes.

`Dpc`

Pointer to a DPC object that the minidriver initialized using <a href="https://msdn.microsoft.com/library/windows/hardware/ff552130">KeInitializeDpc</a>. This parameter is optional.


## Return Value

Returns <b>TRUE</b> if the timer object was already in the system timer queue. Otherwise, returns <b>FALSE</b>.

## Remarks

Minidrivers can optionally supply a <i>KStrSetTimer</i> callback function as an argument to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560955">KsAllocateDefaultClockEx</a>.

Typically, if a minidriver supplies a <i>KStrCorrelatedTime</i> callback function, then the minidriver also supplies a <i>KStrSetTimer</i> callback function.

If minidrivers supply a <i>KStrSetTimer</i> callback function, the function must set timers, based on deltas, to the current presentation time in order to generate event notifications.

If a minidriver supplies a <i>KStrSetTimer</i> callback function, the minidriver must also supply a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567156">KStrCancelTimer</a> callback function to cancel the timer.

The minidriver supplied <i>KStrSetTimer</i> must have the same characteristics as <a href="https://msdn.microsoft.com/library/windows/hardware/ff553292">KeSetTimerEx</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff567156">KStrCancelTimer</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552130">KeInitializeDpc</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553292">KeSetTimerEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560955">KsAllocateDefaultClockEx</a>