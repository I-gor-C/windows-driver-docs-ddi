---
UID: NC.rxcehdlr.PRXCE_IND_RECEIVE
title: PRXCE_IND_RECEIVE
author: windows-driver-content
description: 
ms.assetid: 54781236-51f6-4a45-980e-a7c128fd85b7
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

# PRXCE_IND_RECEIVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRXCE_IND_RECEIVE PrxceIndReceive; 

// Definition

NTSTATUS PrxceIndReceive 
(
	IN PVOID pRxCeEventContext
	IN PRXCE_VC pVc
	IN ULONG ReceiveFlags
	IN ULONG BytesIndicated
	IN ULONG BytesAvailable
	OUT ULONG *BytesTaken
	IN PVOID Tsdu
	OUT PMDL *pDataBufferPointer
	OUT PULONG pDataBufferSize
)
{...}

PRXCE_IND_RECEIVE 


```

## -parameters

### -param pRxCeEventContext: 
### -param pVc: 
### -param ReceiveFlags: 
### -param BytesIndicated: 
### -param BytesAvailable: 
### -param *BytesTaken: 
### -param Tsdu: 
### -param *pDataBufferPointer: 
### -param pDataBufferSize: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also