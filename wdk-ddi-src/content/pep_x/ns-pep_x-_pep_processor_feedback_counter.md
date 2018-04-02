---
UID: NS:pep_x._PEP_PROCESSOR_FEEDBACK_COUNTER
title: "_PEP_PROCESSOR_FEEDBACK_COUNTER"
author: windows-driver-content
description: The PEP_PROCESSOR_FEEDBACK_COUNTER structure describes a feedback counter to the operating system.
old-location: kernel\pep_processor_feedback_counter.htm
old-project: kernel
ms.assetid: 275AE285-6309-4A03-A02C-DBE8D44727CE
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PPEP_PROCESSOR_FEEDBACK_COUNTER, PEP_PROCESSOR_FEEDBACK_COUNTER, PEP_PROCESSOR_FEEDBACK_COUNTER structure [Kernel-Mode Driver Architecture], PPEP_PROCESSOR_FEEDBACK_COUNTER, PPEP_PROCESSOR_FEEDBACK_COUNTER structure pointer [Kernel-Mode Driver Architecture], PROCESSOR_FEEDBACK_COUNTER_FREQUENCY, PROCESSOR_FEEDBACK_COUNTER_PERFORMANCE, PROCESSOR_FEEDBACK_TYPE_INSTANTANEOUS, PROCESSOR_FEEDBACK_TYPE_RELATIVE, _PEP_PROCESSOR_FEEDBACK_COUNTER, kernel.pep_processor_feedback_counter, pepfx/PEP_PROCESSOR_FEEDBACK_COUNTER, pepfx/PPEP_PROCESSOR_FEEDBACK_COUNTER"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pep_x.h
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
-	PEP_PROCESSOR_FEEDBACK_COUNTER
product:
- Windows
targetos: Windows
req.typenames: PEP_PROCESSOR_FEEDBACK_COUNTER, *PPEP_PROCESSOR_FEEDBACK_COUNTER, PEP_PROCESSOR_FEEDBACK_COUNTER, *PPEP_PROCESSOR_FEEDBACK_COUNTER
---

# _PEP_PROCESSOR_FEEDBACK_COUNTER structure
The <b>PEP_PROCESSOR_FEEDBACK_COUNTER</b> structure describes a feedback counter to the operating system.

## Syntax
```
typedef struct _PEP_PROCESSOR_FEEDBACK_COUNTER {
  struct {
    ULONG  : 1  Affinitized;
    ULONG  : 4  Counter;
    ULONG  : 1  DiscountIdle;
    ULONG  : 24 Reserved;
    ULONG  : 2  Type;
  };
  ULONG  NominalRate;
} PEP_PROCESSOR_FEEDBACK_COUNTER, *PPEP_PROCESSOR_FEEDBACK_COUNTER;
```

## Members


`NominalRate`

Specifies the nominal rate of the counter.

## Remarks
This structure

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | pep_x.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/478E1AB1-B888-4EC2-A9C3-A33475E499E3">PEP structures</a>



<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186825">PEP_NOTIFY_PPM_QUERY_PERF_CAPABILITIES notification</a>