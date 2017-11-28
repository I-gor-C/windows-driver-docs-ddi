---
UID: NS.gnssdriver.PGNSS_NI_RESPONSE
title: PGNSS_NI_RESPONSE
author: windows-driver-content
description: This structure contains NI request response information.
old-location: sensors\gnss_ni_response.htm
old-project: sensors
ms.assetid: D2F7C90E-BAF4-419D-94CF-5FC39E7B6A58
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: PGNSS_NI_RESPONSE, GNSS_NI_RESPONSE, *PGNSS_NI_RESPONSE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_NI_RESPONSE
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
req.irql: 
req.iface: 
---

# PGNSS_NI_RESPONSE structure



## -description
<p>This structure contains NI request response information.</p>


## -syntax

````
typedef struct {
  ULONG                 Size;
  ULONG                 Version;
  ULONG                 RequestId;
  GNSS_NI_USER_RESPONSE UserResponse;
} GNSS_NI_RESPONSE, *PGNSS_NI_RESPONSE;
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
<p>The ID to uniquely identify the NI request.</p>
</dd>

### -field <b>UserResponse</b>

<dd>
<p>The user response to the NI request.</p>
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