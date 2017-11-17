---
UID: NC.d3d12umddi.PFND3D12DDI_RESETCOMMANDLIST
title: PFND3D12DDI_RESETCOMMANDLIST
author: windows-driver-content
description: 
ms.assetid: c8126580-f1e6-4135-b07c-4d39ee80ec26
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

# PFND3D12DDI_RESETCOMMANDLIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_RESETCOMMANDLIST Pfnd3d12ddiResetcommandlist; 

// Definition

VOID Pfnd3d12ddiResetcommandlist 
(
	 D3D12DDI_HCOMMANDLIST
	CONST D3D12DDIARG_RESETCOMMANDLIST *
)
{...}

PFND3D12DDI_RESETCOMMANDLIST 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also