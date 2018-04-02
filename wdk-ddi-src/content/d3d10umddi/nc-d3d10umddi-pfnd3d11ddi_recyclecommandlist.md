---
UID: NC:d3d10umddi.PFND3D11DDI_RECYCLECOMMANDLIST
title: PFND3D11DDI_RECYCLECOMMANDLIST
author: windows-driver-content
description: The RecycleCommandList function recycles a command list.
old-location: display\recyclecommandlist.htm
old-project: display
ms.assetid: 4cff7f3d-ba13-4389-bafc-edffc0697ce9
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11DDI_RECYCLECOMMANDLIST, RecycleCommandList, RecycleCommandList callback function [Display Devices], UserModeDisplayDriverDx11_Functions_a917a4c2-4226-46e8-a696-8c51b2960bda.xml, d3d10umddi/RecycleCommandList, display.recyclecommandlist
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: RecycleCommandList is supported beginning with the Windows 7 operating system.
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
-	RecycleCommandList
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_RECYCLECOMMANDLIST callback function
The <i>RecycleCommandList</i> function recycles a command list.

## Syntax

```
PFND3D11DDI_RECYCLECOMMANDLIST Pfnd3d11ddiRecyclecommandlist;

void Pfnd3d11ddiRecyclecommandlist(
   D3D10DDI_HDEVICE,
   D3D11DDI_HCOMMANDLIST
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11DDI_HCOMMANDLIST`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver is only required to implement <i>RecycleCommandList</i> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 threading-capability bit. The driver can return D3D11DDICAPS_COMMANDLISTS_BUILD_2 in the <b>Caps</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a> structure from a call to the driver's <a href="https://msdn.microsoft.com/83cd5f34-5f12-4ead-ad33-366fc3c6e804">GetCaps(D3D10_2)</a> function.

For more information about <i>RecycleCommandList</i>, see <a href="https://msdn.microsoft.com/7bede247-680d-4fd3-a10b-6ef63f0a88ec">Optimization for Small Command Lists</a>.

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, the Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED. However, if device removal interferes with the operation of <i>RecycleCommandList</i> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | RecycleCommandList is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a>



<a href="https://msdn.microsoft.com/83cd5f34-5f12-4ead-ad33-366fc3c6e804">GetCaps(D3D10_2)</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>