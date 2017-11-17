---
UID: NC.ntddvol.CSV_FILECACHE_COMPLETE_CACHE_IO
title: CSV_FILECACHE_COMPLETE_CACHE_IO
author: windows-driver-content
description: 
ms.assetid: cd17b780-cded-4207-b533-efe8c5e50174
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

# CSV_FILECACHE_COMPLETE_CACHE_IO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CSV_FILECACHE_COMPLETE_CACHE_IO CsvFilecacheCompleteCacheIo; 

// Definition

void CsvFilecacheCompleteCacheIo 
(
	PCSV_FILECACHE_CONTEXT CSVContext
)
{...}

CSV_FILECACHE_COMPLETE_CACHE_IO 


```

## -parameters

### -param CSVContext: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also