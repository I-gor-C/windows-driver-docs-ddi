---
UID: NC.ndis.NDIS_M_STATUS_HANDLER
title: NDIS_M_STATUS_HANDLER
author: windows-driver-content
description: 
ms.assetid: f0aa2fb2-d6c3-41ab-9d92-74514fddf2d0
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

# NDIS_M_STATUS_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_M_STATUS_HANDLER NdisMStatusHandler; 

// Definition

VOID NdisMStatusHandler 
(
	NDIS_HANDLE MiniportHandle
	NDIS_STATUS GeneralStatus
	PVOID StatusBuffer
	UINT StatusBufferSize
)
{...}

NDIS_M_STATUS_HANDLER 


```

## -parameters

### -param MiniportHandle: 
### -param GeneralStatus: 
### -param StatusBuffer: 
### -param StatusBufferSize: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also