---
UID: NS.mfapi.tagFaceCharacterizationBlobHeader
title: tagFaceCharacterizationBlobHeader
author: windows-driver-content
description: The FaceCharacterizationBlobHeader structure describes the size and count information of the blob format for the MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS attribute.
old-location: stream\facecharacterizationblobheader.htm
ms.assetid: F3BDB935-A8CB-41BA-B912-0B9264FE0B09
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: mfapi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FaceCharacterizationBlobHeader
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
ms.keywords: tagFaceCharacterizationBlobHeader, FaceCharacterizationBlobHeader
req.iface: 
---

# tagFaceCharacterizationBlobHeader structure



## -description
<p>The <b>FaceCharacterizationBlobHeader</b> structure  describes the size and count information of the blob format for the <b>MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS</b> attribute.</p>


## -syntax

````
typedef struct tagFaceCharacterizationBlobHeader {
  ULONG Size;
  ULONG Count;
} FaceCharacterizationBlobHeader;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Size of this header + all following <a href="https://msdn.microsoft.com/library/windows/hardware/dn927642">FaceCharacterization</a> structures.</p>
</dd>

### -field <b>Count</b>

<dd>
<p>Number of <b>FaceCharacterization</b> structures in the blob. Must match the number of <a href="https://msdn.microsoft.com/library/windows/hardware/dn927644">FaceRectInfo</a> structures in <a href="https://msdn.microsoft.com/library/windows/hardware/dn927645">FaceRectInfoBlobHeader</a>.</p>
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