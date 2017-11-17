---
UID: NE.gnssdriver.GNSS_NI_PLANE_TYPE
title: GNSS_NI_PLANE_TYPE
author: windows-driver-content
description: This enumeration indicates the plane type of a network initiated (NI) request represented by the GNSS_NI_REQUEST_PARAM structure.
old-location: sensors\gnss_ni_plane_type.htm
ms.assetid: F06FFABA-D7AB-4301-9F73-CE4BBB0B8AA6
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: sensors
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_NI_PLANE_TYPE
req.alt-loc: gnssdriver.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_, FWPS_VSWITCH_EVENT_DISPATCH_TABLE0
req.iface: 
---

# GNSS_NI_PLANE_TYPE enumeration



## -description
<p>This enumeration indicates the plane type of a network initiated (NI) request represented by the <a href="https://msdn.microsoft.com/library/windows/hardware/dn925191">GNSS_NI_REQUEST_PARAM</a> structure.</p>


## -syntax

````
typedef enum  { 
  GNSS_NI_SUPL   = 0x01,
  GNSS_NI_CP     = 0x02,
  GNSS_NI_V2UPL  = 0x03
} GNSS_NI_PLANE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="GNSS_NI_SUPL"></a><a id="gnss_ni_supl"></a><b>GNSS_NI_SUPL</b>

<dd>
<p>Indicates the plane type of the request is SUPL.</p>
</dd>

### -field <a id="GNSS_NI_CP"></a><a id="gnss_ni_cp"></a><b>GNSS_NI_CP</b>

<dd>
<p>Indicates the plane type of the request is CP.</p>
</dd>

### -field <a id="GNSS_NI_V2UPL"></a><a id="gnss_ni_v2upl"></a><b>GNSS_NI_V2UPL</b>

<dd>
<p>Indicates plane type of the request is V2UPL.</p>
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
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>