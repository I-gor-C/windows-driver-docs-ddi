---
UID: NS.d3dkmddi._DXGKARG_SETPOINTERPOSITION
title: DXGKARG_SETPOINTERPOSITION
author: windows-driver-content
description: The DXGKARG_SETPOINTERPOSITION structure describes where and how to display the mouse pointer.
old-location: display\dxgkarg_setpointerposition.htm
ms.assetid: a5670b3e-a96b-439c-ac1a-644611110700
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_SETPOINTERPOSITION
req.alt-loc: d3dkmddi.h
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
ms.keywords: DXGKARG_SETPOINTERPOSITION, DXGKARG_SETPOINTERPOSITION
req.iface: 
---

# DXGKARG_SETPOINTERPOSITION structure



## -description
<p>The DXGKARG_SETPOINTERPOSITION structure describes where and how to display the mouse pointer. </p>


## -syntax

````
typedef struct _DXGKARG_SETPOINTERPOSITION {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  INT                            X;
  INT                            Y;
  DXGK_SETPOINTERPOSITIONFLAGS   Flags;
} DXGKARG_SETPOINTERPOSITION;
````


## -struct-fields
<dl>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology that the mouse pointer is located on. </p>
</dd>

### -field <b>X</b>

<dd>
<p>[in] The column, in pixels, that the mouse pointer is located on from the top left.</p>
</dd>

### -field <b>Y</b>

<dd>
<p>[in] The row, in pixels, that the mouse pointer is located on from the top left.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562051">DXGK_SETPOINTERPOSITIONFLAGS</a> structure that identifies, in bit-field flags, information about the mouse pointer.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562051">DXGK_SETPOINTERPOSITIONFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b30e4f19-068c-4ab0-a2e9-b1f57592be1c">DxgkDdiSetPointerPosition</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_SETPOINTERPOSITION structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
