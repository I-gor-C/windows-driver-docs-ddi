---
UID: NC:d3d10umddi.PFND3D11DDI_CREATEDEFERREDCONTEXT
title: PFND3D11DDI_CREATEDEFERREDCONTEXT
author: windows-driver-content
description: The CreateDeferredContext function creates a deferred context.
old-location: display\createdeferredcontext.htm
old-project: display
ms.assetid: 464a2291-55c8-4e51-ba08-219ce426d038
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateDeferredContext, CreateDeferredContext callback function [Display Devices], PFND3D11DDI_CREATEDEFERREDCONTEXT, UserModeDisplayDriverDx11_Functions_8de581fa-3b85-4827-bf32-f0b96d011202.xml, d3d10umddi/CreateDeferredContext, display.createdeferredcontext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CreateDeferredContext is supported beginning with the Windows 7 operating system.
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
-	CreateDeferredContext
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_CREATEDEFERREDCONTEXT callback function
The <b>CreateDeferredContext</b> function creates a deferred context.

## Syntax

```
PFND3D11DDI_CREATEDEFERREDCONTEXT Pfnd3d11ddiCreatedeferredcontext;

void Pfnd3d11ddiCreatedeferredcontext(
   D3D10DDI_HDEVICE,
  CONST D3D11DDIARG_CREATEDEFERREDCONTEXT *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver is only required to implement <b>CreateDeferredContext</b> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability that can be returned in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a> structure from a call to the <a href="https://msdn.microsoft.com/83cd5f34-5f12-4ead-ad33-366fc3c6e804">GetCaps(D3D10_2)</a> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CreateDeferredContext is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542044">D3D11DDIARG_CREATEDEFERREDCONTEXT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a>



<a href="https://msdn.microsoft.com/83cd5f34-5f12-4ead-ad33-366fc3c6e804">GetCaps(D3D10_2)</a>