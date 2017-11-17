---
UID: NC.dispmprt.DXGKDDI_QUERYPROBEDBARS
title: DXGKDDI_QUERYPROBEDBARS
author: windows-driver-content
description: 
ms.assetid: 11c3825c-cd9f-44b3-a888-bb9f5cf37c28
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dispmprt.h
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

# DXGKDDI_QUERYPROBEDBARS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_QUERYPROBEDBARS DxgkddiQueryprobedbars; 

// Definition

VOID DxgkddiQueryprobedbars 
(
	HANDLE Context
	DXGKARG_QUERYPROBEDBARS * pArgs
)
{...}

DXGKDDI_QUERYPROBEDBARS PDXGKDDI_QUERYPROBEDBARS


```

## -parameters

### -param Context: 
### -param pArgs: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also