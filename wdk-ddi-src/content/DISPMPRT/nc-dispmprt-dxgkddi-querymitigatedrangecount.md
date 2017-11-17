---
UID: NC.dispmprt.DXGKDDI_QUERYMITIGATEDRANGECOUNT
title: DXGKDDI_QUERYMITIGATEDRANGECOUNT
author: windows-driver-content
description: 
ms.assetid: 71fd82f2-a5f9-4c19-92e3-4387045da8c5
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

# DXGKDDI_QUERYMITIGATEDRANGECOUNT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_QUERYMITIGATEDRANGECOUNT DxgkddiQuerymitigatedrangecount; 

// Definition

VOID DxgkddiQuerymitigatedrangecount 
(
	HANDLE Context
	DXGKARG_QUERYMITIGATEDRANGECOUNT * pArgs
)
{...}

DXGKDDI_QUERYMITIGATEDRANGECOUNT PDXGKDDI_QUERYMITIGATEDRANGECOUNT


```

## -parameters

### -param Context: 
### -param pArgs: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also