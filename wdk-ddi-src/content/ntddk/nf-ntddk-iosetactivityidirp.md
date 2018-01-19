---
UID : NF:ntddk.IoSetActivityIdIrp
title : IoSetActivityIdIrp function
author : windows-driver-content
description : The IoSetActivityIdIrp routine associates an activity ID with an IRP.
old-location : kernel\iosetactivityidirp.htm
old-project : kernel
ms.assetid : 81D3BE8C-D6E0-47E2-959C-3834988E4C61
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : IoSetActivityIdIrp
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntddk.h
req.include-header : Ntddk.h
req.target-type : Universal
req.target-min-winverclnt : Available starting with  Windows 8.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IoSetActivityIdIrp
req.alt-loc : NtosKrnl.exe
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe
req.irql : Any level if a GUID is passed in, otherwise PASSIVE_LEVEL.
req.typenames : WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# IoSetActivityIdIrp function
The IoSetActivityIdIrp routine associates an activity ID with an IRP.

## Syntax

````
NTSTATUS IoSetActivityIdIrp(
  _In_     PIRP   Irp,
  _In_opt_ LPGUID Guid
);
````

## Parameters

`Irp`

The IRP to associate the activity ID with.

`Guid`

A pointer to the GUID that represents the ID to store in the IRP.  If NULL, IoSetActivityIdIrp attempts to retrieve the activity ID from the current thread if it was the thread that originally issued the request.


## Return Value

IoSetActivityIdIrp returns STATUS_SUCCESS if the call is successful. Possible error return values include the following.
<dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl>No GUID was provided and the ETW activity ID was unavailable.
<dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl>The I/O tracing provider has not been enabled on the IRP.

## Remarks

Drivers should use IoSetActivityIdIrp only on IRPs that have been allocated using <a href="..\wdm\nf-wdm-ioallocateirp.md">IoAllocateIrp</a> (and freed using <a href="..\wdm\nf-wdm-iofreeirp.md">IoFreeIrp</a>). Otherwise, memory leakage may result.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h (include Ntddk.h) |
| **Library** |  |
| **IRQL** | Any level if a GUID is passed in, otherwise PASSIVE_LEVEL. |
| **DDI compliance rules** |  |