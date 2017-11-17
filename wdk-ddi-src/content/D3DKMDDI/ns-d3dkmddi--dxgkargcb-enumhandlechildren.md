---
UID: NS.d3dkmddi._DXGKARGCB_ENUMHANDLECHILDREN
title: DXGKARGCB_ENUMHANDLECHILDREN
author: windows-driver-content
description: The DXGKARGCB_ENUMHANDLECHILDREN structure describes a parent resource and the index of one of its child allocations.
old-location: display\dxgkargcb_enumhandlechildren.htm
ms.assetid: da97b175-a24c-406d-9747-c84122781f79
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
req.alt-api: DXGKARGCB_ENUMHANDLECHILDREN
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
ms.keywords: DXGKARGCB_ENUMHANDLECHILDREN, DXGKARGCB_ENUMHANDLECHILDREN
req.iface: 
---

# DXGKARGCB_ENUMHANDLECHILDREN structure



## -description
<p>The DXGKARGCB_ENUMHANDLECHILDREN structure describes a parent resource and the index of one of its child allocations. </p>


## -syntax

````
typedef struct _DXGKARGCB_ENUMHANDLECHILDREN {
  D3DKMT_HANDLE hObject;
  UINT          Index;
} DXGKARGCB_ENUMHANDLECHILDREN;
````


## -struct-fields
<dl>

### -field <b>hObject</b>

<dd>
<p>[in] A handle to the parent resource of a group of child allocations. This handle is the kernel-mode handle that the Microsoft DirectX graphics kernel subsystem (which is part of <i>Dxgkrnl.sys</i>) assigned for the parent resource.</p>
</dd>

### -field <b>Index</b>

<dd>
<p>[in] The index into the array of allocations that belongs to the resource that <b>hObject</b> specifies.</p>
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
<a href="https://msdn.microsoft.com/36307e63-9e94-4441-92c6-fd4293ea8fa9">DxgkCbEnumHandleChildren</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARGCB_ENUMHANDLECHILDREN structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
