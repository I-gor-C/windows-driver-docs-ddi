---
UID: NC.wsk.PFN_WSK_GET_NAME_INFO
title: PFN_WSK_GET_NAME_INFO
author: windows-driver-content
description: 
ms.assetid: 5ee15281-bdb8-4353-b838-7190c4c0da2c
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

# PFN_WSK_GET_NAME_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_GET_NAME_INFO PfnWskGetNameInfo; 

// Definition

NTSTATUS PfnWskGetNameInfo 
(
	PWSK_CLIENT Client
	PSOCKADDR SockAddr
	ULONG SockAddrLength
	PUNICODE_STRING NodeName
	PUNICODE_STRING ServiceName
	ULONG Flags
	PEPROCESS OwningProcess
	PETHREAD OwningThread
	PIRP Irp
)
{...}

PFN_WSK_GET_NAME_INFO 


```

## -parameters

### -param Client: 
### -param SockAddr: 
### -param SockAddrLength: 
### -param NodeName: 
### -param ServiceName: 
### -param Flags: 
### -param OwningProcess: 
### -param OwningThread: 
### -param Irp: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also