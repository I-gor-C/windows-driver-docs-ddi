---
UID: NC.d3d12umddi.PFND3D12DDI_COPYBUFFERREGION_0003
title: PFND3D12DDI_COPYBUFFERREGION_0003
author: windows-driver-content
description: 
ms.assetid: 7f2d7d0a-6438-46fa-a20d-2b57524f0a59
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

# PFND3D12DDI_COPYBUFFERREGION_0003 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_COPYBUFFERREGION_0003 Pfnd3d12ddiCopybufferregion0003; 

// Definition

VOID Pfnd3d12ddiCopybufferregion0003 
(
	 D3D12DDI_HCOMMANDLIST
	D3D12DDIARG_BUFFER_PLACEMENT Dst
	D3D12DDIARG_BUFFER_PLACEMENT Src
	UINT64 SrcBytes
)
{...}

PFND3D12DDI_COPYBUFFERREGION_0003 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param Dst: 
### -param Src: 
### -param SrcBytes: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also