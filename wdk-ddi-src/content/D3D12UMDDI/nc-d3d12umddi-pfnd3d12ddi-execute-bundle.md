---
UID: NC.d3d12umddi.PFND3D12DDI_EXECUTE_BUNDLE
title: PFND3D12DDI_EXECUTE_BUNDLE
author: windows-driver-content
description: 
ms.assetid: 69d85747-9bee-4fed-9c00-669baa8f3a0f
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

# PFND3D12DDI_EXECUTE_BUNDLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_EXECUTE_BUNDLE Pfnd3d12ddiExecuteBundle; 

// Definition

VOID Pfnd3d12ddiExecuteBundle 
(
	 D3D12DDI_HCOMMANDLIST
	 D3D12DDI_HCOMMANDLIST
)
{...}

PFND3D12DDI_EXECUTE_BUNDLE 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param D3D12DDI_HCOMMANDLIST: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also