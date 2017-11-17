---
UID: NC.ndis.STATUS_HANDLER
title: STATUS_HANDLER
author: windows-driver-content
description: 
ms.assetid: 597fa02d-a08b-47e5-896a-3a8dabe82e95
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

# STATUS_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

STATUS_HANDLER StatusHandler; 

// Definition

VOID StatusHandler 
(
	NDIS_HANDLE ProtocolBindingContext
	NDIS_STATUS GeneralStatus
	PVOID StatusBuffer
	UINT StatusBufferSize
)
{...}

STATUS_HANDLER 


```

## -parameters

### -param ProtocolBindingContext: 
### -param GeneralStatus: 
### -param StatusBuffer: 
### -param StatusBufferSize: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also