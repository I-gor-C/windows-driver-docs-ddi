---
UID: NC.usbcamdi.PCAM_NEW_FRAME_ROUTINE_EX
title: PCAM_NEW_FRAME_ROUTINE_EX
author: windows-driver-content
description: 
ms.assetid: 8034138d-6786-415a-936c-fcecaa66ffe6
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

# PCAM_NEW_FRAME_ROUTINE_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCAM_NEW_FRAME_ROUTINE_EX PcamNewFrameRoutineEx; 

// Definition

VOID PcamNewFrameRoutineEx 
(
	PVOID DeviceContext
	PVOID FrameContext
	ULONG StreamNumber
	PULONG FrameLength
)
{...}

PCAM_NEW_FRAME_ROUTINE_EX 


```

## -parameters

### -param DeviceContext: 
### -param FrameContext: 
### -param StreamNumber: 
### -param FrameLength: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also