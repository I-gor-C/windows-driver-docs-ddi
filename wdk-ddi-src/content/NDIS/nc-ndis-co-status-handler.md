---
UID: NC.ndis.CO_STATUS_HANDLER
title: CO_STATUS_HANDLER
author: windows-driver-content
description: 
ms.assetid: 88b99be7-b354-414d-a3f4-bdb988b914cc
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

# CO_STATUS_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CO_STATUS_HANDLER CoStatusHandler; 

// Definition

VOID CoStatusHandler 
(
	NDIS_HANDLE ProtocolBindingContext
	NDIS_HANDLE ProtocolVcContext
	NDIS_STATUS GeneralStatus
	PVOID StatusBuffer
	UINT StatusBufferSize
)
{...}

CO_STATUS_HANDLER 


```

## -parameters

### -param ProtocolBindingContext: 
### -param ProtocolVcContext: 
### -param GeneralStatus: 
### -param StatusBuffer: 
### -param StatusBufferSize: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also