---
UID: NC:d3d10umddi.PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION
title: PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION
author: windows-driver-content
description: The pfnCreateShaderCacheSession callback function creates a shader cache session.
old-location: display\pfnd3dwddm2_2ddi_create_shadercache_session.htm
old-project: display
ms.assetid: 14B3AB7A-DB27-412F-9578-5BA44628ECE7
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.pfnd3dwddm2_2ddi_create_shadercache_session, pfnCreateShaderCacheSession callback function [Display Devices], pfnCreateShaderCacheSession, PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION, PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION, d3d10umddi/pfnCreateShaderCacheSession
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	d3d10umddi.h
apiname:
-	pfnCreateShaderCacheSession
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
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

Access this callback function by using the <a href="..\d3d10umddi\ns-d3d10umddi-d3dwddm2_2ddi_devicefuncs.md">D3DWDDM2_2DDI_DEVICEFUNCS</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d10umddi.h (include D3d12umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3dwddm2_2ddi_devicefuncs.md">D3DWDDM2_2DDI_DEVICEFUNCS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>