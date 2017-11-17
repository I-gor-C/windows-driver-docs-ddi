---
UID: NS.d3dkmddi._DXGK_CREATECONTEXTFLAGS
title: DXGK_CREATECONTEXTFLAGS
author: windows-driver-content
description: The DXGK_CREATECONTEXTFLAGS structure identifies how to create contexts.
old-location: display\dxgk_createcontextflags.htm
ms.assetid: f7cadf78-c908-4034-889d-b5c7d0ffdaad
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
req.alt-api: DXGK_CREATECONTEXTFLAGS
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
ms.keywords: DXGK_CREATECONTEXTFLAGS, DXGK_CREATECONTEXTFLAGS
req.iface: 
---

# DXGK_CREATECONTEXTFLAGS structure



## -description
<p>The DXGK_CREATECONTEXTFLAGS structure identifies how to create contexts.</p>


## -syntax

````
typedef struct _DXGK_CREATECONTEXTFLAGS {
  union {
    struct {
      UINT SystemContext  :1;
      UINT GdiContext  :1;
      UINT VirtualAddressing  :1;
      UINT SystemProtectedContext  :1;
      UINT Reserved  :28;
    };
    UINT Value;
  };
} DXGK_CREATECONTEXTFLAGS;
````


## -struct-fields
<dl>

### -field <b>SystemContext</b>

<dd>
<p>A UINT value that specifies whether contexts that a driver's <a href="https://msdn.microsoft.com/aea21a36-f3d5-4541-bd2d-aa026668c562">DxgkDdiCreateContext</a> function creates are system contexts for the engine that the <b>EngineAffinity</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557567">DXGKARG_CREATECONTEXT</a> structure specifies. A system context is created for the paging engine only.</p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>GdiContext</b>

<dd>
<p>A UINT value that specifies whether the contexts that a driver's <a href="https://msdn.microsoft.com/aea21a36-f3d5-4541-bd2d-aa026668c562">DxgkDdiCreateContext</a> function creates are GDI-specific contexts for the engine that the <b>EngineAffinity</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557567">DXGKARG_CREATECONTEXT</a> structure specifies.</p>
<p>Setting this member is equivalent to setting the second bit of the 32-bit <b>Value</b> member (0x00000002).</p>
<p>This member is available beginning with Windows 7.</p>
</dd>

### -field <b>VirtualAddressing</b>

<dd>
<p>A UINT value that specifies whether the contexts that a driver's <a href="https://msdn.microsoft.com/aea21a36-f3d5-4541-bd2d-aa026668c562">DxgkDdiCreateContext</a> function creates use virtual addressing.</p>
<p>Setting this member is equivalent to setting the third bit of the 32-bit <b>Value</b> member (0x00000004).</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>SystemProtectedContext</b>

<dd>
<p>A UINT value that specifies whether the context being used to modify the VPR will have access to allocations outside the VPR.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 28 bits (0xFFFFFFFB) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A member in the union that DXGK_CREATECONTEXTFLAGS contains that can hold a 32-bit value that identifies how to create contexts.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557567">DXGKARG_CREATECONTEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/aea21a36-f3d5-4541-bd2d-aa026668c562">DxgkDdiCreateContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_CREATECONTEXTFLAGS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
