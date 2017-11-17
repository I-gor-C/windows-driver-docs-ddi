---
UID: NS.d3dkmddi._DXGKARG_SETROOTPAGETABLE
title: DXGKARG_SETROOTPAGETABLE
author: windows-driver-content
description: DXGKARG_SETROOTPAGETABLE is used by the DxgkDdiSetRootPageTabledevice driver interface (DDI) to notify a context when its associated root page table is resized or moved in memory.
old-location: display\dxgkarg_setrootpagetable.htm
ms.assetid: D3863924-29EE-4886-B8DC-F9020A7C85A4
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_SETROOTPAGETABLE
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
ms.keywords: DXGKARG_SETROOTPAGETABLE, DXGKARG_SETROOTPAGETABLE
req.iface: 
---

# DXGKARG_SETROOTPAGETABLE structure



## -description
<p><b>DXGKARG_SETROOTPAGETABLE</b> is used by the <a href="https://msdn.microsoft.com/BC9E7A2D-690D-4EC2-8D16-22C5FEBA574A">DxgkDdiSetRootPageTable</a>device driver interface (DDI) to notify a context when its associated root page table is resized or moved in memory.</p>


## -syntax

````
typedef struct _DXGKARG_SETROOTPAGETABLE {
  HANDLE                  hContext;
  D3DGPU_PHYSICAL_ADDRESS Address;
  UINT                    NumEntries;
} DXGKARG_SETROOTPAGETABLE;
````


## -struct-fields
<dl>

### -field <b>hContext</b>

<dd>
<p>A context handle returned by <a href="https://msdn.microsoft.com/aea21a36-f3d5-4541-bd2d-aa026668c562">DxgkDdiCreateContext</a>.</p>
</dd>

### -field <b>Address</b>

<dd>
<p>The GPU physical address of the root page table.</p>
</dd>

### -field <b>NumEntries</b>

<dd>
<p> The root page table size in entries. GPU should generate invalid fault when a virtual address has a top level page table entry index, which is greater or equal this value.</p>
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
<a href="https://msdn.microsoft.com/BC9E7A2D-690D-4EC2-8D16-22C5FEBA574A">DxgkDdiSetRootPageTable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/aea21a36-f3d5-4541-bd2d-aa026668c562">DxgkDdiCreateContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_SETROOTPAGETABLE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
