---
UID: NS.ksmedia.PKSPROPERTY_TUNER_IF_MEDIUM_S
title: PKSPROPERTY_TUNER_IF_MEDIUM_S
author: windows-driver-content
description: The KSPROPERTY_TUNER_IF_MEDIUM_S structure returns the Medium GUID for the pin that is capable of supporting tuning to an intermediate frequency.
old-location: stream\ksproperty_tuner_if_medium_s.htm
old-project: stream
ms.assetid: 19f79b01-1a3c-4695-96ec-2f7410f6b4aa
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_TUNER_IF_MEDIUM_S, KSPROPERTY_TUNER_IF_MEDIUM_S, *PKSPROPERTY_TUNER_IF_MEDIUM_S
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
req.alt-api: KSPROPERTY_TUNER_IF_MEDIUM_S
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

# PKSPROPERTY_TUNER_IF_MEDIUM_S structure



## -description
<p>The KSPROPERTY_TUNER_IF_MEDIUM_S structure returns the Medium GUID for the pin that is capable of supporting tuning to an intermediate frequency.</p>


## -syntax

````
typedef struct {
  KSPROPERTY   Property;
  KSPIN_MEDIUM IFMedium;
} KSPROPERTY_TUNER_IF_MEDIUM_S, *PKSPROPERTY_TUNER_IF_MEDIUM_S;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>Specifies an initialized <a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a> structure that describes the property set, property ID, and request type.</p>
</dd>

### -field <b>IFMedium</b>

<dd>
<p>Specifies the GUID for the pin that is capable of supporting an intermediate frequency. If no pin supports an intermediate frequency, the minidriver should return GUID_NULL. </p>
</dd>
</dl>

## -remarks
<p>Support for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565842">KSPROPERTY_TUNER_IF_MEDIUM</a> property causes <i>Kstvtune.ax</i> to create an additional pin representing an MPEG-2 transport stream. A data packet sent on this pin in user mode consists only of a <a href="stream.ks_tvtuner_change_info">KS_TVTUNER_CHANGE_INFO</a> structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567800">PROPSETID_TUNER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565842">KSPROPERTY_TUNER_IF_MEDIUM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_TUNER_IF_MEDIUM_S structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
