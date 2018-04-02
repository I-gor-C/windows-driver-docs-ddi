---
UID: NS:d3dkmthk._D3DKMT_INVALIDATEACTIVEVIDPN
title: "_D3DKMT_INVALIDATEACTIVEVIDPN"
author: windows-driver-content
description: The D3DKMT_INVALIDATEACTIVEVIDPN structure describes parameters that invalidate the active video present network (VidPN) currently in use.
old-location: display\d3dkmt_invalidateactivevidpn.htm
old-project: display
ms.assetid: 51fb1993-b9f3-436a-9a6d-7d4f9bf26083
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_INVALIDATEACTIVEVIDPN, D3DKMT_INVALIDATEACTIVEVIDPN structure [Display Devices], OpenGL_Structs_6610529b-39db-4fc4-981a-96a6b3bf7543.xml, _D3DKMT_INVALIDATEACTIVEVIDPN, d3dkmthk/D3DKMT_INVALIDATEACTIVEVIDPN, display.d3dkmt_invalidateactivevidpn
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
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
-	d3dkmthk.h
api_name:
-	D3DKMT_INVALIDATEACTIVEVIDPN
product: Windows
targetos: Windows
req.typenames: D3DKMT_INVALIDATEACTIVEVIDPN
---

# _D3DKMT_INVALIDATEACTIVEVIDPN structure
The D3DKMT_INVALIDATEACTIVEVIDPN structure describes parameters that invalidate the active video present network (VidPN) currently in use.

## Syntax
```
typedef struct _D3DKMT_INVALIDATEACTIVEVIDPN {
  D3DKMT_HANDLE hAdapter;
  VOID          *pPrivateDriverData;
  UINT          PrivateDriverDataSize;
} D3DKMT_INVALIDATEACTIVEVIDPN;
```

## Members


`hAdapter`

[in] A handle to the graphics adapter that the VidPN exists on.

`pPrivateDriverData`

[in] A pointer to a buffer that contains the display mode (for example, clone-view mode) that the OpenGL installable client driver (ICD) requests for the new VidPN.

`PrivateDriverDataSize`

[in] The size, in bytes, of the buffer that <b>pPrivateDriverData</b> points to.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff547023">D3DKMTInvalidateActiveVidPn</a>