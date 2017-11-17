---
UID: NC.scsiwmi.PSCSIWMI_SET_DATABLOCK
title: PSCSIWMI_SET_DATABLOCK
author: windows-driver-content
description: 
ms.assetid: fcfaf8f9-858b-4a66-b14a-c0e41343f86c
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

# PSCSIWMI_SET_DATABLOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSCSIWMI_SET_DATABLOCK PscsiwmiSetDatablock; 

// Definition

BOOLEAN PscsiwmiSetDatablock 
(
	PVOID DeviceContext
	PSCSIWMI_REQUEST_CONTEXT RequestContext
	ULONG GuidIndex
	ULONG InstanceIndex
	ULONG BufferSize
	PUCHAR Buffer
)
{...}

PSCSIWMI_SET_DATABLOCK 


```

## -parameters

### -param DeviceContext: 
### -param RequestContext: 
### -param GuidIndex: 
### -param InstanceIndex: 
### -param BufferSize: 
### -param Buffer: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also