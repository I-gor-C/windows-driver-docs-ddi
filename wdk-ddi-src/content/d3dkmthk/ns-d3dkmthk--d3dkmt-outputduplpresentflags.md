---
UID: NS.d3dkmthk._D3DKMT_OUTPUTDUPLPRESENTFLAGS
title: D3DKMT_OUTPUTDUPLPRESENTFLAGS
author: windows-driver-content
description: Describes options for a Desktop Duplication API swapchain present operation.
old-location: display\d3dkmt_outputduplpresentflags.htm
old-project: display
ms.assetid: d80bcf24-4d53-4ec9-897d-d3243c7fda25
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_OUTPUTDUPLPRESENTFLAGS, D3DKMT_OUTPUTDUPLPRESENTFLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_OUTPUTDUPLPRESENTFLAGS
req.alt-loc: D3dkmthk.h
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
req.iface: 
---

# D3DKMT_OUTPUTDUPLPRESENTFLAGS structure



## -description
<p>Describes options for a <a href="direct3ddxgi.desktop_dup_api">Desktop Duplication API</a> swapchain present operation.</p>


## -syntax

````
typedef struct _D3DKMT_OUTPUTDUPLPRESENTFLAGS {
  union {
    struct {
      UINT ProtectedContentBlankedOut  :1;
      UINT RemoteSession  :1;
      UINT FullScreenPresent  :1;
      UINT Reserved  :29;
    };
    UINT   Value;
  };
} D3DKMT_OUTPUTDUPLPRESENTFLAGS;
````


## -struct-fields
<dl>

### -field ProtectedContentBlankedOut

<dd>
<p>Specifies whether the desktop image might contain protected content that was already blanked out (black) in the desktop image.</p>
<p><b>TRUE</b> if protected content was already blanked out; otherwise, <b>FALSE</b>.</p>
<p>The application can use this information to notify the remote user that some of the desktop content might be protected and therefore not visible.</p>
</dd>

### -field RemoteSession

<dd>
<p>Specifies if the present operation is directed to a remote session</p>
<p><b>TRUE</b> if the present operation is directed to a remote session; otherwise, <b>FALSE</b>.</p>
<p>If <b>TRUE</b>, the present operation will go through a GDI path.</p>
</dd>

### -field FullScreenPresent

<dd>
<p>Specifies if the present operation is to the full screen.</p>
<p><b>TRUE</b> if the present operation is to the full screen; otherwise, <b>FALSE</b>.</p>
</dd>

### -field Reserved

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 29 bits (0xFFFFFFF8) of the 32-bit <b>Value</b> member to zeros.

</p>
</dd>

### -field Value

<dd>
<p>A 32-bit value that identifies the DDA present options.</p>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>