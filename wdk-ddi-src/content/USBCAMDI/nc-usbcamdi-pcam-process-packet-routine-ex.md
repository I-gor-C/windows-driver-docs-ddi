---
UID: NC.usbcamdi.PCAM_PROCESS_PACKET_ROUTINE_EX
title: PCAM_PROCESS_PACKET_ROUTINE_EX
author: windows-driver-content
description: 
ms.assetid: 8db24864-e687-4d7f-be5b-35a37a316249
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

# PCAM_PROCESS_PACKET_ROUTINE_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCAM_PROCESS_PACKET_ROUTINE_EX PcamProcessPacketRoutineEx; 

// Definition

ULONG PcamProcessPacketRoutineEx 
(
	PDEVICE_OBJECT BusDeviceObject
	PVOID DeviceContext
	PVOID CurrentFrameContext
	PUSBD_ISO_PACKET_DESCRIPTOR SyncPacket
	PVOID SyncBuffer
	PUSBD_ISO_PACKET_DESCRIPTOR DataPacket
	PVOID DataBuffer
	PBOOLEAN FrameComplete
	PULONG PacketFlag
	PULONG ValidDataOffset
)
{...}

PCAM_PROCESS_PACKET_ROUTINE_EX 


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
### -param PacketFlag: 
### -param ValidDataOffset: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also