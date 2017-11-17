---
UID: NE.d3dkmdt._D3DKMDT_TEXT_RENDERING_FORMAT
title: D3DKMDT_TEXT_RENDERING_FORMAT
author: windows-driver-content
description: The D3DKMDT_TEXT_RENDERING_FORMAT enumeration is currently not used.
old-location: display\d3dkmdt_text_rendering_format.htm
ms.assetid: 73ec5d3c-d8f6-4db9-b55f-317eab3b4a39
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_TEXT_RENDERING_FORMAT
req.alt-loc: d3dkmdt.h
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
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
req.iface: 
---

# D3DKMDT_TEXT_RENDERING_FORMAT enumeration



## -description
<p>The D3DKMDT_TEXT_RENDERING_FORMAT enumeration is currently not used.</p>


## -syntax

````
typedef enum _D3DKMDT_TEXT_RENDERING_FORMAT { 
  D3DKMDT_TRF_UNINITIALIZED  = 0
} D3DKMDT_TEXT_RENDERING_FORMAT;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_TRF_UNINITIALIZED"></a><a id="d3dkmdt_trf_uninitialized"></a><b>D3DKMDT_TRF_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type D3DKMDT_TEXT_RENDERING_FORMAT has not yet been assigned a meaningful value.</p>
</dd>
</dl>

## -remarks
<p>The <b>Format.Text</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546724">D3DKMDT_VIDPN_SOURCE_MODE</a> structure is a D3DKMDT_TEXT_RENDERING_FORMAT value.</p>

<p>The <b>Format.Text</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546724">D3DKMDT_VIDPN_SOURCE_MODE</a> structure is a D3DKMDT_TEXT_RENDERING_FORMAT value.</p>

<p>The <b>Format.Text</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546724">D3DKMDT_VIDPN_SOURCE_MODE</a> structure is a D3DKMDT_TEXT_RENDERING_FORMAT value.</p>

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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570558">VidPn Source Mode Set Interface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_TEXT_RENDERING_FORMAT enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
