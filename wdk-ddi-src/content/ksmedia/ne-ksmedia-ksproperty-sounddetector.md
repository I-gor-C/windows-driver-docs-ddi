---
UID: NE.ksmedia.KSPROPERTY_SOUNDDETECTOR
title: KSPROPERTY_SOUNDDETECTOR
author: windows-driver-content
description: The KSPROPERTY_SOUNDDETECTOR enumeration defines constants that are used to register a filter for an audio capture device that also supports a detector.
old-location: audio\ksproperty_sounddetector.htm
ms.assetid: 6AF98B06-1531-4AC9-9E32-D812E6EA424C
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_SOUNDDETECTOR
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
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
req.iface: 
---

# KSPROPERTY_SOUNDDETECTOR enumeration



## -description
<p>The <b>KSPROPERTY_SOUNDDETECTOR</b> enumeration defines constants that are used to register a filter for an audio capture device that also supports a detector.</p>


## -syntax

````
typedef enum  { 
  KSPROPERTY_SOUNDDETECTOR_SUPPORTEDPATTERNS  = 1,
  KSPROPERTY_SOUNDDETECTOR_PATTERNS,
  KSPROPERTY_SOUNDDETECTOR_ARMED,
  KSPROPERTY_SOUNDDETECTOR_MATCHRESULT
} KSPROPERTY_SOUNDDETECTOR;
````


## -enum-fields
<dl>

### -field <a id="KSPROPERTY_SOUNDDETECTOR_SUPPORTEDPATTERNS"></a><a id="ksproperty_sounddetector_supportedpatterns"></a><b>KSPROPERTY_SOUNDDETECTOR_SUPPORTEDPATTERNS</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/dn932152">KSPROPERTY_SOUNDDETECTOR_SUPPORTEDPATTERNS</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_SOUNDDETECTOR_PATTERNS"></a><a id="ksproperty_sounddetector_patterns"></a><b>KSPROPERTY_SOUNDDETECTOR_PATTERNS</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/dn932151">KSPROPERTY_SOUNDDETECTOR_PATTERNS</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_SOUNDDETECTOR_ARMED"></a><a id="ksproperty_sounddetector_armed"></a><b>KSPROPERTY_SOUNDDETECTOR_ARMED</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/dn932149">KSPROPERTY_SOUNDDETECTOR_ARMED</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_SOUNDDETECTOR_MATCHRESULT"></a><a id="ksproperty_sounddetector_matchresult"></a><b>KSPROPERTY_SOUNDDETECTOR_MATCHRESULT</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/dn932150">KSPROPERTY_SOUNDDETECTOR_MATCHRESULT</a> property.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn932153">KSPROPSETID_SoundDetector</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn932152">KSPROPERTY_SOUNDDETECTOR_SUPPORTEDPATTERNS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn932151">KSPROPERTY_SOUNDDETECTOR_PATTERNS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn932149">KSPROPERTY_SOUNDDETECTOR_ARMED</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn932150">KSPROPERTY_SOUNDDETECTOR_MATCHRESULT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSPROPERTY_SOUNDDETECTOR enumeration%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
