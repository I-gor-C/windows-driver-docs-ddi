---
UID: NC.usbcamdi.PCAM_PROCESS_RAW_FRAME_ROUTINE
title: PCAM_PROCESS_RAW_FRAME_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 76302985-d2c7-4f84-afac-29adbb0cf91f
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

# PCAM_PROCESS_RAW_FRAME_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCAM_PROCESS_RAW_FRAME_ROUTINE PcamProcessRawFrameRoutine; 

// Definition

NTSTATUS PcamProcessRawFrameRoutine 
(
	PDEVICE_OBJECT BusDeviceObject
	PVOID DeviceContext
	PVOID FrameContext
	PVOID FrameBuffer
	ULONG FrameLength
	PVOID RawFrameBuffer
	ULONG RawFrameLength
	ULONG NumberOfPackets
	PULONG BytesReturned
)
{...}

PCAM_PROCESS_RAW_FRAME_ROUTINE 


```

## -parameters

### -param BusDeviceObject: 
### -param DeviceContext: 
### -param FrameContext: 
### -param FrameBuffer: 
### -param FrameLength: 
### -param RawFrameBuffer: 
### -param RawFrameLength: 
### -param NumberOfPackets: 
### -param BytesReturned: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also