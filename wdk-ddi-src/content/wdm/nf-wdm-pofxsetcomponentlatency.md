---
UID: NF.wdm.PoFxSetComponentLatency
title: PoFxSetComponentLatency
author: windows-driver-content
description: The PoFxSetComponentLatency routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified component.
old-location: kernel\pofxsetcomponentlatency.htm
old-project: kernel
ms.assetid: 670AFE37-1617-4171-9504-50B13B8E0F76
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PoFxSetComponentLatency
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoFxSetComponentLatency
req.alt-loc: Ntoskrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: Ntoskrnl.exe
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PoFxSetComponentLatency function



## -description
<p>The <b>PoFxSetComponentLatency</b> routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified component.</p>


## -syntax

````
VOID PoFxSetComponentLatency(
  _In_ POHANDLE  Handle,
  _In_ ULONG     Component,
  _In_ ULONGLONG Latency
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>A handle that represents the registration of the device with the power management framework (PoFx). The device driver previously received this handle from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439521">PoFxRegisterDevice</a> routine.</p>
</dd>

### -param <i>Component</i> [in]

<dd>
<p>The index that identifies the component. This parameter is an index into the <b>Components</b> array in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439585">PO_FX_DEVICE</a> structure that the device driver used to register the device with PoFx. If the <b>Components</b> array contains N elements, component indexes range from 0 to N–1.</p>
</dd>

### -param <i>Latency</i> [in]

<dd>
<p>The maximum latency, in 100-nanosecond units, that can be tolerated in the specified component. For more information, see Remarks.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>The calling driver supplies a maximum latency that clients of the device can tolerate in the specified component. This latency is the time required to complete a transition from the idle condition to the active condition. PoFx uses this latency as a hint to improve performance.</p>

<p>When the component switches from the active condition to the idle condition, PoFx selects an appropriate low-power Fx state for the component to enter. After this transition completes, the time required to switch back to the active condition depends on the selected Fx state. PoFx tries to select an Fx state that does not violate the maximum latency requirement.</p>

<p>For example, if a driver supports power states F0, F1, and F2 in the specified component, the F2 state represents a lower power setting than the F1 state. Typically, the time T2 required to wake (to the fully on state, F0) from F2 is longer than the time T1 required to wake from F1. If the maximum latency is greater than T1 but less than T2, PoFx can safely switch the component to the F1 state and still meet the maximum latency requirement. However, PoFx avoids switching the component to the F2 state because doing so violates this requirement.</p>

<p>The device driver can call <b>PoFxSetComponentLatency</b> each time a change in conditions requires a change in the maximum latency. After each call, the new maximum latency remains in effect until the driver calls <b>PoFxSetComponentLatency</b> again to update it.</p>

<p>If a component is in the idle condition when <b>PoFxSetComponentLatency</b> is called, PoFx might change the component’s current Fx state to accommodate the new maximum latency specified by the caller.</p>

<p>The calling driver supplies a maximum latency that clients of the device can tolerate in the specified component. This latency is the time required to complete a transition from the idle condition to the active condition. PoFx uses this latency as a hint to improve performance.</p>

<p>When the component switches from the active condition to the idle condition, PoFx selects an appropriate low-power Fx state for the component to enter. After this transition completes, the time required to switch back to the active condition depends on the selected Fx state. PoFx tries to select an Fx state that does not violate the maximum latency requirement.</p>

<p>For example, if a driver supports power states F0, F1, and F2 in the specified component, the F2 state represents a lower power setting than the F1 state. Typically, the time T2 required to wake (to the fully on state, F0) from F2 is longer than the time T1 required to wake from F1. If the maximum latency is greater than T1 but less than T2, PoFx can safely switch the component to the F1 state and still meet the maximum latency requirement. However, PoFx avoids switching the component to the F2 state because doing so violates this requirement.</p>

<p>The device driver can call <b>PoFxSetComponentLatency</b> each time a change in conditions requires a change in the maximum latency. After each call, the new maximum latency remains in effect until the driver calls <b>PoFxSetComponentLatency</b> again to update it.</p>

<p>If a component is in the idle condition when <b>PoFxSetComponentLatency</b> is called, PoFx might change the component’s current Fx state to accommodate the new maximum latency specified by the caller.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439585">PO_FX_DEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439521">PoFxRegisterDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxSetComponentLatency routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
