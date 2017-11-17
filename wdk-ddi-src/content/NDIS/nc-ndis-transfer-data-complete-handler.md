---
UID: NC.ndis.TRANSFER_DATA_COMPLETE_HANDLER
title: TRANSFER_DATA_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: 36344384-b5a0-4500-833d-7e1315df317e
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

# TRANSFER_DATA_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TRANSFER_DATA_COMPLETE_HANDLER TransferDataCompleteHandler; 

// Definition

VOID TransferDataCompleteHandler 
(
	NDIS_HANDLE ProtocolBindingContext
	PNDIS_PACKET Packet
	NDIS_STATUS Status
	UINT BytesTransferred
)
{...}

TRANSFER_DATA_COMPLETE_HANDLER 


```

## -parameters

### -param ProtocolBindingContext: 
### -param Packet: 
### -param Status: 
### -param BytesTransferred: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also