---
UID: NF.wdm.PoFxSetComponentResidency
title: PoFxSetComponentResidency
author: windows-driver-content
description: The PoFxSetComponentResidency routine sets the estimated time for how long a component is likely to remain idle after the component enters the idle condition.
old-location: kernel\pofxsetcomponentresidency.htm
old-project: kernel
ms.assetid: B4216BA1-FC5C-4A3B-BB74-E071BD2048F8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PoFxSetComponentResidency
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
req.alt-api: PoFxSetComponentResidency
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

# PoFxSetComponentResidency function



## -description
<p>The <b>PoFxSetComponentResidency</b> routine sets the estimated time for how long a component is likely to remain idle after the component enters the idle condition.</p>


## -syntax

````
VOID PoFxSetComponentResidency(
  _In_ POHANDLE  Handle,
  _In_ ULONG     Component,
  _In_ ULONGLONG Residency
);
````


## -parameters
<dl>

### -param Handle [in]

<dd>
<p>A handle that represents the registration of the device with the power management framework (PoFx). The device driver previously received this handle from the <a href="..\wdm\nf-wdm-pofxregisterdevice.md">PoFxRegisterDevice</a> routine.</p>
</dd>

### -param Component [in]

<dd>
<p>The index that identifies the component. This parameter is an index into the <b>Components</b> array in the <a href="kernel.po_fx_device">PO_FX_DEVICE</a> structure that the device driver used to register the device with PoFx. If the <b>Components</b> array contains N elements, component indexes range from 0 to N–1.</p>
</dd>

### -param Residency [in]

<dd>
<p>The estimated residency time, in 100-nanosecond units. This parameter is a hint to PoFx about how long the component is likely to remain idle after a transition from the active condition to the idle condition. For more information, see Remarks.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>The calling driver supplies an estimated residency time that PoFx can use as a hint to improve performance. PoFx uses this hint to select an appropriate low-power Fx state for a component that is in the idle condition.</p>

<p>The device driver can call <b>PoFxSetComponentResidency</b> each time a change in circumstances requires a change in the estimated residency time. After each call, the new estimated residency time remains in effect until the driver calls <b>PoFxSetComponentResidency</b> again to update it.</p>

<p>If a component is in the idle condition when <b>PoFxSetComponentResidency</b> is called, PoFx might change the component’s Fx state to accommodate the new estimated residency time specified by the caller.</p>

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