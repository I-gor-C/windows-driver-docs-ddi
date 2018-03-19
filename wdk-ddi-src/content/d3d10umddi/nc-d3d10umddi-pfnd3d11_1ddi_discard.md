---
UID: NC:d3d10umddi.PFND3D11_1DDI_DISCARD
title: PFND3D11_1DDI_DISCARD
author: windows-driver-content
description: Discards (evicts) an allocation from video display memory. Implemented by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers.
old-location: display\discard_d3d11_1_.htm
old-project: display
ms.assetid: d94234ab-712b-4449-96de-16b9e310d250
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: Discard(D3D11_1), Discard(D3D11_1) callback function [Display Devices], PFND3D11_1DDI_DISCARD, d3d10umddi/Discard(D3D11_1), display.discard_d3d11_1_, display.pfndiscard
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	D3d10umddi.h
api_name:
-	Discard(D3D11_1)
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_DISCARD callback function
Discards (evicts) an allocation from video display memory. Implemented by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers.

## Syntax

```
PFND3D11_1DDI_DISCARD Pfnd3d111DdiDiscard;

void Pfnd3d111DdiDiscard(
   D3D10DDI_HDEVICE,
  D3D11DDI_HANDLETYPE HandleType,
  VOID *hResourceOrView,
  CONST D3D10_DDI_RECT *,
  UINT NumRects
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`HandleType`

A value, of type <a href="..\d3d10umddi\ne-d3d10umddi-d3d11ddi_handletype.md">D3D11DDI_HANDLETYPE</a>, that identifies the context handle type.

`*hResourceOrView`

A pointer to a handle to the resource or to the view that is to be discarded.

`*`



`NumRects`

The number of rectangles in the array that the  <i>pRects</i> parameter specifies.


## Return Value

This callback function does not return a value.

## Remarks

The D3D10_DDI_RECT structure is defined as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure.

<div class="code"><span codelanguage="ManagedCPlusPlus"><table>
<tr>
<th>C++</th>
</tr>
<tr>
<td>
<pre>typedef RECT D3D10_DDI_RECT;</pre>
</td>
</tr>
</table></span></div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_devicefuncs.md">D3D11_1DDI_DEVICEFUNCS</a>



<a href="..\d3d10umddi\ne-d3d10umddi-d3d11ddi_handletype.md">D3D11DDI_HANDLETYPE</a>