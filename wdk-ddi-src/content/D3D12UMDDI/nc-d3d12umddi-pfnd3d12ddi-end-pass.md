---
UID: NC.d3d12umddi.PFND3D12DDI_END_PASS
title: PFND3D12DDI_END_PASS
author: windows-driver-content
description: 
ms.assetid: 2778530c-a0c9-4280-8dcf-7de06266bbc8
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

# PFND3D12DDI_END_PASS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_END_PASS Pfnd3d12ddiEndPass; 

// Definition

VOID Pfnd3d12ddiEndPass 
(
	 D3D12DDI_HCOMMANDLIST
	 D3D12DDI_HPASS
)
{...}

PFND3D12DDI_END_PASS 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param D3D12DDI_HPASS: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also