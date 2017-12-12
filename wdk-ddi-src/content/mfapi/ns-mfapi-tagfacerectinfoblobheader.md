---
UID: NS.MFAPI.TAGFACERECTINFOBLOBHEADER
title: tagFaceRectInfoBlobHeader
author: windows-driver-content
description: The FaceRectInfoBlobHeader structure describes the size and count information of the blob format for the MF_CAPTURE_METADATA_FACEROIS attribute.
old-location: stream\facerectinfoblobheader.htm
old-project: stream
ms.assetid: BDDC33C2-CD2D-4F97-AAD1-DF69250F60B3
ms.author: windowsdriverdev
ms.date: 12/6/2017
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
---

# tagFaceRectInfoBlobHeader structure



## -description
The <b>FaceRectInfoBlobHeader</b> structure describes the size and count information of the blob format for the <b>MF_CAPTURE_METADATA_FACEROIS</b> attribute.



## -syntax

````
typedef struct tagFaceRectInfoBlobHeader {
  ULONG Size;
  ULONG Count;
} FaceRectInfoBlobHeader;
````


## -struct-fields

### -field Size

Size of this header + all following <a href="stream.facerectinfo">FaceRectInfo</a> structures.


### -field Count

Number of <b>FaceRectInfo</b> structures in the blob.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Mfapi.h</dt>
</dl>
</td>
</tr>
</table>