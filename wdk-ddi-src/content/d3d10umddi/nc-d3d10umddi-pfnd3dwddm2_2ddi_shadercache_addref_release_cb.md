---
UID: NC:d3d10umddi.PFND3DWDDM2_2DDI_SHADERCACHE_ADDREF_RELEASE_CB
title: PFND3DWDDM2_2DDI_SHADERCACHE_ADDREF_RELEASE_CB
author: windows-driver-content
description: The pfnShaderCacheAddRefCb callback function supports the ability to extend the lifetime of a shader cache.
old-location: display\pfnd3dwddm2_2ddi_shadercache_addref_release_cb.htm
old-project: display
ms.assetid: 2CE40805-D530-47EF-B251-DB3878208504
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3DWDDM2_2DDI_SHADERCACHE_ADDREF_RELEASE_CB, d3d10umddi/pfnShaderCacheAddRefCb, display.pfnd3dwddm2_2ddi_shadercache_addref_release_cb, pfnShaderCacheAddRefCb, pfnShaderCacheAddRefCb callback function [Display Devices]
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
-	pfnShaderCacheAddRefCb
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3DWDDM2_2DDI_SHADERCACHE_ADDREF_RELEASE_CB callback function
The <i>pfnShaderCacheAddRefCb</i> callback function supports the ability to extend the lifetime of a shader cache.

## Syntax

```
PFND3DWDDM2_2DDI_SHADERCACHE_ADDREF_RELEASE_CB Pfnd3dwddm22DdiShadercacheAddrefReleaseCb;

void Pfnd3dwddm22DdiShadercacheAddrefReleaseCb(
  D3DWDDM2_2DDI_HRTCACHESESSION hCacheSession
)
{...}
```

## Parameters

`hCacheSession`

The handler of a cache session.


## Return Value

This callback function does not return a value.

## Remarks

Access this callback function by using the <a href="..\d3d10umddi\ns-d3d10umddi-d3dwddm2_2ddi_corelayer_devicecallbacks.md">D3DWDDM2_2DDI_CORELAYER_DEVICECALLBACKS</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d10umddi.h (include D3d12umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3dwddm2_2ddi_corelayer_devicecallbacks.md">D3DWDDM2_2DDI_CORELAYER_DEVICECALLBACKS</a>