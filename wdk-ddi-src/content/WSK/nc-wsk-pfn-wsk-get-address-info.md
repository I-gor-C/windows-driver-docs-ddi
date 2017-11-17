---
UID: NC.wsk.PFN_WSK_GET_ADDRESS_INFO
title: PFN_WSK_GET_ADDRESS_INFO
author: windows-driver-content
description: 
ms.assetid: be20bb72-662b-4756-86e9-a0f061a13c24
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

# PFN_WSK_GET_ADDRESS_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_GET_ADDRESS_INFO PfnWskGetAddressInfo; 

// Definition

NTSTATUS PfnWskGetAddressInfo 
(
	PWSK_CLIENT Client
	PUNICODE_STRING NodeName
	PUNICODE_STRING ServiceName
	ULONG NameSpace
	GUID *Provider
	PADDRINFOEXW Hints
	PADDRINFOEXW *Result
	PEPROCESS OwningProcess
	PETHREAD OwningThread
	PIRP Irp
)
{...}

PFN_WSK_GET_ADDRESS_INFO 


```

## -parameters

### -param Client: 
### -param NodeName: 
### -param ServiceName: 
### -param NameSpace: 
### -param *Provider: 
### -param Hints: 
### -param *Result: 
### -param OwningProcess: 
### -param OwningThread: 
### -param Irp: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also