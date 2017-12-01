---
UID: NE.ksmedia.KS_MPEG2Level
title: KS_MPEG2Level
author: windows-driver-content
description: The KS_MPEG2Level enumeration describes MPEG-2 levels.
old-location: stream\ks_mpeg2level.htm
old-project: stream
ms.assetid: 5ba271ba-ed92-402e-9ef9-ac198a8ea510
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: KS_MPEG2Level
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

# KS_MPEG2Level enumeration



## -description
<p>The KS_MPEG2Level enumeration describes MPEG-2 levels.</p>


## -syntax

````
typedef enum  { 
  KS_MPEG2Level_Low       = 0,
  KS_MPEG2Level_Main      = 1,
  KS_MPEG2Level_High1440  = 2,
  KS_MPEG2Level_High      = 3
} KS_MPEG2Level;
````


## -enum-fields
<dl>

### -field <a id="KS_MPEG2Level_Low"></a><a id="ks_mpeg2level_low"></a><a id="KS_MPEG2LEVEL_LOW"></a><b>KS_MPEG2Level_Low</b>

<dd>
<p>Specifies the low MPEG-2 resolution, or 352 × 240 at 30 frames per second.</p>
</dd>

### -field <a id="KS_MPEG2Level_Main"></a><a id="ks_mpeg2level_main"></a><a id="KS_MPEG2LEVEL_MAIN"></a><b>KS_MPEG2Level_Main</b>

<dd>
<p>Specifies the main MPEG-2 resolution, or 720 × 480 at 30 frames per second.</p>
</dd>

### -field <a id="KS_MPEG2Level_High1440"></a><a id="ks_mpeg2level_high1440"></a><a id="KS_MPEG2LEVEL_HIGH1440"></a><b>KS_MPEG2Level_High1440</b>

<dd>
<p>Specifies the high-1440 MPEG-2 resolution, or 1440 × 1152 at 30 frames per second.</p>
</dd>

### -field <a id="KS_MPEG2Level_High"></a><a id="ks_mpeg2level_high"></a><a id="KS_MPEG2LEVEL_HIGH"></a><b>KS_MPEG2Level_High</b>

<dd>
<p>Specifies the high MPEG-2 resolution, or 1920 × 1080 at 30 frames per second.</p>
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

## -see-also
<dl>
<dt>
<a href="stream.ks_mpegvideoinfo2">KS_MPEGVIDEOINFO2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_MPEG2Level enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
