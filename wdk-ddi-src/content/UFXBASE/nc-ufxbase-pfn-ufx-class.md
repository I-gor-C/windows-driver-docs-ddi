---
UID: NC.ufxbase.PFN_UFX_CLASS
title: PFN_UFX_CLASS
author: windows-driver-content
description: 
ms.assetid: 3df9ca86-4747-4cec-b7d7-45f440978eff
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ufxbase.h
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

# PFN_UFX_CLASS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UFX_CLASS PfnUfxClass; 

// Definition

void PfnUfxClass 
(
	 void
)
{...}

PFN_UFX_CLASS 


```

## -parameters

### -param void: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also