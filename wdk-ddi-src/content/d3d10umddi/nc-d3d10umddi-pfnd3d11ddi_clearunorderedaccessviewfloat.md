---
UID: NC:d3d10umddi.PFND3D11DDI_CLEARUNORDEREDACCESSVIEWFLOAT
title: PFND3D11DDI_CLEARUNORDEREDACCESSVIEWFLOAT
author: windows-driver-content
description: The ClearUnorderedAccessViewFLOAT function clears the specified unordered-access view by setting it to a constant value.
old-location: display\clearunorderedaccessviewfloat.htm
old-project: display
ms.assetid: 31734efd-0c17-4476-918d-942c015072bd
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: ClearUnorderedAccessViewFLOAT, ClearUnorderedAccessViewFLOAT callback function [Display Devices], PFND3D11DDI_CLEARUNORDEREDACCESSVIEWFLOAT, UserModeDisplayDriverDx11_Functions_002fe9ed-bdd4-46c4-b7fe-6b783ab47060.xml, d3d10umddi/ClearUnorderedAccessViewFLOAT, display.clearunorderedaccessviewfloat
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: ClearUnorderedAccessViewFLOAT is supported beginning with the Windows 7 operating system.
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
-	ClearUnorderedAccessViewFLOAT
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_CLEARUNORDEREDACCESSVIEWFLOAT callback function
The <b>ClearUnorderedAccessViewFLOAT</b> function clears the specified unordered-access view by setting it to a constant value.

## Syntax

```
PFND3D11DDI_CLEARUNORDEREDACCESSVIEWFLOAT Pfnd3d11ddiClearunorderedaccessviewfloat;

void Pfnd3d11ddiClearunorderedaccessviewfloat(
   D3D10DDI_HDEVICE,
   D3D11DDI_HUNORDEREDACCESSVIEW,
  CONST FLOAT[4]
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11DDI_HUNORDEREDACCESSVIEW`



`FLOAT[4]`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the Remarks section.

## Remarks

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, the Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of <b>ClearUnorderedAccessViewFLOAT</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | ClearUnorderedAccessViewFLOAT is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>