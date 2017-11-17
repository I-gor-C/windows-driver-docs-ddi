---
UID: NC.d3d12umddi.PFND3D12DDI_CONTENTPROTECTIONSESSION_GET_STATUS_0020
title: PFND3D12DDI_CONTENTPROTECTIONSESSION_GET_STATUS_0020
author: windows-driver-content
description: 
ms.assetid: 5d213c54-e61f-4391-b1d6-27796156e54a
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

# PFND3D12DDI_CONTENTPROTECTIONSESSION_GET_STATUS_0020 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CONTENTPROTECTIONSESSION_GET_STATUS_0020 Pfnd3d12ddiContentprotectionsessionGetStatus0020; 

// Definition

HRESULT Pfnd3d12ddiContentprotectionsessionGetStatus0020 
(
	D3D12DDI_HDEVICE hDrvDevice
	D3D12DDI_HCONTENTPROTECTIONSESSION_0020 hDrvContentProtectionSession
	D3D12DDI_CONTENT_PROTECTION_SESSION_STATUS_0020 *pStatus
)
{...}

PFND3D12DDI_CONTENTPROTECTIONSESSION_GET_STATUS_0020 


```

## -parameters

### -param hDrvDevice: 
### -param hDrvContentProtectionSession: 
### -param *pStatus: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also