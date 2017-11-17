---
UID: NC.d3d12umddi.PFND3D12DDI_CREATE_SAMPLER
title: PFND3D12DDI_CREATE_SAMPLER
author: windows-driver-content
description: 
ms.assetid: 62dc9314-bf61-48a2-88f5-8aa186293948
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

# PFND3D12DDI_CREATE_SAMPLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CREATE_SAMPLER Pfnd3d12ddiCreateSampler; 

// Definition

VOID Pfnd3d12ddiCreateSampler 
(
	 D3D12DDI_HDEVICE
	CONST D3D12DDIARG_CREATE_SAMPLER *
	D3D12DDI_CPU_DESCRIPTOR_HANDLE DestDescriptor
)
{...}

PFND3D12DDI_CREATE_SAMPLER 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param *: 
### -param DestDescriptor: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also