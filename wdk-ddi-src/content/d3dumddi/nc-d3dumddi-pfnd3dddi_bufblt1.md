---
UID: NC:d3dumddi.PFND3DDDI_BUFBLT1
title: PFND3DDDI_BUFBLT1
author: windows-driver-content
description: Performs a bit-block transfer (bitblt) operation from a source vertex or index buffer to a destination vertex or index buffer. Implemented by Windows Display Driver Model (WDDM) 1.2 or later user-mode display drivers.
old-location: display\bufblt1.htm
old-project: display
ms.assetid: 92F2AED7-935F-4E3E-934F-D6DF9AA87495
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.bufblt1, BufBlt1 callback function [Display Devices], BufBlt1, PFND3DDDI_BUFBLT1, PFND3DDDI_BUFBLT1, d3dumddi/BufBlt1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	d3dumddi.h
apiname:
-	BufBlt1
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_BUFBLT1 callback function
Performs a bit-block transfer (bitblt) operation from a source vertex or index buffer to a destination vertex or index buffer. Implemented by Windows Display Driver Model (WDDM) 1.2 or later user-mode display drivers.

## Syntax

```
PFND3DDDI_BUFBLT1 Pfnd3dddiBufblt1;

HRESULT Pfnd3dddiBufblt1(
  HANDLE hDevice,
  CONST D3DDDIARG_BUFFERBLT1 *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

Returns S_OK or an appropriate error result if the buffer bitblt operation is not successfully performed.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>



<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_bufferblt1.md">D3DDDIARG_BUFFERBLT1</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_BUFBLT1 callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>