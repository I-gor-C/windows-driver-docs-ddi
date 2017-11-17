---
UID: NC.d3dkmddi.DXGKCB_DXGKCB_MITIGATEDRANGEUPDATE
title: DXGKCB_DXGKCB_MITIGATEDRANGEUPDATE
author: windows-driver-content
description: 
ms.assetid: 2d704b87-f3a3-4260-9706-c685daaf1fd7
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

# DXGKCB_DXGKCB_MITIGATEDRANGEUPDATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKCB_DXGKCB_MITIGATEDRANGEUPDATE DxgkcbDxgkcbMitigatedrangeupdate; 

// Definition

VOID DxgkcbDxgkcbMitigatedrangeupdate 
(
	IN_CONST_HANDLE hAdapter
	IN ULONG
)
{...}

DXGKCB_DXGKCB_MITIGATEDRANGEUPDATE 


```

## -parameters

### -param hAdapter: 
### -param ULONG: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also