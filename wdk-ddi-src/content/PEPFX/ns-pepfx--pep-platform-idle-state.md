---
UID: NS.pepfx._PEP_PLATFORM_IDLE_STATE
title: PEP_PLATFORM_IDLE_STATE
author: windows-driver-content
description: The PEP_PLATFORM_IDLE_STATE structure specifies the properties of a platform idle state.
old-location: kernel\pep_platform_idle_state.htm
ms.assetid: D0503B73-EDFA-4742-BAFA-4FEE56F0A3C8
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_PLATFORM_IDLE_STATE
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
ms.keywords: PEP_PLATFORM_IDLE_STATE, PEP_PLATFORM_IDLE_STATE, *PPEP_PLATFORM_IDLE_STATE
req.iface: 
---

# PEP_PLATFORM_IDLE_STATE structure



## -description
<p>The <b>PEP_PLATFORM_IDLE_STATE</b> structure specifies the properties of a platform idle state.</p>


## -syntax

````
typedef struct _PEP_PLATFORM_IDLE_STATE {
  POHANDLE                                                                                   InitiatingProcessor;
  UCHAR                                                                                      InitiatingState;
  ULONG                                                                                      Latency;
  ULONG                                                                                      BreakEvenDuration;
  _Field_range_(0, DependencyArrayCount) ULONG                                               DependencyArrayUsed;
  ULONG                                                                                      DependencyArrayCount;
  _Field_size_part_(DependencyArrayCount, DependencyArrayUsed) PEP_PROCESSOR_IDLE_DEPENDENCY DependencyArray[ANYSIZE_ARRAY];
} PEP_PLATFORM_IDLE_STATE, *PPEP_PLATFORM_IDLE_STATE;
````


## -struct-fields
<dl>

### -field <b>InitiatingProcessor</b>

<dd>
<p>A <b>POHANDLE</b> value that identifies the processor that initiates the transition to this platform idle state, or <b>NULL</b> if any processor can initiate the transition. If non-NULL, this handle represents the registration of the processor (as a device) with the Windows <a href="https://msdn.microsoft.com/B08F8ABF-FD43-434C-A345-337FBB799D9B">power management framework</a> (PoFx).</p>
</dd>

### -field <b>InitiatingState</b>

<dd>
<p>The index of the processor idle state that the processor enters to initiate the platform's entry to the specified platform idle state. If the <b>IdleStates</b> array in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186824">PEP_PPM_QUERY_IDLE_STATES_V2</a> structure contains N elements, the idle states are numbered 0 to Nâ€“1 in the order in which they appear in the array.</p>
</dd>

### -field <b>Latency</b>

<dd>
<p>The worst-case latency, in 100-nanosecond units, that the platform requires to wake from this idle state in response to a wake event.</p>
</dd>

### -field <b>BreakEvenDuration</b>

<dd>
<p>The minimum amount of time, specified in 100-nanosecond units, that the platform must spend in this idle state to make a transition to this state worthwhile. PoFx uses this member value as a hint to avoid switching the platform to an idle state unless the platform is likely to remain in this state for at least the amount of time specified by <b>BreakEvenDuration</b>.

</p>
</dd>

### -field <b>DependencyArrayUsed</b>

<dd>
<p>The number of items in <b>DependencyArray</b> which were filled in by the PEP.</p>
</dd>

### -field <b>DependencyArrayCount</b>

<dd>
<p>The number of elements in the <b>DependencyArray</b> array. The array contains one element for each processor in the hardware platform.</p>
</dd>

### -field <b>DependencyArray</b>

<dd>
<p>The first element in an array of <a href="https://msdn.microsoft.com/library/windows/hardware/mt186834">PEP_PROCESSOR_IDLE_DEPENDENCY</a> structures. This array specifies the set of dependencies that the platform idle state has on each processor. If the platform contains N processors, the array contains N elements, and processors are numbered 0 to N-1 in the order in which they are represented in the array.</p>
</dd>
</dl>

## -remarks
<p>This structure is used in conjunction with the <a href="kernel.pep_notify_ppm_query_platform_state">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE</a> notification. The <b>State</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/mt186826">PEP_PPM_QUERY_PLATFORM_STATE</a> structure is a <b>PEP_PLATFORM_IDLE_STATE</b> structure.</p>

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
<a href="kernel.pep_notify_ppm_query_platform_state">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186824">PEP_PPM_QUERY_IDLE_STATES_V2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186826">PEP_PPM_QUERY_PLATFORM_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186834">PEP_PROCESSOR_IDLE_DEPENDENCY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PLATFORM_IDLE_STATE structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
