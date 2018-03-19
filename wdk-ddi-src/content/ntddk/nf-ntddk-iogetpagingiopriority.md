---
UID: NF:ntddk.IoGetPagingIoPriority
title: IoGetPagingIoPriority function
author: windows-driver-content
description: The IoGetPagingIoPriority routine indicates the priority level of a paging I/O request.
old-location: kernel\iogetpagingiopriority.htm
old-project: kernel
ms.assetid: 3b0f4fc9-58fd-46ba-be17-2e1b36b16caa
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: IoGetPagingIoPriority, IoGetPagingIoPriority routine [Kernel-Mode Driver Architecture], k104_cde35790-d059-44bb-85c5-abde7cb36319.xml, kernel.iogetpagingiopriority, wdm/IoGetPagingIoPriority
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows Server 2003 and later versions of Windows.
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
-	IoGetPagingIoPriority
product: Windows
targetos: Windows
req.typenames: WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# IoGetPagingIoPriority function
The <b>IoGetPagingIoPriority</b> routine indicates the priority level of a paging I/O request.

## Syntax

````
IO_PAGING_PRIORITY IoGetPagingIoPriority(
  _In_ PIRP Irp
);
````

## Parameters

`Irp`

Pointer to the IRP to be tested for paging priority.


## Return Value

<b>IoGetPagingIoPriority</b> returns the <a href="..\wdm\ne-wdm-_io_paging_priority.md">IO_PAGING_PRIORITY</a> value for the associated IRP.

## Remarks

For I/O requests that causing paging, the system associates an <b>IO_PAGING_PRIORITY</b> value that describes the IRP's priority. Drivers can use this value when queuing IRPs.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows Server 2003 and later versions of Windows.  |
| **Target Platform** | Universal |
| **Header** | ntddk.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | Any level |

## See Also

<a href="..\wdm\ne-wdm-_io_paging_priority.md">IO_PAGING_PRIORITY</a>