---
UID: NS.pepfx._PEP_QUERY_COMPONENT_PERF_SET_NAME
title: PEP_QUERY_COMPONENT_PERF_SET_NAME
author: windows-driver-content
description: The PEP_QUERY_COMPONENT_PERF_SET_NAME structure contains query information about a set of performance state values (P-state set) for a component.
old-location: kernel\pep_query_component_perf_set_name.htm
old-project: kernel
ms.assetid: 7F0C550A-A443-4936-B961-17813F23D6AD
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_QUERY_COMPONENT_PERF_SET_NAME, PEP_QUERY_COMPONENT_PERF_SET_NAME, *PPEP_QUERY_COMPONENT_PERF_SET_NAME
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
req.alt-api: PEP_QUERY_COMPONENT_PERF_SET_NAME
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

# PEP_QUERY_COMPONENT_PERF_SET_NAME structure



## -description
<p>The <b>PEP_QUERY_COMPONENT_PERF_SET_NAME</b> structure contains query information about a set of performance state values (P-state set) for a component.</p>


## -syntax

````
typedef struct _PEP_QUERY_COMPONENT_PERF_SET_NAME {
  PEPHANDLE DeviceHandle;
  ULONG     Component;
  ULONG     Set;
  USHORT    NameSize;
  PWCHAR    Name;
} PEP_QUERY_COMPONENT_PERF_SET_NAME, *PPEP_QUERY_COMPONENT_PERF_SET_NAME;
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
<p>[in] The index that identifies this P-state set. If this component has M P-state sets, P-state set indexes range from 0 to M–1. The PEP previously specified the number of P-state sets in response to a <a href="kernel.pep_dpm_query_component_perf_capabilities">PEP_DPM_QUERY_COMPONENT_PERF_CAPABILITIES</a> notification.</p>
</dd>

### -field <b>NameSize</b>

<dd>
<p>[in, out] On input, the size, in bytes, of the buffer pointed to by the <b>Name</b> member. If <b>Name</b> is NULL, the PEP overwrites the input value of <b>NameSize</b> with the buffer size required for the name string.</p>
</dd>

### -field <b>Name</b>

<dd>
<p>[in] A pointer to an output buffer. The PEP writes the name of the P-state to this buffer. The name is stored as a wide-character, null-terminated string. The <b>Name</b> member is NULL if the Windows power management framework (PoFx) needs to determine how large a buffer to allocate for the name string. If <b>Name</b> is non-NULL, the buffer must be large enough to contain the entire string, including the terminating null character.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="kernel.pep_dpm_query_component_perf_set_name">PEP_DPM_QUERY_COMPONENT_PERF_SET_NAME</a> notification. The <b>DeviceHandle</b>, <b>Component</b>, and <b>Set</b> members of the structure contain input values supplied by PoFx when this notification is sent. If the <b>Name</b> member is non-NULL, the PEP writes a string to the buffer pointed to by <b>Name</b>. If <b>Name</b> is NULL, PEP writes the required buffer size to the <b>NameSize</b> member.</p>

<p>The string that the PEP writes to the output buffer should contain a descriptive name for the P-state set. This name is intended to make log entries and diagnostic messages easier to understand.</p>

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
<a href="kernel.pep_dpm_query_component_perf_capabilities">PEP_DPM_QUERY_COMPONENT_PERF_CAPABILITIES</a>
</dt>
<dt>
<a href="kernel.pep_dpm_query_component_perf_set_name">PEP_DPM_QUERY_COMPONENT_PERF_SET_NAME</a>
</dt>
<dt>
<a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_QUERY_COMPONENT_PERF_SET_NAME structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
