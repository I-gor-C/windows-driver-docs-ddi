---
UID: NC:d3d10umddi.PFND3D10DDI_DESTROYDEVICE
title: PFND3D10DDI_DESTROYDEVICE
author: windows-driver-content
description: The DestroyDevice(D3D10) function destroys the specified device object.
old-location: display\destroydevice_d3d10_.htm
old-project: display
ms.assetid: 90ada8c8-8ad8-4992-aac1-6eb7fdf3f249
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DestroyDevice, DestroyDevice callback function [Display Devices], PFND3D10DDI_DESTROYDEVICE, UserModeDisplayDriverDx10_Functions_4f2918da-90e0-4e85-b019-f9481555e524.xml, d3d10umddi/DestroyDevice, display.destroydevice_d3d10_
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
-	D3d10umddi.h
api_name:
-	DestroyDevice
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_DESTROYDEVICE callback function
The <b>DestroyDevice(D3D10)</b> function destroys the specified device object.

## Syntax

```
PFND3D10DDI_DESTROYDEVICE Pfnd3d10ddiDestroydevice;

void Pfnd3d10ddiDestroydevice(
   D3D10DDI_HDEVICE
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the Remarks section.

## Remarks

Before the Direct3D runtime calls <b>DestroyDevice(D3D10)</b>, it destroys all of the display device's child objects (blend state, resources, and so on).

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, the Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interfered with the operation of <b>DestroyDevice(D3D10)</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>