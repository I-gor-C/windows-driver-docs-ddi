---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_GETDATAFORNEWHARDWAREKEY
title: PFND3DWDDM2_0DDI_GETDATAFORNEWHARDWAREKEY
author: windows-driver-content
description: 
ms.assetid: d13ee20d-83b6-4b10-89d3-413b09741bb9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d10umddi.h
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

# PFND3DWDDM2_0DDI_GETDATAFORNEWHARDWAREKEY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_GETDATAFORNEWHARDWAREKEY Pfnd3dwddm20DdiGetdatafornewhardwarekey; 

// Definition

HRESULT Pfnd3dwddm20DdiGetdatafornewhardwarekey 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HCRYPTOSESSION hCryptoSession
	UINT PrivateInputSize
	 const void *pPrivatInputData
	UINT64 *pPrivateOutputData
)
{...}

PFND3DWDDM2_0DDI_GETDATAFORNEWHARDWAREKEY 


```

## -parameters

### -param hDevice: 
### -param hCryptoSession: 
### -param PrivateInputSize: 
### -param *pPrivatInputData: 
### -param *pPrivateOutputData: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also