---
UID: NC.d3d12umddi.PFND3D12DDI_BEGIN_PASS
title: PFND3D12DDI_BEGIN_PASS
author: windows-driver-content
description: 
ms.assetid: c72e131a-b8d8-4ed1-aa93-6e99ccc0439e
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

# PFND3D12DDI_BEGIN_PASS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_BEGIN_PASS Pfnd3d12ddiBeginPass; 

// Definition

VOID Pfnd3d12ddiBeginPass 
(
	 D3D12DDI_HCOMMANDLIST
	 D3D12DDI_HPASS
	D3D12DDI_PASS_FLAGS PassFlags
)
{...}

PFND3D12DDI_BEGIN_PASS 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param D3D12DDI_HPASS: 
### -param PassFlags: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also