---
UID: NC.ndis.ETH_RCV_INDICATE_HANDLER
title: ETH_RCV_INDICATE_HANDLER
author: windows-driver-content
description: 
ms.assetid: a0fa3def-88b4-45e3-885f-89ea816f7498
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

# ETH_RCV_INDICATE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ETH_RCV_INDICATE_HANDLER EthRcvIndicateHandler; 

// Definition

VOID EthRcvIndicateHandler 
(
	PETH_FILTER Filter
	NDIS_HANDLE MacReceiveContext
	PCHAR Address
	PVOID HeaderBuffer
	UINT HeaderBufferSize
	PVOID LookaheadBuffer
	UINT LookaheadBufferSize
	UINT PacketSize
)
{...}

ETH_RCV_INDICATE_HANDLER 


```

## -parameters

### -param Filter: 
### -param MacReceiveContext: 
### -param Address: 
### -param HeaderBuffer: 
### -param HeaderBufferSize: 
### -param LookaheadBuffer: 
### -param LookaheadBufferSize: 
### -param PacketSize: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also