---
UID: NC.dsm.DSM_INVALIDATE_PATH
title: DSM_INVALIDATE_PATH
author: windows-driver-content
description: 
ms.assetid: 67a1d572-4d79-4af2-9ba3-4147e3d701f9
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

# DSM_INVALIDATE_PATH callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_INVALIDATE_PATH DsmInvalidatePath; 

// Definition

NTSTATUS DsmInvalidatePath 
(
	IN PVOID DsmContext
	IN ULONG ErrorMask
	IN PVOID PathId
	IN OUT PVOID *NewPathId
)
{...}

DSM_INVALIDATE_PATH 


```

## -parameters

### -param DsmContext: 
### -param ErrorMask: 
### -param PathId: 
### -param *NewPathId: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also