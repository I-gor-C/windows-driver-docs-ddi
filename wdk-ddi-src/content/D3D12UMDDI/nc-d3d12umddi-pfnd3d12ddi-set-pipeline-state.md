---
UID: NC.d3d12umddi.PFND3D12DDI_SET_PIPELINE_STATE
title: PFND3D12DDI_SET_PIPELINE_STATE
author: windows-driver-content
description: 
ms.assetid: 366dd266-69bf-4894-af57-63dd0af7b6d2
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

# PFND3D12DDI_SET_PIPELINE_STATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_SET_PIPELINE_STATE Pfnd3d12ddiSetPipelineState; 

// Definition

VOID Pfnd3d12ddiSetPipelineState 
(
	 D3D12DDI_HCOMMANDLIST
	 D3D12DDI_HPIPELINESTATE
)
{...}

PFND3D12DDI_SET_PIPELINE_STATE 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param D3D12DDI_HPIPELINESTATE: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also