---
UID : NS:pepfx._PEP_PROCESSOR_FEEDBACK_COUNTER
title : _PEP_PROCESSOR_FEEDBACK_COUNTER
author : windows-driver-content
description : The PEP_PROCESSOR_FEEDBACK_COUNTER structure describes a feedback counter to the operating system.
old-location : kernel\pep_processor_feedback_counter.htm
old-project : kernel
ms.assetid : 275AE285-6309-4A03-A02C-DBE8D44727CE
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : PROCESSOR_FEEDBACK_COUNTER_FREQUENCY, PEP_PROCESSOR_FEEDBACK_COUNTER, kernel.pep_processor_feedback_counter, PPEP_PROCESSOR_FEEDBACK_COUNTER, PROCESSOR_FEEDBACK_COUNTER_PERFORMANCE, PPEP_PROCESSOR_FEEDBACK_COUNTER structure pointer [Kernel-Mode Driver Architecture], _PEP_PROCESSOR_FEEDBACK_COUNTER, PEP_PROCESSOR_FEEDBACK_COUNTER structure [Kernel-Mode Driver Architecture], PROCESSOR_FEEDBACK_TYPE_INSTANTANEOUS, *PPEP_PROCESSOR_FEEDBACK_COUNTER, pepfx/PPEP_PROCESSOR_FEEDBACK_COUNTER, PROCESSOR_FEEDBACK_TYPE_RELATIVE, pepfx/PEP_PROCESSOR_FEEDBACK_COUNTER
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
req.typenames : PEP_PROCESSOR_FEEDBACK_COUNTER, *PPEP_PROCESSOR_FEEDBACK_COUNTER
---

# _PEP_PROCESSOR_FEEDBACK_COUNTER structure
The <b>PEP_PROCESSOR_FEEDBACK_COUNTER</b> structure describes a feedback counter to the operating system.

## Syntax
````
typedef struct _PEP_PROCESSOR_FEEDBACK_COUNTER {
  struct {
    ULONG Affinitized  :1;
    ULONG Type  :2;
    ULONG Counter  :4;
    ULONG Reserved  :25;
  };
  ULONG  NominalRate;
} PEP_PROCESSOR_FEEDBACK_COUNTER, *PPEP_PROCESSOR_FEEDBACK_COUNTER;
````

## Members


`NominalRate`

Specifies the nominal rate of the counter.

## Remarks
This structure

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | pepfx.h |

## See Also

<a href="https://msdn.microsoft.com/478E1AB1-B888-4EC2-A9C3-A33475E499E3">PEP structures</a>

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186825">PEP_NOTIFY_PPM_QUERY_PERF_CAPABILITIES notification</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PROCESSOR_FEEDBACK_COUNTER structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>