---
UID: NS.d3dkmddi._DXGKARG_PRESENT_DISPLAYONLY
title: DXGKARG_PRESENT_DISPLAYONLY
author: windows-driver-content
description: Indicates how a kernel mode display-only driver (KMDOD) is to perform a present operation.
old-location: display\dxgkarg_present_displayonly.htm
ms.assetid: 7679d4f2-55c6-458c-afd3-020c3b7fd7e2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_PRESENT_DISPLAYONLY
req.alt-loc: D3dkmddi.h
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
ms.keywords: DXGKARG_PRESENT_DISPLAYONLY, DXGKARG_PRESENT_DISPLAYONLY
req.iface: 
---

# DXGKARG_PRESENT_DISPLAYONLY structure



## -description
<p>Indicates how a kernel mode display-only driver (KMDOD) is to perform a present operation.</p>


## -syntax

````
typedef struct _DXGKARG_PRESENT_DISPLAYONLY {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID      VidPnSourceId;
  VOID                                *pSource;
  ULONG                               BytesPerPixel;
  LONG                                Pitch;
  D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS   Flags;
  ULONG                               NumMoves;
  D3DKMT_MOVE_RECT                    *pMoves;
  ULONG                               NumDirtyRects;
  RECT                                *pDirtyRect;
  DXGKCB_PRESENT_DISPLAYONLY_PROGRESS pfnPresentDisplayOnlyProgress;
} DXGKARG_PRESENT_DISPLAYONLY;
````


## -struct-fields
<dl>

### -field <b>VidPnSourceId</b>

<dd>
<p>The zero-based identification number of the video present source in a path of a video present network (VidPN) topology on which to restrict displaying.</p>
</dd>

### -field <b>pSource</b>

<dd>
<p>The virtual start address of the source image.</p>
</dd>

### -field <b>BytesPerPixel</b>

<dd>
<p>The number of bytes per pixel in the source image.</p>
</dd>

### -field <b>Pitch</b>

<dd>
<p>The pitch, in bytes, of each line in the source image—that is, the distance, in bytes, to the start of the next line.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh406547">D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS</a> structure that identifies how to display the source image in the present operation.</p>
</dd>

### -field <b>NumMoves</b>

<dd>
<p>The number of screen-to-screen moves that are pointed to by the <b>pMoves</b> member.</p>
</dd>

### -field <b>pMoves</b>

<dd>
<p>A pointer to a list of <a href="https://msdn.microsoft.com/library/windows/hardware/hh406478">D3DKMT_MOVE_RECT</a> screen-to-screen moves.</p>
</dd>

### -field <b>NumDirtyRects</b>

<dd>
<p>The number of dirty rectangles that are pointed to by the <b>pDirtyRect</b> member.</p>
</dd>

### -field <b>pDirtyRect</b>

<dd>
<p>A pointer to a list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> dirty rectangles.</p>
</dd>

### -field <b>pfnPresentDisplayOnlyProgress</b>

<dd>
<p>Reserved for system use. The operating system sets this member to <b>NULL</b>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406478">D3DKMT_MOVE_RECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406547">D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8970246b-b46f-464f-93b2-973cc351ed07">DxgkCbPresentDisplayOnlyProgress</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b68839e3-ad82-4fcc-8e5a-02dea5db08d9">DxgkDdiPresentDisplayOnly</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_PRESENT_DISPLAYONLY structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
