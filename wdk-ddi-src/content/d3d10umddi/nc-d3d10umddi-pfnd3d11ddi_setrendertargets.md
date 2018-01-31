---
UID : NC:d3d10umddi.PFND3D11DDI_SETRENDERTARGETS
title : PFND3D11DDI_SETRENDERTARGETS
author : windows-driver-content
description : The SetRenderTargets(D3D11) function sets render target surfaces.
old-location : display\setrendertargets_d3d11_.htm
old-project : display
ms.assetid : cfe5f570-4e53-43ee-942d-56da8dfcfe80
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.setrendertargets_d3d11_, SetRenderTargets callback function [Display Devices], SetRenderTargets, PFND3D11DDI_SETRENDERTARGETS, PFND3D11DDI_SETRENDERTARGETS, d3d10umddi/SetRenderTargets, UserModeDisplayDriverDx11_Functions_a24d5500-fe0a-4d17-a3fb-acb6ed9e4698.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : SetRenderTargets(D3D11) is supported beginning with the Windows 7 operating system.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_SETRENDERTARGETS callback function
The <i>SetRenderTargets(D3D11)</i> function sets render target surfaces.

## Syntax

```
PFND3D11DDI_SETRENDERTARGETS Pfnd3d11ddiSetrendertargets;

void Pfnd3d11ddiSetrendertargets(
   D3D10DDI_HDEVICE,
  CONST D3D10DDI_HRENDERTARGETVIEW *,
  UINT NumRTVs,
  UINT ClearSlots,
   D3D10DDI_HDEPTHSTENCILVIEW,
  CONST D3D11DDI_HUNORDEREDACCESSVIEW *,
  CONST UINT *,
  UINT UAVStartSlot,
  UINT NumUAVs,
  UINT UAVRangeStart,
  UINT UAVRangeSize
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`NumRTVs`

The number of elements in the array that <i>phRenderTargetView</i> specifies for the render target views (RTVs) to set.

`ClearSlots`



`D3D10DDI_HDEPTHSTENCILVIEW`



`*`



`*`



`UAVStartSlot`



`NumUAVs`

The number of unordered access view objects (UAVs) to set.

`UAVRangeStart`



`UAVRangeSize`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function, the Microsoft Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of <i>SetRenderTargets(D3D11)</i> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_buffer_unorderedaccessview.md">D3D11DDIARG_BUFFER_UNORDEREDACCESSVIEW</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_SETRENDERTARGETS callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>