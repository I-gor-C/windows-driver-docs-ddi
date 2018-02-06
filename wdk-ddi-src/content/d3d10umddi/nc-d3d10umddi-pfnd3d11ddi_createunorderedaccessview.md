---
UID: NC:d3d10umddi.PFND3D11DDI_CREATEUNORDEREDACCESSVIEW
title: PFND3D11DDI_CREATEUNORDEREDACCESSVIEW
author: windows-driver-content
description: The CreateUnorderedAccessView function creates an unordered access view.
old-location: display\createunorderedaccessview.htm
old-project: display
ms.assetid: c5a258e7-6645-46bb-ab2c-a1c8f5e593b7
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.createunorderedaccessview, CreateUnorderedAccessView callback function [Display Devices], CreateUnorderedAccessView, PFND3D11DDI_CREATEUNORDEREDACCESSVIEW, PFND3D11DDI_CREATEUNORDEREDACCESSVIEW, d3d10umddi/CreateUnorderedAccessView, UserModeDisplayDriverDx11_Functions_4b9c2d38-c780-47be-a5fa-dec2c860732b.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CreateUnorderedAccessView is supported beginning with the Windows 7 operating system.
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
-	CreateUnorderedAccessView
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11DDI_CREATEUNORDEREDACCESSVIEW callback function
The <b>CreateUnorderedAccessView</b> function creates an unordered access view.

## Syntax

```
PFND3D11DDI_CREATEUNORDEREDACCESSVIEW Pfnd3d11ddiCreateunorderedaccessview;

void Pfnd3d11ddiCreateunorderedaccessview(
   D3D10DDI_HDEVICE,
  CONST D3D11DDIARG_CREATEUNORDEREDACCESSVIEW *,
   D3D11DDI_HUNORDEREDACCESSVIEW,
   D3D11DDI_HRTUNORDEREDACCESSVIEW
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D11DDI_HUNORDEREDACCESSVIEW`



`D3D11DDI_HRTUNORDEREDACCESSVIEW`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver might run out of memory. Therefore, the driver can pass E_OUTOFMEMORY or D3DDDIERR_DEVICEREMOVED in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function. The Direct3D runtime determines that any other errors are critical. If the driver passes any errors, which includes D3DDDIERR_DEVICEREMOVED, the Direct3D runtime determines that the handle is invalid; therefore, the runtime does not call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_destroyunorderedaccessview.md">DestroyUnorderedAccessView</a> function to destroy the handle that the <i>hUnorderedAccessView</i> parameter specifies.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CreateUnorderedAccessView is supported beginning with the Windows 7 operating system. CreateUnorderedAccessView is supported beginning with the Windows 7 operating system. |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_destroyunorderedaccessview.md">DestroyUnorderedAccessView</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_createunorderedaccessview.md">D3D11DDIARG_CREATEUNORDEREDACCESSVIEW</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_calcprivateunorderedaccessviewsize.md">CalcPrivateUnorderedAccessViewSize</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_CREATEUNORDEREDACCESSVIEW callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>