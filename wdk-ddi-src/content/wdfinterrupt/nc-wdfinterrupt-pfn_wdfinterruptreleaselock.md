---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTRELEASELOCK
title: PFN_WDFINTERRUPTRELEASELOCK
author: windows-driver-content
description: The WdfInterruptReleaseLock method ends a code sequence that executes at the device's DIRQL while holding an interrupt object's spin lock.
old-location: wdf\wdfinterruptreleaselock.htm
old-project: wdf
ms.assetid: a3b68f6f-d482-4350-a5b8-9fe6afdefb69
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _WDF_COINSTALLER_INSTALL_OPTIONS, PWDF_COINSTALLER_INSTALL_OPTIONS, *PWDF_COINSTALLER_INSTALL_OPTIONS, WDF_COINSTALLER_INSTALL_OPTIONS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfInterruptReleaseLock
req.alt-loc: wdfinterrupt.h
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2, WdfInterruptLock, WdfInterruptLockRelease
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
req.product: Windows 10 or later.
---

# PFN_WDFINTERRUPTRELEASELOCK callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfInterruptReleaseLock</b> method ends a code sequence that executes at the device's DIRQL while holding an interrupt object's spin lock. 

For passive level interrupt objects, the method ends a code sequence that executes at passive level while holding an interrupt object's passive lock.



## -prototype

````
VOID WdfInterruptReleaseLock(
  _In_ WDFINTERRUPT Interrupt
);
````


## -parameters

### -param Interrupt [in]

A handle to a framework interrupt object.


## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
The <b>WdfInterruptReleaseLock</b> method releases the specified interrupt object's spin lock or wait lock and returns the processor's IRQL to the level that it was set to before the driver called <a href="wdf.wdfinterruptacquirelock">WdfInterruptAcquireLock</a>.

Your driver cannot call <b>WdfInterruptReleaseLock</b> before the framework has called the driver's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt_wdf_interrupt_enable.md">EvtInterruptEnable</a> callback function or after the framework has called the driver's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt_wdf_interrupt_disable.md">EvtInterruptDisable</a> callback function.

For more information about the <b>WdfInterruptReleaseLock</b> method, see <a href="wdf.synchronizing_interrupt_code">Synchronizing Interrupt Code</a>.

For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.

This method must be called at the DIRQL that was set by <a href="wdf.wdfinterruptacquirelock">WdfInterruptAcquireLock</a>.

For passive level interrupts, the driver must call <b>WdfInterruptReleaseLock</b> at IRQL = PASSIVE_LEVEL.

For a code example that uses <b>WdfInterruptReleaseLock</b>, see <a href="wdf.wdfinterruptacquirelock">WdfInterruptAcquireLock</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfinterrupt.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
See Remarks section.

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_wdfinterruptlock">WdfInterruptLock</a>, <a href="devtest.kmdf_wdfinterruptlockrelease">WdfInterruptLockRelease</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfinterruptacquirelock">WdfInterruptAcquireLock</a>
</dt>
<dt>
<a href="wdf.wdfinterruptsynchronize">WdfInterruptSynchronize</a>
</dt>
<dt>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt_wdf_interrupt_disable.md">EvtInterruptDisable</a>
</dt>
<dt>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt_wdf_interrupt_enable.md">EvtInterruptEnable</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfInterruptReleaseLock callback function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

