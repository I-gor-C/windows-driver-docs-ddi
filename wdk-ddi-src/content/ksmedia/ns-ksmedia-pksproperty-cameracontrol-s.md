---
UID: NS.ksmedia.PKSPROPERTY_CAMERACONTROL_S
title: PKSPROPERTY_CAMERACONTROL_S
author: windows-driver-content
description: The KSPROPERTY_CAMERACONTROL_S structure describes filter-based properties in the PROPSETID_VIDCAP_CAMERACONTROL property set.
old-location: stream\ksproperty_cameracontrol_s.htm
old-project: stream
ms.assetid: 203c6452-26d4-4dbf-89d4-c7e6d47e7c16
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_CAMERACONTROL_S, KSPROPERTY_CAMERACONTROL_S, *PKSPROPERTY_CAMERACONTROL_S
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
req.alt-api: KSPROPERTY_CAMERACONTROL_S
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

# PKSPROPERTY_CAMERACONTROL_S structure



## -description
<p>The KSPROPERTY_CAMERACONTROL_S structure describes filter-based properties in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567802">PROPSETID_VIDCAP_CAMERACONTROL</a> property set.</p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  LONG       Value;
  ULONG      Flags;
  ULONG      Capabilities;
} KSPROPERTY_CAMERACONTROL_S, *PKSPROPERTY_CAMERACONTROL_S;
````


## -struct-fields
<dl>

### -field Property

<dd>
<p>Specifies an initialized <a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a> structure that describes the property set, property ID, and request type. </p>
</dd>

### -field Value

<dd>
<p>Specifies the value of the property. This member is read/write.</p>
</dd>

### -field Flags

<dd>
<p>Indicates, for Get requests, the current setting for the specified property from the values listed below. Indicates, for Set requests, the desired setting for the specified property from the values listed below. This member can be set to one of the following values that are defined in <i>ksmedia.h</i>:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_MANUAL</p>
</td>
<td>
<p>Indicates that the setting is controlled manually.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_AUTO</p>
</td>
<td>
<p>Indicates that the setting is controlled automatically.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_ABSOLUTE</p>
</td>
<td>
<p>Indicates that the setting is in absolute values.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_RELATIVE</p>
</td>
<td>
<p>Indicates that the setting is in relative values.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Capabilities

<dd>
<p>Indicates the minidriver's camera control capabilities for the specified property. This member is read-only. This member can be set to one of the following values that are defined in <i>ksmedia.h</i>:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_MANUAL</p>
</td>
<td>
<p>Indicates that the device can be controlled manually.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_AUTO</p>
</td>
<td>
<p>Indicates that the device can be controlled automatically.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_ABSOLUTE</p>
</td>
<td>
<p>Indicates that the device settings are in absolute values.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_RELATIVE</p>
</td>
<td>
<p>Indicates that the device settings are in relative values.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567802">PROPSETID_VIDCAP_CAMERACONTROL</a>
</dt>
<dt>
<a href="stream.ksproperty_cameracontrol_node_s">KSPROPERTY_CAMERACONTROL_NODE_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_CAMERACONTROL_S structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
