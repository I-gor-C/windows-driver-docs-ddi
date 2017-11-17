---
UID: NC.d3d12umddi.PFND3D12DDI_DRAWINDEXEDINSTANCED
title: PFND3D12DDI_DRAWINDEXEDINSTANCED
author: windows-driver-content
description: 
ms.assetid: 9743a68a-9929-430c-a13e-750f0ce10137
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

# PFND3D12DDI_DRAWINDEXEDINSTANCED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DRAWINDEXEDINSTANCED Pfnd3d12ddiDrawindexedinstanced; 

// Definition

VOID Pfnd3d12ddiDrawindexedinstanced 
(
	 D3D12DDI_HCOMMANDLIST
	 UINT
	 UINT
	 UINT
	 INT
	 UINT
)
{...}

PFND3D12DDI_DRAWINDEXEDINSTANCED 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param UINT: 
### -param UINT: 
### -param UINT: 
### -param INT: 
### -param UINT: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also