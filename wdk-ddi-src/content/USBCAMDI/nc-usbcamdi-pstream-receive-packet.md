---
UID: NC.usbcamdi.PSTREAM_RECEIVE_PACKET
title: PSTREAM_RECEIVE_PACKET
author: windows-driver-content
description: 
ms.assetid: e9e97667-605e-404c-b77b-82276b8c3b1a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: usbcamdi.h
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

# PSTREAM_RECEIVE_PACKET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSTREAM_RECEIVE_PACKET PstreamReceivePacket; 

// Definition

VOID PstreamReceivePacket 
(
	PVOID Srb
	PVOID DeviceContext
	PBOOLEAN Completed
)
{...}

PSTREAM_RECEIVE_PACKET 


```

## -parameters

### -param Srb: 
### -param DeviceContext: 
### -param Completed: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also