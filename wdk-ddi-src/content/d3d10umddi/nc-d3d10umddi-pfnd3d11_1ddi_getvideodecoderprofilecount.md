---
UID: NC:d3d10umddi.PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT
title: PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT
author: windows-driver-content
description: Queries the number of video decoder profiles that are supported by the display miniport driver.
old-location: display\getvideodecoderprofilecount.htm
old-project: display
ms.assetid: ae24bc29-177e-48a1-adf9-ed8c79b7f39c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT, d3d10umddi/pfnGetVideoDecoderProfileCount, display.getvideodecoderprofilecount, pfnGetVideoDecoderProfileCount, pfnGetVideoDecoderProfileCount callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	pfnGetVideoDecoderProfileCount
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT callback function
Queries the number of video decoder profiles that are supported by the display miniport driver.

## Syntax

```
PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT Pfnd3d111DdiGetvideodecoderprofilecount;

void Pfnd3d111DdiGetvideodecoderprofilecount(
   D3D10DDI_HDEVICE,
  UINT *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |