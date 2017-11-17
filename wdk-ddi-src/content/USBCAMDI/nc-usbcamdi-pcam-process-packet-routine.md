---
UID: NC.usbcamdi.PCAM_PROCESS_PACKET_ROUTINE
title: PCAM_PROCESS_PACKET_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 74871ac8-2395-48f8-a553-66c85c966098
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

# PCAM_PROCESS_PACKET_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCAM_PROCESS_PACKET_ROUTINE PcamProcessPacketRoutine; 

// Definition

ULONG PcamProcessPacketRoutine 
(
	PDEVICE_OBJECT BusDeviceObject
	PVOID DeviceContext
	PVOID CurrentFrameContext
	PUSBD_ISO_PACKET_DESCRIPTOR SyncPacket
	PVOID SyncBuffer
	PUSBD_ISO_PACKET_DESCRIPTOR DataPacket
	PVOID DataBuffer
	PBOOLEAN FrameComplete
	PBOOLEAN NextFrameIsStill
)
{...}

PCAM_PROCESS_PACKET_ROUTINE 


```

## -parameters

### -param BusDeviceObject: 
### -param DeviceContext: 
### -param CurrentFrameContext: 
### -param SyncPacket: 
### -param SyncBuffer: 
### -param DataPacket: 
### -param DataBuffer: 
### -param FrameComplete: 
### -param NextFrameIsStill: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also