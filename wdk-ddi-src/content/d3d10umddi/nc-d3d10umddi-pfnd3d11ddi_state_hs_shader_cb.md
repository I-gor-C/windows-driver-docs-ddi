---
UID : NC:d3d10umddi.PFND3D11DDI_STATE_HS_SHADER_CB
title : PFND3D11DDI_STATE_HS_SHADER_CB
author : windows-driver-content
description : The pfnStateHsShaderCb function causes the Microsoft Direct3D 11 runtime to refresh the hull shader.
old-location : display\pfnstatehsshadercb.htm
old-project : display
ms.assetid : 74b243a2-722b-4eec-b382-936a6f2f990e
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.pfnstatehsshadercb, pfnStateHsShaderCb callback function [Display Devices], pfnStateHsShaderCb, PFND3D11DDI_STATE_HS_SHADER_CB, PFND3D11DDI_STATE_HS_SHADER_CB, d3d10umddi/pfnStateHsShaderCb, d3d11state_functions_b16162bf-d379-49de-bc4a-85d7df7e95bf.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : pfnStateHsShaderCb is supported beginning with the Windows 7 operating system.
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
req.typenames : "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11DDI_STATE_HS_SHADER_CB callback function
The <b>pfnStateHsShaderCb</b> function causes the Microsoft Direct3D 11 runtime to refresh the hull shader.

## Syntax

```
PFND3D11DDI_STATE_HS_SHADER_CB Pfnd3d11ddiStateHsShaderCb;

void Pfnd3d11ddiStateHsShaderCb(
   D3D10DDI_HRTCORELAYER
)
{...}
```

## Parameters

`D3D10DDI_HRTCORELAYER`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | pfnStateHsShaderCb is supported beginning with the Windows 7 operating system. pfnStateHsShaderCb is supported beginning with the Windows 7 operating system. |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_corelayer_devicecallbacks.md">D3D11DDI_CORELAYER_DEVICECALLBACKS</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_createdevice.md">CreateDevice(D3D10)</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_STATE_HS_SHADER_CB callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>