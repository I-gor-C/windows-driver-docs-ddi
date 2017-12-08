---
UID: NS.d3dkmddi._DXGKARG_COLLECTDBGINFO_EXT
title: DXGKARG_COLLECTDBGINFO_EXT
author: windows-driver-content
description: The DXGKARG_COLLECTDBGINFO_EXT structure describes extension information for a debug report.
old-location: display\dxgkarg_collectdbginfo_ext.htm
old-project: display
ms.assetid: cbde31fe-06c1-44af-8940-b66e8044a5cd
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_COLLECTDBGINFO_EXT, DXGKARG_COLLECTDBGINFO_EXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_COLLECTDBGINFO_EXT
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

# DXGKARG_COLLECTDBGINFO_EXT structure



## -description
<p>The DXGKARG_COLLECTDBGINFO_EXT structure describes extension information for a debug report.</p>


## -syntax

````
typedef struct _DXGKARG_COLLECTDBGINFO_EXT {
  UINT BucketingKey;
  UINT CurrentDmaBufferOffset;
  UINT Reserved2;
  UINT Reserved3;
  UINT Reserved4;
  UINT Reserved5;
  UINT Reserved6;
  UINT Reserved7;
} DXGKARG_COLLECTDBGINFO_EXT;
````


## -struct-fields
<dl>

### -field BucketingKey

<dd>
<p>[out] The optional integer key for Microsoft Online Crash Analysis (OCA) bucketing (that is, the categorizing of minidumps). </p>
</dd>

### -field CurrentDmaBufferOffset

<dd>
<p>[out] The optional execution offset into the current DMA buffer. The operating system uses the offset to optimize DMA data collection.</p>
</dd>

### -field Reserved2

<dd>
<p>Reserved for future use.</p>
</dd>

### -field Reserved3

<dd>
<p>Reserved for future use.</p>
</dd>

### -field Reserved4

<dd>
<p>Reserved for future use.</p>
</dd>

### -field Reserved5

<dd>
<p>Reserved for future use.</p>
</dd>

### -field Reserved6

<dd>
<p>Reserved for future use.</p>
</dd>

### -field Reserved7

<dd>
<p>Reserved for future use.</p>
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
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-collectdbginfo.md">DXGKARG_COLLECTDBGINFO</a>
</dt>
<dt>
<a href="display.dxgkddicollectdbginfo">DxgkDdiCollectDbgInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_COLLECTDBGINFO_EXT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
