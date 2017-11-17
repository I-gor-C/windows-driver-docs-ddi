---
UID: NC.d3d12umddi.PFND3D12DDI_OM_SETBLENDFACTOR
title: PFND3D12DDI_OM_SETBLENDFACTOR
author: windows-driver-content
description: 
ms.assetid: 43efb856-ae0a-440f-8650-f493a353b3ce
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

# PFND3D12DDI_OM_SETBLENDFACTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_OM_SETBLENDFACTOR Pfnd3d12ddiOmSetblendfactor; 

// Definition

VOID Pfnd3d12ddiOmSetblendfactor 
(
	 D3D12DDI_HCOMMANDLIST
	CONST FLOAT[4]
)
{...}

PFND3D12DDI_OM_SETBLENDFACTOR 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param FLOAT[4]: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also