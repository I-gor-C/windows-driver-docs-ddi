---
UID: NE.gnssdriver.GNSS_NI_REQUEST_TYPE
title: GNSS_NI_REQUEST_TYPE
author: windows-driver-content
description: This enumeration indicates the network initiated (NI) request type represented by the GNSS_NI_REQUEST_PARAM structure.
old-location: sensors\gnss_ni_request_type.htm
old-project: sensors
ms.assetid: 79AFC7D8-5A51-49CC-8ADA-7D21C6859254
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_, FWPS_VSWITCH_EVENT_DISPATCH_TABLE0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_NI_REQUEST_TYPE
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
req.iface: 
---

# GNSS_NI_REQUEST_TYPE enumeration



## -description
<p>This enumeration indicates the network initiated (NI) request type represented by the <a href="https://msdn.microsoft.com/library/windows/hardware/dn925191">GNSS_NI_REQUEST_PARAM</a> structure.</p>


## -syntax

````
typedef enum  { 
  GNSS_NI_Request_SingleShot   = 0x01,
  GNSS_NI_Request_AreaTrigger  = 0x02
} GNSS_NI_REQUEST_TYPE;
````


## -enum-fields
<dl>

### -field <a id="GNSS_NI_Request_SingleShot"></a><a id="gnss_ni_request_singleshot"></a><a id="GNSS_NI_REQUEST_SINGLESHOT"></a><b>GNSS_NI_Request_SingleShot</b>

<dd>
<p>Indicates the request type is single shot.</p>
</dd>

### -field <a id="GNSS_NI_Request_AreaTrigger"></a><a id="gnss_ni_request_areatrigger"></a><a id="GNSS_NI_REQUEST_AREATRIGGER"></a><b>GNSS_NI_Request_AreaTrigger</b>

<dd>
<p>Indicates the request type is tracking.</p>
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