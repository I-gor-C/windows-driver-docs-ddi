---
UID: NF.storport.StorPortPoFxActivateComponent
title: StorPortPoFxActivateComponent
author: windows-driver-content
description: The StorPortPoFxActivateComponent routine increments the activation reference count on the specified component of a storage device.
old-location: storage\storportpofxactivatecomponent.htm
old-project: storage
ms.assetid: 23872334-F9C3-4EB5-9B26-0BDB239D8F4E
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortPoFxActivateComponent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available in starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortPoFxActivateComponent
req.alt-loc: storport.lib,storport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: IRQL <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# StorPortPoFxActivateComponent function



## -description
<p>The <b>StorPortPoFxActivateComponent</b> routine increments the activation reference count on the specified component of a storage device.</p>


## -syntax

````
ULONG StorPortPoFxActivateComponent(
  _In_     PVOID               HwDeviceExtension,
  _In_opt_ PSTOR_ADDRESS       Address,
  _In_opt_ PSCSI_REQUEST_BLOCK Srb,
  _In_     ULONG               Component,
  _In_     ULONG               Flags
);
````


## -parameters
<dl>

### -param HwDeviceExtension [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param Address [in, optional]

<dd>
<p>The address of a storage device unit. This parameter is <b>NULL</b> when activating a storage adapter component.</p>
</dd>

### -param Srb [in, optional]

<dd>
<p>The SRB triggering the component activation. This parameter is <b>NULL</b> if the miniport is activating a device component for a request not sent through Storport.</p>
</dd>

### -param Component [in]

<dd>
<p>The index that identifies the component. This parameter is an index into the <b>Components</b> array in the <a href="..\storport\ns-storport--stor-pofx-device.md">STOR_POFX_DEVICE</a> structure that the miniport driver registered for the device with a call to <a href="..\storport\nf-storport-storportinitializepofxpower.md">StorPortInitializePoFxPower</a>. If the <b>Components</b> array contains N elements, component indexes range from 0 to N–1.</p>
</dd>

### -param Flags [in]

<dd>
<p>Not used. Set to 0.</p>
</dd>
</dl>

## -returns
<p>The <b>StorPortPoFxActivateComponent</b> routine returns one of these status codes:</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The storage device activation reference was successfully incremented and the component is in the active state.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Either <i>HwDeviceExtension</i> or <i>Device</i> is NULL.</p>

<p>-or-</p>

<p><i>Address</i> points to an invalid unit address structure.</p>

<p>-or-</p>

<p>The storage device specified by <i>Address</i> is not found.</p>

<p>-or-</p>

<p>The storage device is  not registered with the power management framework (PoFx).</p>

<p>-or-</p>

<p>The SRB pointed to by <i>Srb</i> is not sent from Storport.</p>

<p>-or-</p>

<p>The <i>Flags</i> parameter is nonzero.</p><dl>
<dt><b>STOR_STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>TThe adapter or unit does not support PoFx.</p><dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl><p>The current IRQL &gt; DISPATCH_LEVEL.</p><dl>
<dt><b>STOR_STATUS_BUSY</b></dt>
</dl><p> The storage device activation reference was successfully incremented but the component is still in the idle state</p>

<p> </p>

## -remarks
<p>Currently, both adapter devices and unit devices have maximum component count of 1. The index in <i>Component</i> must always be set to 0.</p>

<p>Each call to <b>StorPortPoFxActivateComponent</b> must be matched with a subsequent call to <a href="..\storport\nf-storport-storportpofxidlecomponent.md">StorPortPoFxIdleComponent</a>.</p>

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
<p>Available in starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>IRQL &lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\storport\ns-storport--stor-pofx-device.md">STOR_POFX_DEVICE</a>
</dt>
<dt>
<a href="..\storport\nf-storport-storportinitializepofxpower.md">StorPortInitializePoFxPower</a>
</dt>
<dt>
<a href="..\storport\nf-storport-storportpofxidlecomponent.md">StorPortPoFxIdleComponent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortPoFxActivateComponent routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
