---
UID: NS.msviddrv.tag_video_geterrortext_parms
title: tag_video_geterrortext_parms
author: windows-driver-content
description: TBD.
old-location: stream\video_geterrortext_parms.htm
ms.assetid: 6CF06E9A-D6A1-42A7-9C34-44BC52713621
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: msviddrv.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_GETERRORTEXT_PARMS
req.alt-loc: Msviddrv.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: tag_video_geterrortext_parms, VIDEO_GETERRORTEXT_PARMS, *LPVIDEO_GETERRORTEXT_PARMS
req.iface: 
---

# tag_video_geterrortext_parms structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct tag_video_geterrortext_parms {
  DWORD  dwError;
#ifdef _WIN32
  LPWSTR lpText;
#else 
  LPSTR  lpText;
#endif 
  DWORD  dwLength;
} VIDEO_GETERRORTEXT_PARMS, *LPVIDEO_GETERRORTEXT_PARMS;
````


## -struct-fields
<dl>

### -field <b>dwError</b>

<dd>
<p>Specifies the error number to identify.</p>
</dd>

### -field <b>lpText</b>

<dd>
<p>Specifies the text buffer to fill.</p>
</dd>

### -field <b>lpText</b>

<dd>
<p>Specifies the text buffer to fill.</p>
</dd>

### -field <b>dwLength</b>

<dd>
<p>Specifies the size of the text buffer in characters.</p>
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
<dt>Msviddrv.h</dt>
</dl>
</td>
</tr>
</table>