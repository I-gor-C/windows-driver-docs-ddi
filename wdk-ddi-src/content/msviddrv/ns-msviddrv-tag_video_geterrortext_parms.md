---
UID: NS.MSVIDDRV.TAG_VIDEO_GETERRORTEXT_PARMS
title: tag_video_geterrortext_parms
author: windows-driver-content
description: .
old-location: stream\video_geterrortext_parms.htm
old-project: stream
ms.assetid: 6CF06E9A-D6A1-42A7-9C34-44BC52713621
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: tag_video_geterrortext_parms, VIDEO_GETERRORTEXT_PARMS, *LPVIDEO_GETERRORTEXT_PARMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
---

# tag_video_geterrortext_parms structure



## -description




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

### -field dwError

Specifies the error number to identify.


### -field lpText

Specifies the text buffer to fill.


### -field lpText

Specifies the text buffer to fill.


### -field dwLength

Specifies the size of the text buffer in characters.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Msviddrv.h</dt>
</dl>
</td>
</tr>
</table>