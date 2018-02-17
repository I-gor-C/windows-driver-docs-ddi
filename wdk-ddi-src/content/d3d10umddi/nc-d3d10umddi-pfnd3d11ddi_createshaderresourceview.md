---
UID: NC:d3d10umddi.PFND3D11DDI_CREATESHADERRESOURCEVIEW
title: PFND3D11DDI_CREATESHADERRESOURCEVIEW
author: windows-driver-content
description: The CreateShaderResourceView(D3D11) function creates a shader resource view.
old-location: display\createshaderresourceview_d3d11_.htm
old-project: display
ms.assetid: 7ca462c7-ec43-4af7-92c8-ed69e5d324e2
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.createshaderresourceview_d3d11_, CreateShaderResourceView callback function [Display Devices], CreateShaderResourceView, PFND3D11DDI_CREATESHADERRESOURCEVIEW, PFND3D11DDI_CREATESHADERRESOURCEVIEW, d3d10umddi/CreateShaderResourceView, UserModeDisplayDriverDx11_Functions_abe7b0fb-121d-4486-af02-885ff37a4e81.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CreateShaderResourceView(D3D11) is supported beginning with the Windows 7 operating system.
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
-	CreateShaderResourceView
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11DDI_CREATESHADERRESOURCEVIEW callback function
The <b>CreateShaderResourceView(D3D11)</b> function creates a shader resource view.

## Syntax

```
PFND3D11DDI_CREATESHADERRESOURCEVIEW Pfnd3d11ddiCreateshaderresourceview;

void Pfnd3d11ddiCreateshaderresourceview(
   D3D10DDI_HDEVICE,
  CONST D3D11DDIARG_CREATESHADERRESOURCEVIEW *,
   D3D10DDI_HSHADERRESOURCEVIEW,
   D3D10DDI_HRTSHADERRESOURCEVIEW
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HSHADERRESOURCEVIEW`



`D3D10DDI_HRTSHADERRESOURCEVIEW`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver might run out of memory. Therefore, the driver can pass E_OUTOFMEMORY or D3DDDIERR_DEVICEREMOVED in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function. The Direct3D runtime determines that any other errors are critical. If the driver passes any errors, which includes D3DDDIERR_DEVICEREMOVED, the Direct3D runtime determines that the handle is invalid; therefore, the runtime does not call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroyshaderresourceview.md">DestroyShaderResourceView</a> function to destroy the handle that the <i>hShaderResourceView</i> parameter specifies.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CreateShaderResourceView(D3D11) is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroyshaderresourceview.md">DestroyShaderResourceView</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_calcprivateshaderresourceviewsize.md">CalcPrivateShaderResourceViewSize(D3D11)</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_createshaderresourceview.md">D3D11DDIARG_CREATESHADERRESOURCEVIEW</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_CREATESHADERRESOURCEVIEW callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>