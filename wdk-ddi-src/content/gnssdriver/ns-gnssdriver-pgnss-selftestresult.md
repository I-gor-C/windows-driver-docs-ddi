---
UID: NS.gnssdriver.PGNSS_SELFTESTRESULT
title: PGNSS_SELFTESTRESULT
author: windows-driver-content
description: This structure defines the specific data elements associated with a carrier wave test results returned from the driver.
old-location: sensors\gnss_selftestresult.htm
old-project: sensors
ms.assetid: 572A2C38-A990-4225-A3FC-6E899A248B1C
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PGNSS_SELFTESTRESULT, GNSS_SELFTESTRESULT, *PGNSS_SELFTESTRESULT
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
req.alt-api: GNSS_SELFTESTRESULT
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

# PGNSS_SELFTESTRESULT structure



## -description
<p>This structure defines the specific data elements associated with a carrier wave test results returned from the driver.</p>


## -syntax

````
typedef struct {
  ULONG    Size;
  ULONG    Version;
  NTSTATUS TestResultStatus;
  ULONG    Result;
  ULONG    PinFailedBitMask;
  BYTE     Unused[512];
  ULONG    OutBufLen;
  BYTE     OutBuffer[BYTE];
} GNSS_SELFTESTRESULT, *PGNSS_SELFTESTRESULT;
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

### -field <b>TestResultStatus</b>

<dd>
<p>NTSTATUS value indicating:</p>
<ul>
<li>
<p>Success (self-test passed).</p>
</li>
<li>
<p>Failed (indicating the problem detected or indicating that the is test not implemented).</p>
</li>
</ul>
</dd>

### -field <b>Result</b>

<dd>
<p>The final result of the self-test.</p>
</dd>

### -field <b>PinFailedBitMask</b>

<dd>
<p>The bit mask for adapter pins that failed the test.</p>
</dd>

### -field <b>Unused[512]</b>

<dd>
<p>Padding buffer.</p>
</dd>

### -field <b>OutBufLen</b>

<dd>
<p>The length of the buffer for returning any additional information about the self-test.</p>
</dd>

### -field <b>OutBuffer[BYTE]</b>

<dd>
<p>The buffer that will contain the additional information about the self-test.</p>
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