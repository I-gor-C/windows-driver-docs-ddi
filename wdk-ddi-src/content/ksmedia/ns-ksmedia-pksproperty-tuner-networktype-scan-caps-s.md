---
UID: NS.ksmedia.PKSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S
title: PKSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S
author: windows-driver-content
description: The KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S structure describes the scanning capabilities of a broadcast network type that a tuning device supports.
old-location: stream\ksproperty_tuner_networktype_scan_caps_s.htm
old-project: stream
ms.assetid: e6fe9278-d34e-4fba-80f9-84d6ededbfc1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S, KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S, *PKSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S
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

# PKSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S structure



## -description
<p>The KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S structure describes the scanning capabilities of a broadcast network type that a tuning device supports.</p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  GUID       NetworkType;
  ULONG      BufferSize;
  PVOID      NetworkTunerCapabilities;
} KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S, *PKSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>Specifies an initialized <a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a> structure that describes the property set, property ID, and request type.</p>
</dd>

### -field <b>NetworkType</b>

<dd>
<p>A GUID for the broadcast network type for which the tuner filter receives capabilities. The driver returned this GUID as an element in the array that the <b>GUIDBucket</b> member of the <a href="stream.ksproperty_tuner_scan_caps_s">KSPROPERTY_TUNER_SCAN_CAPS_S</a> structure specifies in a call to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff565887">KSPROPERTY_TUNER_SCAN_CAPS</a> property. </p>
</dd>

### -field <b>BufferSize</b>

<dd>
<p>The size, in bytes, of the buffer that is required to hold the network capabilities and that the <b>NetworkTunerCapabilities</b> member points to. </p>
</dd>

### -field <b>NetworkTunerCapabilities</b>

<dd>
<p>A pointer to a buffer to hold the scanning capabilities of a broadcast network type. For example, if the ANALOG_TV_NETWORK_TYPE GUID is set in the <b>NetworkType</b> member, the driver fills the buffer with a populated <a href="stream.tuner_analog_caps_s">TUNER_ANALOG_CAPS_S</a> structure. </p>
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
<p>Available in Windows Vista and later versions of the operating system.</p>
</td>
</tr>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565881">KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565887">KSPROPERTY_TUNER_SCAN_CAPS</a>
</dt>
<dt>
<a href="stream.ksproperty_tuner_scan_caps_s">KSPROPERTY_TUNER_SCAN_CAPS_S</a>
</dt>
<dt>
<a href="stream.tuner_analog_caps_s">TUNER_ANALOG_CAPS_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
