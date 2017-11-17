---
UID: NC.ntddvol.CSV_BLOCKCACHE_PURGE_CACHE
title: CSV_BLOCKCACHE_PURGE_CACHE
author: windows-driver-content
description: 
ms.assetid: a6e589fb-6f3e-451b-aa67-e5d5fb9cfdfd
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddvol.h
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

# CSV_BLOCKCACHE_PURGE_CACHE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CSV_BLOCKCACHE_PURGE_CACHE CsvBlockcachePurgeCache; 

// Definition

void CsvBlockcachePurgeCache 
(
	PVOID CallbackContext
	ULONGLONG Offset
	ULONGLONG Length
)
{...}

CSV_BLOCKCACHE_PURGE_CACHE 


```

## -parameters

### -param CallbackContext: 
### -param Offset: 
### -param Length: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also