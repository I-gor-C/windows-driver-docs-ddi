---
UID: NC.ntddser.PSERENUM_READPORT
title: PSERENUM_READPORT
author: windows-driver-content
description: 
ms.assetid: 93faea35-fbe1-42f1-af69-e332673a1e28
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

# PSERENUM_READPORT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSERENUM_READPORT PserenumReadport; 

// Definition

UCHAR PserenumReadport 
(
	PVOID SerPortAddress
)
{...}

PSERENUM_READPORT 


```

## -parameters

### -param SerPortAddress: 



## -returns

Returns UCHAR that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also