---
UID: NC.fltkernel.PFLT_MESSAGE_NOTIFY
title: PFLT_MESSAGE_NOTIFY
author: windows-driver-content
description: 
ms.assetid: 5916a42d-7293-4a10-a8b8-d1c18f963b94
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: fltkernel.h
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

# PFLT_MESSAGE_NOTIFY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFLT_MESSAGE_NOTIFY PfltMessageNotify; 

// Definition

NTSTATUS PfltMessageNotify 
(
	PVOID PortCookie
	PVOID InputBuffer
	ULONG InputBufferLength
	PVOID OutputBuffer
	ULONG OutputBufferLength
	PULONG ReturnOutputBufferLength
)
{...}

PFLT_MESSAGE_NOTIFY 


```

## -parameters

### -param PortCookie: 
### -param InputBuffer: 
### -param InputBufferLength: 
### -param OutputBuffer: 
### -param OutputBufferLength: 
### -param ReturnOutputBufferLength: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also