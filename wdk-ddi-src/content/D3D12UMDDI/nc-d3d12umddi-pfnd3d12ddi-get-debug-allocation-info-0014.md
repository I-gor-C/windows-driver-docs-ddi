---
UID: NC.d3d12umddi.PFND3D12DDI_GET_DEBUG_ALLOCATION_INFO_0014
title: PFND3D12DDI_GET_DEBUG_ALLOCATION_INFO_0014
author: windows-driver-content
description: 
ms.assetid: f537abd3-57ea-493f-8ffb-86ea0aa3d67b
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

# PFND3D12DDI_GET_DEBUG_ALLOCATION_INFO_0014 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_GET_DEBUG_ALLOCATION_INFO_0014 Pfnd3d12ddiGetDebugAllocationInfo0014; 

// Definition

VOID Pfnd3d12ddiGetDebugAllocationInfo0014 
(
	D3D12DDI_HDEVICE hDevice
	D3D12DDI_HANDLE_AND_TYPE Object
	UINT *pNumVirtualAddressInfos
	D3D12DDI_DEBUG_VIRTUAL_ADDRESS_ALLOCATION_INFO_0012 *pVirtualAddressInfos
	UINT *pNumKMTInfos
	D3D12DDI_DEBUG_KMT_ALLOCATION_INFO_0014 *pKMTInfos
)
{...}

PFND3D12DDI_GET_DEBUG_ALLOCATION_INFO_0014 


```

## -parameters

### -param hDevice: 
### -param Object: 
### -param *pNumVirtualAddressInfos: 
### -param *pVirtualAddressInfos: 
### -param *pNumKMTInfos: 
### -param *pKMTInfos: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also