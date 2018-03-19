---
UID: NF:ntddk.PsGetProcessId
title: PsGetProcessId function
author: windows-driver-content
description: The PsGetProcessId routine returns the process identifier (process ID) that is associated with a specified process.
old-location: kernel\psgetprocessid.htm
old-project: kernel
ms.assetid: 9e1f6a57-bc48-41c6-815c-6a44e8d01699
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: PsGetProcessId, PsGetProcessId routine [Kernel-Mode Driver Architecture], k108_b0733011-4102-4e10-83e3-e7e9d7172d08.xml, kernel.psgetprocessid, ntddk/PsGetProcessId
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of Windows.
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
req.irql: Any level
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	PsGetProcessId
product: Windows
targetos: Windows
req.typenames: WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# PsGetProcessId function
The <b>PsGetProcessId</b> routine returns the process identifier (process ID) that is associated with a specified process.

## Syntax

````
HANDLE PsGetProcessId(
  _In_ PEPROCESS Process
);
````

## Parameters

`Process`

A pointer to a process object structure.


## Return Value

<b>PsGetProcessId</b> returns the process ID of the process that the <i>Process</i> parameter specifies.

## Remarks

The EPROCESS-typed process object structure is an opaque data structure that the operating system uses internally. To obtain a pointer to the EPROCESS structure for the current process, a driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559933">PsGetCurrentProcess</a>. To obtain a pointer to the EPROCESS structure for a different process, the driver can call <a href="..\wdm\nf-wdm-obreferenceobjectbyhandle.md">ObReferenceObjectByHandle</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows XP and later versions of Windows.  |
| **Target Platform** | Universal |
| **Header** | ntddk.h (include Ntddk.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | Any level |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff559933">PsGetCurrentProcess</a>



<a href="..\wdm\nf-wdm-obreferenceobjectbyhandle.md">ObReferenceObjectByHandle</a>