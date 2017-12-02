---
UID: NS.gnssdriver.PGNSS_CWTESTDATA
title: PGNSS_CWTESTDATA
author: windows-driver-content
description: This structure defines specific data elements associated with carrier wave test results returned from the driver.
old-location: sensors\gnss_cwtestdata.htm
old-project: sensors
ms.assetid: 7F1C8574-8891-4ACB-BB25-2666148E3D02
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: PGNSS_CWTESTDATA, GNSS_CWTESTDATA, *PGNSS_CWTESTDATA
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
req.alt-api: GNSS_CWTESTDATA
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

# PGNSS_CWTESTDATA structure



## -description
<p>This structure defines specific data elements associated with  carrier wave test results returned from the driver.</p>


## -syntax

````
typedef struct {
  ULONG    Size;
  ULONG    Version;
  NTSTATUS TestResultStatus;
  double   SignalToNoiseRatio;
  double   Frequency;
  BYTE     Unused[512];
} GNSS_CWTESTDATA, *PGNSS_CWTESTDATA;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>Structure size.</p>
</dd>

### -field Version

<dd>
<p>Version number.</p>
</dd>

### -field TestResultStatus

<dd>
<p>NTSTATUS value indicating whether this fix contains a valid data, or if the GNSS engine or driver encountered any errors in getting the measurements for the carrier wave test.</p>
<ul>
<li>
<p>Success - carrier wave test successfully started.</p>
</li>
<li>
<p>Failed - with error code: test not implemented, carrier wave test already in progress, fix session in progress, or other failure.</p>
</li>
</ul>
</dd>

### -field SignalToNoiseRatio

<dd>
<p>Signal to noise ratio in the carrier wave in dB-Hz.</p>
</dd>

### -field Frequency

<dd>
<p>Frequency of the carrier wave detected in the measurement band.</p>
<p>This frequency is provided as a difference to GPS frequency (1575.42 MHz) in kHz.</p>
</dd>

### -field Unused[512]

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