---
UID: NS:pepfx._PEP_PROCESSOR_IDLE_STATE_V2
title: "_PEP_PROCESSOR_IDLE_STATE_V2"
author: windows-driver-content
description: The PEP_PROCESSOR_IDLE_STATE_V2 structure describes a processor idle state that the platform extension plug-in (PEP) supports.
old-location: kernel\pep_processor_idle_state_v2.htm
old-project: kernel
ms.assetid: DEA8B166-5236-4BE3-B16D-9EE1B34796F8
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PPEP_PROCESSOR_IDLE_STATE_V2, PEP_PROCESSOR_IDLE_STATE_V2, PEP_PROCESSOR_IDLE_STATE_V2 structure [Kernel-Mode Driver Architecture], PPEP_PROCESSOR_IDLE_STATE_V2, PPEP_PROCESSOR_IDLE_STATE_V2 structure pointer [Kernel-Mode Driver Architecture], _PEP_PROCESSOR_IDLE_STATE_V2, kernel.pep_processor_idle_state_v2, pepfx/PEP_PROCESSOR_IDLE_STATE_V2, pepfx/PPEP_PROCESSOR_IDLE_STATE_V2"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: Pep_x.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	pepfx.h
api_name:
-	PEP_PROCESSOR_IDLE_STATE_V2
product: Windows
targetos: Windows
req.typenames: PEP_PROCESSOR_IDLE_STATE_V2, *PPEP_PROCESSOR_IDLE_STATE_V2
---

# _PEP_PROCESSOR_IDLE_STATE_V2 structure
The <b>PEP_PROCESSOR_IDLE_STATE_V2</b> structure describes a processor idle state that the platform extension plug-in (PEP) supports.

## Syntax
```
typedef struct _PEP_PROCESSOR_IDLE_STATE_V2 {
  union {
    ULONG Ulong;
    struct {
      ULONG  : 1  Interruptible;
      ULONG  : 1  CacheCoherent;
      ULONG  : 1  ThreadContextRetained;
      ULONG  : 4  CStateType;
      ULONG  : 1  WakesSpuriously;
      ULONG  : 1  PlatformOnly;
      ULONG  : 1  Autonomous;
      ULONG  : 22 Reserved;
    };
  };
  ULONG Latency;
  ULONG BreakEvenDuration;
} *PPEP_PROCESSOR_IDLE_STATE_V2, PEP_PROCESSOR_IDLE_STATE_V2;
```

## Members


`Latency`

The worst-case latency, in 100-nanosecond units,  that the processor requires to wake from this idle state in response to a wake event.

`BreakEvenDuration`

The minimum amount of time, specified in 100-nanosecond units, that the processor must spend in this idle state to make a transition to this state worthwhile. The Windows <a href="https://msdn.microsoft.com/B08F8ABF-FD43-434C-A345-337FBB799D9B">power management framework</a> (PoFx) uses this member value as a hint to avoid switching a processor to an idle state unless the processor is likely to remain in this state for at least the amount of time specified by <b>BreakEvenDuration</b>.

## Remarks
This structure is used in conjunction with the <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186824">PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2</a> notification. The <b>IdleStates</b>  member of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186824">PEP_PPM_QUERY_IDLE_STATES_V2</a> structure is the first element in an array of <b>PEP_PROCESSOR_IDLE_STATE_V2</b> structures.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | pepfx.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186824">PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt186824">PEP_PPM_QUERY_IDLE_STATES_V2</a>