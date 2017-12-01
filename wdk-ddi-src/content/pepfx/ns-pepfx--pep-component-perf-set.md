---
UID: NS.pepfx._PEP_COMPONENT_PERF_SET
title: PEP_COMPONENT_PERF_SET
author: windows-driver-content
description: The PEP_COMPONENT_PERF_SET structure describes the performance states (P-states) in a P-state set.
old-location: kernel\pep_component_perf_set.htm
old-project: kernel
ms.assetid: E4EB8052-545C-46AE-A879-1F216B7FD20B
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_COMPONENT_PERF_SET, PEP_COMPONENT_PERF_SET, *PPEP_COMPONENT_PERF_SET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_COMPONENT_PERF_SET
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PEP_COMPONENT_PERF_SET structure



## -description
<p>The <b>PEP_COMPONENT_PERF_SET</b> structure describes the performance states (P-states) in a P-state set.</p>


## -syntax

````
typedef struct _PEP_COMPONENT_PERF_SET {
  UNICODE_STRING      Name;
  ULONGLONG           Flags;
  PEP_PERF_STATE_UNIT Unit;
  PEP_PERF_STATE_TYPE Type;
  union {
    struct {
      ULONG           Count;
      PPEP_PERF_STATE States;
    } Discrete;
    struct {
      ULONGLONG Minimum;
      ULONGLONG Maximum;
    } Range;
  };
} PEP_COMPONENT_PERF_SET, *PPEP_COMPONENT_PERF_SET;
````


## -struct-fields
<dl>

### -field <b>Name</b>

<dd>
<p>An optional string that describes the device property controlled by this P-state set.  For example, this string might be "Clock frequency" or "Memory bandwidth". If no such string is available for this P-state, the <b>Name</b> member is set to NULL. Otherwise, this member contains a pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains the string.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Set to zero. No flag bits are currently defined for this member.</p>
</dd>

### -field <b>Unit</b>

<dd>
<p>A <a href="..\pepfx\ne-pepfx--pep-perf-state-unit.md">PEP_PERF_STATE_UNIT</a> structure that specifies the units in which the performance values for this P-state set are expressed. Component performance can be expressed in hertz (frequency) or in bits per second (bandwidth).</p>
</dd>

### -field <b>Type</b>

<dd>
<p>A <a href="..\pepfx\ne-pepfx--pep-perf-state-type.md">PEP_PERF_STATE_TYPE</a> enumeration value that indicates the type of performance information that is specified for this component. This member indicates whether the performance values for this P-state set are specified as a list of discrete values or as a continuous range of values.</p>
</dd>

### -field ( <i>unnamed union</i> )

<dd>
<p>A union that contains the performance measurement values for this P-state. This union contains either a list of discrete values (if <b>Type</b> = <b>PepPerfStateTypeDiscrete</b>) or a continuous range of values (if <b>Type</b> = <b>PepPerfStateTypeRange</b>).</p>
<dl>

### -field <b>Discrete</b>

<dd>
<p>The list of discrete performance values for this P-state set.</p>
<dl>

### -field <b>Count</b>

<dd>
<p>The number of P-states in this P-state set.</p>
</dd>

### -field <b>States</b>

<dd>
<p>A pointer to an array of <a href="..\pepfx\ns-pepfx--pep-perf-state.md">PEP_PERF_STATE</a> structures, each of which describes a discrete performance value in this P-state set. The <b>Count</b> member specifies the number of elements in this array. A P-state is identified by its array index. If the array contains N elements, P-state indexes range from 0 to N–1.</p>
</dd>
</dl>
</dd>

### -field <b>Range</b>

<dd>
<p>The range of discrete performance measurement values for this P-state set.</p>
<dl>

### -field <b>Minimum</b>

<dd>
<p>The minimum value in the range. This value is expressed in the units indicated by the <b>Unit</b> member.</p>
</dd>

### -field <b>Maximum</b>

<dd>
<p>The maximum value in the range. This value is expressed in the units indicated by the <b>Unit</b> member.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>PerfStateSets</b> member of the <a href="..\pepfx\ns-pepfx--pep-component-perf-info.md">PEP_COMPONENT_PERF_INFO</a> is the first element in an array of <b>PEP_COMPONENT_PERF_SET</b> structures. All members of the <b>PEP_COMPONENT_PERF_SET</b> structure contain input values that are supplied by the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx). The platform extension plug-in (PEP) must not write to this structure.</p>

<p>Device drivers use the <a href="..\wdm\ns-wdm--po-fx-component-perf-set.md">PO_FX_COMPONENT_PERF_SET</a> structure, which is similar to the <b>PEP_COMPONENT_PERF_SET</b> structure.</p>

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
<a href="..\pepfx\ns-pepfx--pep-component-perf-info.md">PEP_COMPONENT_PERF_INFO</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-perf-state.md">PEP_PERF_STATE</a>
</dt>
<dt>
<a href="..\pepfx\ne-pepfx--pep-perf-state-unit.md">PEP_PERF_STATE_UNIT</a>
</dt>
<dt>
<a href="..\pepfx\ne-pepfx--pep-perf-state-type.md">PEP_PERF_STATE_TYPE</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--po-fx-component-perf-set.md">PO_FX_COMPONENT_PERF_SET</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_COMPONENT_PERF_SET structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
