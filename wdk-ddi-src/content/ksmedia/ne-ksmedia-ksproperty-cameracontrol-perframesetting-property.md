---
UID: NE.ksmedia.KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_PROPERTY
title: KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_PROPERTY
author: windows-driver-content
description: This enumeration contains the property IDs defined for the per-frame property set.
old-location: stream\ksproperty_cameracontrol_perframesetting_property.htm
old-project: stream
ms.assetid: 59328DD6-3E7B-43C3-A1FF-E02DC24228BA
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_PROPERTY
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

# KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_PROPERTY enumeration



## -description
<p>This enumeration contains the property IDs defined for the per-frame property set.</p>


## -syntax

````
typedef enum  { 
  KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CAPABILITY  = 0,
  KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_SET,
  KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CLEAR
} KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_PROPERTY;
````


## -enum-fields
<dl>

### -field <a id="KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CAPABILITY"></a><a id="ksproperty_cameracontrol_perframesetting_capability"></a><b>KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CAPABILITY</b>

<dd>
<p>This is used to query the driver’s per-frame settings capabilities.</p>
</dd>

### -field <a id="KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_SET"></a><a id="ksproperty_cameracontrol_perframesetting_set"></a><b>KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_SET</b>

<dd>
<p>This is used to configure the per-frame settings.</p>
</dd>

### -field <a id="KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CLEAR"></a><a id="ksproperty_cameracontrol_perframesetting_clear"></a><b>KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CLEAR</b>

<dd>
<p>This is used to clear the per-frame settings previously configured.</p>
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