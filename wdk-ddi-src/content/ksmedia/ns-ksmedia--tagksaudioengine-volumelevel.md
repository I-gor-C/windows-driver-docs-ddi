---
UID: NS.ksmedia._tagKSAUDIOENGINE_VOLUMELEVEL
title: tagKSAUDIOENGINE_VOLUMELEVEL
author: windows-driver-content
description: The KSAUDIOENGINE_VOLUMELEVEL structure specifies the target volume level, ramp type, and duration within which the volume level should change, for a given volume level request via the KSPROPERTY_AUDIOENGINE_VOLUMELEVEL property.
old-location: audio\ksaudioengine_volumelevel.htm
old-project: audio
ms.assetid: E29E6F8B-F708-493B-94C3-A9DEE691ED3C
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagKSAUDIOENGINE_VOLUMELEVEL, KSAUDIOENGINE_VOLUMELEVEL, *PKSAUDIOENGINE_VOLUMELEVEL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSAUDIOENGINE_VOLUMELEVEL
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

# tagKSAUDIOENGINE_VOLUMELEVEL structure



## -description
<p>The <b>KSAUDIOENGINE_VOLUMELEVEL</b> structure specifies the target volume level, ramp type, and duration within which the volume level should change, for a given volume level request via the <a href="https://msdn.microsoft.com/library/windows/hardware/hh831855">KSPROPERTY_AUDIOENGINE_VOLUMELEVEL</a> property.</p>


## -syntax

````
typedef struct _KSAUDIOENGINE_VOLUMELEVEL {
  LONG             TargetVolume;
  AUDIO_CURVE_TYPE CurveType;
  ULONGLONG        CurveDuration;
} KSAUDIOENGINE_VOLUMELEVEL, *PKSAUDIOENGINE_VOLUMELEVEL;
````


## -struct-fields
<dl>

### -field TargetVolume

<dd>
<p>Specifies the desired final volume level using the scale defined for the <b>KSPROPERTY_AUDIOENGINE_VOLUMELEVEL</b> property.</p>
</dd>

### -field CurveType

<dd>
<p>Uses the <a href="..\ksmedia\ne-ksmedia-audio-curve-type.md">AUDIO_CURVE_TYPE</a> enumeration to specify the curve algorithm to apply over the duration specified, in order to reach the desired level.  The curve begins at the current volume level and ends at the target volume level specified in the <b>TargetVolume</b> parameter.</p>
</dd>

### -field CurveDuration

<dd>
<p>Specifies the duration, in hundreds of nanoseconds, over which the volume curve must take effect.</p>
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
<p>Windows 8</p>
</td>
</tr>
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

## -see-also
<dl>
<dt>
<a href="..\ksmedia\ne-ksmedia-audio-curve-type.md">AUDIO_CURVE_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh831855">KSPROPERTY_AUDIOENGINE_VOLUMELEVEL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSAUDIOENGINE_VOLUMELEVEL structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
