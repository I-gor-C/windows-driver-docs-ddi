---
UID: NC.d3d12umddi.PFND3D12DDI_EXECUTE_INDIRECT
title: PFND3D12DDI_EXECUTE_INDIRECT
author: windows-driver-content
description: 
ms.assetid: 5056e151-1655-4c28-88d2-4d5a81d6ff2d
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

# PFND3D12DDI_EXECUTE_INDIRECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_EXECUTE_INDIRECT Pfnd3d12ddiExecuteIndirect; 

// Definition

VOID Pfnd3d12ddiExecuteIndirect 
(
	 D3D12DDI_HCOMMANDLIST
	 D3D12DDI_HCOMMANDSIGNATURE
	UINT MaxCommandCount
	D3D12DDIARG_BUFFER_PLACEMENT ArgumentBuffer
	D3D12DDIARG_BUFFER_PLACEMENT CountBuffer
)
{...}

PFND3D12DDI_EXECUTE_INDIRECT 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param D3D12DDI_HCOMMANDSIGNATURE: 
### -param MaxCommandCount: 
### -param ArgumentBuffer: 
### -param CountBuffer: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also