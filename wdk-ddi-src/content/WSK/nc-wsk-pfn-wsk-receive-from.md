---
UID: NC.wsk.PFN_WSK_RECEIVE_FROM
title: PFN_WSK_RECEIVE_FROM
author: windows-driver-content
description: 
ms.assetid: fec04f81-a2e4-408e-911c-4db65cf3033b
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

# PFN_WSK_RECEIVE_FROM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_RECEIVE_FROM PfnWskReceiveFrom; 

// Definition

NTSTATUS PfnWskReceiveFrom 
(
	PWSK_SOCKET Socket
	PWSK_BUF Buffer
	ULONG Flags
	PSOCKADDR RemoteAddress
	PULONG ControlLength
	PCMSGHDR ControlInfo
	PULONG ControlFlags
	PIRP Irp
)
{...}

PFN_WSK_RECEIVE_FROM 


```

## -parameters

### -param Socket: 
### -param Buffer: 
### -param Flags: 
### -param RemoteAddress: 
### -param ControlLength: 
### -param ControlInfo: 
### -param ControlFlags: 
### -param Irp: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also