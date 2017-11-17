---
UID: NC.ntddvol.CSV_FILECACHE_HANDLE_CACHE_MISS_V2
title: CSV_FILECACHE_HANDLE_CACHE_MISS_V2
author: windows-driver-content
description: 
ms.assetid: d44c75e4-c576-4220-bb8f-df85df90d302
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

# CSV_FILECACHE_HANDLE_CACHE_MISS_V2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CSV_FILECACHE_HANDLE_CACHE_MISS_V2 CsvFilecacheHandleCacheMissV2; 

// Definition

void CsvFilecacheHandleCacheMissV2 
(
	PCSV_FILECACHE_IO_CONTEXT pContext
	ULONG cRanges
	CSV_FILECACHE_IO_RANGE const
)
{...}

CSV_FILECACHE_HANDLE_CACHE_MISS_V2 


```

## -parameters

### -param pContext: 
### -param cRanges: 
### -param const: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also