---
UID: NS.d3dkmddi._DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES
title: DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES
author: windows-driver-content
description: DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES describes the operation used copy page table entries from one location to another.
old-location: display\dxgk_buildpagingbuffer_copypagetableentries.htm
old-project: display
ms.assetid: 627FB3E6-3C5D-4104-B129-08D3EC0B963E
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES, DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES
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
req.alt-api: DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES
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

# DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES structure



## -description
<p><b>DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES</b> describes the operation used copy page table entries from one location to another. </p>


## -syntax

````
typedef struct _DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES {
  UINT                              NumRanges;
  DXGK_BUILDPAGINGBUFFER_COPY_RANGE *pRanges;
} DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES;
````


## -struct-fields
<dl>

### -field <b>NumRanges</b>

<dd>
<p>The number of elements in the <b>pRanges</b> array.</p>
</dd>

### -field <b>pRanges</b>

<dd>
<p>A pointer to a <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-buildpagingbuffer-copy-range.md">DXGK_BUILDPAGINGBUFFER_COPY_RANGE</a> structure describing each range of page table entries to copy.</p>
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
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-buildpagingbuffer.md">DXGKARG_BUILDPAGINGBUFFER</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-buildpagingbuffer-copy-range.md">DXGK_BUILDPAGINGBUFFER_COPY_RANGE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
