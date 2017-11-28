---
UID: NS.mfapi.tagFaceRectInfoBlobHeader
title: tagFaceRectInfoBlobHeader
author: windows-driver-content
description: The FaceRectInfoBlobHeader structure describes the size and count information of the blob format for the MF_CAPTURE_METADATA_FACEROIS attribute.
old-location: stream\facerectinfoblobheader.htm
old-project: stream
ms.assetid: BDDC33C2-CD2D-4F97-AAD1-DF69250F60B3
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagFaceRectInfoBlobHeader, FaceRectInfoBlobHeader
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mfapi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FaceRectInfoBlobHeader
req.alt-loc: mfapi.h
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

# tagFaceRectInfoBlobHeader structure



## -description
<p>The <b>FaceRectInfoBlobHeader</b> structure describes the size and count information of the blob format for the <b>MF_CAPTURE_METADATA_FACEROIS</b> attribute.</p>


## -syntax

````
typedef struct tagFaceRectInfoBlobHeader {
  ULONG Size;
  ULONG Count;
} FaceRectInfoBlobHeader;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Size of this header + all following <a href="https://msdn.microsoft.com/library/windows/hardware/dn927644">FaceRectInfo</a> structures.</p>
</dd>

### -field <b>Count</b>

<dd>
<p>Number of <b>FaceRectInfo</b> structures in the blob.</p>
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
<dt>Mfapi.h</dt>
</dl>
</td>
</tr>
</table>