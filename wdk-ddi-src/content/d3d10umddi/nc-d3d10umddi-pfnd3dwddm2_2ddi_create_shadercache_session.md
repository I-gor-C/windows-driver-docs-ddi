---
UID: NC:d3d10umddi.PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION
title: PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION
author: windows-driver-content
description: The pfnCreateShaderCacheSession callback function creates a shader cache session.
old-location: display\pfnd3dwddm2_2ddi_create_shadercache_session.htm
old-project: display
ms.assetid: 14B3AB7A-DB27-412F-9578-5BA44628ECE7
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION, d3d10umddi/pfnCreateShaderCacheSession, display.pfnd3dwddm2_2ddi_create_shadercache_session, pfnCreateShaderCacheSession, pfnCreateShaderCacheSession callback function [Display Devices]
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
-	pfnCreateShaderCacheSession
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION callback function
The <i>pfnCreateShaderCacheSession</i> callback function creates a shader cache session.

## Syntax

```
PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION Pfnd3dwddm22DdiCreateShadercacheSession;

void Pfnd3dwddm22DdiCreateShadercacheSession(
   D3D10DDI_HDEVICE,
   D3DWDDM2_2DDI_HCACHESESSION,
   D3DWDDM2_2DDI_HRTCACHESESSION
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3DWDDM2_2DDI_HCACHESESSION`



`D3DWDDM2_2DDI_HRTCACHESESSION`




## Return Value

This callback function does not return a value.

## Remarks

The runtime uses the object that is created to inform the driver of different caching contexts. It can be used to direct the caching callbacks towards a process-local cache or a per-component cache which is shared by multiple processes.

Access this callback function by using the <a href="https://msdn.microsoft.com/4E082193-70BA-4F36-9001-2A12014F3AC3">D3DWDDM2_2DDI_DEVICEFUNCS</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d10umddi.h (include D3d12umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/4E082193-70BA-4F36-9001-2A12014F3AC3">D3DWDDM2_2DDI_DEVICEFUNCS</a>