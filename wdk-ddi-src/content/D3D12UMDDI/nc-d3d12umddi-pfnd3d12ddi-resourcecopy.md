---
UID: NC.d3d12umddi.PFND3D12DDI_RESOURCECOPY
title: PFND3D12DDI_RESOURCECOPY
author: windows-driver-content
description: 
ms.assetid: ed1dd8ea-ffb6-4e7a-9b6c-ef70242b89f2
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

# PFND3D12DDI_RESOURCECOPY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_RESOURCECOPY Pfnd3d12ddiResourcecopy; 

// Definition

VOID Pfnd3d12ddiResourcecopy 
(
	 D3D12DDI_HCOMMANDLIST
	 D3D12DDI_HRESOURCE
	 D3D12DDI_HRESOURCE
)
{...}

PFND3D12DDI_RESOURCECOPY 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param D3D12DDI_HRESOURCE: 
### -param D3D12DDI_HRESOURCE: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also