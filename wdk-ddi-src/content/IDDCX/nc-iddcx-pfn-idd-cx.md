---
UID: NC.iddcx.PFN_IDD_CX
title: PFN_IDD_CX
author: windows-driver-content
description: 
ms.assetid: f16beac5-7dd8-48ce-b40e-c146287d87c0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: iddcx.h
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

# PFN_IDD_CX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_IDD_CX PfnIddCx; 

// Definition

VOID PfnIddCx 
(
	 VOID
)
{...}

PFN_IDD_CX 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also