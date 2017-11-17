---
UID: NC.d3d12umddi.PFND3D12DDI_GETOPTIONALDDITTABLES
title: PFND3D12DDI_GETOPTIONALDDITTABLES
author: windows-driver-content
description: 
ms.assetid: 114577c4-534f-4e5d-95fc-a71d4e02073c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d12umddi.h
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

# PFND3D12DDI_GETOPTIONALDDITTABLES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_GETOPTIONALDDITTABLES Pfnd3d12ddiGetoptionalddittables; 

// Definition

HRESULT Pfnd3d12ddiGetoptionalddittables 
(
	 D3D12DDI_HADAPTER
	UINT32 *puEntries
	D3D12DDI_TABLE_REQUEST *
)
{...}

PFND3D12DDI_GETOPTIONALDDITTABLES 


```

## -parameters

### -param D3D12DDI_HADAPTER: 
### -param *puEntries: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also