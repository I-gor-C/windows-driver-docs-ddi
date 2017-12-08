---
UID: NE.wdm._PO_FX_PERF_STATE_TYPE
title: PO_FX_PERF_STATE_TYPE
author: windows-driver-content
description: The PO_FX_PERF_STATE_TYPE enumeration contains values that describe the type of performance states in a PO_FX_COMPONENT_PERF_SET.
old-location: kernel\po_fx_perf_state_type.htm
old-project: kernel
ms.assetid: E3BFBF03-8130-4EFF-95F4-030107AF4D75
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PO_FX_PERF_STATE_TYPE
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PO_FX_PERF_STATE_TYPE enumeration



## -description
<p>The <b>PO_FX_PERF_STATE_TYPE</b> enumeration contains values that describe the type of performance states in a <a href="..\wdm\ns-wdm--po-fx-component-perf-set.md">PO_FX_COMPONENT_PERF_SET</a>.</p>


## -syntax

````
typedef enum _PO_FX_PERF_STATE_TYPE { 
  PoFxPerfStateTypeDiscrete,
  PoFxPerfStateTypeRange,
  PoFxPerfStateTypeMaximum
} PO_FX_PERF_STATE_TYPE, *PPO_FX_PERF_STATE_TYPE;
````


## -enum-fields
<dl>

### -field PoFxPerfStateTypeDiscrete

<dd>
<p>Indicates that the performance state set contains a discrete number of states.</p>
</dd>

### -field PoFxPerfStateTypeRange

<dd>
<p>Indicates that the performance state set contains a continuous distribution of  states between a minimum and maximum value.</p>
</dd>

### -field PoFxPerfStateTypeMaximum

<dd>
<p>This value is reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>The <b>Type</b> member of the <a href="..\wdm\ns-wdm--po-fx-component-perf-set.md">PO_FX_COMPONENT_PERF_SET</a> structure is a value from the <b>PO_FX_PERF_STATE_TYPE</b> enumeration.</p>

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
<a href="..\wdm\ns-wdm--po-fx-component-perf-set.md">PO_FX_COMPONENT_PERF_SET</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-pofxregistercomponentperfstates.md">PoFxRegisterComponentPerfStates</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PO_FX_PERF_STATE_TYPE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
