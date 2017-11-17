---
UID: NC.dispmprt.DXGKDDI_GETDEVICELOCATION
title: DXGKDDI_GETDEVICELOCATION
author: windows-driver-content
description: 
ms.assetid: b6b5f684-9907-41b1-95fd-633ab1d9acd4
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

# DXGKDDI_GETDEVICELOCATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_GETDEVICELOCATION DxgkddiGetdevicelocation; 

// Definition

VOID DxgkddiGetdevicelocation 
(
	HANDLE Context
	DXGKARG_GETDEVICELOCATION * pArgs
)
{...}

DXGKDDI_GETDEVICELOCATION PDXGKDDI_GETDEVICELOCATION


```

## -parameters

### -param Context: 
### -param pArgs: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also