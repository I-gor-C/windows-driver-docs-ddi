---
UID: NC:d3dumddi.PFND3DDDI_SETDEPTHSTENCIL
title: PFND3DDDI_SETDEPTHSTENCIL
author: windows-driver-content
description: The SetDepthStencil function sets the depth buffer in the driver's context.
old-location: display\setdepthstencil.htm
old-project: display
ms.assetid: 7c4b01c8-2376-4956-9b18-649647c19b2b
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.setdepthstencil, SetDepthStencil callback function [Display Devices], SetDepthStencil, PFND3DDDI_SETDEPTHSTENCIL, PFND3DDDI_SETDEPTHSTENCIL, d3dumddi/SetDepthStencil, UserModeDisplayDriver_Functions_0279a98e-e1a5-4e33-8ced-9ac07e5e2921.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	d3dumddi.h
apiname:
-	SetDepthStencil
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_SETDEPTHSTENCIL callback function
The <i>SetDepthStencil</i> function sets the depth buffer in the driver's context.

## Syntax

```
PFND3DDDI_SETDEPTHSTENCIL Pfnd3dddiSetdepthstencil;

HRESULT Pfnd3dddiSetdepthstencil(
  HANDLE hDevice,
  CONST D3DDDIARG_SETDEPTHSTENCIL *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<i>SetDepthStencil</i> returns S_OK or an appropriate error result if the depth buffer is not successfully set.

## Remarks

The user-mode display driver should store the depth buffer in the driver's context when the Microsoft Direct3D runtime calls <i>SetDepthStencil</i>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>



<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_setdepthstencil.md">D3DDDIARG_SETDEPTHSTENCIL</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETDEPTHSTENCIL callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>