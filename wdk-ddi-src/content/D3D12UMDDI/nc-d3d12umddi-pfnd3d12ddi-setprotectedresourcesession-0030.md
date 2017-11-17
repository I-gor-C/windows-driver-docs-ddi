---
UID: NC.d3d12umddi.PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030
title: PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030
author: windows-driver-content
description: 
ms.assetid: e0aaef16-79bf-43b9-a350-5d063babd2b2
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

# PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030 Pfnd3d12ddiSetprotectedresourcesession0030; 

// Definition

VOID Pfnd3d12ddiSetprotectedresourcesession0030 
(
	 D3D12DDI_HCOMMANDLIST
	 D3D12DDI_HPROTECTEDRESOURCESESSION_0030
)
{...}

PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param D3D12DDI_HPROTECTEDRESOURCESESSION_0030: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also