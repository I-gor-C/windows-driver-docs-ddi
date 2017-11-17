---
UID: NC.ntddvol.CSV_FILECACHE_HANDLE_CACHE_MISS
title: CSV_FILECACHE_HANDLE_CACHE_MISS
author: windows-driver-content
description: 
ms.assetid: 373a12bc-5a4a-4d1c-8302-68a8a0c3fa70
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

# CSV_FILECACHE_HANDLE_CACHE_MISS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CSV_FILECACHE_HANDLE_CACHE_MISS CsvFilecacheHandleCacheMiss; 

// Definition

LONG CsvFilecacheHandleCacheMiss 
(
	PCSV_FILECACHE_CONTEXT CSVContext
)
{...}

CSV_FILECACHE_HANDLE_CACHE_MISS 


```

## -parameters

### -param CSVContext: 



## -returns

Returns LONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also