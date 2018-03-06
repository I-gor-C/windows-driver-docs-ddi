---
UID: NC:d3d10umddi.PFND3D10DDI_CREATEELEMENTLAYOUT
title: PFND3D10DDI_CREATEELEMENTLAYOUT
author: windows-driver-content
description: The CreateElementLayout function creates an element layout.
old-location: display\createelementlayout.htm
old-project: display
ms.assetid: 5af2189a-a064-4c62-be09-733c1d632983
ms.author: windowsdriverdev
ms.date: 2/26/2018
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

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver can pass E_OUTOFMEMORY (if the driver runs out of memory) or D3DDDIERR_DEVICEREMOVED (if the device has been removed) in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is invalid; therefore, the runtime will not call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroyelementlayout.md">DestroyElementLayout</a> function to destroy the handle that the <i>hElementLayout</i> parameter specifies.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_calcprivateelementlayoutsize.md">CalcPrivateElementLayoutSize</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_createelementlayout.md">D3D10DDIARG_CREATEELEMENTLAYOUT</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroyelementlayout.md">DestroyElementLayout</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi_devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_CREATEELEMENTLAYOUT callback function%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>