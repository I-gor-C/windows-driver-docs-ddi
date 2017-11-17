---
UID: NC.rxcehdlr.PRXCE_IND_ENDPOINT_ERROR
title: PRXCE_IND_ENDPOINT_ERROR
author: windows-driver-content
description: 
ms.assetid: d5c4cc05-145b-472b-9d1c-c6ea916a28d1
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: rxcehdlr.h
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

# PRXCE_IND_ENDPOINT_ERROR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRXCE_IND_ENDPOINT_ERROR PrxceIndEndpointError; 

// Definition

NTSTATUS PrxceIndEndpointError 
(
	IN PVOID pRxCeEventContext
	IN NTSTATUS Status
)
{...}

PRXCE_IND_ENDPOINT_ERROR 


```

## -parameters

### -param pRxCeEventContext: 
### -param Status: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also