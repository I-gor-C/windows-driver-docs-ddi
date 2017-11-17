---
UID: NC.prefix.PRX_TABLE_LOOKUPNAME
title: PRX_TABLE_LOOKUPNAME
author: windows-driver-content
description: 
ms.assetid: ce5b0b46-16ab-4c7e-82d5-1aada4c4d863
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: prefix.h
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

# PRX_TABLE_LOOKUPNAME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRX_TABLE_LOOKUPNAME PrxTableLookupname; 

// Definition

PVOID PrxTableLookupname 
(
	IN PRX_PREFIX_TABLE ThisTable
	IN PUNICODE_STRING CanonicalName
	OUT PUNICODE_STRING RemainingName
)
{...}

PRX_TABLE_LOOKUPNAME 


```

## -parameters

### -param ThisTable: 
### -param CanonicalName: 
### -param RemainingName: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also