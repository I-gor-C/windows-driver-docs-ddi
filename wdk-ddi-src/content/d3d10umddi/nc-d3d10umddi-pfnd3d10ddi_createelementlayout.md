---
UID: NC:d3d10umddi.PFND3D10DDI_CREATEELEMENTLAYOUT
title: PFND3D10DDI_CREATEELEMENTLAYOUT
author: windows-driver-content
description: The CreateElementLayout function creates an element layout.
old-location: display\createelementlayout.htm
old-project: display
ms.assetid: 5af2189a-a064-4c62-be09-733c1d632983
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateElementLayout, CreateElementLayout callback function [Display Devices], PFND3D10DDI_CREATEELEMENTLAYOUT, UserModeDisplayDriverDx10_Functions_ca001144-74f8-4ff7-9cce-664d4070ad3d.xml, d3d10umddi/CreateElementLayout, display.createelementlayout
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
-	CreateElementLayout
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_CREATEELEMENTLAYOUT callback function
The <b>CreateElementLayout</b> function creates an element layout.

## Syntax

```
PFND3D10DDI_CREATEELEMENTLAYOUT Pfnd3d10ddiCreateelementlayout;

void Pfnd3d10ddiCreateelementlayout(
   D3D10DDI_HDEVICE,
  CONST D3D10DDIARG_CREATEELEMENTLAYOUT *,
   D3D10DDI_HELEMENTLAYOUT,
   D3D10DDI_HRTELEMENTLAYOUT
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HELEMENTLAYOUT`



`D3D10DDI_HRTELEMENTLAYOUT`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver can pass E_OUTOFMEMORY (if the driver runs out of memory) or D3DDDIERR_DEVICEREMOVED (if the device has been removed) in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is invalid; therefore, the runtime will not call the <a href="https://msdn.microsoft.com/8b6a07b5-5358-45d3-af42-84f8a6327535">DestroyElementLayout</a> function to destroy the handle that the <i>hElementLayout</i> parameter specifies.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/9fc80cea-8e4a-467a-b232-74333d2ceb5f">CalcPrivateElementLayoutSize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541674">D3D10DDIARG_CREATEELEMENTLAYOUT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/8b6a07b5-5358-45d3-af42-84f8a6327535">DestroyElementLayout</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>