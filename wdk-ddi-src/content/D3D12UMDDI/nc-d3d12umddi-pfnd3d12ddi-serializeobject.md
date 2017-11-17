---
UID: NC.d3d12umddi.PFND3D12DDI_SERIALIZEOBJECT
title: PFND3D12DDI_SERIALIZEOBJECT
author: windows-driver-content
description: 
ms.assetid: 6fd88db4-86b0-4912-8543-39dbe03d10a0
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

# PFND3D12DDI_SERIALIZEOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_SERIALIZEOBJECT Pfnd3d12ddiSerializeobject; 

// Definition

HRESULT Pfnd3d12ddiSerializeobject 
(
	D3D12DDI_HDEVICE hDevice
	D3D12DDI_HANDLETYPE HandleType
	HANDLE hObject
	SIZE_T *BlobSize
	 const UINT **ppBlob
)
{...}

PFND3D12DDI_SERIALIZEOBJECT 


```

## -parameters

### -param hDevice: 
### -param HandleType: 
### -param hObject: 
### -param *BlobSize: 
### -param **ppBlob: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also