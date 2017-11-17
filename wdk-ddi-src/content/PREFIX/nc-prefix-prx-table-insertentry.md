---
UID: NC.prefix.PRX_TABLE_INSERTENTRY
title: PRX_TABLE_INSERTENTRY
author: windows-driver-content
description: 
ms.assetid: 0657ae9a-7980-47dc-9e18-89a48c154282
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

# PRX_TABLE_INSERTENTRY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRX_TABLE_INSERTENTRY PrxTableInsertentry; 

// Definition

PRX_PREFIX_ENTRY PrxTableInsertentry 
(
	IN OUT PRX_PREFIX_TABLE ThisTable
	IN OUT PRX_PREFIX_ENTRY ThisEntry
)
{...}

PRX_TABLE_INSERTENTRY 


```

## -parameters

### -param ThisTable: 
### -param ThisEntry: 



## -returns

Returns PRX_PREFIX_ENTRY that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also