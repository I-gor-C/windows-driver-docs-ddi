---
UID: NC.ntddvol.CSV_FILECACHE_FILE_CREATE
title: CSV_FILECACHE_FILE_CREATE
author: windows-driver-content
description: 
ms.assetid: abb0e3bd-6e4b-42d2-ad9e-33733e86f345
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

# CSV_FILECACHE_FILE_CREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CSV_FILECACHE_FILE_CREATE CsvFilecacheFileCreate; 

// Definition

NTSTATUS CsvFilecacheFileCreate 
(
	PVOID pRegContext
	VOLUME_SIG_T const *volSig
	FILE_SIG_T const *fileSig
	PVOID *ppContext
)
{...}

CSV_FILECACHE_FILE_CREATE 


```

## -parameters

### -param pRegContext: 
### -param *volSig: 
### -param *fileSig: 
### -param *ppContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also