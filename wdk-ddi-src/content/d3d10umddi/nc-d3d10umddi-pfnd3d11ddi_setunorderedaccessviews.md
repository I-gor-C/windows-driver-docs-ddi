---
UID: NC:d3d10umddi.PFND3D11DDI_SETUNORDEREDACCESSVIEWS
title: PFND3D11DDI_SETUNORDEREDACCESSVIEWS
author: windows-driver-content
description: The CsSetUnorderedAccessViews function sets unordered access view (UAV) objects for a compute shader.
old-location: display\cssetunorderedaccessviews.htm
old-project: display
ms.assetid: ab8c529b-19e2-4a2a-af68-0e3998829788
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: CsSetUnorderedAccessViews, CsSetUnorderedAccessViews callback function [Display Devices], PFND3D11DDI_SETUNORDEREDACCESSVIEWS, UserModeDisplayDriverDx11_Functions_2e3d1f2b-5113-4cbe-afa8-11f4caf88859.xml, d3d10umddi/CsSetUnorderedAccessViews, display.cssetunorderedaccessviews
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CsSetUnorderedAccessViews is supported beginning with the Windows 7 operating system.
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
-	CsSetUnorderedAccessViews
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_SETUNORDEREDACCESSVIEWS callback function
The <i>CsSetUnorderedAccessViews</i> function sets unordered access view (UAV) objects for a compute shader.

## Syntax

```
PFND3D11DDI_SETUNORDEREDACCESSVIEWS Pfnd3d11ddiSetunorderedaccessviews;

void Pfnd3d11ddiSetunorderedaccessviews(
   D3D10DDI_HDEVICE,
  UINT StartSlot,
  UINT NumViews,
  CONST D3D11DDI_HUNORDEREDACCESSVIEW *,
  CONST UINT *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`StartSlot`



`NumViews`

The total number of views to set.

`*`



`*`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function, the Microsoft Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of <i>CsSetUnorderedAccessViews</i> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CsSetUnorderedAccessViews is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_buffer_unorderedaccessview.md">D3D11DDIARG_BUFFER_UNORDEREDACCESSVIEW</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_SETUNORDEREDACCESSVIEWS callback function%20 RELEASE:%20(2/24/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>