---
UID: NC.ndis.TRANSFER_DATA_HANDLER
title: TRANSFER_DATA_HANDLER
author: windows-driver-content
description: 
ms.assetid: 1b8f9c74-7cdb-4575-8faa-07d8d32b0119
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

# TRANSFER_DATA_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TRANSFER_DATA_HANDLER TransferDataHandler; 

// Definition

NDIS_STATUS TransferDataHandler 
(
	NDIS_HANDLE NdisBindingHandle
	NDIS_HANDLE MacReceiveContext
	UINT ByteOffset
	UINT BytesToTransfer
	PNDIS_PACKET Packet
	PUINT BytesTransferred
)
{...}

TRANSFER_DATA_HANDLER 


```

## -parameters

### -param NdisBindingHandle: 
### -param MacReceiveContext: 
### -param ByteOffset: 
### -param BytesToTransfer: 
### -param Packet: 
### -param BytesTransferred: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also