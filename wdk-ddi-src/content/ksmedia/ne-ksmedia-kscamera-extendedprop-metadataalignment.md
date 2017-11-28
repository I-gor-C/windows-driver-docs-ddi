---
UID: NE.ksmedia.KSCAMERA_EXTENDEDPROP_MetadataAlignment
title: KSCAMERA_EXTENDEDPROP_MetadataAlignment
author: windows-driver-content
description: This enumeration contains identifiers for the metadata alignment.
old-location: stream\kscamera_extendedprop_metadataalignment.htm
old-project: stream
ms.assetid: A122F923-D98E-4D73-896A-551A233E7491
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_EXTENDEDPROP_MetadataAlignment
req.alt-loc: Ksmedia.h
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

# KSCAMERA_EXTENDEDPROP_MetadataAlignment enumeration



## -description
<p>This enumeration contains identifiers for the metadata alignment.</p>


## -syntax

````
typedef enum  { 
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_16    = 4,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_32,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_64,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_128,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_256,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_512,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_1024,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_2048,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_4096,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_8192
} KSCAMERA_EXTENDEDPROP_MetadataAlignment;
````


## -enum-fields
<dl>

### -field <a id="KSCAMERA_EXTENDEDPROP_MetadataAlignment_16"></a><a id="kscamera_extendedprop_metadataalignment_16"></a><a id="KSCAMERA_EXTENDEDPROP_METADATAALIGNMENT_16"></a><b>KSCAMERA_EXTENDEDPROP_MetadataAlignment_16</b>

<dd>
<p>This identifies an alignment of 16 bytes.</p>
</dd>

### -field <a id="KSCAMERA_EXTENDEDPROP_MetadataAlignment_32"></a><a id="kscamera_extendedprop_metadataalignment_32"></a><a id="KSCAMERA_EXTENDEDPROP_METADATAALIGNMENT_32"></a><b>KSCAMERA_EXTENDEDPROP_MetadataAlignment_32</b>

<dd>
<p>This identifies an alignment of 32 bytes.</p>
</dd>

### -field <a id="KSCAMERA_EXTENDEDPROP_MetadataAlignment_64"></a><a id="kscamera_extendedprop_metadataalignment_64"></a><a id="KSCAMERA_EXTENDEDPROP_METADATAALIGNMENT_64"></a><b>KSCAMERA_EXTENDEDPROP_MetadataAlignment_64</b>

<dd>
<p>This identifies an alignment of 64 bytes.</p>
</dd>

### -field <a id="KSCAMERA_EXTENDEDPROP_MetadataAlignment_128"></a><a id="kscamera_extendedprop_metadataalignment_128"></a><a id="KSCAMERA_EXTENDEDPROP_METADATAALIGNMENT_128"></a><b>KSCAMERA_EXTENDEDPROP_MetadataAlignment_128</b>

<dd>
<p>This identifies an alignment of 128 bytes.</p>
</dd>

### -field <a id="KSCAMERA_EXTENDEDPROP_MetadataAlignment_256"></a><a id="kscamera_extendedprop_metadataalignment_256"></a><a id="KSCAMERA_EXTENDEDPROP_METADATAALIGNMENT_256"></a><b>KSCAMERA_EXTENDEDPROP_MetadataAlignment_256</b>

<dd>
<p>This identifies an alignment of 256 bytes.</p>
</dd>

### -field <a id="KSCAMERA_EXTENDEDPROP_MetadataAlignment_512"></a><a id="kscamera_extendedprop_metadataalignment_512"></a><a id="KSCAMERA_EXTENDEDPROP_METADATAALIGNMENT_512"></a><b>KSCAMERA_EXTENDEDPROP_MetadataAlignment_512</b>

<dd>
<p>This identifies an alignment of 512 bytes.</p>
</dd>

### -field <a id="KSCAMERA_EXTENDEDPROP_MetadataAlignment_1024"></a><a id="kscamera_extendedprop_metadataalignment_1024"></a><a id="KSCAMERA_EXTENDEDPROP_METADATAALIGNMENT_1024"></a><b>KSCAMERA_EXTENDEDPROP_MetadataAlignment_1024</b>

<dd>
<p>This identifies an alignment of 1024 bytes.</p>
</dd>

### -field <a id="KSCAMERA_EXTENDEDPROP_MetadataAlignment_2048"></a><a id="kscamera_extendedprop_metadataalignment_2048"></a><a id="KSCAMERA_EXTENDEDPROP_METADATAALIGNMENT_2048"></a><b>KSCAMERA_EXTENDEDPROP_MetadataAlignment_2048</b>

<dd>
<p>This identifies an alignment of 2048 bytes.</p>
</dd>

### -field <a id="KSCAMERA_EXTENDEDPROP_MetadataAlignment_4096"></a><a id="kscamera_extendedprop_metadataalignment_4096"></a><a id="KSCAMERA_EXTENDEDPROP_METADATAALIGNMENT_4096"></a><b>KSCAMERA_EXTENDEDPROP_MetadataAlignment_4096</b>

<dd>
<p>This identifies an alignment of 4096 bytes.</p>
</dd>

### -field <a id="KSCAMERA_EXTENDEDPROP_MetadataAlignment_8192"></a><a id="kscamera_extendedprop_metadataalignment_8192"></a><a id="KSCAMERA_EXTENDEDPROP_METADATAALIGNMENT_8192"></a><b>KSCAMERA_EXTENDEDPROP_MetadataAlignment_8192</b>

<dd>
<p>This identifies an alignment of 8192 bytes.</p>
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
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>