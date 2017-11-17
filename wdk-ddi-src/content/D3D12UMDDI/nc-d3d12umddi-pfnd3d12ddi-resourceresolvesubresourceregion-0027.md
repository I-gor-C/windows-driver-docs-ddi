---
UID: NC.d3d12umddi.PFND3D12DDI_RESOURCERESOLVESUBRESOURCEREGION_0027
title: PFND3D12DDI_RESOURCERESOLVESUBRESOURCEREGION_0027
author: windows-driver-content
description: 
ms.assetid: 567b92a9-3c54-43f9-8a79-9cc4e9d75389
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

# PFND3D12DDI_RESOURCERESOLVESUBRESOURCEREGION_0027 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_RESOURCERESOLVESUBRESOURCEREGION_0027 Pfnd3d12ddiResourceresolvesubresourceregion0027; 

// Definition

VOID Pfnd3d12ddiResourceresolvesubresourceregion0027 
(
	 D3D12DDI_HCOMMANDLIST
	D3D12DDI_HRESOURCE DstResource
	UINT DstSubresource
	UINT DstX
	UINT DstY
	D3D12DDI_HRESOURCE SrcResource
	UINT SrcSubresource
	D3D12DDI_RECT *pSrcRect
	DXGI_FORMAT Format
	D3D12DDI_RESOLVE_MODE ResolveMode
)
{...}

PFND3D12DDI_RESOURCERESOLVESUBRESOURCEREGION_0027 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param DstResource: 
### -param DstSubresource: 
### -param DstX: 
### -param DstY: 
### -param SrcResource: 
### -param SrcSubresource: 
### -param *pSrcRect: 
### -param Format: 
### -param ResolveMode: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also