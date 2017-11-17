---
UID: NC.d3dkmddi.DXGKDDI_SETSTABLEPOWERSTATE
title: DXGKDDI_SETSTABLEPOWERSTATE
author: windows-driver-content
description: 
ms.assetid: 33eb9791-0e19-4134-9f4a-958a13ffbf61
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmddi.h
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

# DXGKDDI_SETSTABLEPOWERSTATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_SETSTABLEPOWERSTATE DxgkddiSetstablepowerstate; 

// Definition

VOID DxgkddiSetstablepowerstate 
(
	IN_CONST_HANDLE hAdapter
	IN_CONST_PDXGKARG_SETSTABLEPOWERSTATE pArgs
)
{...}

DXGKDDI_SETSTABLEPOWERSTATE PDXGKDDI_SETSTABLEPOWERSTATE


```

## -parameters

### -param hAdapter: 
### -param pArgs: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also