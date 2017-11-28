---
UID: NS.d3dkmdt._D3DKMDT_VIDEO_PRESENT_SOURCE
title: D3DKMDT_VIDEO_PRESENT_SOURCE
author: windows-driver-content
description: The D3DKMDT_VIDEO_PRESENT_SOURCE structure contains the unique identifier of a video present source.
old-location: display\d3dkmdt_video_present_source.htm
old-project: display
ms.assetid: 907df90c-dfea-40bf-9d08-5f5d87571ed8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMDT_VIDEO_PRESENT_SOURCE,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_VIDEO_PRESENT_SOURCE
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
req.irql: 
req.iface: 
---

# D3DKMDT_VIDEO_PRESENT_SOURCE structure



## -description
<p>The D3DKMDT_VIDEO_PRESENT_SOURCE structure contains the unique identifier of a video present source.</p>


## -syntax

````
typedef struct _D3DKMDT_VIDEO_PRESENT_SOURCE {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID Id;
  DWORD                          dwReserved;
} D3DKMDT_VIDEO_PRESENT_SOURCE;
````


## -struct-fields
<dl>

### -field <b>Id</b>

<dd>
<p>The identifier of a video present source.</p>
</dd>

### -field <b>dwReserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks
<p>The D3DDDI_VIDEO_PRESENT_SOURCE_ID data type is defined in <i>D3dukmdt.h</i>.</p>

<p>Video present source identifiers are assigned by the operating system. <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a>, implemented by the display miniport driver, returns the number N of video present sources supported by the display adapter. Then the operating system assigns identifiers 0, 1, 2, ... NÂ -Â 1.</p>

<p>For more information about video present sources, see <a href="https://msdn.microsoft.com/62a92f00-b1da-41c2-99af-eef8140b064e">Introduction to Video Present Networks</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546617">D3DKMDT_VIDEO_PRESENT_TARGET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546647">D3DKMDT_VIDPN_PRESENT_PATH</a>
</dt>
<dt>
<a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_VIDEO_PRESENT_SOURCE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
