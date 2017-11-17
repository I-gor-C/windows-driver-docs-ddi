---
UID: NC.tdikrnl.PTDI_IND_CHAINED_RECEIVE
title: PTDI_IND_CHAINED_RECEIVE
author: windows-driver-content
description: 
ms.assetid: 2296c587-7961-4a9e-9371-6fce2be47292
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: tdikrnl.h
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

# PTDI_IND_CHAINED_RECEIVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PTDI_IND_CHAINED_RECEIVE PtdiIndChainedReceive; 

// Definition

NTSTATUS PtdiIndChainedReceive 
(
	PVOID TdiEventContext
	CONNECTION_CONTEXT ConnectionContext
	ULONG ReceiveFlags
	ULONG ReceiveLength
	ULONG StartingOffset
	PMDL Tsdu
	PVOID TsduDescriptor
)
{...}

PTDI_IND_CHAINED_RECEIVE 


```

## -parameters

### -param TdiEventContext: 
### -param ConnectionContext: 
### -param ReceiveFlags: 
### -param ReceiveLength: 
### -param StartingOffset: 
### -param Tsdu: 
### -param TsduDescriptor: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also