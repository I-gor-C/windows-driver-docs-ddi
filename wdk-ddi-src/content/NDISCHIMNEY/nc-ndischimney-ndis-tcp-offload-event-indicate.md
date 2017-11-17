---
UID: NC.ndischimney.NDIS_TCP_OFFLOAD_EVENT_INDICATE
title: NDIS_TCP_OFFLOAD_EVENT_INDICATE
author: windows-driver-content
description: 
ms.assetid: d14dd52b-7667-42d5-b63f-2d0a1d0ac4c2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndischimney.h
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

# NDIS_TCP_OFFLOAD_EVENT_INDICATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_TCP_OFFLOAD_EVENT_INDICATE NdisTcpOffloadEventIndicate; 

// Definition

VOID NdisTcpOffloadEventIndicate 
(
	IN NDIS_HANDLE NdisOffloadHandle
	IN ULONG EventType
	IN ULONG EventSpecificInformation
)
{...}

NDIS_TCP_OFFLOAD_EVENT_INDICATE 


```

## -parameters

### -param NdisOffloadHandle: 
### -param EventType: 
### -param EventSpecificInformation: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also