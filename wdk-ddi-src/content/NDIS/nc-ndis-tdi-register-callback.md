---
UID: NC.ndis.TDI_REGISTER_CALLBACK
title: TDI_REGISTER_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 763b5ece-b2b2-4667-9a5f-f6d495d6f5f3
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

# TDI_REGISTER_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TDI_REGISTER_CALLBACK TdiRegisterCallback; 

// Definition

NTSTATUS TdiRegisterCallback 
(
	PUNICODE_STRING DeviceName
	HANDLE *TdiHandle
)
{...}

TDI_REGISTER_CALLBACK 


```

## -parameters

### -param DeviceName: 
### -param *TdiHandle: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also