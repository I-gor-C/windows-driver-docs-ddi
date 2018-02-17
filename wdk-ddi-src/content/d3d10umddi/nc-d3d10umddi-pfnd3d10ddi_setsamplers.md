---
UID: NC:d3d10umddi.PFND3D10DDI_SETSAMPLERS
title: PFND3D10DDI_SETSAMPLERS
author: windows-driver-content
description: The CsSetSamplers function sets samplers for a compute shader.
old-location: display\cssetsamplers.htm
old-project: display
ms.assetid: 7bf05fb6-e959-464a-9e6b-74c568d1d88c
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.cssetsamplers, CsSetSamplers callback function [Display Devices], CsSetSamplers, PFND3D10DDI_SETSAMPLERS, PFND3D10DDI_SETSAMPLERS, d3d10umddi/CsSetSamplers, UserModeDisplayDriverDx11_Functions_a2d1c287-1dab-4852-a643-8d568d04f64d.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CsSetSamplers is supported beginning with the Windows 7 operating system.
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
-	CsSetSamplers
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D10DDI_SETSAMPLERS callback function
The <b>CsSetSamplers</b> function sets samplers for a compute shader.

## Syntax

```
PFND3D10DDI_SETSAMPLERS Pfnd3d10ddiSetsamplers;

void Pfnd3d10ddiSetsamplers(
   D3D10DDI_HDEVICE,
  UINT StartSlot,
  UINT NumSamplers,
  CONST D3D10DDI_HSAMPLER *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`StartSlot`



`NumSamplers`

The total number of samplers to set.

`*`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function, the Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of <b>CsSetSamplers</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CsSetSamplers is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_SETSAMPLERS callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>