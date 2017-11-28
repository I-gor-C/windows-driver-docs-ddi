---
UID: NS.gnssdriver.PGNSS_SUPL_VERSION
title: PGNSS_SUPL_VERSION
author: windows-driver-content
description: This structure contains SUPL version information.
old-location: sensors\gnss_supl_version.htm
old-project: sensors
ms.assetid: D004DAEF-F25F-442D-9A6D-91FB8A18E0DB
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: PGNSS_SUPL_VERSION, GNSS_SUPL_VERSION, *PGNSS_SUPL_VERSION
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
req.alt-api: GNSS_SUPL_VERSION
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

# PGNSS_SUPL_VERSION structure



## -description
<p>This structure contains SUPL version information.

</p>


## -syntax

````
typedef struct {
  ULONG MajorVersion;
  ULONG MinorVersion;
} GNSS_SUPL_VERSION, *PGNSS_SUPL_VERSION;
````


## -struct-fields
<dl>

### -field <b>MajorVersion</b>

<dd>
<p>Major version number.</p>
</dd>

### -field <b>MinorVersion</b>

<dd>
<p>Minor version number.</p>
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