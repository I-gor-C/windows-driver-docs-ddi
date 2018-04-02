---
UID: NS:d3dkmthk._D3DKMT_CLOSEADAPTER
title: "_D3DKMT_CLOSEADAPTER"
author: windows-driver-content
description: The D3DKMT_CLOSEADAPTER structure specifies the graphics adapter to close.
old-location: display\d3dkmt_closeadapter.htm
old-project: display
ms.assetid: ef85d18a-c4cd-4999-8782-19e4114a0594
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_CLOSEADAPTER, D3DKMT_CLOSEADAPTER structure [Display Devices], OpenGL_Structs_578046d6-1625-4485-b43c-16ce2b7e812c.xml, _D3DKMT_CLOSEADAPTER, d3dkmthk/D3DKMT_CLOSEADAPTER, display.d3dkmt_closeadapter
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
-	D3DKMT_CLOSEADAPTER
product:
- Windows
targetos: Windows
req.typenames: D3DKMT_CLOSEADAPTER
---

# _D3DKMT_CLOSEADAPTER structure
The D3DKMT_CLOSEADAPTER structure specifies the graphics adapter to close.

## Syntax
```
typedef struct _D3DKMT_CLOSEADAPTER {
  D3DKMT_HANDLE hAdapter;
} D3DKMT_CLOSEADAPTER;
```

## Members


`hAdapter`

[in] A handle to the graphics adapter to close.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546787">D3DKMTCloseAdapter</a>