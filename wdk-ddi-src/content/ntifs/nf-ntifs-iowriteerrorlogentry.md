---
UID : NF:ntifs.IoWriteErrorLogEntry
title : IoWriteErrorLogEntry function
author : windows-driver-content
description : The IoWriteErrorLogEntry routine queues a given error log packet to the system error logging thread.
old-location : kernel\iowriteerrorlogentry.htm
old-project : kernel
ms.assetid : 1259c344-584c-410a-a152-5de1f433082c
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : wdm/IoWriteErrorLogEntry, k104_1822a499-059a-41c8-b97b-aa3a5bfd22e3.xml, kernel.iowriteerrorlogentry, IoWriteErrorLogEntry, IoWriteErrorLogEntry routine [Kernel-Mode Driver Architecture]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntifs.h
req.include-header : Wdm.h, Ntddk.h, Ntifs.h
req.target-type : Universal
req.target-min-winverclnt : Available starting with Windows 2000.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : IrqlDispatch
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe
req.irql : "<= DISPATCH_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : TOKEN_TYPE
---


# IoWriteErrorLogEntry function
The <b>IoWriteErrorLogEntry</b> routine queues a given error log packet to the system error logging thread.

## Syntax

````
VOID IoWriteErrorLogEntry(
  _In_ PVOID ElEntry
);
````

## Parameters

`ElEntry`

Pointer to the error log packet the driver has allocated with <a href="..\wdm\nf-wdm-ioallocateerrorlogentry.md">IoAllocateErrorLogEntry</a> and filled in by the caller.


## Return Value

None

## Remarks

<b>IoWriteErrorLogEntry</b> frees the error log entry. Drivers must not call <b>IoFreeErrorLogEntry</b> on a log entry that they have already passed to <b>IoWriteErrorLogEntry</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000. Available starting with Windows 2000. |
| **Target Platform** | Universal |
| **Header** | ntifs.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** | IrqlDispatch |

## See Also

<a href="..\wdm\nf-wdm-ioallocateerrorlogentry.md">IoAllocateErrorLogEntry</a>

<a href="..\wdm\nf-wdm-iofreeerrorlogentry.md">IoFreeErrorLogEntry</a>

<a href="..\wdm\ns-wdm-_io_error_log_packet.md">IO_ERROR_LOG_PACKET</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoWriteErrorLogEntry routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>