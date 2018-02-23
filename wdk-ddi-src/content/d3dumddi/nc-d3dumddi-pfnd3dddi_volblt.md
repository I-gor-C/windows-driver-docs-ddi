---
UID: NC:d3dumddi.PFND3DDDI_VOLBLT
title: PFND3DDDI_VOLBLT
author: windows-driver-content
description: The VolBlt function performs a bit-block transfer (bitblt) operation from a source volume texture to a destination volume texture.
old-location: display\volblt.htm
old-project: display
ms.assetid: 249a55a3-f2cf-4838-8a0f-b7108a17cd78
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: display.volblt, VolBlt callback function [Display Devices], VolBlt, PFND3DDDI_VOLBLT, PFND3DDDI_VOLBLT, d3dumddi/VolBlt, UserModeDisplayDriver_Functions_2e451776-9da9-48d0-b766-979f361b96eb.xml
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
-	VolBlt
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_VOLBLT callback function
The <i>VolBlt</i> function performs a bit-block transfer (bitblt) operation from a source volume texture to a destination volume texture.

## Syntax

```
PFND3DDDI_VOLBLT Pfnd3dddiVolblt;

HRESULT Pfnd3dddiVolblt(
  HANDLE hDevice,
  CONST D3DDDIARG_VOLUMEBLT *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<i>VolBlt</i> returns S_OK or an appropriate error result if the volume bitblt operation is not successfully performed.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_volumeblt.md">D3DDDIARG_VOLUMEBLT</a>



<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_VOLBLT callback function%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>