---
UID: NS.ksmedia.tagKSCAMERA_EXTENDEDPROP_METADATAINFO
title: tagKSCAMERA_EXTENDEDPROP_METADATAINFO
author: windows-driver-content
description: This structure represents the metadata information for the extended property control.
old-location: stream\kscamera_extendedprop_metadatainfo.htm
old-project: stream
ms.assetid: 6AE59150-8A10-43B6-B910-AEBEDC2FD272
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagKSCAMERA_EXTENDEDPROP_METADATAINFO, KSCAMERA_EXTENDEDPROP_METADATAINFO, *PKSCAMERA_EXTENDEDPROP_METADATAINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_EXTENDEDPROP_METADATAINFO
req.alt-loc: Ksmedia.h
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

# tagKSCAMERA_EXTENDEDPROP_METADATAINFO structure



## -description
<p>This structure represents the metadata information for the extended property control.</p>


## -syntax

````
typedef struct tagKSCAMERA_EXTENDEDPROP_METADATAINFO {
  LONG  BufferAlignment;
  ULONG MaxMetadataBufferSize;
} KSCAMERA_EXTENDEDPROP_METADATAINFO, *PKSCAMERA_EXTENDEDPROP_METADATAINFO;
````


## -struct-fields
<dl>

### -field <b>BufferAlignment</b>

<dd>
<p>The required alignment for the metadata buffer.</p>
<p><i>BufferAlignment</i> can be one of the following values:</p>
<ul>
<li>
<p>KSCAMERA_EXTENDEDPROP_MetadataAlignment_16</p>
</li>
<li>
<p>KSCAMERA_EXTENDEDPROP_MetadataAlignment_32</p>
</li>
<li>
<p>KSCAMERA_EXTENDEDPROP_MetadataAlignment_64</p>
</li>
<li>
<p>KSCAMERA_EXTENDEDPROP_MetadataAlignment_128</p>
</li>
<li>
<p>KSCAMERA_EXTENDEDPROP_MetadataAlignment_256</p>
</li>
<li>
<p>KSCAMERA_EXTENDEDPROP_MetadataAlignment_512</p>
</li>
<li>
<p>KSCAMERA_EXTENDEDPROP_MetadataAlignment_1024</p>
</li>
<li>
<p>KSCAMERA_EXTENDEDPROP_MetadataAlignment_2048</p>
</li>
<li>
<p>KSCAMERA_EXTENDEDPROP_MetadataAlignment_4096</p>
</li>
<li>
<p>KSCAMERA_EXTENDEDPROP_MetadataAlignment_8192</p>
</li>
</ul>
</dd>

### -field <b>MaxMetadataBufferSize</b>

<dd>
<p>The size of the metadata buffer.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>