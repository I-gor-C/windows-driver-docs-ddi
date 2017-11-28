---
UID: NS.wdm._PO_FX_PERF_STATE
title: PO_FX_PERF_STATE
author: windows-driver-content
description: The PO_FX_PERF_STATE structure represents a performance state for a single component within a device.
old-location: kernel\po_fx_perf_state.htm
old-project: kernel
ms.assetid: 06A41593-A052-43A7-B3A7-02185B557FA3
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PO_FX_PERF_STATE, PO_FX_PERF_STATE, *PPO_FX_PERF_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PO_FX_PERF_STATE
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# PO_FX_PERF_STATE structure



## -description
<p>The <b>PO_FX_PERF_STATE</b> structure represents a performance state for a single component within a device.</p>


## -syntax

````
typedef struct _PO_FX_PERF_STATE {
  ULONGLONG Value;
  PVOID     Context;
} PO_FX_PERF_STATE, *PPO_FX_PERF_STATE;
````


## -struct-fields
<dl>

### -field <b>Value</b>

<dd>
<p>The value of this performance state. The units are specified by the <b>Unit</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn939833">PO_FX_COMPONENT_PERF_SET</a> that contains this performance state. For example, if <b>Value</b> is 100000000 and the <b>Unit</b> member of the  <b>PO_FX_COMPONENT_PERF_SET</b> is <b>PoFxPerfStateUnitFrequency</b>, this performance state represents 100 MHz.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>A pointer to additional context for the performance state that cannot be presented by the <b>Value</b> member. This data can be shared between the driver and the platform extension plug-in (PEP).</p>
<div class="alert"><b>Note</b>  Using the <b>Context</b> member can hinder the visualization of performance states in Windows Performance Analyzer.</div>
<div> </div>
</dd>
</dl>

## -remarks
<p>The <b>States</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn939833">PO_FX_COMPONENT_PERF_SET</a> structure contains an array of <b>PO_FX_PERF_STATE</b> elements. </p>

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
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/D5341D6D-7C71-43CB-9C70-7E939B32C33F">Device Performance State Management</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn939778">PoFxRegisterComponentPerfStates</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn939833">PO_FX_COMPONENT_PERF_SET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn939838">PO_FX_PERF_STATE_UNIT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PO_FX_PERF_STATE structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
