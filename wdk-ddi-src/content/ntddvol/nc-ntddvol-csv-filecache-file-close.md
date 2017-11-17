---
UID: NC.ntddvol.CSV_FILECACHE_FILE_CLOSE
title: CSV_FILECACHE_FILE_CLOSE
author: windows-driver-content
description: 
ms.assetid: f5d2b838-2a66-4f76-a2d1-2aeaf17b4938
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

# CSV_FILECACHE_FILE_CLOSE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CSV_FILECACHE_FILE_CLOSE CsvFilecacheFileClose; 

// Definition

void CsvFilecacheFileClose 
(
	PVOID pRegContext
	PVOID pContext
)
{...}

CSV_FILECACHE_FILE_CLOSE 


```

## -parameters

### -param pRegContext: 
### -param pContext: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also