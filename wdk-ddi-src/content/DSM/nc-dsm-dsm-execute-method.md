---
UID: NC.dsm.DSM_EXECUTE_METHOD
title: DSM_EXECUTE_METHOD
author: windows-driver-content
description: 
ms.assetid: 8556700e-7bd4-4a57-bf12-88b61fcc5d6f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsm.h
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

# DSM_EXECUTE_METHOD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_EXECUTE_METHOD DsmExecuteMethod; 

// Definition

NTSTATUS DsmExecuteMethod 
(
	IN PVOID DsmContext
	IN PIRP Irp
	IN ULONG GuidIndex
	IN ULONG InstanceIndex
	IN ULONG MethodId
	IN ULONG InBufferSize
	IN PULONG OutBufferSize
	IN OUT PUCHAR Buffer
)
{...}

DSM_EXECUTE_METHOD 


```

## -parameters

### -param DsmContext: 
### -param Irp: 
### -param GuidIndex: 
### -param InstanceIndex: 
### -param MethodId: 
### -param InBufferSize: 
### -param OutBufferSize: 
### -param Buffer: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also