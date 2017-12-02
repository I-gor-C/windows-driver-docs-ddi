---
UID: NF.storport.StorPortPoFxSetComponentLatency
title: StorPortPoFxSetComponentLatency
author: windows-driver-content
description: The StorPortPoFxSetComponentLatency routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified storage device component.
old-location: storage\storportpofxsetcomponentlatency.htm
old-project: storage
ms.assetid: F175ED42-3DB6-4568-96CA-EFC283B14887
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortPoFxSetComponentLatency
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
req.alt-api: StorPortPoFxSetComponentLatency
req.alt-loc: storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# StorPortPoFxSetComponentLatency function



## -description
<p>The <b>StorPortPoFxSetComponentLatency</b> routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified storage device component.</p>


## -syntax

````
ULONG StorPortPoFxSetComponentLatency(
  _In_     PVOID         HwDeviceExtension,
  _In_opt_ PSTOR_ADDRESS Address,
  _In_     ULONG         Component,
  _In_     ULONGLONG     Latency
);
````


## -parameters
<dl>

### -param HwDeviceExtension [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA). This is the device extension used to register the device in a prior call to <a href="..\storport\nf-storport-storportinitializepofxpower.md">StorPortInitializePoFxPower</a>.</p>
</dd>

### -param Address [in, optional]

<dd>
<p>The address of a storage device unit. This parameter is <b>NULL</b> when setting the latency of a storage adapter component.</p>
</dd>

### -param Component [in]

<dd>
<p>The index that identifies the component. This parameter is an index into the <b>Components</b> array in the <a href="..\storport\ns-storport--stor-pofx-device.md">STOR_POFX_DEVICE</a> structure that the miniport driver registered for the device with a call to <a href="..\storport\nf-storport-storportinitializepofxpower.md">StorPortInitializePoFxPower</a>. If the <b>Components</b> array contains N elements, component indexes range from 0 to N–1.</p>
</dd>

### -param Latency [in]

<dd>
<p>The time, in units of 100 nanoseconds, that the storage device component can tolerate  for a transition from an  idle state the active state.</p>
</dd>
</dl>

## -returns
<p>The <b>StorPortPoFxSetComponentLatency</b> routine returns one of these status codes:</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The component latency successfully set.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Either <i>HwDeviceExtension</i> or <i>Device</i> is NULL.</p>

<p>-or-</p>

<p><i>Address</i> points to an invalid unit address structure.</p>

<p>-or-</p>

<p>The storage device specified by <i>Address</i> is not found.</p>

<p>-or-</p>

<p>The index in <i>Component</i> specifies a component greater than the component count for the device.</p><dl>
<dt><b>STOR_STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The storage device is  not registered with the  power management framework (PoFx).</p><dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl><p>The current IRQL &gt; DISPATCH_LEVEL.</p>

<p> </p>

## -remarks


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
<a href="..\wdm\nf-wdm-pofxsetcomponentlatency.md">PoFxSetComponentLatency</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortPoFxSetComponentLatency routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
