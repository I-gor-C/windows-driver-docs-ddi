---
UID: NC.ntddvol.CSV_FILECACHE_COMPLETE_CACHE_MISS_V2
title: CSV_FILECACHE_COMPLETE_CACHE_MISS_V2
author: windows-driver-content
description: 
ms.assetid: 15466ac1-6a88-47ce-99d2-bd4d064492cb
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

# CSV_FILECACHE_COMPLETE_CACHE_MISS_V2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CSV_FILECACHE_COMPLETE_CACHE_MISS_V2 CsvFilecacheCompleteCacheMissV2; 

// Definition

void CsvFilecacheCompleteCacheMissV2 
(
	PVOID pRegContext
	PCSV_FILECACHE_IO_CONTEXT pContext
)
{...}

CSV_FILECACHE_COMPLETE_CACHE_MISS_V2 


```

## -parameters

### -param pRegContext: 
### -param pContext: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also