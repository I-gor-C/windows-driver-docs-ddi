---
UID: NS.ksmedia.PKSPROPERTY_TVAUDIO_S
title: PKSPROPERTY_TVAUDIO_S
author: windows-driver-content
description: The KSPROPERTY_TVAUDIO_S structure describes the current TV audio mode, such as stereo or mono audio and language settings.
old-location: stream\ksproperty_tvaudio_s.htm
old-project: stream
ms.assetid: a2e26798-322a-4057-8c29-3429711e36a4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_TVAUDIO_S, KSPROPERTY_TVAUDIO_S, *PKSPROPERTY_TVAUDIO_S
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
req.alt-api: KSPROPERTY_TVAUDIO_S
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

# PKSPROPERTY_TVAUDIO_S structure



## -description
<p>The KSPROPERTY_TVAUDIO_S structure describes the current TV audio mode, such as stereo or mono audio and language settings.</p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  ULONG      Mode;
} KSPROPERTY_TVAUDIO_S, *PKSPROPERTY_TVAUDIO_S;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>Specifies an initialized <a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a> structure that describes the property set, property ID, and request type.</p>
</dd>

### -field <b>Mode</b>

<dd>
<p>Specifies the mode of the TV audio device. For Get requests, the minidriver returns the current mode of the TV audio device. For Set requests, the minidriver sets the current mode of the TV audio device to the specified value. This member can be one or more (logically ORed) of the following values:</p>
<table>
<tr>
<th>Mode</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KS_TVAUDIO_MODE_MONO</p>
</td>
<td>
<p>Indicates that the audio is in mono.</p>
</td>
</tr>
<tr>
<td>
<p>KS_TVAUDIO_MODE_STEREO</p>
</td>
<td>
<p>Indicates that the audio is in stereo.</p>
</td>
</tr>
<tr>
<td>
<p>KS_TVAUDIO_MODE_LANG_A</p>
</td>
<td>
<p>Indicates that the audio is in the primary language.</p>
</td>
</tr>
<tr>
<td>
<p>KS_TVAUDIO_MODE_LANG_B</p>
</td>
<td>
<p>Indicates that the audio is in the second language supported by the device.</p>
</td>
</tr>
<tr>
<td>
<p>KS_TVAUDIO_MODE_LANG_C</p>
</td>
<td>
<p>Indicates that the audio is in the third language supported by the device.</p>
</td>
</tr>
</table>
<p> </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565944">KSPROPERTY_TVAUDIO_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_TVAUDIO_S structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
