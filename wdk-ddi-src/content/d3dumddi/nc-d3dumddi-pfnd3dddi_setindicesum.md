---
UID: NC:d3dumddi.PFND3DDDI_SETINDICESUM
title: PFND3DDDI_SETINDICESUM
author: windows-driver-content
description: The SetIndicesUM function sets the current index buffer to the given user memory buffer.
old-location: display\setindicesum.htm
old-project: display
ms.assetid: 9ca38004-8953-4416-8552-c76813192561
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.setindicesum, SetIndicesUM callback function [Display Devices], SetIndicesUM, PFND3DDDI_SETINDICESUM, PFND3DDDI_SETINDICESUM, d3dumddi/SetIndicesUM, UserModeDisplayDriver_Functions_f692c944-6130-46e3-8e63-f3dbeb051782.xml
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
-	SetIndicesUM
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_SETINDICESUM callback function
The <i>SetIndicesUM</i> function sets the current index buffer to the given user memory buffer.

## Syntax

```
PFND3DDDI_SETINDICESUM Pfnd3dddiSetindicesum;

HRESULT Pfnd3dddiSetindicesum(
  HANDLE hDevice,
   UINT,
  CONST VOID *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`UINT`



`*`




## Return Value

<i>SetIndicesUM</i> returns S_OK or an appropriate error result if the index buffer is not successfully set to the given user memory buffer.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETINDICESUM callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>