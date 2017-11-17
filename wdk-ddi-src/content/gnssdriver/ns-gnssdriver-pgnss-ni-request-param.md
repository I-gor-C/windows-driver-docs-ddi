---
UID: NS.gnssdriver.PGNSS_NI_REQUEST_PARAM
title: PGNSS_NI_REQUEST_PARAM
author: windows-driver-content
description: This structure contains the NI request parameters.
old-location: sensors\gnss_ni_request_param.htm
ms.assetid: 0528EEE6-31D6-4CF6-8192-3557C28B4D10
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: sensors
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_NI_REQUEST_PARAM
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
ms.keywords: PGNSS_NI_REQUEST_PARAM, GNSS_NI_REQUEST_PARAM, *PGNSS_NI_REQUEST_PARAM
req.iface: 
---

# PGNSS_NI_REQUEST_PARAM structure



## -description
<p>This structure contains the NI request parameters.</p>


## -syntax

````
typedef struct {
  ULONG                     Size;
  ULONG                     Version;
  ULONG                     RequestId;
  GNSS_NI_REQUEST_TYPE      RequestType;
  GNSS_NI_NOTIFICATION_TYPE NotificationType;
  GNSS_NI_PLANE_TYPE        RequestPlaneType;
  union {
    GNSS_SUPL_NI_INFO  SuplNiInfo;
    GNSS_CP_NI_INFO    CpNiInfo;
    GNSS_V2UPL_NI_INFO V2UplNiInfo;
  };
  ULONG                     ResponseTimeInSec;
  ULONG                     EmergencyLocation;
} GNSS_NI_REQUEST_PARAM, *PGNSS_NI_REQUEST_PARAM;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Structure size.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Version number.</p>
</dd>

### -field <b>RequestId</b>

<dd>
<p>The ID that uniquely identifies the NI request. It is used later by the NI response to identify the request to respond to.</p>
</dd>

### -field <b>RequestType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn925194">GNSS_NI_REQUEST_TYPE</a> enumeration value that specifies the request type.</p>
</dd>

### -field <b>NotificationType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn925185">GNSS_NI_NOTIFICATION_TYPE</a> enumeration value that specifies the notification type.</p>
</dd>

### -field <b>RequestPlaneType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn925188">GNSS_NI_PLANE_TYPE</a> enumeration value that specifies the plane type.</p>
</dd>

### -field <b>SuplNiInfo</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn925231">GNSS_SUPL_NI_INFO</a> structure that contains the SUPL NI information.</p>
</dd>

### -field <b>CpNiInfo</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn925101">GNSS_CP_NI_INFO</a> structure that contains CP NI information.</p>
</dd>

### -field <b>V2UplNiInfo</b>

<dd>
<p>V2Upl NI request information.</p>
</dd>

### -field <b>ResponseTimeInSec</b>

<dd>
<p>The required response time, in seconds.</p>
</dd>

### -field <b>EmergencyLocation</b>

<dd>
<p>Indicates an emergency request, so an existing NI dialog will be dismissed and the new request will be processed immediately.</p>
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