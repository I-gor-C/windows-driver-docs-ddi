---
UID: NE.ksmedia.KSPROPERTY_AUDIOMODULE
title: KSPROPERTY_AUDIOMODULE
author: windows-driver-content
description: The KSPROPERTY_AUDIOMODULE enumeration defines constants that are used by audio drivers to communicate information about partner defined audio modules.
old-location: audio\ksproperty_audiomodule.htm
old-project: audio
ms.assetid: 94873A4A-A40F-40A7-B7A2-B693A5253714
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_AUDIOMODULE
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

# KSPROPERTY_AUDIOMODULE enumeration



## -description
<p>The KSPROPERTY_AUDIOMODULE enumeration defines constants that are used  by audio drivers to communicate information about partner  defined audio modules.</p>
<p>For more information about audio modules, see  <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/audio/implementing-audio-module-communication">Implementing Audio Module Discovery</a>. </p>


## -syntax

````
typedef enum  { 
  KSPROPERTY_AUDIOMODULE_DESCRIPTORS             = 1,
  KSPROPERTY_AUDIOMODULE_COMMAND                 = 2,
  KSPROPERTY_AUDIOMODULE_NOTIFICATION_DEVICE_ID  = 3
} KSPROPERTY_AUDIOMODULE;
````


## -enum-fields
<dl>

### -field <a id="KSPROPERTY_AUDIOMODULE_DESCRIPTORS__"></a><a id="ksproperty_audiomodule_descriptors__"></a><b>KSPROPERTY_AUDIOMODULE_DESCRIPTORS  </b>

<dd>
<p>Specifies the ID for the <a href="audio.ksproperty_audiomodule_descriptors">KSPROPERTY_AUDIOMODULE_DESCRIPTORS</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_AUDIOMODULE_COMMAND"></a><a id="ksproperty_audiomodule_command"></a><b>KSPROPERTY_AUDIOMODULE_COMMAND</b>

<dd>
<p>Specifies the ID for the <a href="audio.ksproperty_audiomodule_command">KSPROPERTY_AUDIOMODULE_COMMAND</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_AUDIOMODULE_NOTIFICATION_DEVICE_ID"></a><a id="ksproperty_audiomodule_notification_device_id"></a><b>KSPROPERTY_AUDIOMODULE_NOTIFICATION_DEVICE_ID</b>

<dd>
<p>Specifies the ID for the <a href="audio.ksproperty_audiomodule_notification_device_id">KSPROPERTY_AUDIOMODULE_NOTIFICATION_DEVICE_ID</a>    property.</p>
</dd>
</dl>

## -remarks
<p>All KS Property calls must be non-blocking because the  hardware effects are part of the processing chain and should not wait. </p>

<p>All KS Property calls must be non-blocking because the  hardware effects are part of the processing chain and should not wait. </p>

<p>All KS Property calls must be non-blocking because the  hardware effects are part of the processing chain and should not wait. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1703</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>None supported</p>
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
<a href="audio.kspropsetid_audiomodule">KSPROPSETID_AudioModule</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSPROPERTY_AUDIOMODULE enumeration%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
