---
UID: NC.ndis.RECEIVE_COMPLETE_HANDLER
title: RECEIVE_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: 207f505e-4d00-42db-8706-13b3dd2a41d3
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

# RECEIVE_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RECEIVE_COMPLETE_HANDLER ReceiveCompleteHandler; 

// Definition

VOID ReceiveCompleteHandler 
(
	NDIS_HANDLE ProtocolBindingContext
)
{...}

RECEIVE_COMPLETE_HANDLER 


```

## -parameters

### -param ProtocolBindingContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also