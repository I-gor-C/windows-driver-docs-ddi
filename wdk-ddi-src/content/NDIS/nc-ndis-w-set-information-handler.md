---
UID: NC.ndis.W_SET_INFORMATION_HANDLER
title: W_SET_INFORMATION_HANDLER
author: windows-driver-content
description: 
ms.assetid: 38918f5c-9c6d-4c0b-b11d-9b4830ce4000
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

# W_SET_INFORMATION_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_SET_INFORMATION_HANDLER WSetInformationHandler; 

// Definition

NDIS_STATUS WSetInformationHandler 
(
	NDIS_HANDLE MiniportAdapterContext
	NDIS_OID Oid
	PVOID InformationBuffer
	ULONG InformationBufferLength
	PULONG BytesRead
	PULONG BytesNeeded
)
{...}

W_SET_INFORMATION_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 
### -param Oid: 
### -param InformationBuffer: 
### -param InformationBufferLength: 
### -param BytesRead: 
### -param BytesNeeded: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also