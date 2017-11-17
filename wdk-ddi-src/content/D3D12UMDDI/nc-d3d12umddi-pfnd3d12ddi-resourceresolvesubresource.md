---
UID: NC.d3d12umddi.PFND3D12DDI_RESOURCERESOLVESUBRESOURCE
title: PFND3D12DDI_RESOURCERESOLVESUBRESOURCE
author: windows-driver-content
description: 
ms.assetid: 4403bff2-969e-4f66-9b78-e9b7a377d6a9
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

# PFND3D12DDI_RESOURCERESOLVESUBRESOURCE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_RESOURCERESOLVESUBRESOURCE Pfnd3d12ddiResourceresolvesubresource; 

// Definition

VOID Pfnd3d12ddiResourceresolvesubresource 
(
	 D3D12DDI_HCOMMANDLIST
	 D3D12DDI_HRESOURCE
	 UINT
	 D3D12DDI_HRESOURCE
	 UINT
	 DXGI_FORMAT
)
{...}

PFND3D12DDI_RESOURCERESOLVESUBRESOURCE 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param D3D12DDI_HRESOURCE: 
### -param UINT: 
### -param D3D12DDI_HRESOURCE: 
### -param UINT: 
### -param DXGI_FORMAT: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also