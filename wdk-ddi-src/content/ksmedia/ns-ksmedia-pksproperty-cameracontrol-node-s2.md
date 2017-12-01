---
UID: NS.ksmedia.PKSPROPERTY_CAMERACONTROL_NODE_S2
title: PKSPROPERTY_CAMERACONTROL_NODE_S2
author: windows-driver-content
description: The KSPROPERTY_CAMERACONTROL_NODE_S2 structure describes node-based properties in the PROPSETID_VIDCAP_CAMERACONTROL property set that use two values at the same time. This structure specifies property values in requests to the USB video class driver.
old-location: stream\ksproperty_cameracontrol_node_s2.htm
old-project: stream
ms.assetid: 0d3ed82e-3565-4b0b-bca9-1d0b91732d18
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_CAMERACONTROL_NODE_S2, KSPROPERTY_CAMERACONTROL_NODE_S2, *PKSPROPERTY_CAMERACONTROL_NODE_S2
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
req.alt-api: KSPROPERTY_CAMERACONTROL_NODE_S2
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

# PKSPROPERTY_CAMERACONTROL_NODE_S2 structure



## -description
<p>The KSPROPERTY_CAMERACONTROL_NODE_S2 structure describes node-based properties in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567802">PROPSETID_VIDCAP_CAMERACONTROL</a> property set that use two values at the same time. This structure specifies property values in requests to the USB video class driver.</p>


## -syntax

````
typedef struct {
  KSP_NODE NodeProperty;
  LONG     Value1;
  ULONG    Flags;
  ULONG    Capabilities;
  LONG     Value2;
} KSPROPERTY_CAMERACONTROL_NODE_S2, *PKSPROPERTY_CAMERACONTROL_NODE_S2;
````


## -struct-fields
<dl>

### -field <b>NodeProperty</b>

<dd>
<p>Specifies an initialized <a href="stream.ksp_node">KSP_NODE</a> structure that describes the property set, property ID, request type, and node ID. </p>
</dd>

### -field <b>Value1</b>

<dd>
<p>Specifies the first value of the property. This member is read/write.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Indicates, for get requests, the current setting for the specified property from the values listed below. Indicates, for set requests, the desired setting for the specified property from the values listed below. This member can be set to one of the following values that are defined in <i>ksmedia.h</i>:</p>
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
<p>Indicates that the setting is controlled manually</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_AUTO</p>
</td>
<td>
<p>Indicates that the setting is controlled automatically</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_ABSOLUTE</p>
</td>
<td>
<p>Indicates that the setting is in absolute values</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_RELATIVE</p>
</td>
<td>
<p>Indicates that the setting is in relative values</p>
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
<p>Indicates that the device can be controlled manually</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_AUTO</p>
</td>
<td>
<p>Indicates that the device can be controlled automatically</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_ABSOLUTE</p>
</td>
<td>
<p>Indicates that the device settings are in absolute values</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_CAMERACONTROL_FLAGS_RELATIVE</p>
</td>
<td>
<p>Indicates that the device settings are in relative values</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Value2</b>

<dd>
<p>Specifies the second value of the property. This member is read/write.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by <a href="https://msdn.microsoft.com/library/windows/hardware/ff564425">KSPROPERTY_CAMERACONTROL_PANTILT</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff564427">KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE</a> for node-based get/set property requests.</p>

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