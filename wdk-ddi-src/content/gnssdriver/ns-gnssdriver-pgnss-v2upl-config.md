---
UID: NS.gnssdriver.PGNSS_V2UPL_CONFIG
title: PGNSS_V2UPL_CONFIG
author: windows-driver-content
description: This structure contains V2UPL configuration information.
old-location: sensors\gnss_v2upl_config.htm
old-project: sensors
ms.assetid: A1DCC547-8CAA-46B9-A855-5F591C69A3B0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PGNSS_V2UPL_CONFIG, GNSS_V2UPL_CONFIG, *PGNSS_V2UPL_CONFIG
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
req.alt-api: GNSS_V2UPL_CONFIG
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

# PGNSS_V2UPL_CONFIG structure



## -description
<p>This structure contains V2UPL configuration information.</p>


## -syntax

````
typedef struct {
  ULONG Size;
  ULONG Version;
  CHAR  MPC[MAX_SERVER_URL_NAME];
  CHAR  PDE[MAX_SERVER_URL_NAME];
  BYTE  ApplicationTypeIndicator_MR;
} GNSS_V2UPL_CONFIG, *PGNSS_V2UPL_CONFIG;
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

### -field <b>MPC[MAX_SERVER_URL_NAME]</b>

<dd>
<p>MPC address and port number.</p>
</dd>

### -field <b>PDE[MAX_SERVER_URL_NAME]</b>

<dd>
<p>PDE address and port number.</p>
</dd>

### -field <b>ApplicationTypeIndicator_MR</b>

<dd>
<p>Application type indicator for any mobile originated location request to the MPC. It shall be set to the value for Microsoft resident applications based on intelligent platform.</p>
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