---
UID: NC:d3d10umddi.PFND3D10DDI_DRAWINSTANCED
title: PFND3D10DDI_DRAWINSTANCED
author: windows-driver-content
description: The DrawInstanced function draws particular instances of nonindexed primitives.
old-location: display\drawinstanced.htm
old-project: display
ms.assetid: c539cf8b-e056-476a-9b23-7e360917a7d9
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DrawInstanced, DrawInstanced callback function [Display Devices], PFND3D10DDI_DRAWINSTANCED, UserModeDisplayDriverDx10_Functions_15fe8a07-36ca-4ab1-8570-01250eed4866.xml, d3d10umddi/DrawInstanced, display.drawinstanced
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
-	DrawInstanced
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_DRAWINSTANCED callback function
The <b>DrawInstanced</b> function draws particular instances of nonindexed primitives.

## Syntax

```
PFND3D10DDI_DRAWINSTANCED Pfnd3d10ddiDrawinstanced;

void Pfnd3d10ddiDrawinstanced(
   D3D10DDI_HDEVICE,
   UINT,
   UINT,
   UINT,
   UINT
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`UINT`



`UINT`



`UINT`



`UINT`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, the Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interfered with the operation of <b>DrawInstanced</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>