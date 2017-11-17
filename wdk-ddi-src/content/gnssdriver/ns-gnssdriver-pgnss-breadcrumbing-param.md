---
UID: NS.gnssdriver.PGNSS_BREADCRUMBING_PARAM
title: PGNSS_BREADCRUMBING_PARAM
author: windows-driver-content
description: This structure contains the configuration passed into the start of breadcrumbing via IOCTL_GNSS_START_BREADCRUMBING.
old-location: sensors\gnss_breadcrumbing_param.htm
ms.assetid: 1EAD5B17-B662-4D97-B045-ED09E4AF6E99
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
req.alt-api: GNSS_BREADCRUMBING_PARAM
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
ms.keywords: PGNSS_BREADCRUMBING_PARAM, GNSS_BREADCRUMBING_PARAM, *PGNSS_BREADCRUMBING_PARAM
req.iface: 
---

# PGNSS_BREADCRUMBING_PARAM structure



## -description
<p>This structure contains the configuration passed into the start of breadcrumbing via <a href="https://msdn.microsoft.com/library/windows/hardware/mt767993">IOCTL_GNSS_START_BREADCRUMBING</a>.</p>


## -syntax

````
typedef struct {
  ULONG Size;
  ULONG Version;
  ULONG MaximumHorizontalUncertainty;
  ULONG MinDistanceBetweenFixes;
  ULONG MaximumErrorTimeoutMs;
  BYTE  Unused[512];
} GNSS_BREADCRUMBING_PARAM, *PGNSS_BREADCRUMBING_PARAM;
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

### -field <b>MaximumHorizontalUncertainty</b>

<dd>
<p>Contains the maximum horizontal uncertainty value. Any fix with an error radius larger than this value shall not be recorded.</p>
</dd>

### -field <b>MinDistanceBetweenFixes</b>

<dd>
<p>Contains the minimum distance between fixes. Only record a fix if the center of it is at least as  far apart as this value from center of the last fix, using a Haversine distance calculation.</p>
</dd>

### -field <b>MaximumErrorTimeoutMs</b>

<dd>
<p>Contains the maximum error timeout in milliseconds. If the location of the device is unknown for this duration, an error must be recorded in the breadcrumb data. Errors can be recorded earlier if they were already known.</p>
</dd>

### -field <b>Unused[512]</b>

<dd>
<p>Padding buffer.</p>
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