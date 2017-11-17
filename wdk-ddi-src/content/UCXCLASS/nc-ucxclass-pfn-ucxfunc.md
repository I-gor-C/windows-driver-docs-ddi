---
UID: NC.ucxclass.PFN_UCXFUNC
title: PFN_UCXFUNC
author: windows-driver-content
description: 
ms.assetid: 9d2f244e-850a-4b53-96b1-fe6beccc2721
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxclass.h
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

# PFN_UCXFUNC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXFUNC PfnUcxfunc; 

// Definition

void PfnUcxfunc 
(
	 void
)
{...}

PFN_UCXFUNC 


```

## -parameters

### -param void: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also