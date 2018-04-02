---
UID: NC:d3d10umddi.PFND3D10DDI_SETSHADERRESOURCES
title: PFND3D10DDI_SETSHADERRESOURCES
author: windows-driver-content
description: The CsSetShaderResources function sets resources for a compute shader.
old-location: display\cssetshaderresources.htm
old-project: display
ms.assetid: 29570c3b-eb3b-4d8f-b471-8f3ea6226e23
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CsSetShaderResources, CsSetShaderResources callback function [Display Devices], PFND3D10DDI_SETSHADERRESOURCES, UserModeDisplayDriverDx11_Functions_0fe556e4-8c6f-4848-b502-d35744c60713.xml, d3d10umddi/CsSetShaderResources, display.cssetshaderresources
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CsSetShaderResources is supported beginning with the Windows 7 operating system.
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
-	CsSetShaderResources
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_SETSHADERRESOURCES callback function
The <b>CsSetShaderResources</b> function sets resources for a compute shader.

## Syntax

```
PFND3D10DDI_SETSHADERRESOURCES Pfnd3d10ddiSetshaderresources;

void Pfnd3d10ddiSetshaderresources(
   D3D10DDI_HDEVICE,
  UINT StartSlot,
  UINT NumViews,
  CONST D3D10DDI_HSHADERRESOURCEVIEW *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`StartSlot`



`NumViews`

The total number of views to set.

`*`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, the Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of <b>CsSetShaderResources</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CsSetShaderResources is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>