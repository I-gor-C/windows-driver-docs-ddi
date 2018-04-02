---
UID: NC:d3d10umddi.PFND3D11DDI_CREATEUNORDEREDACCESSVIEW
title: PFND3D11DDI_CREATEUNORDEREDACCESSVIEW
author: windows-driver-content
description: The CreateUnorderedAccessView function creates an unordered access view.
old-location: display\createunorderedaccessview.htm
old-project: display
ms.assetid: c5a258e7-6645-46bb-ab2c-a1c8f5e593b7
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateUnorderedAccessView, CreateUnorderedAccessView callback function [Display Devices], PFND3D11DDI_CREATEUNORDEREDACCESSVIEW, UserModeDisplayDriverDx11_Functions_4b9c2d38-c780-47be-a5fa-dec2c860732b.xml, d3d10umddi/CreateUnorderedAccessView, display.createunorderedaccessview
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	d3d10umddi.h
api_name:
-	CreateUnorderedAccessView
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
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

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver might run out of memory. Therefore, the driver can pass E_OUTOFMEMORY or D3DDDIERR_DEVICEREMOVED in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function. The Direct3D runtime determines that any other errors are critical. If the driver passes any errors, which includes D3DDDIERR_DEVICEREMOVED, the Direct3D runtime determines that the handle is invalid; therefore, the runtime does not call the <a href="https://msdn.microsoft.com/1bce3519-f333-4b47-b29b-bde1b5c3005c">DestroyUnorderedAccessView</a> function to destroy the handle that the <i>hUnorderedAccessView</i> parameter specifies.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CreateUnorderedAccessView is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/6aca5d33-c8c6-4c6b-a66a-e28a958cbc2e">CalcPrivateUnorderedAccessViewSize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542086">D3D11DDIARG_CREATEUNORDEREDACCESSVIEW</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/1bce3519-f333-4b47-b29b-bde1b5c3005c">DestroyUnorderedAccessView</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>