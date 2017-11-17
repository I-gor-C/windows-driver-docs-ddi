---
UID: NC.storport.PStorPortAllocatePool
title: PStorPortAllocatePool
author: windows-driver-content
description: 
ms.assetid: 45df40b0-63d5-4ccd-9f27-5ac4a076b6ea
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: storport.h
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

# PStorPortAllocatePool callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PStorPortAllocatePool Pstorportallocatepool; 

// Definition

PVOID Pstorportallocatepool 
(
	ULONG NumberOfBytes
	ULONG Tag
	PVOID HwDeviceExtension
	PVOID *PMdl
)
{...}

PStorPortAllocatePool 


```

## -parameters

### -param NumberOfBytes: 
### -param Tag: 
### -param HwDeviceExtension: 
### -param *PMdl: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also