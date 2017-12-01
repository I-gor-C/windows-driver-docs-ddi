---
UID: NS.pepfx._PEP_QUERY_COMPONENT_PERF_STATES
title: PEP_QUERY_COMPONENT_PERF_STATES
author: windows-driver-content
description: The PEP_QUERY_COMPONENT_PERF_STATES structure contains a list of discrete performance state (P-state) values for the specified P-state set.
old-location: kernel\pep_query_component_perf_states.htm
old-project: kernel
ms.assetid: D14CB726-2576-490E-B3FD-E970F8B3C87F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_QUERY_COMPONENT_PERF_STATES, PEP_QUERY_COMPONENT_PERF_STATES, *PPEP_QUERY_COMPONENT_PERF_STATES
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
req.alt-api: PEP_QUERY_COMPONENT_PERF_STATES
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

# PEP_QUERY_COMPONENT_PERF_STATES structure



## -description
<p>The <b>PEP_QUERY_COMPONENT_PERF_STATES</b> structure contains a list of discrete performance state (P-state) values for the specified P-state set.</p>


## -syntax

````
typedef struct _PEP_QUERY_COMPONENT_PERF_STATES {
  PEPHANDLE       DeviceHandle;
  ULONG           Component;
  ULONG           Set;
  PPEP_PERF_STATE States;
} PEP_QUERY_COMPONENT_PERF_STATES, *PPEP_QUERY_COMPONENT_PERF_STATES;
````


## -struct-fields
<dl>

### -field <b>DeviceHandle</b>

<dd>
<p>[in] A PEPHANDLE value that identifies the device. The PEP supplied this handle in response to a previous <a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a> notification.</p>
</dd>

### -field <b>Component</b>

<dd>
<p>[in] The index that identifies the component. This member is an index into the <b>Components</b> array in the <a href="..\pepfx\ns-pepfx--pep-device-register-v2.md">PEP_DEVICE_REGISTER_V2</a> structure that the PEP previously supplied in response to the <b>PEP_DPM_REGISTER_DEVICE</b> notification for this device. If the <b>Components</b> array contains N elements, component indexes range from 0 to N–1.</p>
</dd>

### -field <b>Set</b>

<dd>
<p>[in] The index that identifies this P-state set. If M is the number of P-state sets for this component, P-state set indexes range from 0 to M–1. The PEP previously specified the number of P-state sets in response to a <a href="kernel.pep_dpm_query_component_perf_capabilities">PEP_DPM_QUERY_COMPONENT_PERF_CAPABILITIES</a> notification.</p>
</dd>

### -field <b>States</b>

<dd>
<p>[in] A pointer to an output buffer. The PEP writes an array of <a href="..\pepfx\ns-pepfx--pep-perf-state.md">PEP_PERF_STATE</a> structures to this buffer. Each array element describes one P-state in the P-state set specified by the <b>Set</b> member. The Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx) allocated this buffer, which is guaranteed to be large enough to contain an array of the length that the PEP previously wrote to the <b>Discrete.Count</b> member of the <a href="..\pepfx\ns-pepfx--pep-query-component-perf-set.md">PEP_QUERY_COMPONENT_PERF_SET</a> structure in response to a <a href="kernel.pep_dpm_query_component_perf_set">PEP_DPM_QUERY_COMPONENT_PERF_SET</a> notification.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="kernel.pep_dpm_query_component_perf_states">PEP_DPM_QUERY_COMPONENT_PERF_STATES</a> notification. All four members of this structure contain input values that are supplied by PoFx when this notification is sent.</p>

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
<a href="..\pepfx\ns-pepfx--pep-device-register-v2.md">PEP_DEVICE_REGISTER_V2</a>
</dt>
<dt>
<a href="kernel.pep_dpm_query_component_perf_states">PEP_DPM_QUERY_COMPONENT_PERF_STATES</a>
</dt>
<dt>
<a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-perf-state.md">PEP_PERF_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_QUERY_COMPONENT_PERF_STATES structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
