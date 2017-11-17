---
UID: NC.ndis.RECEIVE_HANDLER
title: RECEIVE_HANDLER
author: windows-driver-content
description: 
ms.assetid: 936183be-a65e-435c-a233-0002c431b4a5
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

# RECEIVE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RECEIVE_HANDLER ReceiveHandler; 

// Definition

NDIS_STATUS ReceiveHandler 
(
	NDIS_HANDLE ProtocolBindingContext
	NDIS_HANDLE MacReceiveContext
	PVOID HeaderBuffer
	UINT HeaderBufferSize
	PVOID LookAheadBuffer
	UINT LookaheadBufferSize
	UINT PacketSize
)
{...}

RECEIVE_HANDLER 


```

## -parameters

### -param ProtocolBindingContext: 
### -param MacReceiveContext: 
### -param HeaderBuffer: 
### -param HeaderBufferSize: 
### -param LookAheadBuffer: 
### -param LookaheadBufferSize: 
### -param PacketSize: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also