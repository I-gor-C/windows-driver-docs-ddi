---
UID: NC:d3d10umddi.PFND3D10DDI_SETERROR_CB
title: PFND3D10DDI_SETERROR_CB
author: windows-driver-content
description: The pfnSetErrorCb function sets the return error code of a user-mode display driver's function.
old-location: display\pfnseterrorcb.htm
old-project: display
ms.assetid: 968b04a7-8869-410c-a6fc-83d57726858f
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D10DDI_SETERROR_CB, d3d10state_functions_1d57cbc9-ec37-47ce-ab4f-71535419375a.xml, d3d10umddi/pfnSetErrorCb, display.pfnseterrorcb, pfnSetErrorCb, pfnSetErrorCb callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
-	pfnSetErrorCb
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_SETERROR_CB callback function
The <b>pfnSetErrorCb</b> function sets the return error code of a user-mode display driver's function.

## Syntax

```
PFND3D10DDI_SETERROR_CB Pfnd3d10ddiSeterrorCb;

void Pfnd3d10ddiSeterrorCb(
   D3D10DDI_HRTCORELAYER,
   HRESULT
)
{...}
```

## Parameters

`D3D10DDI_HRTCORELAYER`



`HRESULT`




## Return Value

None

## Remarks

A user-mode display driver can call <b>pfnSetErrorCb</b> many times for each driver invocation. For the driver's functions that do not return status codes, the driver uses <b>pfnSetErrorCb</b> to return error information to the Direct3D runtime.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541820">D3D10DDI_CORELAYER_DEVICECALLBACKS</a>