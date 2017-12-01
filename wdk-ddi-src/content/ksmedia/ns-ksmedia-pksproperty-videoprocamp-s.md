---
UID: NS.ksmedia.PKSPROPERTY_VIDEOPROCAMP_S
title: PKSPROPERTY_VIDEOPROCAMP_S
author: windows-driver-content
description: The KSPROPERTY_VIDEOPROCAMP_S structure describes filter-based property settings in the PROPSETID_VIDCAP_VIDEOPROCAMP property set.
old-location: stream\ksproperty_videoprocamp_s.htm
old-project: stream
ms.assetid: e8b9c381-2159-4cb2-92e2-11c1d3698f2d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_VIDEOPROCAMP_S, KSPROPERTY_VIDEOPROCAMP_S, *PKSPROPERTY_VIDEOPROCAMP_S
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
req.alt-api: KSPROPERTY_VIDEOPROCAMP_S
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

# PKSPROPERTY_VIDEOPROCAMP_S structure



## -description
<p>The KSPROPERTY_VIDEOPROCAMP_S structure describes filter-based property settings in the PROPSETID_VIDCAP_VIDEOPROCAMP property set.</p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  LONG       Value;
  ULONG      Flags;
  ULONG      Capabilities;
} KSPROPERTY_VIDEOPROCAMP_S, *PKSPROPERTY_VIDEOPROCAMP_S;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>Specifies an initialized <a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a> structure that describes the property set, property ID, and request type.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>Specifies the value of a request. For Set requests, the minidriver should set the property specified in <b>Property</b> to this value. For Get requests, the minidriver should return the value of the property specified in <b>Property</b>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Specifies the flags of a request. For Set requests, this value indicates the desired setting. For Get requests, this value contains the current setting. This member can be set to one of the values that are defined in <i>ksmedia.h</i>:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KSPROPERTY_VIDEOPROCAMP_FLAGS_MANUAL</p>
</td>
<td>
<p>Indicates that the property is to be adjusted manually.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_VIDEOPROCAMP_FLAGS_AUTO</p>
</td>
<td>
<p>Indicates that the property is to be adjusted automatically.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Capabilities</b>

<dd>
<p>Specifies the capabilities of a property. This member has meaning only for Get requests. The minidriver should return the capabilities of the VideoProcAmp with respect to the property specified in <b>Property</b>. This member should be set to one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KSPROPERTY_VIDEOPROCAMP_FLAGS_MANUAL</p>
</td>
<td>
<p>The device supports manual setting of the specified property.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_VIDEOPROCAMP_FLAGS_AUTO</p>
</td>
<td>
<p>The device supports automatic setting of the specified property.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568122">PROPSETID_VIDCAP_VIDEOPROCAMP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566063">KSPROPERTY_VIDEOPROCAMP_BACKLIGHT_COMPENSATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566065">KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566066">KSPROPERTY_VIDEOPROCAMP_COLORENABLE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566070">KSPROPERTY_VIDEOPROCAMP_CONTRAST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566076">KSPROPERTY_VIDEOPROCAMP_GAMMA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566078">KSPROPERTY_VIDEOPROCAMP_HUE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566092">KSPROPERTY_VIDEOPROCAMP_SATURATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566093">KSPROPERTY_VIDEOPROCAMP_SHARPNESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566095">KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_VIDEOPROCAMP_S structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
