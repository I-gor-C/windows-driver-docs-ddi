---
UID: NS.ksmedia.PKSPROPERTY_CAMERACONTROL_NODE_S
title: PKSPROPERTY_CAMERACONTROL_NODE_S
author: windows-driver-content
description: The KSPROPERTY_CAMERACONTROL_NODE_S structure describes node-based properties in the PROPSETID_VIDCAP_CAMERACONTROL property set. This structure specifies property values in requests to the USB Video Class driver.
old-location: stream\ksproperty_cameracontrol_node_s.htm
old-project: stream
ms.assetid: ced1d848-fb6e-4207-bdb0-29ca82249d06
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSPROPERTY_CAMERACONTROL_NODE_S, KSPROPERTY_CAMERACONTROL_NODE_S, PKSPROPERTY_CAMERACONTROL_NODE_S
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
req.alt-api: KSPROPERTY_CAMERACONTROL_NODE_S
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

# PKSPROPERTY_CAMERACONTROL_NODE_S structure



## -description
<p>The KSPROPERTY_CAMERACONTROL_NODE_S structure describes node-based properties in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567802">PROPSETID_VIDCAP_CAMERACONTROL</a> property set. This structure specifies property values in requests to the USB Video Class driver.</p>


## -syntax

````
typedef struct {
  KSP_NODE NodeProperty;
  LONG     Value;
  ULONG    Flags;
  ULONG    Capabilities;
} KSPROPERTY_CAMERACONTROL_NODE_S, *PKSPROPERTY_CAMERACONTROL_NODE_S;
````


## -struct-fields
<dl>

### -field <b>NodeProperty</b>

<dd>
<p>Specifies an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff566720">KSP_NODE</a> structure that describes the property set, property ID, request type, and node ID. </p>
</dd>

### -field <b>Value</b>

<dd>
<p>Specifies the value of the property. This member is read/write.</p>
</dd>

### -field <b>Flags</b>

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

### -field <b>Capabilities</b>

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
<p>See related information about the <a href="NULL">USB Video Class Driver</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567802">PROPSETID_VIDCAP_CAMERACONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564439">KSPROPERTY_CAMERACONTROL_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_CAMERACONTROL_NODE_S structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
