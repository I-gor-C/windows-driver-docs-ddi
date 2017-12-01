---
UID: NE.portcls.eChannelTargetType
title: eChannelTargetType
author: windows-driver-content
description: The eChannelTargetType enumeration defines constants that specify a type of node (target) in a given channel.
old-location: audio\echanneltargettype.htm
old-project: audio
ms.assetid: 44C5BE49-E8D5-4E6C-BDC5-494F180D580A
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BarcodeSymbologyAttributesData, BarcodeSymbologyAttributesData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: eChannelTargetType
req.alt-loc: Portcls.h
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

# eChannelTargetType enumeration



## -description
<p>The <b>eChannelTargetType</b> enumeration defines constants that specify a type of node (target) in a given channel.</p>


## -syntax

````
typedef enum _eChannelTargetType { 
  eVolumeAttribute,
  eMuteAttribute,
  ePeakMeterAttribute
} eChannelTargetType;
````


## -enum-fields
<dl>

### -field <a id="eVolumeAttribute"></a><a id="evolumeattribute"></a><a id="EVOLUMEATTRIBUTE"></a><b>eVolumeAttribute</b>

<dd>
<p>Indicates a volume level control node.</p>
</dd>

### -field <a id="eMuteAttribute"></a><a id="emuteattribute"></a><a id="EMUTEATTRIBUTE"></a><b>eMuteAttribute</b>

<dd>
<p>Indicates a Mute node.</p>
</dd>

### -field <a id="ePeakMeterAttribute"></a><a id="epeakmeterattribute"></a><a id="EPEAKMETERATTRIBUTE"></a><b>ePeakMeterAttribute</b>

<dd>
<p>Indicates a PeakMeter node.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>