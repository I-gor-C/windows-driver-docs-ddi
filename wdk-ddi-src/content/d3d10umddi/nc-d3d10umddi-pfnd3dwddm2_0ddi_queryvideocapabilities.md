---
UID: NC:d3d10umddi.PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES
title: PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES
author: windows-driver-content
description: Queries the driver for video capabilities. Required for Windows Display Driver Model (WDDM) 2.0 or later drivers.
old-location: display\queryvideocapabilities.htm
old-project: display
ms.assetid: C86C7D1C-541F-4EC3-B4C8-126826BE3529
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES, d3d10umddi/pfnQueryVideoCapabilities, display.queryvideocapabilities, pfnQueryVideoCapabilities, pfnQueryVideoCapabilities callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	D3d10umddi.h
api_name:
-	pfnQueryVideoCapabilities
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES callback function
Queries the driver for video capabilities. Required for Windows Display Driver Model (WDDM) 2.0 or later drivers.

## Syntax

```
PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES Pfnd3dwddm20DdiQueryvideocapabilities;

void Pfnd3dwddm20DdiQueryvideocapabilities(
  D3D10DDI_HDEVICE hDevice,
  D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY QueryType,
  UINT DataSize,
  VOID *pData
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context). The Direct3D runtime passed the user-mode driver this handle as the <b>hDevice</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542931">D3DDDIARG_CREATEDEVICE</a> structure at device creation.

`QueryType`

Specifies the <a href="https://msdn.microsoft.com/library/windows/hardware/dn894616">D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY</a> value indicating the type of data being queried.

`DataSize`

Specifies the size of the <b>pData</b> member. This is dependent on the <b>QueryType</b> member.

`*pData`

Pointer to a structure containing data further identifying input parameters and output parameters to be filled in by the driver. The following structures are supported for the following query types:


## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn894615">D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn894616">D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn894617">D3DWDDM2_0DDI_VIDEO_CAPABILITY_RECOMMEND_DECODER_DOWNSAMPLING</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn894620">D3DWDDM2_0DDI_VIDEO_DECODER_CAPS</a>