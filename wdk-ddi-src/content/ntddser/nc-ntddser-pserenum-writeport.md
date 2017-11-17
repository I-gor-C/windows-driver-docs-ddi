---
UID: NC.ntddser.PSERENUM_WRITEPORT
title: PSERENUM_WRITEPORT
author: windows-driver-content
description: 
ms.assetid: a4205406-47fb-4c36-a8f3-8e9e90f9cfbc
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddser.h
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

# PSERENUM_WRITEPORT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSERENUM_WRITEPORT PserenumWriteport; 

// Definition

VOID PserenumWriteport 
(
	PVOID SerPortAddress
	UCHAR Value
)
{...}

PSERENUM_WRITEPORT 


```

## -parameters

### -param SerPortAddress: 
### -param Value: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also