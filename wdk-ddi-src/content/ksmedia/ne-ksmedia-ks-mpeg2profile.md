---
UID: NE.ksmedia.KS_MPEG2Profile
title: KS_MPEG2Profile
author: windows-driver-content
description: The KS_MPEG2Profile enumeration describes MPEG-2 profiles.
old-location: stream\ks_mpeg2profile.htm
old-project: stream
ms.assetid: 1846e6b7-5b98-4850-86d6-ef6a29ce050b
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
req.alt-api: KS_MPEG2Profile
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

# KS_MPEG2Profile enumeration



## -description
<p>The KS_MPEG2Profile enumeration describes MPEG-2 profiles.</p>


## -syntax

````
typedef enum  { 
  KS_MPEG2Profile_Simple             = 0,
  KS_MPEG2Profile_Main               = 1,
  KS_MPEG2Profile_SNRScalable        = 2,
  KS_MPEG2Profile_SpatiallyScalable  = 3,
  KS_MPEG2Profile_High               = 4
} KS_MPEG2Profile;
````


## -enum-fields
<dl>

### -field <a id="KS_MPEG2Profile_Simple"></a><a id="ks_mpeg2profile_simple"></a><a id="KS_MPEG2PROFILE_SIMPLE"></a><b>KS_MPEG2Profile_Simple</b>

<dd>
<p>Specifies the simple MPEG-2 profile, generally intended for software applications and some cable television.</p>
</dd>

### -field <a id="KS_MPEG2Profile_Main"></a><a id="ks_mpeg2profile_main"></a><a id="KS_MPEG2PROFILE_MAIN"></a><b>KS_MPEG2Profile_Main</b>

<dd>
<p>Specifies the main MPEG-2 profile, generally intended for cable or satellite television.</p>
</dd>

### -field <a id="KS_MPEG2Profile_SNRScalable"></a><a id="ks_mpeg2profile_snrscalable"></a><a id="KS_MPEG2PROFILE_SNRSCALABLE"></a><b>KS_MPEG2Profile_SNRScalable</b>

<dd>
<p>Similar to <b>KS_MPEG2Profile_Main</b>, with scalable signal-to-noise.</p>
</dd>

### -field <a id="KS_MPEG2Profile_SpatiallyScalable"></a><a id="ks_mpeg2profile_spatiallyscalable"></a><a id="KS_MPEG2PROFILE_SPATIALLYSCALABLE"></a><b>KS_MPEG2Profile_SpatiallyScalable</b>

<dd>
<p>Similar to <b>KS_MPEG2Profile_Main</b>, with spatial scalability.</p>
</dd>

### -field <a id="KS_MPEG2Profile_High"></a><a id="ks_mpeg2profile_high"></a><a id="KS_MPEG2PROFILE_HIGH"></a><b>KS_MPEG2Profile_High</b>

<dd>
<p>Similar to <b>KS_MPEG2Profile_Main</b>, with spatial scalability, scalable signal-to-noise, and 4:2:2 macroblocks.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567667">KS_MPEGVIDEOINFO2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_MPEG2Profile enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
