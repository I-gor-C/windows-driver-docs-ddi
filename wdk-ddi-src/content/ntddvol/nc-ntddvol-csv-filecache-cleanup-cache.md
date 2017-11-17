---
UID: NC.ntddvol.CSV_FILECACHE_CLEANUP_CACHE
title: CSV_FILECACHE_CLEANUP_CACHE
author: windows-driver-content
description: 
ms.assetid: d06fd5d4-00fd-4976-a21b-c72ed4f33c6e
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

# CSV_FILECACHE_CLEANUP_CACHE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CSV_FILECACHE_CLEANUP_CACHE CsvFilecacheCleanupCache; 

// Definition

void CsvFilecacheCleanupCache 
(
	PVOID pRegContext
)
{...}

CSV_FILECACHE_CLEANUP_CACHE 


```

## -parameters

### -param pRegContext: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also