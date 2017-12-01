---
UID: NS.ksmedia.PKSPROPERTY_VIDEOPROCAMP_NODE_S2
title: PKSPROPERTY_VIDEOPROCAMP_NODE_S2
author: windows-driver-content
description: The KSPROPERTY_VIDEOPROCAMP_NODE_S2 structure describes node-based property settings in the PROPSETID_VIDCAP_VIDEOPROCAMP property set that use two values at the same time.
old-location: stream\ksproperty_videoprocamp_node_s2.htm
old-project: stream
ms.assetid: 767ea5d2-4c11-4ba8-bb1f-c5f6038244f5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_VIDEOPROCAMP_NODE_S2, KSPROPERTY_VIDEOPROCAMP_NODE_S2, *PKSPROPERTY_VIDEOPROCAMP_NODE_S2
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
req.alt-api: KSPROPERTY_VIDEOPROCAMP_NODE_S2
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

# PKSPROPERTY_VIDEOPROCAMP_NODE_S2 structure



## -description
<p>The KSPROPERTY_VIDEOPROCAMP_NODE_S2 structure describes node-based property settings in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568122">PROPSETID_VIDCAP_VIDEOPROCAMP</a> property set that use two values at the same time.</p>


## -syntax

````
typedef struct {
  KSP_NODE NodeProperty;
  LONG     Value1;
  ULONG    Flags;
  ULONG    Capabilities;
  LONG     Value2;
} KSPROPERTY_VIDEOPROCAMP_NODE_S2, *PKSPROPERTY_VIDEOPROCAMP_NODE_S2;
````


## -struct-fields
<dl>

### -field <b>NodeProperty</b>

<dd>
<p>Specifies an initialized <a href="stream.ksp_node">KSP_NODE</a> structure that describes the node, property set, property ID, and request type.</p>
</dd>

### -field <b>Value1</b>

<dd>
<p>Specifies the first value of a request. For set requests, the minidriver should set the property specified in <b>Property</b> to this value. For get requests, the minidriver should return the value of the property specified in <b>Property</b>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Specifies the flags of a request. For set requests, this value indicates the desired setting. For get requests, this value contains the current setting. This member can be set to one of the values that are defined in <i>ksmedia.h</i>:</p>
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
<p>Indicates that the property is to be adjusted manually</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_VIDEOPROCAMP_FLAGS_AUTO</p>
</td>
<td>
<p>Indicates that the property is to be adjusted automatically</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Capabilities</b>

<dd>
<p>Specifies the capabilities of a property. This member has meaning only for get requests. The minidriver should return the capabilities of the video processing amplifier with respect to the property specified in <b>Property</b>. This member should be set to one of the following values:</p>
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
<p>The device supports manual setting of the specified property</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_VIDEOPROCAMP_FLAGS_AUTO</p>
</td>
<td>
<p>The device supports automatic setting of the specified property</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Value2</b>

<dd>
<p>Specifies the second value of a request. For set requests, the minidriver should set the property specified in <b>Property</b> to this value. For get requests, the minidriver should return the value of the property specified in <b>Property</b>.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by <a href="https://msdn.microsoft.com/library/windows/hardware/ff566097">KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE_COMPONENT</a>.</p>

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