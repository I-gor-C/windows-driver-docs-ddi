---
UID: NC:d3d10umddi.PFND3D11DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT
title: PFND3D11DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT
author: windows-driver-content
description: The CreateGeometryShaderWithStreamOutput(D3D11) function creates a geometry shader with stream output.
old-location: display\creategeometryshaderwithstreamoutput_d3d11_.htm
old-project: display
ms.assetid: 86970ea4-e7d2-4fc3-9f97-75a946a21a17
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.creategeometryshaderwithstreamoutput_d3d11_, CreateGeometryShaderWithStreamOutput callback function [Display Devices], CreateGeometryShaderWithStreamOutput, PFND3D11DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT, PFND3D11DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT, d3d10umddi/CreateGeometryShaderWithStreamOutput, UserModeDisplayDriverDx11_Functions_65b14f27-0df8-421d-95bb-f8a4ebc7c1c1.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CreateGeometryShaderWithStreamOutput(D3D11) is supported beginning with the Windows 7 operating system.
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
-	CreateGeometryShaderWithStreamOutput
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT callback function
The <b>CreateGeometryShaderWithStreamOutput(D3D11)</b> function creates a geometry shader with stream output.

## Syntax

```
PFND3D11DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT Pfnd3d11ddiCreategeometryshaderwithstreamoutput;

void Pfnd3d11ddiCreategeometryshaderwithstreamoutput(
   D3D10DDI_HDEVICE,
  CONST D3D11DDIARG_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT *,
   D3D10DDI_HSHADER,
   D3D10DDI_HRTSHADER,
  CONST D3D10DDIARG_STAGE_IO_SIGNATURES *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HSHADER`



`D3D10DDI_HRTSHADER`



`*`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver can pass E_OUTOFMEMORY (if the driver runs out of memory) or D3DDDIERR_DEVICEREMOVED (if the device is removed) in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function. The Direct3D runtime determines that any other errors are critical. If the driver passes any errors, which includes D3DDDIERR_DEVICEREMOVED, the Direct3D runtime determines that the handle is invalid; therefore, the runtime does not call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroyshader.md">DestroyShader</a> function to destroy the handle that the <i>hShader</i> parameter specifies.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CreateGeometryShaderWithStreamOutput(D3D11) is supported beginning with the Windows 7 operating system. CreateGeometryShaderWithStreamOutput(D3D11) is supported beginning with the Windows 7 operating system. |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_stage_io_signatures.md">D3D10DDIARG_STAGE_IO_SIGNATURES</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroyshader.md">DestroyShader</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_creategeometryshaderwithstreamoutput.md">D3D11DDIARG_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_calcprivategeometryshaderwithstreamoutput.md">CalcPrivateGeometryShaderWithStreamOutput(D3D11)</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>