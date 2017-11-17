---
UID: NF.ntddk.IoRegisterDriverReinitialization
title: IoRegisterDriverReinitialization
author: windows-driver-content
description: The IoRegisterDriverReinitialization routine is called by a driver during its initialization or reinitialization to register its Reinitialize routine to be called again before the driver's and, possibly the system's, initialization is complete.
old-location: kernel\ioregisterdriverreinitialization.htm
ms.assetid: bdee26f9-e108-4753-b2e5-a1427212bce9
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoRegisterDriverReinitialization
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlIoPassive5, PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
ms.keywords: IoRegisterDriverReinitialization
req.iface: 
---

# IoRegisterDriverReinitialization function



## -description
<p>The <b>IoRegisterDriverReinitialization</b> routine is called by a driver during its initialization or reinitialization to register its <a href="https://msdn.microsoft.com/library/windows/hardware/ff561022">Reinitialize</a> routine to be called again before the driver's and, possibly the system's, initialization is complete.</p>


## -syntax

````
VOID IoRegisterDriverReinitialization(
  _In_     PDRIVER_OBJECT       DriverObject,
  _In_     PDRIVER_REINITIALIZE DriverReinitializationRoutine,
  _In_opt_ PVOID                Context
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>Pointer to the driver object that was input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine.</p>
</dd>

### -param <i>DriverReinitializationRoutine</i> [in]

<dd>
<p>Pointer to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff561022">Reinitialize</a> routine. </p>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>Pointer to the context to be passed to the driver's <i>Reinitialize</i> routine.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A driver can call this routine only if its <i>DriverEntry</i> routine will return STATUS_SUCCESS. If the driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff561022">Reinitialize</a> routine must use the registry, the <i>DriverEntry</i> routine should include a copy of the string to which  <i>RegistryPath</i> points as part of the context passed to the <i>Reinitialize</i> routine in this call.</p>

<p>If the driver is loaded dynamically, it is possible for this to occur during a normally running system, so all references to the reinitialization queue must be synchronized.</p>

<p>The <i>Count</i> input to a <i>DriverReinitializationRoutine</i> indicates how many times this routine has been called, including the current call.</p>

<p>The <i>DriverEntry</i> routine can call <b>IoRegisterDriverReinitialization</b> only once. If the <i>Reinitialize</i> routine should be run again after any other drivers' <i>Reinitialize</i> routines have returned control, the <i>Reinitialize</i> routine also can call <b>IoRegisterDriverReinitialization</b> as many times as the driver's <i>Reinitialize</i> routine should be run.</p>

<p>Usually, a driver with a <i>Reinitialize</i> routine is a higher-level driver that controls both PnP and legacy devices. Such a driver must not only create device objects for the devices that the PnP manager detects (and for which the PnP manager calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine), the driver must also create device objects for legacy devices that the PnP manager does not detect. A driver can use a <i>Reinitialize</i> routine to create those device objects and layer the driver over the next-lower driver for the underlying device.</p>

<p>A driver can call this routine only if its <i>DriverEntry</i> routine will return STATUS_SUCCESS. If the driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff561022">Reinitialize</a> routine must use the registry, the <i>DriverEntry</i> routine should include a copy of the string to which  <i>RegistryPath</i> points as part of the context passed to the <i>Reinitialize</i> routine in this call.</p>

<p>If the driver is loaded dynamically, it is possible for this to occur during a normally running system, so all references to the reinitialization queue must be synchronized.</p>

<p>The <i>Count</i> input to a <i>DriverReinitializationRoutine</i> indicates how many times this routine has been called, including the current call.</p>

<p>The <i>DriverEntry</i> routine can call <b>IoRegisterDriverReinitialization</b> only once. If the <i>Reinitialize</i> routine should be run again after any other drivers' <i>Reinitialize</i> routines have returned control, the <i>Reinitialize</i> routine also can call <b>IoRegisterDriverReinitialization</b> as many times as the driver's <i>Reinitialize</i> routine should be run.</p>

<p>Usually, a driver with a <i>Reinitialize</i> routine is a higher-level driver that controls both PnP and legacy devices. Such a driver must not only create device objects for the devices that the PnP manager detects (and for which the PnP manager calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine), the driver must also create device objects for legacy devices that the PnP manager does not detect. A driver can use a <i>Reinitialize</i> routine to create those device objects and layer the driver over the next-lower driver for the underlying device.</p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547796">IrqlIoPassive5</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549494">IoRegisterBootDriverReinitialization</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoRegisterDriverReinitialization routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
