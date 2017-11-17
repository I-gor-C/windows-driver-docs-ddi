---
UID: NC.rxcehdlr.PRXCE_IND_SEND_POSSIBLE
title: PRXCE_IND_SEND_POSSIBLE
author: windows-driver-content
description: 
ms.assetid: 8bd9e5ca-50aa-478e-bdf1-102809cf0a5f
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

# PRXCE_IND_SEND_POSSIBLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRXCE_IND_SEND_POSSIBLE PrxceIndSendPossible; 

// Definition

NTSTATUS PrxceIndSendPossible 
(
	IN PVOID pRxCeEventContext
	IN PRXCE_VC pVc
	IN ULONG BytesAvailable
)
{...}

PRXCE_IND_SEND_POSSIBLE 


```

## -parameters

### -param pRxCeEventContext: 
### -param pVc: 
### -param BytesAvailable: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also