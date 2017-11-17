---
UID: NC.ndis.NDIS_M_TD_COMPLETE_HANDLER
title: NDIS_M_TD_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: ec4ccadd-64a3-4888-87a5-db4b9e313346
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

# NDIS_M_TD_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_M_TD_COMPLETE_HANDLER NdisMTdCompleteHandler; 

// Definition

VOID NdisMTdCompleteHandler 
(
	NDIS_HANDLE MiniportAdapterHandle
	PNDIS_PACKET Packet
	NDIS_STATUS Status
	UINT BytesTransferred
)
{...}

NDIS_M_TD_COMPLETE_HANDLER 


```

## -parameters

### -param MiniportAdapterHandle: 
### -param Packet: 
### -param Status: 
### -param BytesTransferred: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also