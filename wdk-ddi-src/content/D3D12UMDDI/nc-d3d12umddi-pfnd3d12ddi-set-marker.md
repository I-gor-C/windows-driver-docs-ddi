---
UID: NC.d3d12umddi.PFND3D12DDI_SET_MARKER
title: PFND3D12DDI_SET_MARKER
author: windows-driver-content
description: 
ms.assetid: 4d232c75-81ac-4d9a-9740-b5d2dd9458b5
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

# PFND3D12DDI_SET_MARKER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_SET_MARKER Pfnd3d12ddiSetMarker; 

// Definition

VOID Pfnd3d12ddiSetMarker 
(
	 D3D12DDI_HCOMMANDLIST
	 UINT64
)
{...}

PFND3D12DDI_SET_MARKER 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param UINT64: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also