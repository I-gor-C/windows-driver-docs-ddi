---
UID: NC.extsfns.KDEXT_DUMP_HANDLE_CALLBACK
title: KDEXT_DUMP_HANDLE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: e842a02e-67f3-4c17-b7f6-3b3d44795114
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# KDEXT_DUMP_HANDLE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

KDEXT_DUMP_HANDLE_CALLBACK KdextDumpHandleCallback; 

// Definition

BOOLEAN KdextDumpHandleCallback 
(
	PKDEXT_HANDLE_INFORMATION HandleInfo
	ULONG Flags
	PVOID Context
)
{...}

KDEXT_DUMP_HANDLE_CALLBACK 


```

## -parameters

### -param HandleInfo: 
### -param Flags: 
### -param Context: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also