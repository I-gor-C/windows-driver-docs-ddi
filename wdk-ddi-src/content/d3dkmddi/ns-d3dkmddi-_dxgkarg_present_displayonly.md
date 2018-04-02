---
UID: NS:d3dkmddi._DXGKARG_PRESENT_DISPLAYONLY
title: "_DXGKARG_PRESENT_DISPLAYONLY"
author: windows-driver-content
description: Indicates how a kernel mode display-only driver (KMDOD) is to perform a present operation.
old-location: display\dxgkarg_present_displayonly.htm
old-project: display
ms.assetid: 7679d4f2-55c6-458c-afd3-020c3b7fd7e2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGKARG_PRESENT_DISPLAYONLY, DXGKARG_PRESENT_DISPLAYONLY structure [Display Devices], _DXGKARG_PRESENT_DISPLAYONLY, d3dkmddi/DXGKARG_PRESENT_DISPLAYONLY, display.dxgkarg_present_displayonly
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3dkmddi.h
api_name:
-	DXGKARG_PRESENT_DISPLAYONLY
product:
- Windows
targetos: Windows
req.typenames: DXGKARG_PRESENT_DISPLAYONLY
---

# _DXGKARG_PRESENT_DISPLAYONLY structure
Indicates how a kernel mode display-only driver (KMDOD) is to perform a present operation.

## Syntax
```
typedef struct _DXGKARG_PRESENT_DISPLAYONLY {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID      VidPnSourceId;
  VOID                                *pSource;
  ULONG                               BytesPerPixel;
  LONG                                Pitch;
  D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS   Flags;
  ULONG                               NumMoves;
  D3DKMT_MOVE_RECT                    *pMoves;
  ULONG                               NumDirtyRects;
  RECT                                *pDirtyRect;
  DXGKCB_PRESENT_DISPLAYONLY_PROGRESS pfnPresentDisplayOnlyProgress;
} DXGKARG_PRESENT_DISPLAYONLY;
```

## Members


`VidPnSourceId`

The zero-based identification number of the video present source in a path of a video present network (VidPN) topology on which to restrict displaying.

`pSource`

The virtual start address of the source image.

`BytesPerPixel`

The number of bytes per pixel in the source image.

`Pitch`

The pitch, in bytes, of each line in the source image—that is, the distance, in bytes, to the start of the next line.

`Flags`

A <a href="https://msdn.microsoft.com/library/windows/hardware/hh406547">D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS</a> structure that identifies how to display the source image in the present operation.

`NumMoves`

The number of screen-to-screen moves that are pointed to by the <b>pMoves</b> member.

`pMoves`

A pointer to a list of <a href="https://msdn.microsoft.com/library/windows/hardware/hh406478">D3DKMT_MOVE_RECT</a> screen-to-screen moves.

`NumDirtyRects`

The number of dirty rectangles that are pointed to by the <b>pDirtyRect</b> member.

`pDirtyRect`

A pointer to a list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> dirty rectangles.

`pfnPresentDisplayOnlyProgress`

Reserved for system use. The operating system sets this member to <b>NULL</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406478">D3DKMT_MOVE_RECT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh406547">D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS</a>



<a href="https://msdn.microsoft.com/8970246b-b46f-464f-93b2-973cc351ed07">DxgkCbPresentDisplayOnlyProgress</a>



<a href="https://msdn.microsoft.com/b68839e3-ad82-4fcc-8e5a-02dea5db08d9">DxgkDdiPresentDisplayOnly</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>