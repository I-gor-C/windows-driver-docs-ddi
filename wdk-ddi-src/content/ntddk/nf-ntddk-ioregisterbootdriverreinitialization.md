---
UID: NF.ntddk.IoRegisterBootDriverReinitialization
title: IoRegisterBootDriverReinitialization
author: windows-driver-content
description: The IoRegisterBootDriverReinitialization routine is called by a boot driver to register the driver's reinitialization routine with the I/O manager to be called after all devices have been enumerated and started.
old-location: kernel\ioregisterbootdriverreinitialization.htm
old-project: kernel
ms.assetid: af1c1f4b-7710-4cf7-9596-32d11db98abb
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoRegisterBootDriverReinitialization
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntifs.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoRegisterBootDriverReinitialization
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
---

# IoRegisterBootDriverReinitialization function



## -description
<p>The <b>IoRegisterBootDriverReinitialization</b> routine is called by a boot driver to register the driver's reinitialization routine with the I/O manager to be called after all devices have been enumerated and started.</p>


## -syntax

````
VOID IoRegisterBootDriverReinitialization(
  _In_     PDRIVER_OBJECT       DriverObject,
  _In_     PDRIVER_REINITIALIZE DriverReinitializationRoutine,
  _In_opt_ PVOID                Context
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>Pointer to the driver object for the boot driver to be reinitialized.</p>
</dd>

### -param <i>DriverReinitializationRoutine</i> [in]

<dd>
<p>Pointer to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff561022">Reinitialize</a> routine.</p>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>Optional context pointer to be passed to the driver's reinitialization routine.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A boot driver normally calls <b>IoRegisterBootDriverReinitialization</b> from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine, which is run during boot driver initialization. <b>IoRegisterBootDriverReinitialization</b> registers the driver's reinitialization callback routine to be called by the I/O manager after all devices have been enumerated and started. The <i>DriverReinitializationRoutine</i> is run in a system thread at IRQL = PASSIVE_LEVEL. </p>

<p>A driver should call <b>IoRegisterBootDriverReinitialization</b> only if its <i>DriverEntry</i> routine will return STATUS_SUCCESS. </p>

<p>If the <i>DriverReinitializationRoutine</i> uses the registry, the <i>DriverEntry</i> routine must include in <b>IoRegisterBootDriverReinitialization</b>'s <i>Context</i> parameter a copy of the string to which <i>DriverEntry</i>'s own <i>RegistryPath</i> parameter points. </p>

<p>The <i>DriverEntry</i> routine can call <b>IoRegisterBootDriverReinitialization</b> only once. If the reinitialization routine needs to be run more than once, the <i>DriverReinitializationRoutine</i> can call <b>IoRegisterBootDriverReinitialization</b> as many additional times as needed, using the <i>Count</i> parameter to keep track of the number of times the <i>DriverReinitializationRoutine</i> has been called. </p>

<p>A boot driver normally calls <b>IoRegisterBootDriverReinitialization</b> from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine, which is run during boot driver initialization. <b>IoRegisterBootDriverReinitialization</b> registers the driver's reinitialization callback routine to be called by the I/O manager after all devices have been enumerated and started. The <i>DriverReinitializationRoutine</i> is run in a system thread at IRQL = PASSIVE_LEVEL. </p>

<p>A driver should call <b>IoRegisterBootDriverReinitialization</b> only if its <i>DriverEntry</i> routine will return STATUS_SUCCESS. </p>

<p>If the <i>DriverReinitializationRoutine</i> uses the registry, the <i>DriverEntry</i> routine must include in <b>IoRegisterBootDriverReinitialization</b>'s <i>Context</i> parameter a copy of the string to which <i>DriverEntry</i>'s own <i>RegistryPath</i> parameter points. </p>

<p>The <i>DriverEntry</i> routine can call <b>IoRegisterBootDriverReinitialization</b> only once. If the reinitialization routine needs to be run more than once, the <i>DriverReinitializationRoutine</i> can call <b>IoRegisterBootDriverReinitialization</b> as many additional times as needed, using the <i>Count</i> parameter to keep track of the number of times the <i>DriverReinitializationRoutine</i> has been called. </p>

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
<dt>Ntddk.h (include Ntifs.h, Ntddk.h, or Ntifs.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549511">IoRegisterDriverReinitialization</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561022">Reinitialize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoRegisterBootDriverReinitialization routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
