---
UID: NS:d3dumddi._DXVADDI_DECODEINPUT
title: "_DXVADDI_DECODEINPUT"
author: windows-driver-content
description: The DXVADDI_DECODEINPUT structure describes a render target format that is supported by a Microsoft DirectX Video Acceleration (DirectX VA) decode type.
old-location: display\dxvaddi_decodeinput.htm
old-project: display
ms.assetid: 6f62ce8d-058b-4838-bc7a-fae84c1b5111
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXVA2_Structs_9b88e486-0ea5-4fc3-bac9-1f7fcc2f5492.xml, DXVADDI_DECODEINPUT, DXVADDI_DECODEINPUT structure [Display Devices], _DXVADDI_DECODEINPUT, d3dumddi/DXVADDI_DECODEINPUT, display.dxvaddi_decodeinput
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
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
-	HeaderDef
api_location:
-	d3dumddi.h
api_name:
-	DXVADDI_DECODEINPUT
product: Windows
targetos: Windows
req.typenames: DXVADDI_DECODEINPUT
---

# _DXVADDI_DECODEINPUT structure
The DXVADDI_DECODEINPUT structure describes a render target format that is supported by a Microsoft DirectX Video Acceleration (DirectX VA) decode type.

## Syntax
```
typedef struct _DXVADDI_DECODEINPUT {
  CONST GUID        *pGuid;
  DXVADDI_VIDEODESC VideoDesc;
} DXVADDI_DECODEINPUT;
```

## Members


`pGuid`

[in] A pointer to the GUID that represents the DirectX VA decode type.

`VideoDesc`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562944">DXVADDI_VIDEODESC</a> structure for the render target that is supported by the decode type that <b>pGuid</b> points to.

## Remarks
A pointer to the DXVADDI_DECODEINPUT structure is specified in the <b>pInfo</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543148">D3DDDIARG_GETCAPS</a> structure--along with a D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFO value in the <b>Type</b> member of D3DDDIARG_GETCAPS--in a call to the user-mode display driver's <a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a> function to retrieve information about the types of compressed buffers that are required to decode video. The compressed buffer information is returned in a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562900">DXVADDI_DECODEBUFFERINFO</a> structure through the <b>pData</b> member of D3DDDIARG_GETCAPS.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543148">D3DDDIARG_GETCAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544132">D3DDDICAPS_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562900">DXVADDI_DECODEBUFFERINFO</a>



<a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a>