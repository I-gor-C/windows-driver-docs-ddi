---
UID: NC.scsiwmi.PSCSIWMI_EXECUTE_METHOD
title: PSCSIWMI_EXECUTE_METHOD
author: windows-driver-content
description: 
ms.assetid: bd6e46ff-e7c5-400a-a65d-ef289e7c1232
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: scsiwmi.h
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

# PSCSIWMI_EXECUTE_METHOD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSCSIWMI_EXECUTE_METHOD PscsiwmiExecuteMethod; 

// Definition

BOOLEAN PscsiwmiExecuteMethod 
(
	PVOID DeviceContext
	PSCSIWMI_REQUEST_CONTEXT RequestContext
	ULONG GuidIndex
	ULONG InstanceIndex
	ULONG MethodId
	ULONG InBufferSize
	ULONG OutBufferSize
	PUCHAR Buffer
)
{...}

PSCSIWMI_EXECUTE_METHOD 


```

## -parameters

### -param DeviceContext: 
### -param RequestContext: 
### -param GuidIndex: 
### -param InstanceIndex: 
### -param MethodId: 
### -param InBufferSize: 
### -param OutBufferSize: 
### -param Buffer: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also