---
UID: NC.nfccx.PFN_NFC_CX
title: PFN_NFC_CX
author: windows-driver-content
description: 
ms.assetid: 98765e39-dd02-4640-a241-e73684501122
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: nfccx.h
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

# PFN_NFC_CX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NFC_CX PfnNfcCx; 

// Definition

VOID PfnNfcCx 
(
	 VOID
)
{...}

PFN_NFC_CX 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also