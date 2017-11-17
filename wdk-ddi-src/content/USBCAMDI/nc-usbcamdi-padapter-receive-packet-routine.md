---
UID: NC.usbcamdi.PADAPTER_RECEIVE_PACKET_ROUTINE
title: PADAPTER_RECEIVE_PACKET_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 6387a2e0-b07f-4449-9e58-a68715c9ffae
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

# PADAPTER_RECEIVE_PACKET_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PADAPTER_RECEIVE_PACKET_ROUTINE PadapterReceivePacketRoutine; 

// Definition

VOID PadapterReceivePacketRoutine 
(
	PHW_STREAM_REQUEST_BLOCK Srb
)
{...}

PADAPTER_RECEIVE_PACKET_ROUTINE 


```

## -parameters

### -param Srb: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also