---
UID: NS:pepfx._PEP_PPM_IDLE_EXECUTE_V2
title: "_PEP_PPM_IDLE_EXECUTE_V2"
author: windows-driver-content
description: The PEP_PPM_IDLE_EXECUTE_V2 structure specifies the idle state that the processor is to enter.
old-location: kernel\pep_ppm_idle_execute_v2.htm
old-project: kernel
ms.assetid: 28CF8291-E7C3-4289-909C-C89D350A9D83
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PPEP_PPM_IDLE_EXECUTE_V2, PEP_PPM_IDLE_EXECUTE_V2, PEP_PPM_IDLE_EXECUTE_V2 structure [Kernel-Mode Driver Architecture], PPEP_PPM_IDLE_EXECUTE_V2, PPEP_PPM_IDLE_EXECUTE_V2 structure pointer [Kernel-Mode Driver Architecture], _PEP_PPM_IDLE_EXECUTE_V2, kernel.pep_ppm_idle_execute_v2, pepfx/PEP_PPM_IDLE_EXECUTE_V2, pepfx/PPEP_PPM_IDLE_EXECUTE_V2"
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
-	PEP_PPM_IDLE_EXECUTE_V2
product:
- Windows
targetos: Windows
req.typenames: PEP_PPM_IDLE_EXECUTE_V2, *PPEP_PPM_IDLE_EXECUTE_V2
---

# _PEP_PPM_IDLE_EXECUTE_V2 structure
The <b>PEP_PPM_IDLE_EXECUTE_V2</b> structure specifies the idle state that the processor is to enter.

## Syntax
```
typedef struct _PEP_PPM_IDLE_EXECUTE_V2 {
  NTSTATUS Status;
  ULONG    ProcessorState;
  ULONG    PlatformState;
  ULONG    CoordinatedStateCount;
  PULONG   CoordinatedStates;
} PEP_PPM_IDLE_EXECUTE_V2, *PPEP_PPM_IDLE_EXECUTE_V2;
```

## Members


`Status`

[out] An <b>NTSTATUS</b> value that indicates whether the processor idle state transition was successful. The platform extension plug-in (PEP) sets this member to <b>STATUS_SUCCESSFUL</b> if the transition succeeded. Otherwise, this member is set to an appropriate error status code.

`ProcessorState`

[in] The index of the processor idle state that the processor is to enter. The PEP previously specified the supported processor idle states in response to a <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186824">PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2</a> notification. If the PEP specified N processor idle states, valid processor-idle-state indexes range from 0 to N-1.

`PlatformState`

[in] The index of the platform idle state that the hardware platform will enter when the processor enters the processor idle state specified by <b>ProcessorState</b>. The PEP previously specified the supported platform idle states in response to a <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186826">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES</a> notification. If the PEP specified M platform idle states, valid platform-idle-state indexes range from 0 to M-1. If no change in platform idle state will occur, this member will contain the value <b>PEP_PLATFORM_IDLE_STATE_NONE</b> (0xffffffff).

`CoordinatedStateCount`

Supplies the number of coordinated idle states being entered by this transition.

`CoordinatedStates`

Supplies a pointer to an array of coordinated idle states that are being entered by this transition.

## Remarks
This structure is used by the <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186807">PEP_NOTIFY_PPM_IDLE_EXECUTE</a> notification. The <b>ProcessorState</b> and <b>PlatformState</b> members contain input values that are supplied by the Windows <a href="https://msdn.microsoft.com/B08F8ABF-FD43-434C-A345-337FBB799D9B">power management framework</a> (PoFx). The <b>Status</b> member contains an output value that the PEP writes to this member.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | pepfx.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186807">PEP_NOTIFY_PPM_IDLE_EXECUTE</a>



<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186824">PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2</a>



<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186826">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES</a>