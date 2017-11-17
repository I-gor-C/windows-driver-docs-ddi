---
UID: NC.wdm.CLFS_BLOCK_ALLOCATION
title: CLFS_BLOCK_ALLOCATION
author: windows-driver-content
description: 
ms.assetid: ff74b6c5-fea4-46fc-b645-2775a5282548
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# CLFS_BLOCK_ALLOCATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CLFS_BLOCK_ALLOCATION ClfsBlockAllocation; 

// Definition

PVOID ClfsBlockAllocation 
(
	ULONG cbBufferLength
	PVOID pvUserContext
)
{...}

CLFS_BLOCK_ALLOCATION 


```

## -parameters

### -param cbBufferLength: 
### -param pvUserContext: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also