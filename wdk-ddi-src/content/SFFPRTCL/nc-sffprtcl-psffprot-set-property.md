---
UID: NC.sffprtcl.PSFFPROT_SET_PROPERTY
title: PSFFPROT_SET_PROPERTY
author: windows-driver-content
description: 
ms.assetid: 1ac93639-1a2e-4c0e-bd02-cb54da992e41
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sffprtcl.h
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

# PSFFPROT_SET_PROPERTY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSFFPROT_SET_PROPERTY PsffprotSetProperty; 

// Definition

NTSTATUS PsffprotSetProperty 
(
	IN PVOID Context
	IN SFFPROT_PROPERTY Property
	IN ULONG BufferLength
	IN PVOID PropertyBuffer
)
{...}

PSFFPROT_SET_PROPERTY 


```

## -parameters

### -param Context: 
### -param Property: 
### -param BufferLength: 
### -param PropertyBuffer: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also