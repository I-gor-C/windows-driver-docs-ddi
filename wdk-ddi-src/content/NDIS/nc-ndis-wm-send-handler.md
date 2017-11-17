---
UID: NC.ndis.WM_SEND_HANDLER
title: WM_SEND_HANDLER
author: windows-driver-content
description: 
ms.assetid: 568dc848-f9c7-467f-88fe-3a91f557d27d
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

# WM_SEND_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

WM_SEND_HANDLER WmSendHandler; 

// Definition

NDIS_STATUS WmSendHandler 
(
	NDIS_HANDLE MiniportAdapterContext
	NDIS_HANDLE NdisLinkHandle
	PNDIS_WAN_PACKET Packet
)
{...}

WM_SEND_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 
### -param NdisLinkHandle: 
### -param Packet: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also