---
UID: NS.pepfx._PEP_PPM_IDLE_COMPLETE
title: PEP_PPM_IDLE_COMPLETE
author: windows-driver-content
description: The PEP_PPM_IDLE_COMPLETE structure describe the idle states from which the processor and hardware platform are waking.
old-location: kernel\pep_ppm_idle_complete.htm
old-project: kernel
ms.assetid: F44C7FCC-0693-4F43-BF23-7160B67EDD3D
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_PPM_IDLE_COMPLETE, PEP_PPM_IDLE_COMPLETE, *PPEP_PPM_IDLE_COMPLETE
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
req.alt-api: PEP_PPM_IDLE_COMPLETE
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

# PEP_PPM_IDLE_COMPLETE structure



## -description
<p>The <b>PEP_PPM_IDLE_COMPLETE</b> structure describe the idle states from which the processor and hardware platform are waking.</p>


## -syntax

````
typedef struct _PEP_PPM_IDLE_COMPLETE {
  ULONG ProcessorState;
  ULONG PlatformState;
} PEP_PPM_IDLE_COMPLETE, *PPEP_PPM_IDLE_COMPLETE;
````


## -struct-fields
<dl>

### -field <b>ProcessorState</b>

<dd>
<p>[in] An index that identifies the idle state from which the processor is waking. The platform extension plug-in (PEP) previously specified the supported processor idle states in response to a <a href="kernel.pep_notify_ppm_query_idle_states_v2">PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2</a> notification. If the PEP specified N processor idle states, valid processor-idle-state indexes range from 0 to N-1. When the hypervisor is enabled and the platform wakes from an idle state, this member is set to <b>PEP_PROCESSOR_IDLE_STATE_UNKNOWN</b> (0xffffffff). For more information, see <a href="kernel.pep_notify_ppm_idle_complete">PEP_NOTIFY_PPM_IDLE_COMPLETE</a>.</p>
</dd>

### -field <b>PlatformState</b>

<dd>
<p>[in] An index that identifies the idle state from which the platform is waking. The PEP previously specified the supported platform idle states in response to a <a href="kernel.pep_notify_ppm_query_platform_states">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES</a> notification. If the PEP specified M platform idle states, valid platform-idle-state indexes range from 0 to M-1. If the transition from the processor idle state does not involve a transition from an platform idle state, this member will contain the value <b>PEP_PLATFORM_IDLE_STATE_NONE</b> (0xffffffff).</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="kernel.pep_notify_ppm_idle_complete">PEP_NOTIFY_PPM_IDLE_COMPLETE</a> notification. The <b>ProcessorState</b> and <b>PlatformState</b> members contain input values that are supplied by the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx) when this notification is sent to the PEP.</p>

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
<a href="kernel.pep_notify_ppm_idle_complete">PEP_NOTIFY_PPM_IDLE_COMPLETE</a>
</dt>
<dt>
<a href="kernel.pep_notify_ppm_query_idle_states_v2">PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2</a>
</dt>
<dt>
<a href="kernel.pep_notify_ppm_query_platform_states">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PPM_IDLE_COMPLETE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
