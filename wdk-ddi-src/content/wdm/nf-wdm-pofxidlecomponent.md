---
UID: NF.wdm.PoFxIdleComponent
title: PoFxIdleComponent
author: windows-driver-content
description: The PoFxIdleComponent routine decrements the activation reference count on the specified component.
old-location: kernel\pofxidlecomponent.htm
old-project: kernel
ms.assetid: 07282994-5E04-432D-85A6-4677DB2DA84A
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PoFxIdleComponent
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
req.alt-api: PoFxIdleComponent
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

# PoFxIdleComponent function



## -description
<p>The <b>PoFxIdleComponent</b> routine decrements the activation reference count on the specified component.</p>


## -syntax

````
VOID PoFxIdleComponent(
  _In_ POHANDLE Handle,
  _In_ ULONG    Component,
  _In_ ULONG    Flags
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>A handle that represents the registration of the device with the power management framework (PoFx). The device driver previously received this handle from the <a href="..\wdm\nf-wdm-pofxregisterdevice.md">PoFxRegisterDevice</a> routine.</p>
</dd>

### -param <i>Component</i> [in]

<dd>
<p>The index that identifies the component. This parameter is an index into the <b>Components</b> array in the <a href="kernel.po_fx_device">PO_FX_DEVICE</a> structure that the device driver used to register the device with PoFx. If the <b>Components</b> array contains N elements, component indexes range from 0 to N–1.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>The flags for the idle operation. Set this member to zero or to one of the following flag <a href="kernel.po_fx_flag_xxx">PO_FX_FLAG_XXX</a> bits:</p>
<ul>
<li><b>PO_FX_FLAG_BLOCKING</b></li>
<li><b>PO_FX_FLAG_ASYNC_ONLY</b></li>
</ul>
<p>These two flag bits are mutually exclusive. For more information, see Remarks.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>A device driver calls <b>PoFxIdleComponent</b> to release an activation reference to a component in a device. The driver obtained the activation reference in a previous call to the <a href="..\wdm\nf-wdm-pofxactivatecomponent.md">PoFxActivateComponent</a> routine. The driver should hold an activation reference on a component only while the driver needs to access the component. To hold an activation reference on a component that is not being used prevents the component from entering a low-power Fx state.</p>

<p>If the driver holds no other activation references to the component, <b>PoFxIdleComponent</b> initiates a transition from the active condition to the idle condition. When this transition completes, PoFx calls the driver's <a href="kernel.componentidleconditioncallback">ComponentIdleConditionCallback</a> routine to notify the driver. If the driver retains one or more additional activation references on the component, the component stays in the active condition, and the <i>ComponentIdleConditionCallback</i> routine is not called.</p>

<p>PoFx maintains an activation reference count for each component in the device. The <b>PoFxActivateComponent</b> routine increments this count, and <b>PoFxIdleComponent</b> decrements it. The component remains in the active condition while this count is nonzero. When the driver releases its last activation reference to a component, the count decrements to zero and the component enters the idle condition. After the component enters the idle condition, PoFx can potentially switch the component to a low-power Fx state. For more information, see <a href="..\wdm\nf-wdm-pofxactivatecomponent.md">PoFxActivateComponent</a>.</p>

<p>If <i>Flags</i> = <b>PO_FX_FLAG_BLOCKING</b>, the <b>PoFxIdleComponent</b> call is synchronous. In this case, <b>PoFxIdleComponent</b> waits to return until the component completes the transition to the idle condition. <b>PoFxIdleComponent</b> calls the driver's <i>ComponentIdleConditionCallback</i> callback routine to inform the driver that the component is in the idle condition. This callback occurs in the same thread as the call to <b>PoFxIdleComponent</b>, and <b>PoFxIdleComponent</b> returns only after the <i>ComponentIdleConditionCallback</i> callback returns.</p>

<p>If <i>Flags</i> = <b>PO_FX_FLAG_ASYNC_ONLY</b>, the <b>PoFxIdleComponent</b> call is asynchronous. In this case, <b>PoFxIdleComponent</b> schedules the <i>ComponentIdleConditionCallback</i> callback to occur in another thread, and then returns without waiting for the callback to occur. The callback can occur before or after <b>PoFxIdleComponent</b> returns. The driver should rely on the <i>ComponentIdleConditionCallback</i> callback to determine when the component completes the transition to the idle condition. Until this callback occurs, the driver should assume that the component might still be in the active condition.</p>

<p>The driver can set <i>Flags</i> = 0 to indicate that it does not care whether the <b>PoFxIdleComponent</b> call is synchronous or asynchronous. In this case, PoFx decides whether to make the call synchronous or asynchronous.</p>

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
<a href="kernel.componentidleconditioncallback">ComponentIdleConditionCallback</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-pofxactivatecomponent.md">PoFxActivateComponent</a>
</dt>
<dt>
<a href="kernel.po_fx_device">PO_FX_DEVICE</a>
</dt>
<dt>
<a href="kernel.po_fx_flag_xxx">PO_FX_FLAG_XXX</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-pofxregisterdevice.md">PoFxRegisterDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxIdleComponent routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
