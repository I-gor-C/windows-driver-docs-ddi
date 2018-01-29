---
UID : NF:storport.StorPortBuildMdlForNonPagedPool
title : StorPortBuildMdlForNonPagedPool function
author : windows-driver-content
description : The StorPortBuildMdlForNonPagedPool routine updates the MDL to describe the associated non-paged memory.
old-location : storage\storportbuildmdlfornonpagedpool.htm
old-project : storage
ms.assetid : f22dbf1e-4b40-4294-bca5-3011f0a97644
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : StorPortBuildMdlForNonPagedPool, StorPortBuildMdlForNonPagedPool routine [Storage Devices], storport/StorPortBuildMdlForNonPagedPool, storage.storportbuildmdlfornonpagedpool, storprt_98151881-8a9f-4bf9-8365-ec50aecced4f.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : storport.h
req.include-header : Storport.h
req.target-type : Universal
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : StorPortIrql
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : "<=DISPATCH_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : STOR_SPINLOCK
req.product : Windows 10 or later.
---


# StorPortBuildMdlForNonPagedPool function
The <b>StorPortBuildMdlForNonPagedPool</b> routine updates the MDL to describe the associated non-paged memory.

## Syntax

````
ULONG StorPortBuildMdlForNonPagedPool(
  _In_    PVOID HwDeviceExtension,
  _Inout_ PVOID Mdl
);
````

## Parameters

`HwDeviceExtension`

A pointer to the hardware device extension for the host bus adapter (HBA).

`Mdl`

A pointer to the MDL that specifies the memory buffer.


## Return Value

StorPortBuildMdlForNonPagedPool returns one of the following status codes:
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl>
</td>
<td width="60%">
This function is not implemented on the active operating system.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
Indicates that the MDL was updated successfully.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
The pointer to the MDL is <b>NULL</b>.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl>
</td>
<td width="60%">
The call was made at an invalid IRQL. 

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | storport.h (include Storport.h) |
| **Library** |  |
| **IRQL** | <=DISPATCH_LEVEL |
| **DDI compliance rules** | StorPortIrql |