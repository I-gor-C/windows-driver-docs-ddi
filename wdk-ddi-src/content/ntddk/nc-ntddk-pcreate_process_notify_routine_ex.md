---
UID: NC:ntddk.PCREATE_PROCESS_NOTIFY_ROUTINE_EX
title: PCREATE_PROCESS_NOTIFY_ROUTINE_EX
author: windows-driver-content
description: A callback routine implemented by a driver to notify the caller when a process is created or exits.
old-location: kernel\pcreate_process_notify_routine_ex.htm
old-project: kernel
ms.assetid: 071BD24F-AA58-4A39-8059-CEF6D7105DB6
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: PCREATE_PROCESS_NOTIFY_ROUTINE_EX, SetCreateProcessNotifyRoutineEx, SetCreateProcessNotifyRoutineEx callback function [Kernel-Mode Driver Architecture], kernel.pcreate_process_notify_routine_ex, ntddk/SetCreateProcessNotifyRoutineEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
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
-	UserDefined
api_location:
-	Ntddk.h
api_name:
-	SetCreateProcessNotifyRoutineEx
product: Windows
targetos: Windows
req.typenames: FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
---


# PCREATE_PROCESS_NOTIFY_ROUTINE_EX callback function
A callback routine implemented by a driver to notify the caller when a process is created or exits.
<div class="alert"><b>Warning</b>  The actions that  you can perform in this routine are restricted for safe calls. See <a href="https://msdn.microsoft.com/c01b3fd9-7f4e-4d1a-a726-b31b0eebf094">Best Practices</a>. </div><div> </div>

## Syntax

```
PCREATE_PROCESS_NOTIFY_ROUTINE_EX PcreateProcessNotifyRoutineEx;

void PcreateProcessNotifyRoutineEx(
  PEPROCESS Process,
  HANDLE ProcessId,
  PPS_CREATE_NOTIFY_INFO CreateInfo
)
{...}
```

## Parameters

`Process`



`ProcessId`

The process ID of the process.

`CreateInfo`

A pointer to a <a href="..\ntddk\ns-ntddk-_ps_create_notify_info.md">PS_CREATE_NOTIFY_INFO</a> structure that contains information about the new process.


## Return Value

This callback function does not return a value.

## Remarks

Highest-level drivers call <a href="..\ntddk\nf-ntddk-pssetcreateprocessnotifyroutineex.md">PsSetCreateProcessNotifyRoutineEx</a> to register their implementation of  <i>PCREATE_PROCESS_NOTIFY_ROUTINE_EX</i> routine. An installable file system (IFS) or highest-level system-profiling driver might register a process-creation callback routine to track which processes are created and deleted against the driver's internal state across the system.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | ntddk.h (include Ntddk.h) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\ntddk\nf-ntddk-pssetcreateprocessnotifyroutineex2.md">PsSetCreateProcessNotifyRoutineEx2</a>



<a href="..\ntddk\nf-ntddk-pssetcreateprocessnotifyroutineex.md">PsSetCreateProcessNotifyRoutineEx</a>