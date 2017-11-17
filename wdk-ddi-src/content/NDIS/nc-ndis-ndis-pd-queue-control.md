---
UID: NC.ndis.NDIS_PD_QUEUE_CONTROL
title: NDIS_PD_QUEUE_CONTROL
author: windows-driver-content
description: 
ms.assetid: 3b26c455-0b02-43c1-8048-9e03d8b60b0e
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

# NDIS_PD_QUEUE_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_PD_QUEUE_CONTROL NdisPdQueueControl; 

// Definition

NTSTATUS() NdisPdQueueControl 
(
	NDIS_PD_QUEUE * NdisPDQueue
	NDIS_PD_CONTROL_TYPE ControlType
	NDIS_PD_QUEUE_CONTROL_CODE ControlCode
	PVOID InBuffer
	ULONG InBufferSize
	PVOID OutBuffer
	ULONG OutBufferSize
	ULONG * BytesReturned
)
{...}

NDIS_PD_QUEUE_CONTROL NDIS_PD_QUEUE_CONTROL_HANDLER


```

## -parameters

### -param NdisPDQueue: 
### -param ControlType: 
### -param ControlCode: 
### -param InBuffer: 
### -param InBufferSize: 
### -param OutBuffer: 
### -param OutBufferSize: 
### -param BytesReturned: 



## -returns

Returns NTSTATUS() that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also