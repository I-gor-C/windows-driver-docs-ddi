---
UID: NC.wsk.PFN_WSK_SOCKET_CONNECT
title: PFN_WSK_SOCKET_CONNECT
author: windows-driver-content
description: 
ms.assetid: 57259beb-47e4-4909-bc15-6615cdf5cbea
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

# PFN_WSK_SOCKET_CONNECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_SOCKET_CONNECT PfnWskSocketConnect; 

// Definition

NTSTATUS PfnWskSocketConnect 
(
	PWSK_CLIENT Client
	USHORT SocketType
	ULONG Protocol
	PSOCKADDR LocalAddress
	PSOCKADDR RemoteAddress
	ULONG Flags
	PVOID SocketContext
	CONST WSK_CLIENT_CONNECTION_DISPATCH *Dispatch
	PEPROCESS OwningProcess
	PETHREAD OwningThread
	PSECURITY_DESCRIPTOR SecurityDescriptor
	PIRP Irp
)
{...}

PFN_WSK_SOCKET_CONNECT 


```

## -parameters

### -param Client: 
### -param SocketType: 
### -param Protocol: 
### -param LocalAddress: 
### -param RemoteAddress: 
### -param Flags: 
### -param SocketContext: 
### -param *Dispatch: 
### -param OwningProcess: 
### -param OwningThread: 
### -param SecurityDescriptor: 
### -param Irp: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also