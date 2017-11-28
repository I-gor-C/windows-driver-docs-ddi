---
UID: NS.d3dkmddi._DXGK_QUERYSEGMENTIN4
title: DXGK_QUERYSEGMENTIN4
author: windows-driver-content
description: The DXGK_QUERYSEGMENTIN4 structure is used to specify the adapter to query.
old-location: display\dxgk_querysegmentin4.htm
old-project: display
ms.assetid: B78E5AEF-DC31-44B2-92D8-DE7C83726E29
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_QUERYSEGMENTIN4, DXGK_QUERYSEGMENTIN4
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
req.alt-api: DXGK_QUERYSEGMENTIN4
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

# DXGK_QUERYSEGMENTIN4 structure



## -description
<p>The <b>DXGK_QUERYSEGMENTIN4</b> structure is used to specify the adapter to query.</p>


## -syntax

````
typedef struct _DXGK_QUERYSEGMENTIN4 {
  UINT PhysicalAdapterIndex;
} DXGK_QUERYSEGMENTIN4;
````


## -struct-fields
<dl>

### -field <b>PhysicalAdapterIndex</b>

<dd>
<p>A zero-based physical adapter index in a linked display adapter  (LDA) link. Zero for non-LDA configurations. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906840">DXGK_QUERYSEGMENTOUT4</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_QUERYSEGMENTIN4 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
