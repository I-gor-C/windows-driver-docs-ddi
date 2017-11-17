---
UID: NC.wsk.PFN_WSK_CONTROL_SOCKET
title: PFN_WSK_CONTROL_SOCKET
author: windows-driver-content
description: 
ms.assetid: 1a8a4ee7-e1b7-4fce-8200-2eba8d7cd7b1
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

# PFN_WSK_CONTROL_SOCKET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_CONTROL_SOCKET PfnWskControlSocket; 

// Definition

NTSTATUS PfnWskControlSocket 
(
	PWSK_SOCKET Socket
	WSK_CONTROL_SOCKET_TYPE RequestType
	ULONG ControlCode
	ULONG Level
	SIZE_T InputSize
	PVOID InputBuffer
	SIZE_T OutputSize
	PVOID OutputBuffer
	SIZE_T *OutputSizeReturned
	PIRP Irp
)
{...}

PFN_WSK_CONTROL_SOCKET 


```

## -parameters

### -param Socket: 
### -param RequestType: 
### -param ControlCode: 
### -param Level: 
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