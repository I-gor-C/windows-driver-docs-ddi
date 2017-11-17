---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_GETRESOURCELAYOUT
title: PFND3DWDDM2_0DDI_GETRESOURCELAYOUT
author: windows-driver-content
description: 
ms.assetid: ff3f8a7b-3770-4dee-9ccb-8b776704fd6b
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

# PFND3DWDDM2_0DDI_GETRESOURCELAYOUT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_GETRESOURCELAYOUT Pfnd3dwddm20DdiGetresourcelayout; 

// Definition

VOID Pfnd3dwddm20DdiGetresourcelayout 
(
	 D3D10DDI_HDEVICE
	 D3D10DDI_HRESOURCE
	UINT SubresourceCount
	D3DKMT_HANDLE *
	D3DWDDM2_0DDI_TEXTURE_LAYOUT *
	UINT *pMipLevelSwizzleTransition
	D3DWDDM2_0DDI_SUBRESOURCE_LAYOUT *
)
{...}

PFND3DWDDM2_0DDI_GETRESOURCELAYOUT 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D10DDI_HRESOURCE: 
### -param SubresourceCount: 
### -param *: 
### -param *: 
### -param *pMipLevelSwizzleTransition: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also