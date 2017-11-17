---
UID: NC.d3dkmddi.DXGKDDI_SETROOTPAGETABLE
title: DXGKDDI_SETROOTPAGETABLE
author: windows-driver-content
description: 
ms.assetid: 1853dbef-5991-4604-8ef8-0921c22daedf
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

# DXGKDDI_SETROOTPAGETABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_SETROOTPAGETABLE DxgkddiSetrootpagetable; 

// Definition

VOID DxgkddiSetrootpagetable 
(
	IN_CONST_HANDLE hAdapter
	IN_CONST_PDXGKARG_SETROOTPAGETABLE pSetPageTable
)
{...}

DXGKDDI_SETROOTPAGETABLE PDXGKDDI_SETROOTPAGETABLE


```

## -parameters

### -param hAdapter: 
### -param pSetPageTable: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also