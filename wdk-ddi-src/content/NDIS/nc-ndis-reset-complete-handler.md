---
UID: NC.ndis.RESET_COMPLETE_HANDLER
title: RESET_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: 8f487b38-d159-4b79-aa17-fc9b823be1a5
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

# RESET_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RESET_COMPLETE_HANDLER ResetCompleteHandler; 

// Definition

VOID ResetCompleteHandler 
(
	NDIS_HANDLE ProtocolBindingContext
	NDIS_STATUS Status
)
{...}

RESET_COMPLETE_HANDLER 


```

## -parameters

### -param ProtocolBindingContext: 
### -param Status: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also