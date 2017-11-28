---
UID: NS.pep_x._PEP_PPM_IDLE_SELECT
title: PEP_PPM_IDLE_SELECT
author: windows-driver-content
description: The PEP_PPM_IDLE_SELECT structure describes the most energy-efficient idle state that the processor can enter and still satisfy the constraints specified by the operating system.
old-location: kernel\pep_ppm_idle_select.htm
old-project: kernel
ms.assetid: 4783CB44-3A55-4C7C-8EA2-1A72317CC955
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PEP_PPM_IDLE_SELECT, PEP_PPM_IDLE_SELECT, *PPEP_PPM_IDLE_SELECT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pep_x.h
req.include-header: Pepfx.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_PPM_IDLE_SELECT
req.alt-loc: pep_x.h
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

# PEP_PPM_IDLE_SELECT structure



## -description
<p>The <b>PEP_PPM_IDLE_SELECT</b> structure describes the most energy-efficient idle state that the processor can enter and still satisfy the constraints specified by the operating system.</p>


## -syntax

````
typedef struct _PEP_PPM_IDLE_SELECT {
  PPEP_PROCESSOR_IDLE_CONSTRAINTS Constraints;
  BOOLEAN                         AbortTransition;
  ULONG                           IdleStateIndex;
  ULONG                           DependencyArrayUsed;
  ULONG                           DependencyArrayCount;
  PPEP_PROCESSOR_IDLE_DEPENDENCY  DependencyArray;
  ULONG                           PlatformIdleStateIndex;
} PEP_PPM_IDLE_SELECT, *PPEP_PPM_IDLE_SELECT;
````


## -struct-fields
<dl>

### -field <b>Constraints</b>

<dd>
<p>[in] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/mt629124">PEP_PROCESSOR_IDLE_CONSTRAINTS</a> structure that specifies the constraints that the selected processor idle state must satisfy. The operating system sets the values in this structure. The platform extension plug-in (PEP) must select a processor idle state that satisfies these constraints.</p>
</dd>

### -field <b>AbortTransition</b>

<dd>
<p>[out] Whether to cancel the pending transition to a processor idle state. Set this member to TRUE if the PEP requires the operating system to cancel the pending transition, and to FALSE otherwise. The PEP selects this option if it wants to queue work and have the Windows kernel process this work before the processor enters idle.</p>
</dd>

### -field <b>IdleStateIndex</b>

<dd>
<p>[out] The index that identifies the idle state that the processor is to enter. This member is ignored if <b>AbortTransition</b> = TRUE. If the processor supports N idle states, idle state indexes range from 0 to N–1. The PEP supplied the number of supported idle states for this processor in response to a previous <a href="kernel.pep_notify_ppm_query_idle_states">PEP_NOTIFY_PPM_QUERY_IDLE_STATES</a> notification.</p>
</dd>

### -field <b>DependencyArrayUsed</b>

<dd>
<p>[out] The number of array elements that the PEP has actually written to the output buffer pointed to the <b>DependencyArray</b> member.</p>
</dd>

### -field <b>DependencyArrayCount</b>

<dd>
<p>[in] The maximum number of elements in the array pointed to by the <b>DependencyArray</b> member. The <b>DependencyArrayCount</b> member value is equal to the <b>MaximumCoordinatedProcessors</b> value that the PEP previously supplied in response to the <a href="kernel.pep_notify_ppm_query_idle_states">PEP_NOTIFY_PPM_QUERY_IDLE_STATES</a> notification.</p>
</dd>

### -field <b>DependencyArray</b>

<dd>
<p>[in] A pointer to an output buffer to which the PEP writes an array of <a href="https://msdn.microsoft.com/library/windows/hardware/mt186834">PEP_PROCESSOR_IDLE_DEPENDENCY</a> structures. The elements of this array specify processor idle dependencies or wake dependencies that must be met for this idle transition to succeed. The PEP sets the <b>DependencyArrayUsed</b> member to the actual number of array elements that the PEP writes to the buffer. The output buffer is allocated by the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx) and is guaranteed to be large enough to contain the number of array elements specified by the <b>DependencyArrayCount</b> member.</p>
</dd>

### -field <b>PlatformIdleStateIndex</b>

<dd>
<p>[out] The index of the platform idle state that the platform is to enter when the processor enters the selected processor idle state. The PEP should set this member only if the platform enters an idle state at the same time as the processor. This member is ignored if <b>AbortTransition</b> is TRUE.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="kernel.pep_notify_ppm_idle_select">PEP_NOTIFY_PPM_IDLE_SELECT</a> notification. The <b>Constraints</b>, <b>DependencyArrayCount</b>, and <b>DependencyArray</b> members of the structure contain input values supplied by PoFx when this notification is sent. The remaining members contain output values that the PEP writes to the structure in response to the notification.</p>

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
<dt>Pep_x.h (include Pepfx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pep_notify_ppm_query_idle_states">PEP_NOTIFY_PPM_QUERY_IDLE_STATES</a>
</dt>
<dt>
<a href="kernel.pep_notify_ppm_idle_select">PEP_NOTIFY_PPM_IDLE_SELECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt629124">PEP_PROCESSOR_IDLE_CONSTRAINTS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186834">PEP_PROCESSOR_IDLE_DEPENDENCY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PPM_IDLE_SELECT structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
