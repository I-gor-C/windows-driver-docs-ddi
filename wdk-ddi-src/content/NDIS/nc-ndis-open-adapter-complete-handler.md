---
UID: NC.ndis.OPEN_ADAPTER_COMPLETE_HANDLER
title: OPEN_ADAPTER_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: 2044f6f3-e971-492d-8ab1-f2f0ad7eea36
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

# OPEN_ADAPTER_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

OPEN_ADAPTER_COMPLETE_HANDLER OpenAdapterCompleteHandler; 

// Definition

VOID OpenAdapterCompleteHandler 
(
	NDIS_HANDLE ProtocolBindingContext
	NDIS_STATUS Status
	NDIS_STATUS OpenErrorStatus
)
{...}

OPEN_ADAPTER_COMPLETE_HANDLER 


```

## -parameters

### -param ProtocolBindingContext: 
### -param Status: 
### -param OpenErrorStatus: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also