---
UID: NE.d3dkmthk._D3DKMT_OFFER_PRIORITY
title: D3DKMT_OFFER_PRIORITY
author: windows-driver-content
description: Indicates the importance of video memory resources that the user-mode display driver offers for reuse.
old-location: display\d3dkmt_offer_priority.htm
old-project: display
ms.assetid: fec15098-3130-42d6-b889-579ecab6f162
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_OFFER_PRIORITY
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

# D3DKMT_OFFER_PRIORITY enumeration



## -description
<p>Indicates the importance of video memory resources  that the user-mode display driver offers for reuse.</p>


## -syntax

````
typedef enum _D3DKMT_OFFER_PRIORITY { 
  D3DKMT_OFFER_PRIORITY_LOW     = 1,
  D3DKMT_OFFER_PRIORITY_NORMAL  = 2,
  D3DKMT_OFFER_PRIORITY_HIGH    = 3,
  D3DKMT_OFFER_PRIORITY_AUTO    = 4
} D3DKMT_OFFER_PRIORITY;
````


## -enum-fields
<dl>

### -field <a id="D3DKMT_OFFER_PRIORITY_LOW"></a><a id="d3dkmt_offer_priority_low"></a><b>D3DKMT_OFFER_PRIORITY_LOW</b>

<dd>
<p>The allocation has low value and should be discarded before other offered allocations. Specify this type for allocations that have no useful content.</p>
</dd>

### -field <a id="D3DKMT_OFFER_PRIORITY_NORMAL"></a><a id="d3dkmt_offer_priority_normal"></a><b>D3DKMT_OFFER_PRIORITY_NORMAL</b>

<dd>
<p>The allocation has useful content but can easily be regenerated.</p>
</dd>

### -field <a id="D3DKMT_OFFER_PRIORITY_HIGH"></a><a id="d3dkmt_offer_priority_high"></a><b>D3DKMT_OFFER_PRIORITY_HIGH</b>

<dd>
<p>The allocation has useful content and cannot easily be regenerated. The video memory manager (which is part of Dxgkrnl.sys) should therefore avoid discarding this allocation before other offered allocations.</p>
</dd>

### -field <a id="D3DKMT_OFFER_PRIORITY_AUTO"></a><a id="d3dkmt_offer_priority_auto"></a><b>D3DKMT_OFFER_PRIORITY_AUTO</b>

<dd>
<p>The video memory manager should make a policy decision on the allocation's value based on its  priority for eviction.</p>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406482">D3DKMT_OFFERALLOCATIONS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_OFFER_PRIORITY enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
