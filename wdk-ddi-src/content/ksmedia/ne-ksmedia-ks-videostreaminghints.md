---
UID: NE.ksmedia.KS_VideoStreamingHints
title: KS_VideoStreamingHints
author: windows-driver-content
description: The KS_VideoStreamingHints enumeration defines video compression hints.
old-location: stream\ks_videostreaminghints.htm
old-project: stream
ms.assetid: 06f26404-c955-4034-8dd3-ad641c7b8010
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_VideoStreamingHints
req.alt-loc: ksmedia.h
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

# KS_VideoStreamingHints enumeration



## -description
<p>The KS_VideoStreamingHints enumeration defines video compression hints.</p>


## -syntax

````
typedef enum  { 
  KS_StreamingHint_FrameInterval   = 0x0100,
  KS_StreamingHint_KeyFrameRate    = 0x0200,
  KS_StreamingHint_PFrameRate      = 0x0400,
  KS_StreamingHint_CompQuality     = 0x0800,
  KS_StreamingHint_CompWindowSize  = 0x1000
} KS_VideoStreamingHints;
````


## -enum-fields
<dl>

### -field <a id="KS_StreamingHint_FrameInterval"></a><a id="ks_streaminghint_frameinterval"></a><a id="KS_STREAMINGHINT_FRAMEINTERVAL"></a><b>KS_StreamingHint_FrameInterval</b>

<dd>
<p>Specifies compression that is based on the interval between video frames.</p>
</dd>

### -field <a id="KS_StreamingHint_KeyFrameRate"></a><a id="ks_streaminghint_keyframerate"></a><a id="KS_STREAMINGHINT_KEYFRAMERATE"></a><b>KS_StreamingHint_KeyFrameRate</b>

<dd>
<p>Specifies compression that is based on key frames.</p>
</dd>

### -field <a id="KS_StreamingHint_PFrameRate"></a><a id="ks_streaminghint_pframerate"></a><a id="KS_STREAMINGHINT_PFRAMERATE"></a><b>KS_StreamingHint_PFrameRate</b>

<dd>
<p>Specifies compression that is based on predicted frames.</p>
</dd>

### -field <a id="KS_StreamingHint_CompQuality"></a><a id="ks_streaminghint_compquality"></a><a id="KS_STREAMINGHINT_COMPQUALITY"></a><b>KS_StreamingHint_CompQuality</b>

<dd>
<p>Specifies compression that is based on compression quality.</p>
</dd>

### -field <a id="KS_StreamingHint_CompWindowSize"></a><a id="ks_streaminghint_compwindowsize"></a><a id="KS_STREAMINGHINT_COMPWINDOWSIZE"></a><b>KS_StreamingHint_CompWindowSize</b>

<dd>
<p>Specifies compression that is based on compression window size.</p>
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
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>