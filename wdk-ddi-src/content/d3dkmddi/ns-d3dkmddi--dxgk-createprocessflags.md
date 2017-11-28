---
UID: NS.d3dkmddi._DXGK_CREATEPROCESSFLAGS
title: DXGK_CREATEPROCESSFLAGS
author: windows-driver-content
description: DXGK_CREATEPROCESSFLAGS is used with DXGKARG_CREATEPROCESS and DxgkDdiCreateProcess to create a kernel mode driver object for a Microsoft DirectX graphics kernel process object.
old-location: display\dxgk_createprocessflags.htm
old-project: display
ms.assetid: 43B8202C-6AC1-4596-BA85-FEB9FB0B5746
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CREATEPROCESSFLAGS, DXGK_CREATEPROCESSFLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_CREATEPROCESSFLAGS
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
req.iface: 
---

# DXGK_CREATEPROCESSFLAGS structure



## -description
<p><b>DXGK_CREATEPROCESSFLAGS</b> is used with <a href="https://msdn.microsoft.com/library/windows/hardware/dn914470">DXGKARG_CREATEPROCESS</a> and <a href="display.dxgkddicreateprocess">DxgkDdiCreateProcess</a> to create a kernel mode driver object for a Microsoft DirectX graphics kernel process object.</p>


## -syntax

````
typedef struct _DXGK_CREATEPROCESSFLAGS {
  union {
    struct {
      UINT SystemProcess  :1;
      UINT GdiProcess  :1;
      UINT Reserved  :30;
    };
    UINT   Value;
  };
} DXGK_CREATEPROCESSFLAGS;
````


## -struct-fields
<dl>

### -field <b>SystemProcess</b>

<dd>
<p>Indicates that a system process is being created.</p>
</dd>

### -field <b>GdiProcess</b>

<dd>
<p>Indicates that a GDI process is being created.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>The consolidated value of the bitfield members of the structure.</p>
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
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn914470">DXGKARG_CREATEPROCESS</a>
</dt>
<dt>
<a href="display.dxgkddicreateprocess">DxgkDdiCreateProcess</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_CREATEPROCESSFLAGS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
