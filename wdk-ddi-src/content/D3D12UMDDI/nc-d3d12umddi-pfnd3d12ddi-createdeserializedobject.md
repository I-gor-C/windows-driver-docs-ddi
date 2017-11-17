---
UID: NC.d3d12umddi.PFND3D12DDI_CREATEDESERIALIZEDOBJECT
title: PFND3D12DDI_CREATEDESERIALIZEDOBJECT
author: windows-driver-content
description: 
ms.assetid: 68169f68-d22e-450a-92bd-33d249a5d35e
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

# PFND3D12DDI_CREATEDESERIALIZEDOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CREATEDESERIALIZEDOBJECT Pfnd3d12ddiCreatedeserializedobject; 

// Definition

HRESULT Pfnd3d12ddiCreatedeserializedobject 
(
	D3D12DDI_HDEVICE HDEVICE
	D3D12DDI_HANDLETYPE HandleType
	SIZE_T BlobSize
	CONST UINT *pBlob
	VOID *hObject
	VOID *hRTObject
)
{...}

PFND3D12DDI_CREATEDESERIALIZEDOBJECT 


```

## -parameters

### -param HDEVICE: 
### -param HandleType: 
### -param BlobSize: 
### -param *pBlob: 
### -param *hObject: 
### -param *hRTObject: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also