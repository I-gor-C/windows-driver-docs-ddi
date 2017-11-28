---
UID: NF.ks.KsAddDevice
title: KsAddDevice
author: windows-driver-content
description: The KsAddDevice function is the default AddDevice handler installed by KsInitializeDriver.
old-location: stream\ksadddevice.htm
old-project: stream
ms.assetid: e7be1bb8-eb8a-4ebd-b824-bbaa41b21ca5
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsAddDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsAddDevice
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# KsAddDevice function



## -description
<p>The<b> KsAddDevice </b>function is the default <i>AddDevice</i> handler installed by <a href="https://msdn.microsoft.com/library/windows/hardware/ff562683">KsInitializeDriver</a>. </p>


## -syntax

````
NTSTATUS KsAddDevice(
  _In_ PDRIVER_OBJECT DriverObject,
  _In_ PDEVICE_OBJECT PhysicalDeviceObject
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>A pointer to the WDM driver object for the minidriver.</p>
</dd>

### -param <i>PhysicalDeviceObject</i> [in]

<dd>
<p>A pointer to the WDM physical device object.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS indicating the device was successfully created or an error status from <a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff562682">KsInitializeDevice</a>.</p>

## -remarks
<p>Normally, an AVStream minidriver does not call this function directly.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554081">AddDevice Routine for AVStream Minidrivers</a>.</p>

<p><b>KsAddDevice</b> extracts the device descriptor stored in the device extension allocated from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562683">KsInitializeDriver</a> and creates the device described by it. If <b>KsInitializeDriver</b> is not used to initialize the driver, this function creates a device with the default characteristics and no filter factories. The minidriver always has the option of calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff561647">KsCreateDevice</a> directly, in which case the driver extension is not used by AVStream. Because <b>KsAddDevice</b> calls <b>KsCreateDevice</b>, drivers that call <b>KsAddDevice</b> should not call <b>KsCreateDevice</b> separately.</p>

<p>Normally, an AVStream minidriver does not call this function directly.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554081">AddDevice Routine for AVStream Minidrivers</a>.</p>

<p><b>KsAddDevice</b> extracts the device descriptor stored in the device extension allocated from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562683">KsInitializeDriver</a> and creates the device described by it. If <b>KsInitializeDriver</b> is not used to initialize the driver, this function creates a device with the default characteristics and no filter factories. The minidriver always has the option of calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff561647">KsCreateDevice</a> directly, in which case the driver extension is not used by AVStream. Because <b>KsAddDevice</b> calls <b>KsCreateDevice</b>, drivers that call <b>KsAddDevice</b> should not call <b>KsCreateDevice</b> separately.</p>

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
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561647">KsCreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562682">KsInitializeDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562683">KsInitializeDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561709">KsDispatchIrp</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsAddDevice function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
