---
UID: NC.wsk.PFN_WSK_CONTROL_CLIENT
title: PFN_WSK_CONTROL_CLIENT
author: windows-driver-content
description: 
ms.assetid: 23a58d24-487e-49e5-8964-cbedc3d4dede
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wsk.h
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

# PFN_WSK_CONTROL_CLIENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_CONTROL_CLIENT PfnWskControlClient; 

// Definition

NTSTATUS PfnWskControlClient 
(
	PWSK_CLIENT Client
	ULONG ControlCode
	SIZE_T InputSize
	PVOID InputBuffer
	SIZE_T OutputSize
	PVOID OutputBuffer
	SIZE_T *OutputSizeReturned
	PIRP Irp
)
{...}

PFN_WSK_CONTROL_CLIENT 


```

## -parameters

### -param Client: 
### -param ControlCode: 
### -param InputSize: 
### -param InputBuffer: 
### -param OutputSize: 
### -param OutputBuffer: 
### -param *OutputSizeReturned: 
### -param Irp: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also