---
UID: NC.d3d12umddi.PFND3D12DDI_GETSUPPORTEDVERSIONS
title: PFND3D12DDI_GETSUPPORTEDVERSIONS
author: windows-driver-content
description: 
ms.assetid: 414c3c4e-b2a5-4b4e-b439-bca3723d1990
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

# PFND3D12DDI_GETSUPPORTEDVERSIONS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_GETSUPPORTEDVERSIONS Pfnd3d12ddiGetsupportedversions; 

// Definition

HRESULT Pfnd3d12ddiGetsupportedversions 
(
	 D3D12DDI_HADAPTER
	UINT32 *puEntries
	UINT64 *pSupportedDDIInterfaceVersions
)
{...}

PFND3D12DDI_GETSUPPORTEDVERSIONS 


```

## -parameters

### -param D3D12DDI_HADAPTER: 
### -param *puEntries: 
### -param *pSupportedDDIInterfaceVersions: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also