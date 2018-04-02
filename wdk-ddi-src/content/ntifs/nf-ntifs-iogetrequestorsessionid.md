---
UID: NF:ntifs.IoGetRequestorSessionId
title: IoGetRequestorSessionId function
author: windows-driver-content
description: The IoGetRequestorSessionId routine returns the session ID for the process that originally requested a given I/O operation.
old-location: ifsk\iogetrequestorsessionid.htm
old-project: ifsk
ms.assetid: 9e13cf62-d71e-4878-becd-d34beb2f59b3
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IoGetRequestorSessionId, IoGetRequestorSessionId routine [Installable File System Drivers], ifsk.iogetrequestorsessionid, ioref_fe60ee3b-1b5b-4d9c-a4f2-456e05575349.xml, ntifs/IoGetRequestorSessionId
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows Server 2003 SP1 and later.
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
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: "<= APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	IoGetRequestorSessionId
product:
- Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# IoGetRequestorSessionId function
The <b>IoGetRequestorSessionId</b> routine returns the session ID for the process that originally requested a given I/O operation.

## Syntax

```
NTKERNELAPI NTSTATUS IoGetRequestorSessionId(
  PIRP   Irp,
  PULONG pSessionId
);
```

## Parameters

`Irp`

A pointer to the I/O request packet (IRP) for the I/O operation.

`pSessionId`

A pointer to a caller-allocated variable that receives the session ID for the process that requested the I/O operation. If the call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548391">IoGetRequestorProcessId</a> fails, this variable is set to -1.


## Return Value

<a href="https://msdn.microsoft.com/library/windows/hardware/ff548391">IoGetRequestorProcessId</a> returns STATUS_SUCCESS if the session ID is successfully returned, STATUS_UNSUCCESSFUL otherwise. STATUS_UNSUCCESSFUL is an error NTSTATUS value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This routine is available on Microsoft Windows Server 2003 SP1 and later.  |
| **Target Platform** | Universal |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff548385">IoGetRequestorProcess</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548391">IoGetRequestorProcessId</a>