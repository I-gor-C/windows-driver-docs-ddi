---
UID: NC.ks.PFNKSFILTERPROCESS
title: PFNKSFILTERPROCESS
author: windows-driver-content
description: 
ms.assetid: cfa225dc-5ed1-4762-94d7-a9118b68567c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSFILTERPROCESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSFILTERPROCESS Pfnksfilterprocess; 

// Definition

NTSTATUS Pfnksfilterprocess 
(
	PKSFILTER Filter
	PKSPROCESSPIN_INDEXENTRY Index
)
{...}

PFNKSFILTERPROCESS 


```

## -parameters

### -param Filter: 
### -param Index: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also