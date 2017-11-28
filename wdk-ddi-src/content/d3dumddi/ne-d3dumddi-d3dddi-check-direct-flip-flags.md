---
UID: NE.d3dumddi.D3DDDI_CHECK_DIRECT_FLIP_FLAGS
title: D3DDDI_CHECK_DIRECT_FLIP_FLAGS
author: windows-driver-content
description: Used by the CheckDirectFlipFlags parameter of the CheckDirectFlipSupport function to specify seamless flipping of video memory.
old-location: display\d3dddi_check_direct_flip_flags.htm
old-project: display
ms.assetid: 72b49af8-4d98-4fc0-ab40-72f1e19eef96
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dumddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_CHECK_DIRECT_FLIP_FLAGS
req.alt-loc: D3dumddi.h
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

# D3DDDI_CHECK_DIRECT_FLIP_FLAGS enumeration



## -description
<p>Used by the <i>CheckDirectFlipFlags</i> parameter of the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-checkdirectflipsupport.md">CheckDirectFlipSupport</a> function to specify seamless flipping of video memory.</p>


## -syntax

````
typedef enum D3DDDI_CHECK_DIRECT_FLIP_FLAGS { 
  D3DDDI_CHECKDIRECTFLIP_IMMEDIATE  = 0x00000001
} D3DDDI_CHECK_DIRECT_FLIP_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="D3DDDI_CHECKDIRECTFLIP_IMMEDIATE"></a><a id="d3dddi_checkdirectflip_immediate"></a><b>D3DDDI_CHECKDIRECTFLIP_IMMEDIATE</b>

<dd>
<p>Seamless flipping should occur immediately and does not have to be synchronized with a VSync interrupt.</p>
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
<dt>D3dumddi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-checkdirectflipsupport.md">CheckDirectFlipSupport</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451172">D3DDDI_CHECK_DIRECT_FLIP_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_CHECK_DIRECT_FLIP_FLAGS enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
