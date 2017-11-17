---
UID: NC.rxcehdlr.PRXCE_IND_SEND_COMPLETE
title: PRXCE_IND_SEND_COMPLETE
author: windows-driver-content
description: 
ms.assetid: a07b9bf2-518f-4605-9b19-cfb61f642222
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

# PRXCE_IND_SEND_COMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRXCE_IND_SEND_COMPLETE PrxceIndSendComplete; 

// Definition

NTSTATUS PrxceIndSendComplete 
(
	IN PVOID pEventContext
	IN PVOID pCompletionContext
	IN NTSTATUS Status
)
{...}

PRXCE_IND_SEND_COMPLETE 


```

## -parameters

### -param pEventContext: 
### -param pCompletionContext: 
### -param Status: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also