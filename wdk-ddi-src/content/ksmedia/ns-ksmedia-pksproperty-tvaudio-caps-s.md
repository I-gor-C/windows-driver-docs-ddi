---
UID: NS.ksmedia.PKSPROPERTY_TVAUDIO_CAPS_S
title: PKSPROPERTY_TVAUDIO_CAPS_S
author: windows-driver-content
description: The KSPROPERTY_TVAUDIO_CAPS_S structure describes the capability of a TV audio device, such as stereo versus mono audio support and language capabilities.
old-location: stream\ksproperty_tvaudio_caps_s.htm
old-project: stream
ms.assetid: 991208ee-d245-41d1-a5e6-0e79368e37a8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_TVAUDIO_CAPS_S, KSPROPERTY_TVAUDIO_CAPS_S, *PKSPROPERTY_TVAUDIO_CAPS_S
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_TVAUDIO_CAPS_S
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

# PKSPROPERTY_TVAUDIO_CAPS_S structure



## -description
<p>The KSPROPERTY_TVAUDIO_CAPS_S structure describes the capability of a TV audio device, such as stereo versus mono audio support and language capabilities.</p>


## -syntax

````
typedef struct {
  KSPROPERTY   Property;
  ULONG        Capabilities;
  KSPIN_MEDIUM InputMedium;
  KSPIN_MEDIUM OutputMedium;
} KSPROPERTY_TVAUDIO_CAPS_S, *PKSPROPERTY_TVAUDIO_CAPS_S;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>Specifies an initialized <a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a> structure that describes the property set, property ID, and request type.</p>
</dd>

### -field <b>Capabilities</b>

<dd>
<p>Specifies the capabilities of the TV audio device. The minidriver returns the capabilities of the TV audio device by setting this member to one or more (logically ORed) values that are defined in <i>ksmedia.h</i>:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KS_TVAUDIO_MODE_MONO</p>
</td>
<td>
<p>Indicates the device supports mono audio.</p>
</td>
</tr>
<tr>
<td>
<p>KS_TVAUDIO_MODE_STEREO</p>
</td>
<td>
<p>Indicates the device supports stereo audio.</p>
</td>
</tr>
<tr>
<td>
<p>KS_TVAUDIO_MODE_LANG_A</p>
</td>
<td>
<p>Indicates the device supports a primary (default) language.</p>
</td>
</tr>
<tr>
<td>
<p>KS_TVAUDIO_MODE_LANG_B</p>
</td>
<td>
<p>Indicates the device supports a second language.</p>
</td>
</tr>
<tr>
<td>
<p>KS_TVAUDIO_MODE_LANG_C</p>
</td>
<td>
<p>Indicates the device supports a third language.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>InputMedium</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>OutputMedium</b>

<dd>
<p>Reserved for system use.</p>
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
<a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567811">PROPSETID_VIDCAP_TVAUDIO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565933">KSPROPERTY_TVAUDIO_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_TVAUDIO_CAPS_S structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
