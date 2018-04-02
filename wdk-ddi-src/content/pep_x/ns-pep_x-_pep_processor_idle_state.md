---
UID: NS:pep_x._PEP_PROCESSOR_IDLE_STATE
title: "_PEP_PROCESSOR_IDLE_STATE"
author: windows-driver-content
description: The PEP_PROCESSOR_IDLE_STATE structure describes the capabilities of a processor idle state.
old-location: kernel\pep_processor_idle_state.htm
old-project: kernel
ms.assetid: 10CAB3CA-83BF-421B-81F5-2B42790B8928
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PPEP_PROCESSOR_IDLE_STATE, PEP_PROCESSOR_IDLE_STATE, PEP_PROCESSOR_IDLE_STATE structure [Kernel-Mode Driver Architecture], PPEP_PROCESSOR_IDLE_STATE, PPEP_PROCESSOR_IDLE_STATE structure pointer [Kernel-Mode Driver Architecture], _PEP_PROCESSOR_IDLE_STATE, kernel.pep_processor_idle_state, pep_x/PEP_PROCESSOR_IDLE_STATE, pep_x/PPEP_PROCESSOR_IDLE_STATE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pep_x.h
req.include-header: Pepfx.h
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
-	pep_x.h
api_name:
-	PEP_PROCESSOR_IDLE_STATE
product:
- Windows
targetos: Windows
req.typenames: PEP_PROCESSOR_IDLE_STATE, *PPEP_PROCESSOR_IDLE_STATE
---

# _PEP_PROCESSOR_IDLE_STATE structure
The <b>PEP_PROCESSOR_IDLE_STATE</b> structure describes the capabilities of a processor idle state.

## Syntax
```
typedef struct _PEP_PROCESSOR_IDLE_STATE {
  union {
    ULONG Ulong;
    struct {
      ULONG  : 1  Interruptible;
      ULONG  : 1  CacheCoherent;
      ULONG  : 1  ThreadContextRetained;
      ULONG  : 4  CStateType;
      ULONG  : 25 Reserved;
    };
  };
} PEP_PROCESSOR_IDLE_STATE, *PPEP_PROCESSOR_IDLE_STATE;
```

## Members


## Remarks
The <b>IdleStates</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt629121">PEP_PPM_QUERY_IDLE_STATES</a> structure is the first element in an array of <b>PEP_PROCESSOR_IDLE_STATE</b> structures.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | pep_x.h (include Pepfx.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt629121">PEP_PPM_QUERY_IDLE_STATES</a>