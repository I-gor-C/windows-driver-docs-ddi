---
UID: NF:ntddk.IoGetActivityIdIrp
title: IoGetActivityIdIrp function
author: windows-driver-content
description: The IoGetActivityIdIrp routine retrieves the current activity ID associated with an IRP.
old-location: kernel\iogetactivityidirp.htm
old-project: kernel
ms.assetid: FAFF65EF-F1D8-4B54-B281-D5C4AC124E32
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: IoGetActivityIdIrp, IoGetActivityIdIrp routine [Kernel-Mode Driver Architecture], kernel.iogetactivityidirp, ntddk/IoGetActivityIdIrp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	DllExport
apilocation:
-	NtosKrnl.exe
apiname:
-	IoGetActivityIdIrp
product: Windows
targetos: Windows
req.typenames: "*PWHEA_RAW_DATA_FORMAT, WHEA_RAW_DATA_FORMAT"
---


# IoGetActivityIdIrp function
The IoGetActivityIdIrp routine retrieves the current activity ID associated with an IRP.

## Syntax

````
NTSTATUS IoGetActivityIdIrp(
  _In_  PIRP   Irp,
  _Out_ LPGUID Guid
);
````

## Parameters

`Irp`

The IRP from which to retrieve the activity ID.

`Guid`

A pointer to a location  to store the retrieved GUID.


## Return Value

IoGetActivityIdIrp returns STATUS_SUCCESS if the call is successful. Possible error return values include the following.

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl>
</td>
<td width="60%">
No activity ID is associated with the request.

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 8.  |
| **Target Platform** | Universal |
| **Header** | ntddk.h (include Ntddk.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | Any level |