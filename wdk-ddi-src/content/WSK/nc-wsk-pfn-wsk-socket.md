---
UID: NC.wsk.PFN_WSK_SOCKET
title: PFN_WSK_SOCKET
author: windows-driver-content
description: 
ms.assetid: 13caa904-5177-4c23-bc6f-b7022bae5891
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

# PFN_WSK_SOCKET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_SOCKET PfnWskSocket; 

// Definition

NTSTATUS PfnWskSocket 
(
	PWSK_CLIENT Client
	ADDRESS_FAMILY AddressFamily
	USHORT SocketType
	ULONG Protocol
	ULONG Flags
	PVOID SocketContext
	CONST VOID *Dispatch
	PEPROCESS OwningProcess
	PETHREAD OwningThread
	PSECURITY_DESCRIPTOR SecurityDescriptor
	PIRP Irp
)
{...}

PFN_WSK_SOCKET 


```

## -parameters

### -param Client: 
### -param AddressFamily: 
### -param SocketType: 
### -param Protocol: 
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