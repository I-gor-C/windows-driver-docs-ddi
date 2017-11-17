---
UID: NC.d3d12umddi.PFND3D12DDI_OM_SETSTENCILREF
title: PFND3D12DDI_OM_SETSTENCILREF
author: windows-driver-content
description: 
ms.assetid: c08f1246-a212-4c3c-9a2d-681660a15e05
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

# PFND3D12DDI_OM_SETSTENCILREF callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_OM_SETSTENCILREF Pfnd3d12ddiOmSetstencilref; 

// Definition

VOID Pfnd3d12ddiOmSetstencilref 
(
	 D3D12DDI_HCOMMANDLIST
	 UINT
)
{...}

PFND3D12DDI_OM_SETSTENCILREF 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param UINT: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also