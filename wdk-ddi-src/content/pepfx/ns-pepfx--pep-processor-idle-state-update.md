---
UID: NS.pepfx._PEP_PROCESSOR_IDLE_STATE_UPDATE
title: PEP_PROCESSOR_IDLE_STATE_UPDATE
author: windows-driver-content
description: The PEP_PROCESSOR_IDLE_STATE_UPDATE structure contains the updated properties of a processor idle state.
old-location: kernel\pep_processor_idle_state_update.htm
old-project: kernel
ms.assetid: A05617FB-5105-4FCA-807F-C49F32BD1399
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_PROCESSOR_IDLE_STATE_UPDATE, PEP_PROCESSOR_IDLE_STATE_UPDATE, *PPEP_PROCESSOR_IDLE_STATE_UPDATE
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
req.alt-api: PEP_PROCESSOR_IDLE_STATE_UPDATE
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

# PEP_PROCESSOR_IDLE_STATE_UPDATE structure



## -description
<p>The <b>PEP_PROCESSOR_IDLE_STATE_UPDATE</b> structure contains the updated properties of a processor idle state.</p>


## -syntax

````
typedef struct _PEP_PROCESSOR_IDLE_STATE_UPDATE {
  ULONG Version;
  ULONG Latency;
  ULONG BreakEvenDuration;
} PEP_PROCESSOR_IDLE_STATE_UPDATE, *PPEP_PROCESSOR_IDLE_STATE_UPDATE;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version number of this structure. Set this member to PEP_PROCESSOR_IDLE_STATE_UPDATE_VERSION.</p>
</dd>

### -field <b>Latency</b>

<dd>
<p>The worst-case latency, in 100-nanosecond units, that the platform requires to wake from this platform idle state in response to a wake event.</p>
</dd>

### -field <b>BreakEvenDuration</b>

<dd>
<p>The minimum amount of time, specified in 100-nanosecond units, that the platform must spend in this idle state to make a transition to this state worthwhile. PoFx uses this member value as a hint to avoid switching the platform to an idle state unless the platform is likely to remain in this state for at least the amount of time specified by <b>BreakEvenDuration</b>.</p>
</dd>
</dl>

## -remarks
<p>The <i>Update</i> parameter to the <a href="kernel.updateprocessoridlestate">UpdateProcessorIdleState</a> routine is a pointer to a <b>PEP_PROCESSOR_IDLE_STATE_UPDATE</b> structure. This routine updates the properties of the specified idle state for a processor. The PEP must not call this routine until it has responded to a <a href="kernel.pep_notify_ppm_query_idle_states_v2">PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2</a> notification for this processor.</p>

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
<a href="kernel.pep_notify_ppm_query_idle_states_v2">PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2</a>
</dt>
<dt>
<a href="kernel.updateprocessoridlestate">UpdateProcessorIdleState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PROCESSOR_IDLE_STATE_UPDATE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
