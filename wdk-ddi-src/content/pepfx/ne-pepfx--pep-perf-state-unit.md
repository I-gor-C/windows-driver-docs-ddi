---
UID: NE.pepfx._PEP_PERF_STATE_UNIT
title: PEP_PERF_STATE_UNIT
author: windows-driver-content
description: The PEP_PERF_STATE_UNIT enumeration indicates the measurement units in which the performance state (P-state) of a component is specified.
old-location: kernel\pep_perf_state_unit.htm
old-project: kernel
ms.assetid: 5E5F049D-4306-4382-B3F7-06C1F5FFE93E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VPCI_PNP_ID, VPCI_PNP_ID, *PVPCI_PNP_ID
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_PERF_STATE_UNIT
req.alt-loc: pepfx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks.
req.iface: 
---

# PEP_PERF_STATE_UNIT enumeration



## -description
<p>The <b>PEP_PERF_STATE_UNIT</b> enumeration indicates the measurement units in which the performance state (P-state) of a component is specified.</p>


## -syntax

````
typedef enum _PEP_PERF_STATE_UNIT { 
  PepPerfStateUnitOther      = 0,
  PepPerfStateUnitFrequency,
  PepPerfStateUnitBandwidth,
  PepPerfStateUnitMax
} PEP_PERF_STATE_UNIT;
````


## -enum-fields
<dl>

### -field <a id="PepPerfStateUnitOther"></a><a id="pepperfstateunitother"></a><a id="PEPPERFSTATEUNITOTHER"></a><b>PepPerfStateUnitOther</b>

<dd>
<p>Some other type of measurement units not explicitly described by this enumeration.</p>
</dd>

### -field <a id="PepPerfStateUnitFrequency"></a><a id="pepperfstateunitfrequency"></a><a id="PEPPERFSTATEUNITFREQUENCY"></a><b>PepPerfStateUnitFrequency</b>

<dd>
<p>Hertz (frequency units).</p>
</dd>

### -field <a id="PepPerfStateUnitBandwidth"></a><a id="pepperfstateunitbandwidth"></a><a id="PEPPERFSTATEUNITBANDWIDTH"></a><b>PepPerfStateUnitBandwidth</b>

<dd>
<p>Bits per second (bandwidth units).</p>
</dd>

### -field <a id="PepPerfStateUnitMax"></a><a id="pepperfstateunitmax"></a><a id="PEPPERFSTATEUNITMAX"></a><b>PepPerfStateUnitMax</b>

<dd>
<p>Reserved for use by operating system.</p>
</dd>
</dl>

## -remarks
<p>The <b>Type</b> member of the <a href="..\pepfx\ns-pepfx--pep-component-perf-set.md">PEP_COMPONENT_PERF_SET</a> structure is a <b>PEP_PERF_STATE_UNIT</b> enumeration value.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\pepfx\ns-pepfx--pep-component-perf-set.md">PEP_COMPONENT_PERF_SET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PERF_STATE_UNIT enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
