---
UID: NC.scsiwmi.PSCSIWMI_SET_DATAITEM
title: PSCSIWMI_SET_DATAITEM
author: windows-driver-content
description: 
ms.assetid: 49a21360-25e6-441d-9279-b3b91d856862
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

# PSCSIWMI_SET_DATAITEM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSCSIWMI_SET_DATAITEM PscsiwmiSetDataitem; 

// Definition

BOOLEAN PscsiwmiSetDataitem 
(
	PVOID DeviceContext
	PSCSIWMI_REQUEST_CONTEXT RequestContext
	ULONG GuidIndex
	ULONG InstanceIndex
	ULONG DataItemId
	ULONG BufferSize
	PUCHAR Buffer
)
{...}

PSCSIWMI_SET_DATAITEM 


```

## -parameters

### -param DeviceContext: 
### -param RequestContext: 
### -param GuidIndex: 
### -param InstanceIndex: 
### -param DataItemId: 
### -param BufferSize: 
### -param Buffer: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also