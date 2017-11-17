---
UID: NC.d3d12umddi.PFND3D12DDI_OM_SET_RENDER_TARGETS_0003
title: PFND3D12DDI_OM_SET_RENDER_TARGETS_0003
author: windows-driver-content
description: 
ms.assetid: aa9a77dc-d4a1-4ace-8033-2bf4216a3f79
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

# PFND3D12DDI_OM_SET_RENDER_TARGETS_0003 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_OM_SET_RENDER_TARGETS_0003 Pfnd3d12ddiOmSetRenderTargets0003; 

// Definition

VOID Pfnd3d12ddiOmSetRenderTargets0003 
(
	 D3D12DDI_HCOMMANDLIST
	UINT NumRenderTargetDescriptors
	CONST D3D12DDI_CPU_DESCRIPTOR_HANDLE *pRenderTargetDescriptors
	BOOL RTsSingleHandleToDescriptorRange
	CONST D3D12DDI_CPU_DESCRIPTOR_HANDLE *pDepthStencilDescriptor
)
{...}

PFND3D12DDI_OM_SET_RENDER_TARGETS_0003 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param NumRenderTargetDescriptors: 
### -param *pRenderTargetDescriptors: 
### -param RTsSingleHandleToDescriptorRange: 
### -param *pDepthStencilDescriptor: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also