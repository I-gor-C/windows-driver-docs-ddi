---
UID: NC:d3d10umddi.PFND3D11DDI_RECYCLECREATECOMMANDLIST
title: PFND3D11DDI_RECYCLECREATECOMMANDLIST
author: windows-driver-content
description: The RecycleCreateCommandList function creates a command list and makes a previously unused DDI handle completely valid again.
old-location: display\recyclecreatecommandlist.htm
old-project: display
ms.assetid: c387545e-2891-401d-b7ca-ee7549a52603
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D11DDI_RECYCLECREATECOMMANDLIST, RecycleCreateCommandList, RecycleCreateCommandList callback function [Display Devices], UserModeDisplayDriverDx11_Functions_ae724488-211a-4590-abcc-f2c8f954531e.xml, d3d10umddi/RecycleCreateCommandList, display.recyclecreatecommandlist
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: RecycleCreateCommandList is supported beginning with the Windows 7 operating system.
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
-	RecycleCreateCommandList
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_RECYCLECREATECOMMANDLIST callback function
The <i>RecycleCreateCommandList</i> function creates a command list and makes a previously unused DDI handle completely valid again.

## Syntax

```
PFND3D11DDI_RECYCLECREATECOMMANDLIST Pfnd3d11ddiRecyclecreatecommandlist;

HRESULT Pfnd3d11ddiRecyclecreatecommandlist(
   D3D10DDI_HDEVICE,
  CONST D3D11DDIARG_CREATECOMMANDLIST *,
   D3D11DDI_HCOMMANDLIST,
   D3D11DDI_HRTCOMMANDLIST
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D11DDI_HCOMMANDLIST`



`D3D11DDI_HRTCOMMANDLIST`




## Return Value

<i>RecycleCreateCommandList</i> returns one of the following values:

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>S_OK</b></dt>
</dl>
</td>
<td width="60%">
The command list is successfully created.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
</td>
<td width="60%">
<i>RecycleCreateCommandList</i> could not allocate memory that is required for it to complete.

</td>
</tr>
</table>

## Remarks

The driver is only required to implement <i>RecycleCreateCommandList</i> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability, which can be returned in the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_threading_caps.md">D3D11DDI_THREADING_CAPS</a> structure from a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10_2ddi_getcaps.md">GetCaps(D3D10_2)</a> function.

For more information about <i>RecycleCreateCommandList</i>, see <a href="https://msdn.microsoft.com/7bede247-680d-4fd3-a10b-6ef63f0a88ec">Optimization for Small Command Lists</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | RecycleCreateCommandList is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_createcommandlist.md">D3D11DDIARG_CREATECOMMANDLIST</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10_2ddi_getcaps.md">GetCaps(D3D10_2)</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_threading_caps.md">D3D11DDI_THREADING_CAPS</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_calcprivatecommandlistsize.md">CalcPrivateCommandListSize</a>