---
UID: NE.d3d10umddi.D3D11_1_DDI_CHECK_DIRECT_FLIP_FLAGS
title: D3D11_1_DDI_CHECK_DIRECT_FLIP_FLAGS
author: windows-driver-content
description: Used by the CheckDirectFlipFlags parameter of the CheckDirectFlipSupport(D3D11_1) function to specify seamless flipping of video memory.
old-location: display\d3d11_1_ddi_check_direct_flip_flags.htm
old-project: display
ms.assetid: beead760-8f93-48da-b2fc-2f8a0031019c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1_DDI_CHECK_DIRECT_FLIP_FLAGS
req.alt-loc: D3d10umddi.h
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

# D3D11_1_DDI_CHECK_DIRECT_FLIP_FLAGS enumeration



## -description
<p>Used by the <i>CheckDirectFlipFlags</i> parameter of the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-checkdirectflipsupport.md">CheckDirectFlipSupport(D3D11_1)</a> function to specify seamless flipping of video memory.</p>


## -syntax

````
typedef enum D3D11_1_DDI_CHECK_DIRECT_FLIP_FLAGS { 
  D3D11_1DDI_CHECK_DIRECT_FLIP_IMMEDIATE  = 0x00000001
} D3D11_1_DDI_CHECK_DIRECT_FLIP_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="D3D11_1DDI_CHECK_DIRECT_FLIP_IMMEDIATE"></a><a id="d3d11_1ddi_check_direct_flip_immediate"></a><b>D3D11_1DDI_CHECK_DIRECT_FLIP_IMMEDIATE</b>

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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-checkdirectflipsupport.md">CheckDirectFlipSupport(D3D11_1)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1_DDI_CHECK_DIRECT_FLIP_FLAGS enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
