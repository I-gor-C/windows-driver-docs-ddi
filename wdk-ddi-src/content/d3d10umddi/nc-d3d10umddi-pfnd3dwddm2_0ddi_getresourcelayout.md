---
UID: NC:d3d10umddi.PFND3DWDDM2_0DDI_GETRESOURCELAYOUT
title: PFND3DWDDM2_0DDI_GETRESOURCELAYOUT
author: windows-driver-content
description: The pfnGetResourceLayout callback function supports getting resource layout information.
old-location: display\pfnd3dwddm2_0ddi_getresourcelayout.htm
old-project: display
ms.assetid: 0158F1B4-AA6E-41F9-BAEF-A3C688758205
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: PFND3DWDDM2_0DDI_GETRESOURCELAYOUT, d3d10umddi/pfnGetResourceLayout, display.pfnd3dwddm2_0ddi_getresourcelayout, pfnGetResourceLayout, pfnGetResourceLayout callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	d3d10umddi.h
api_name:
-	pfnGetResourceLayout
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3DWDDM2_0DDI_GETRESOURCELAYOUT callback function
The <i>pfnGetResourceLayout</i> callback function supports getting resource layout information.

## Syntax

```
PFND3DWDDM2_0DDI_GETRESOURCELAYOUT Pfnd3dwddm20DdiGetresourcelayout;

void Pfnd3dwddm20DdiGetresourcelayout(
   D3D10DDI_HDEVICE,
   D3D10DDI_HRESOURCE,
  UINT SubresourceCount,
  D3DKMT_HANDLE *,
  D3DWDDM2_0DDI_TEXTURE_LAYOUT *,
  UINT *pMipLevelSwizzleTransition,
  D3DWDDM2_0DDI_SUBRESOURCE_LAYOUT *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D10DDI_HRESOURCE`



`SubresourceCount`

The subresource count.

`*`



`*`



`*pMipLevelSwizzleTransition`

A pointer to a MIP level swizzle transition.

`*`




## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d10umddi.h (include D3d12umddi.h) |