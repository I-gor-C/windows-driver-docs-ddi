---
UID: NF.wdm.PoFxActivateComponent
title: PoFxActivateComponent
author: windows-driver-content
description: The PoFxActivateComponent routine increments the activation reference count on the specified component.
old-location: kernel\pofxactivatecomponent.htm
old-project: kernel
ms.assetid: B964B836-68C1-4254-963C-8D46ACE64107
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PoFxActivateComponent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoFxActivateComponent
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

# PoFxActivateComponent function



## -description
<p>The <b>PoFxActivateComponent</b> routine increments the activation reference count on the specified component.</p>


## -syntax

````
VOID PoFxActivateComponent(
  _In_ POHANDLE Handle,
  _In_ ULONG    Component,
  _In_ ULONG    Flags
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

### -param <i>Flags</i> [in]

<dd>
<p>The flags for the activation operation. Set this member to zero or to one of the following flag <b>PO_FX_FLAG_<i>XXX</i></b> bits:</p>
<p>These two flag bits are mutually exclusive. For more information, see Remarks.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="PO_FX_FLAG_BLOCKING"></a><a id="po_fx_flag_blocking"></a><dl>

### -param <b>PO_FX_FLAG_BLOCKING</b>


### -param 0x1

</dl>
</td>
<td width="60%">
<p>Make the condition change synchronous. If this flag is set, the routine that requests the condition change does not return control to the calling driver until the component hardware completes the transition to the new condition. This flag can be used only if the caller is running at IRQL &lt; DISPATCH_LEVEL.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PO_FX_FLAG_ASYNC_ONLY"></a><a id="po_fx_flag_async_only"></a><dl>

### -param <b>PO_FX_FLAG_ASYNC_ONLY</b>


### -param 0x2

</dl>
</td>
<td width="60%">
<p>Make the condition change fully asynchronous. If this flag is set, the calling driver's callback routine is called from a thread other than the thread in which the routine that requests the condition change is called. Thus, the routine that requests the condition change always returns asynchronously without waiting for the callback to complete.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>Before a device driver can access a component in a device, the driver must first call <b>PoFxActivateComponent</b> to obtain an activation reference to the component. If the component is not already in the active condition, this call initiates a transition from the idle condition to the active condition. When this transition completes, PoFx calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh406416">ComponentActiveConditionCallback</a> routine to notify the driver. The driver can access the hardware registers in a component only when the component is in the active condition.</p>

<p>If the component is already in the active condition when <b>PoFxActivateComponent</b> is called, no transition is required, and the <i>ComponentActiveConditionCallback</i> routine is not called.</p>

<p>After a component enters the active condition, it remains in the active condition for as long as the driver holds one or more activation references on the component. To release an activation reference, the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406717">PoFxIdleComponent</a> routine. When the driver releases the last activation reference on a component, <b>PoFxIdleComponent</b> initiates a transition from the active condition to the idle condition. A component that is in the idle condition can potentially enter a low-power Fx state.</p>

<p>If <i>Flags</i> = <b>PO_FX_FLAG_BLOCKING</b>, the <b>PoFxActivateComponent</b> call is synchronous. If the component is already in the active condition, the call increments the activation reference count and returns without waiting. Otherwise, <b>PoFxActivateComponent</b> waits to return until the component completes the transition to the active condition. In this case, if the component is not already in the F0 state when the call occurs, <b>PoFxActivateComponent</b> calls the driver's <i>ComponentIdleStateCallback</i> routine to initiate the transition to F0. After the component enters the F0 state, <b>PoFxActivateComponent</b> calls the driver's <i>ComponentActiveConditionCallback</i> routine to inform the driver that the component is in the active condition. These callbacks occur in the same thread as the call to <b>PoFxActivateComponent</b>, and <b>PoFxActivateComponent</b> returns only after the <i>ComponentActiveConditionCallback</i> callback returns.</p>

<p>If <i>Flags</i> = <b>PO_FX_FLAG_ASYNC_ONLY</b>, the <b>PoFxActivateComponent</b> call is asynchronous. If the component is already in the active condition, the call increments the activation reference count and returns. Otherwise, <b>PoFxActivateComponent</b> schedules the <i>ComponentIdleStateCallback</i> (if necessary) and <i>ComponentActiveConditionCallback</i> callbacks to occur in another thread, and then returns without waiting for either callback to occur. The callbacks can occur before or after <b>PoFxActivateComponent</b> returns. The driver relies on the <i>ComponentActiveConditionCallback</i> callback to determine when the component completes the transition to the active condition.</p>

<p>The driver can set <i>Flags</i> = 0 to indicate that it does not care whether the <b>PoFxActivateComponent</b> call is synchronous or asynchronous. In this case, PoFx decides whether to make the call synchronous or asynchronous.</p>

<p>Two or more code paths in the same driver might need to concurrently access a particular component. The <b>PoFxActivateComponent</b> and <b>PoFxIdleComponent</b> routines use activation reference counts to enable the various parts of the driver to independently maintain access to the component without requiring the driver to centrally manage access to the component.</p>

<p>PoFx maintains an activation reference count for each component in a device. A <b>PoFxActivateComponent</b> call increments this count by one, and a <b>PoFxIdleComponent</b> call decrements the count by one. When the count is nonzero, the component either is in the active condition or is in the process of switching to the active condition. A component that has a count of zero either is in the idle condition or is in the process of switching to the idle condition.</p>

<p>When a <b>PoFxActivateComponent</b> call causes the activation reference count to increment from 0 to 1, <b>PoFxActivateComponent</b> initiates a transition from the idle condition to the active condition. When a <b>PoFxIdleComponent</b> call causes the count to decrement from 1 to 0, <b>PoFxIdleComponent</b> initiates a transition from the active condition to the idle condition.</p>

<p>PoFx notifies the driver when a transition between the active condition and idle condition occurs. A <i>ComponentActiveConditionCallback</i> callback notifies the driver of a transition to the active condition, and a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406420">ComponentIdleConditionCallback</a> callback notifies the driver of a transition to the idle condition. When a <b>PoFxActivateComponent</b> or <b>PoFxIdleComponent</b> call simply increments or decrements the activation reference count without causing such a transition, the driver receives no notification.</p>

<p>Before a device driver can access a component in a device, the driver must first call <b>PoFxActivateComponent</b> to obtain an activation reference to the component. If the component is not already in the active condition, this call initiates a transition from the idle condition to the active condition. When this transition completes, PoFx calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh406416">ComponentActiveConditionCallback</a> routine to notify the driver. The driver can access the hardware registers in a component only when the component is in the active condition.</p>

<p>If the component is already in the active condition when <b>PoFxActivateComponent</b> is called, no transition is required, and the <i>ComponentActiveConditionCallback</i> routine is not called.</p>

<p>After a component enters the active condition, it remains in the active condition for as long as the driver holds one or more activation references on the component. To release an activation reference, the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406717">PoFxIdleComponent</a> routine. When the driver releases the last activation reference on a component, <b>PoFxIdleComponent</b> initiates a transition from the active condition to the idle condition. A component that is in the idle condition can potentially enter a low-power Fx state.</p>

<p>If <i>Flags</i> = <b>PO_FX_FLAG_BLOCKING</b>, the <b>PoFxActivateComponent</b> call is synchronous. If the component is already in the active condition, the call increments the activation reference count and returns without waiting. Otherwise, <b>PoFxActivateComponent</b> waits to return until the component completes the transition to the active condition. In this case, if the component is not already in the F0 state when the call occurs, <b>PoFxActivateComponent</b> calls the driver's <i>ComponentIdleStateCallback</i> routine to initiate the transition to F0. After the component enters the F0 state, <b>PoFxActivateComponent</b> calls the driver's <i>ComponentActiveConditionCallback</i> routine to inform the driver that the component is in the active condition. These callbacks occur in the same thread as the call to <b>PoFxActivateComponent</b>, and <b>PoFxActivateComponent</b> returns only after the <i>ComponentActiveConditionCallback</i> callback returns.</p>

<p>If <i>Flags</i> = <b>PO_FX_FLAG_ASYNC_ONLY</b>, the <b>PoFxActivateComponent</b> call is asynchronous. If the component is already in the active condition, the call increments the activation reference count and returns. Otherwise, <b>PoFxActivateComponent</b> schedules the <i>ComponentIdleStateCallback</i> (if necessary) and <i>ComponentActiveConditionCallback</i> callbacks to occur in another thread, and then returns without waiting for either callback to occur. The callbacks can occur before or after <b>PoFxActivateComponent</b> returns. The driver relies on the <i>ComponentActiveConditionCallback</i> callback to determine when the component completes the transition to the active condition.</p>

<p>The driver can set <i>Flags</i> = 0 to indicate that it does not care whether the <b>PoFxActivateComponent</b> call is synchronous or asynchronous. In this case, PoFx decides whether to make the call synchronous or asynchronous.</p>

<p>Two or more code paths in the same driver might need to concurrently access a particular component. The <b>PoFxActivateComponent</b> and <b>PoFxIdleComponent</b> routines use activation reference counts to enable the various parts of the driver to independently maintain access to the component without requiring the driver to centrally manage access to the component.</p>

<p>PoFx maintains an activation reference count for each component in a device. A <b>PoFxActivateComponent</b> call increments this count by one, and a <b>PoFxIdleComponent</b> call decrements the count by one. When the count is nonzero, the component either is in the active condition or is in the process of switching to the active condition. A component that has a count of zero either is in the idle condition or is in the process of switching to the idle condition.</p>

<p>When a <b>PoFxActivateComponent</b> call causes the activation reference count to increment from 0 to 1, <b>PoFxActivateComponent</b> initiates a transition from the idle condition to the active condition. When a <b>PoFxIdleComponent</b> call causes the count to decrement from 1 to 0, <b>PoFxIdleComponent</b> initiates a transition from the active condition to the idle condition.</p>

<p>PoFx notifies the driver when a transition between the active condition and idle condition occurs. A <i>ComponentActiveConditionCallback</i> callback notifies the driver of a transition to the active condition, and a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406420">ComponentIdleConditionCallback</a> callback notifies the driver of a transition to the idle condition. When a <b>PoFxActivateComponent</b> or <b>PoFxIdleComponent</b> call simply increments or decrements the activation reference count without causing such a transition, the driver receives no notification.</p>

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
<p>Available starting with  Windows 8.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406416">ComponentActiveConditionCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450931">ComponentIdleStateCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439585">PO_FX_DEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406717">PoFxIdleComponent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439521">PoFxRegisterDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxActivateComponent routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
