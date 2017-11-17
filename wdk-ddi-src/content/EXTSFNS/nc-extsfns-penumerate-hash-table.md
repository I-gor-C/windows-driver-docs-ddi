---
UID: NC.extsfns.PENUMERATE_HASH_TABLE
title: PENUMERATE_HASH_TABLE
author: windows-driver-content
description: 
ms.assetid: c18f470d-a18d-4054-ba6d-70519e61b894
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

# PENUMERATE_HASH_TABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PENUMERATE_HASH_TABLE PenumerateHashTable; 

// Definition

HRESULT PenumerateHashTable 
(
	PDEBUG_CLIENT Client
	ULONG64 HashTable
	EXTS_TABLE_ENTRY_CALLBACK Callback
	PVOID Context
)
{...}

PENUMERATE_HASH_TABLE 


```

## -parameters

### -param Client: 
### -param HashTable: 
### -param Callback: 
### -param Context: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also