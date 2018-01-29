---
UID : NS:pepfx._PEP_PROCESSOR_IDLE_STATE_V2
title : _PEP_PROCESSOR_IDLE_STATE_V2
author : windows-driver-content
description : The PEP_PROCESSOR_IDLE_STATE_V2 structure describes a processor idle state that the platform extension plug-in (PEP) supports.
old-location : kernel\pep_processor_idle_state_v2.htm
old-project : kernel
ms.assetid : DEA8B166-5236-4BE3-B16D-9EE1B34796F8
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : pepfx/PPEP_PROCESSOR_IDLE_STATE_V2, PPEP_PROCESSOR_IDLE_STATE_V2 structure pointer [Kernel-Mode Driver Architecture], _PEP_PROCESSOR_IDLE_STATE_V2, pepfx/PEP_PROCESSOR_IDLE_STATE_V2, PEP_PROCESSOR_IDLE_STATE_V2, kernel.pep_processor_idle_state_v2, PEP_PROCESSOR_IDLE_STATE_V2 structure [Kernel-Mode Driver Architecture], PPEP_PROCESSOR_IDLE_STATE_V2, *PPEP_PROCESSOR_IDLE_STATE_V2
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : pepfx.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Supported starting with Windows 10.
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
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PPEP_PROCESSOR_IDLE_STATE_V2, PEP_PROCESSOR_IDLE_STATE_V2"
---

# _PEP_PROCESSOR_IDLE_STATE_V2 structure
The <b>PEP_PROCESSOR_IDLE_STATE_V2</b> structure describes a processor idle state that the platform extension plug-in (PEP) supports.

## Syntax
````
typedef struct _PEP_PROCESSOR_IDLE_STATE_V2 {
  union {
    ULONG  Ulong;
    struct {
      ULONG Interruptible  :1;
      ULONG CacheCoherent  :1;
      ULONG ThreadContextRetained  :1;
      ULONG CStateType  :4;
      ULONG WakesSpuriously  :1;
      ULONG PlatformOnly  :1;
      ULONG Autonomous  :1;
      ULONG Reserved  :22;
    };
  };
  ULONG Latency;
  ULONG BreakEvenDuration;
} PEP_PROCESSOR_IDLE_STATE_V2, *PPEP_PROCESSOR_IDLE_STATE_V2;
````

## Members


`BreakEvenDuration`

The minimum amount of time, specified in 100-nanosecond units, that the processor must spend in this idle state to make a transition to this state worthwhile. The Windows <a href="https://msdn.microsoft.com/B08F8ABF-FD43-434C-A345-337FBB799D9B">power management framework</a> (PoFx) uses this member value as a hint to avoid switching a processor to an idle state unless the processor is likely to remain in this state for at least the amount of time specified by <b>BreakEvenDuration</b>.

`Latency`

The worst-case latency, in 100-nanosecond units,  that the processor requires to wake from this idle state in response to a wake event.

## Remarks
This structure is used in conjunction with the <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186824">PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2</a> notification. The <b>IdleStates</b>  member of the <a href="..\pepfx\ns-pepfx-_pep_ppm_query_idle_states_v2.md">PEP_PPM_QUERY_IDLE_STATES_V2</a> structure is the first element in an array of <b>PEP_PROCESSOR_IDLE_STATE_V2</b> structures.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | pepfx.h |

## See Also

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186824">PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2</a>

<a href="..\pepfx\ns-pepfx-_pep_ppm_query_idle_states_v2.md">PEP_PPM_QUERY_IDLE_STATES_V2</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PROCESSOR_IDLE_STATE_V2 structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>