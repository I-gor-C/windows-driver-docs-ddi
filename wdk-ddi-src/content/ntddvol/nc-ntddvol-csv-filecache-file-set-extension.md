---
UID: NC.ntddvol.CSV_FILECACHE_FILE_SET_EXTENSION
title: CSV_FILECACHE_FILE_SET_EXTENSION
author: windows-driver-content
description: 
ms.assetid: 4c0e1d49-43e0-40a8-9c1c-1472a0b99df5
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

# CSV_FILECACHE_FILE_SET_EXTENSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CSV_FILECACHE_FILE_SET_EXTENSION CsvFilecacheFileSetExtension; 

// Definition

PCSV_FILECACHE_FILE_CONTEXT_EXTENSION CsvFilecacheFileSetExtension 
(
	PVOID pRegContext
	PCSV_FILECACHE_IO_CONTEXT pContext
	PCSV_FILECACHE_FILE_CONTEXT_EXTENSION pExtension
)
{...}

CSV_FILECACHE_FILE_SET_EXTENSION 


```

## -parameters

### -param pRegContext: 
### -param pContext: 
### -param pExtension: 



## -returns

Returns PCSV_FILECACHE_FILE_CONTEXT_EXTENSION that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also