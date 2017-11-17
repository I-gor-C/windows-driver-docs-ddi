---
UID: NC.d3d12umddi.PFND3D12DDI_SET_ROOT_DESCRIPTOR_TABLE
title: PFND3D12DDI_SET_ROOT_DESCRIPTOR_TABLE
author: windows-driver-content
description: 
ms.assetid: 4c5d4423-2878-4285-a640-85e49095fca8
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

# PFND3D12DDI_SET_ROOT_DESCRIPTOR_TABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_SET_ROOT_DESCRIPTOR_TABLE Pfnd3d12ddiSetRootDescriptorTable; 

// Definition

VOID Pfnd3d12ddiSetRootDescriptorTable 
(
	 D3D12DDI_HCOMMANDLIST
	UINT RootParameterIndex
	D3D12DDI_GPU_DESCRIPTOR_HANDLE BaseDescriptor
)
{...}

PFND3D12DDI_SET_ROOT_DESCRIPTOR_TABLE 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param RootParameterIndex: 
### -param BaseDescriptor: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also