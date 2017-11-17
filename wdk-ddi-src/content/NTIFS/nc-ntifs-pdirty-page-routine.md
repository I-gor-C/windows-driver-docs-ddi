---
UID: NC.ntifs.PDIRTY_PAGE_ROUTINE
title: PDIRTY_PAGE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 41611b96-af2b-4bfe-9589-b1d19c4d233e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntifs.h
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

# PDIRTY_PAGE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDIRTY_PAGE_ROUTINE PdirtyPageRoutine; 

// Definition

VOID PdirtyPageRoutine 
(
	PFILE_OBJECT FileObject
	PLARGE_INTEGER FileOffset
	ULONG Length
	PLARGE_INTEGER OldestLsn
	PLARGE_INTEGER NewestLsn
	PVOID Context1
	PVOID Context2
)
{...}

PDIRTY_PAGE_ROUTINE 


```

## -parameters

### -param FileObject: 
### -param FileOffset: 
### -param Length: 
### -param OldestLsn: 
### -param NewestLsn: 
### -param Context1: 
### -param Context2: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also