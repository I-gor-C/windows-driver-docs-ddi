---
UID: NC.ndis.TDI_PNP_HANDLER
title: TDI_PNP_HANDLER
author: windows-driver-content
description: 
ms.assetid: bc514985-6bd5-4a3c-9f94-a59f5eeeb747
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndis.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# TDI_PNP_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TDI_PNP_HANDLER TdiPnpHandler; 

// Definition

NTSTATUS TdiPnpHandler 
(
	PUNICODE_STRING UpperComponent
	PUNICODE_STRING LowerComponent
	PUNICODE_STRING BindList
	PVOID ReconfigBuffer
	UINT ReconfigBufferSize
	UINT Operation
)
{...}

TDI_PNP_HANDLER 


```

## -parameters

### -param UpperComponent: 
### -param LowerComponent: 
### -param BindList: 
### -param ReconfigBuffer: 
### -param ReconfigBufferSize: 
### -param Operation: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also