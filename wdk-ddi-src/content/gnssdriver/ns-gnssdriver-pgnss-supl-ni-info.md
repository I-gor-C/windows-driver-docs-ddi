---
UID: NS.gnssdriver.PGNSS_SUPL_NI_INFO
title: PGNSS_SUPL_NI_INFO
author: windows-driver-content
description: This structure contains the requested SUPL NI information.
old-location: sensors\gnss_supl_ni_info.htm
old-project: sensors
ms.assetid: 78D19A0C-E247-4DDA-A689-494B5A61A673
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: PGNSS_SUPL_NI_INFO, GNSS_SUPL_NI_INFO, *PGNSS_SUPL_NI_INFO
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
req.alt-api: GNSS_SUPL_NI_INFO
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

# PGNSS_SUPL_NI_INFO structure



## -description
<p>This structure contains the requested SUPL NI information.</p>


## -syntax

````
typedef struct {
  ULONG Size;
  ULONG Version;
  WCHAR RequestorId[MAX_PATH];
  WCHAR ClientName[MAX_PATH];
  CHAR  SuplNiUrl[MAX_SERVER_URL_NAME];
} GNSS_SUPL_NI_INFO, *PGNSS_SUPL_NI_INFO;
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

### -field <b>RequestorId[MAX_PATH]</b>

<dd>
<p>Requestor ID.</p>
<p>This will be displayed on the notification dialog to the user. The GNSS driver must provide a UNICODE string that is decoded per the encoding scheme required by the mobile operator.</p>
</dd>

### -field <b>ClientName[MAX_PATH]</b>

<dd>
<p>Name of the client that requests the location of the device.</p>
<p>This will be displayed on the notification dialog to the user. The GNSS driver must provide a UNICODE string that is decoded per the encoding scheme required by the mobile operator.</p>
</dd>

### -field <b>SuplNiUrl[MAX_SERVER_URL_NAME]</b>

<dd>
<p>NI URL information.</p>
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