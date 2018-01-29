---
UID : NF:wdm.RtlFillMemory
title : RtlFillMemory macro
author : windows-driver-content
description : The RtlFillMemory routine fills a block of memory with the specified fill value.
old-location : kernel\rtlfillmemory.htm
old-project : kernel
ms.assetid : 9a73331a-cc73-4a47-948b-a821600ca6a6
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlFillMemory, k109_db7a2a9f-c7b5-40c3-9755-e386bbaf5353.xml, wdm/RtlFillMemory, RtlFillMemory routine [Kernel-Mode Driver Architecture], kernel.rtlfillmemory
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : macro
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
req.lib : NtDll.lib (user mode); NtosKrnl.lib (kernel mode)
req.dll : NtDll.dll (user mode); NtosKrnl.exe (kernel mode)
req.irql : Any level (See Remarks section)
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WORK_QUEUE_TYPE
req.product : Windows 10 or later.
---


# RtlFillMemory function
The <b>RtlFillMemory</b> routine fills a block of memory with the specified fill value.

## Syntax

````
VOID RtlFillMemory(
  _Out_ VOID UNALIGNED *Destination,
  _In_  SIZE_T         Length,
  _In_  UCHAR          Fill
);
````

## Parameters

`Destination`

A pointer to the block of memory to be filled.

`Length`

The number of bytes in the block of memory to be filled.

`Fill`

The value to fill the destination memory block with. This value is copied to every byte in the memory block that is defined by <i>Destination</i> and <i>Length</i>.


## Return Value

None

## Remarks

Callers of <b>RtlFillMemory</b> can be running at any IRQL if the destination memory block is in nonpaged system memory. Otherwise, the caller must be running at IRQL &lt;= APC_LEVEL.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** |  |
| **IRQL** | Any level (See Remarks section) |
| **DDI compliance rules** |  |

## See Also

<a href="..\wdm\nf-wdm-rtlzeromemory.md">RtlZeroMemory</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlFillMemory routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>