---
UID: NC.ntifs.PIO_IRP_EXT_PROCESS_TRACKED_OFFSET_CALLBACK
title: PIO_IRP_EXT_PROCESS_TRACKED_OFFSET_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 07d1489f-1d9b-4ed8-b34e-7c30ffef0942
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntifs.h
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

# PIO_IRP_EXT_PROCESS_TRACKED_OFFSET_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PIO_IRP_EXT_PROCESS_TRACKED_OFFSET_CALLBACK PioIrpExtProcessTrackedOffsetCallback; 

// Definition

VOID PioIrpExtProcessTrackedOffsetCallback 
(
	_IO_IRP_EXT_TRACK_OFFSET_HEADER *SourceContext
	_IO_IRP_EXT_TRACK_OFFSET_HEADER *TargetContext
	LONGLONG RelativeOffset
)
{...}

PIO_IRP_EXT_PROCESS_TRACKED_OFFSET_CALLBACK 


```

## -parameters

### -param *SourceContext: 
### -param *TargetContext: 
### -param RelativeOffset: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also