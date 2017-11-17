---
UID: NC.ndis.W_TRANSFER_DATA_HANDLER
title: W_TRANSFER_DATA_HANDLER
author: windows-driver-content
description: 
ms.assetid: f49dc4a6-f078-4c52-b753-5b136fad9343
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

# W_TRANSFER_DATA_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_TRANSFER_DATA_HANDLER WTransferDataHandler; 

// Definition

NDIS_STATUS WTransferDataHandler 
(
	PNDIS_PACKET Packet
	PUINT BytesTransferred
	NDIS_HANDLE MiniportAdapterContext
	NDIS_HANDLE MiniportReceiveContext
	UINT ByteOffset
	UINT BytesToTransfer
)
{...}

W_TRANSFER_DATA_HANDLER 


```

## -parameters

### -param Packet: 
### -param BytesTransferred: 
### -param MiniportAdapterContext: 
### -param MiniportReceiveContext: 
### -param ByteOffset: 
### -param BytesToTransfer: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also