---
UID: NC.wdm.CLFS_BLOCK_DEALLOCATION
title: CLFS_BLOCK_DEALLOCATION
author: windows-driver-content
description: 
ms.assetid: 0ecb29fe-4d47-467b-a2dd-1ea87e5065ee
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

# CLFS_BLOCK_DEALLOCATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CLFS_BLOCK_DEALLOCATION ClfsBlockDeallocation; 

// Definition

void ClfsBlockDeallocation 
(
	PVOID pvBuffer
	PVOID pvUserContext
)
{...}

CLFS_BLOCK_DEALLOCATION 


```

## -parameters

### -param pvBuffer: 
### -param pvUserContext: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also