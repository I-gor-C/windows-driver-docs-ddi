---
UID: NC.prefix.PRX_TABLE_REMOVEENTRY
title: PRX_TABLE_REMOVEENTRY
author: windows-driver-content
description: 
ms.assetid: dc1a534d-c633-4ad0-ab14-10090265d9a6
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

# PRX_TABLE_REMOVEENTRY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRX_TABLE_REMOVEENTRY PrxTableRemoveentry; 

// Definition

VOID PrxTableRemoveentry 
(
	IN OUT PRX_PREFIX_TABLE ThisTable
	IN OUT PRX_PREFIX_ENTRY Entry
)
{...}

PRX_TABLE_REMOVEENTRY 


```

## -parameters

### -param ThisTable: 
### -param Entry: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also