---
UID: NC.wsk.PFN_WSK_ACCEPT
title: PFN_WSK_ACCEPT
author: windows-driver-content
description: 
ms.assetid: 1e1ef1ae-3d3e-493a-a422-6d5388c61d3a
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

# PFN_WSK_ACCEPT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_ACCEPT PfnWskAccept; 

// Definition

NTSTATUS PfnWskAccept 
(
	PWSK_SOCKET ListenSocket
	ULONG Flags
	PVOID AcceptSocketContext
	CONST WSK_CLIENT_CONNECTION_DISPATCH *AcceptSocketDispatch
	PSOCKADDR LocalAddress
	PSOCKADDR RemoteAddress
	PIRP Irp
)
{...}

PFN_WSK_ACCEPT 


```

## -parameters

### -param ListenSocket: 
### -param Flags: 
### -param AcceptSocketContext: 
### -param *AcceptSocketDispatch: 
### -param LocalAddress: 
### -param RemoteAddress: 
### -param Irp: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also