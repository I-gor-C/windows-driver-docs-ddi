---
UID: NS.ksmedia.PKSPROPERTY_TUNER_MODE_CAPS_S
title: PKSPROPERTY_TUNER_MODE_CAPS_S
author: windows-driver-content
description: The KS_PROPERTY_TUNER_MODE_CAPS_S structure describes the capabilities of TV and radio tuner devices.
old-location: stream\ksproperty_tuner_mode_caps_s.htm
ms.assetid: e2376cde-7e13-475d-a118-0cf48ba8a742
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_TUNER_MODE_CAPS_S
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
ms.keywords: PKSPROPERTY_TUNER_MODE_CAPS_S, KSPROPERTY_TUNER_MODE_CAPS_S, *PKSPROPERTY_TUNER_MODE_CAPS_S
req.iface: 
---

# PKSPROPERTY_TUNER_MODE_CAPS_S structure



## -description
<p>The KS_PROPERTY_TUNER_MODE_CAPS_S structure describes the capabilities of TV and radio tuner devices.</p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  ULONG      Mode;
  ULONG      StandardsSupported;
  ULONG      MinFrequency;
  ULONG      MaxFrequency;
  ULONG      TuningGranularity;
  ULONG      NumberOfInputs;
  ULONG      SettlingTime;
  ULONG      Strategy;
} KSPROPERTY_TUNER_MODE_CAPS_S, *PKSPROPERTY_TUNER_MODE_CAPS_S;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>Specifies an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> structure that describes the property set, property ID, and request type.</p>
</dd>

### -field <b>Mode</b>

<dd>
<p>Specifies the tuner mode that the caller is requesting capability information about. It can be one of the following tuner modes from the KSPROPERTY_TUNER_MODES enumeration that is defined in <i>ksmedia.h</i>:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KSPROPERTY_TUNER_MODE_TV</p>
</td>
<td>
<p>Indicates that the tuner is capable of tuning analog broadcast or cable television channels.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_TUNER_MODE_FM_RADIO</p>
</td>
<td>
<p>Indicates that the tuner is capable of tuning FM radio channels.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_TUNER_MODE_AM_RADIO</p>
</td>
<td>
<p>Indicates that the tuner is capable of tuning AM radio channels.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_TUNER_MODE_DSS</p>
</td>
<td>
<p>Indicates that the tuner is capable of tuning DSS channels.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_TUNER_MODE_ATSC</p>
</td>
<td>
<p>Indicates that the tuner is capable of tuning Advanced Television Systems Committee broadcasts (Digital TV for the United States) or other digital television standard.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>StandardsSupported</b>

<dd>
<p>Describes the analog video standards supported. If <b>Mode</b> is set to KSPROPERTY_TUNER_MODE_TV, this member may be set to one or more (logically ORed) values from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567297">KS_AnalogVideoStandard</a> enumeration.</p>
</dd>

### -field <b>MinFrequency</b>

<dd>
<p>Specifies the lowest frequency supported by the tuner. This value is in hertz (Hz).</p>
</dd>

### -field <b>MaxFrequency</b>

<dd>
<p>Specifies the highest frequency supported by the tuner. This value is in hertz (Hz).</p>
</dd>

### -field <b>TuningGranularity</b>

<dd>
<p>Specifies the smallest possible step size between two settings of the tuning frequency. This value is in hertz (Hz).</p>
</dd>

### -field <b>NumberOfInputs</b>

<dd>
<p>Specifies the number of inputs on the tuner.</p>
</dd>

### -field <b>SettlingTime</b>

<dd>
<p>Specifies the time, in milliseconds, for a new frequency setting to become stable.</p>
</dd>

### -field <b>Strategy</b>

<dd>
<p>Specifies the tuning method. This member must be set to only one of the values from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567687">KS_TUNER_STRATEGY</a> enumeration.</p>
</dd>
</dl>

## -remarks
<p>The minidriver fills in the mode capabilities for the requested tuner mode.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567297">KS_AnalogVideoStandard</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567687">KS_TUNER_STRATEGY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567800">PROPSETID_TUNER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565865">KSPROPERTY_TUNER_MODE_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_TUNER_MODE_CAPS_S structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
