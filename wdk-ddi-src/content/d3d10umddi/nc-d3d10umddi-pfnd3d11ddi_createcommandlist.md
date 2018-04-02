---
UID: NC:d3d10umddi.PFND3D11DDI_CREATECOMMANDLIST
title: PFND3D11DDI_CREATECOMMANDLIST
author: windows-driver-content
description: The CreateCommandList function creates a command list.
old-location: display\createcommandlist.htm
old-project: display
ms.assetid: 583bde52-ba21-44ce-9f48-8ace6f7a70cc
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateCommandList, CreateCommandList callback function [Display Devices], PFND3D11DDI_CREATECOMMANDLIST, UserModeDisplayDriverDx11_Functions_4383a01d-9aee-4c8e-8a54-f7463e8995d9.xml, d3d10umddi/CreateCommandList, display.createcommandlist
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CreateCommandList is supported beginning with the Windows 7 operating system.
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
-	CreateCommandList
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_CREATECOMMANDLIST callback function
The <b>CreateCommandList</b> function creates a command list.

## Syntax

```
PFND3D11DDI_CREATECOMMANDLIST Pfnd3d11ddiCreatecommandlist;

void Pfnd3d11ddiCreatecommandlist(
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

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver is only required to implement <b>CreateCommandList</b> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability that can be returned in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a> structure from a call to the <a href="https://msdn.microsoft.com/83cd5f34-5f12-4ead-ad33-366fc3c6e804">GetCaps(D3D10_2)</a> function.

The driver can pass E_OUTOFMEMORY (if the driver runs out of memory) or D3DDDIERR_DEVICEREMOVED (if the device is removed) in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function. The Direct3D runtime determines that any other errors are critical. If the driver passes any errors, which includes D3DDDIERR_DEVICEREMOVED, the Direct3D runtime determines that the handle is invalid; therefore, the runtime does not call the <a href="https://msdn.microsoft.com/9f03c193-f017-4189-a082-908e28a2e9f7">DestroyCommandList</a> function to destroy the handle that the <i>hCommandList</i> parameter specifies.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CreateCommandList is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/04725df2-6373-4e04-862e-d533363af00b">CalcPrivateCommandListSize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542040">D3D11DDIARG_CREATECOMMANDLIST</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a>



<a href="https://msdn.microsoft.com/9f03c193-f017-4189-a082-908e28a2e9f7">DestroyCommandList</a>



<a href="https://msdn.microsoft.com/83cd5f34-5f12-4ead-ad33-366fc3c6e804">GetCaps(D3D10_2)</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>