---
UID: NF.wudfddi.IWDFInterrupt.AcquireInterruptLock
title: IWDFInterrupt::AcquireInterruptLock
author: windows-driver-content
description: The AcquireInterruptLock method begins a code sequence that executes while holding an interrupt object's lock.
old-location: wdf\iwdfinterrupt_acquireinterruptlock.htm
ms.assetid: 2ED55AEC-2446-4E66-AAFD-A22BAB3FC9C7
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IWDFInterrupt.AcquireInterruptLock
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
ms.keywords: IWDFInterrupt, AcquireInterruptLock, IWDFInterrupt::AcquireInterruptLock
req.iface: IWDFInterrupt
req.product: Windows 10 or later.
---

# IWDFInterrupt::AcquireInterruptLock method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>AcquireInterruptLock</b> method begins a code sequence that executes while holding an interrupt object's lock.</p>


## -syntax

````
void AcquireInterruptLock();
````


## -parameters


## -returns
<p>This method does not return a value.</p>

<p>This method does not return a value.</p>

<p>This method does not return a value.</p>

## -remarks
<p>When a driver calls <b>AcquireInterruptLock</b>, the system acquires the framework's interrupt lock.</p>

<p>When the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a>, the system releases the interrupt lock.</p>

<p>You can use <b>AcquireInterruptLock</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a> if your driver must execute a few lines of code without being preempted and with interrupt servicing disabled.</p>

<p>

Your driver cannot call <b>AcquireInterruptLock</b> before the framework has called the driver's <a href="https://msdn.microsoft.com/6C091427-59FF-4101-ACD6-353C959794F6">OnInterruptEnable</a> callback function or after the framework has called the driver's <a href="https://msdn.microsoft.com/3ADBD4C2-075E-4988-BF13-EB0C3E0C02BF">OnInterruptDisable</a> callback function.

After your driver calls <b>AcquireInterruptLock</b>, it must not call the method again for the same interrupt object before calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a>.

</p>

<p>When running in an arbitrary thread, such as an I/O queue callback method, drivers must call <a href="https://msdn.microsoft.com/4A109CDF-C5DE-4BAE-AA4E-294EA5CE86C5">IWDFInterrupt::TryToAcquireInterruptLock</a> instead of <b>IWDFInterrupt::AcquireInterruptLock</b>. For example, the driver calls <b>IWDFInterrupt::TryToAcquireInterruptLock</b> from <a href="https://msdn.microsoft.com/library/windows/hardware/ff556875">IQueueCallbackRead::OnRead</a>.</p>

<p>Doing so avoids the possibility of deadlock, as described in the following scenario.</p>

<p>The driver must not attempt to acquire the lock recursively. If connected to the debugger, the framework introduces a breakpoint in this scenario.</p>

<p>For more information about manual interrupt locking, see <a href="wdf.synchronizing_interrupt_code">Synchronizing Interrupt Code</a>.</p>

<p>For more information about handling interrupts in UMDF drivers, see <a href="wdf.accessing_hardware_and_handling_interrupts">Accessing Hardware and Handling Interrupts</a>.</p>

<p>When a driver calls <b>AcquireInterruptLock</b>, the system acquires the framework's interrupt lock.</p>

<p>When the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a>, the system releases the interrupt lock.</p>

<p>You can use <b>AcquireInterruptLock</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a> if your driver must execute a few lines of code without being preempted and with interrupt servicing disabled.</p>

<p>

Your driver cannot call <b>AcquireInterruptLock</b> before the framework has called the driver's <a href="https://msdn.microsoft.com/6C091427-59FF-4101-ACD6-353C959794F6">OnInterruptEnable</a> callback function or after the framework has called the driver's <a href="https://msdn.microsoft.com/3ADBD4C2-075E-4988-BF13-EB0C3E0C02BF">OnInterruptDisable</a> callback function.

After your driver calls <b>AcquireInterruptLock</b>, it must not call the method again for the same interrupt object before calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a>.

</p>

<p>When running in an arbitrary thread, such as an I/O queue callback method, drivers must call <a href="https://msdn.microsoft.com/4A109CDF-C5DE-4BAE-AA4E-294EA5CE86C5">IWDFInterrupt::TryToAcquireInterruptLock</a> instead of <b>IWDFInterrupt::AcquireInterruptLock</b>. For example, the driver calls <b>IWDFInterrupt::TryToAcquireInterruptLock</b> from <a href="https://msdn.microsoft.com/library/windows/hardware/ff556875">IQueueCallbackRead::OnRead</a>.</p>

<p>Doing so avoids the possibility of deadlock, as described in the following scenario.</p>

<p>The driver must not attempt to acquire the lock recursively. If connected to the debugger, the framework introduces a breakpoint in this scenario.</p>

<p>For more information about manual interrupt locking, see <a href="wdf.synchronizing_interrupt_code">Synchronizing Interrupt Code</a>.</p>

<p>For more information about handling interrupts in UMDF drivers, see <a href="wdf.accessing_hardware_and_handling_interrupts">Accessing Hardware and Handling Interrupts</a>.</p>

<p>When a driver calls <b>AcquireInterruptLock</b>, the system acquires the framework's interrupt lock.</p>

<p>When the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a>, the system releases the interrupt lock.</p>

<p>You can use <b>AcquireInterruptLock</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a> if your driver must execute a few lines of code without being preempted and with interrupt servicing disabled.</p>

<p>

Your driver cannot call <b>AcquireInterruptLock</b> before the framework has called the driver's <a href="https://msdn.microsoft.com/6C091427-59FF-4101-ACD6-353C959794F6">OnInterruptEnable</a> callback function or after the framework has called the driver's <a href="https://msdn.microsoft.com/3ADBD4C2-075E-4988-BF13-EB0C3E0C02BF">OnInterruptDisable</a> callback function.

After your driver calls <b>AcquireInterruptLock</b>, it must not call the method again for the same interrupt object before calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a>.

</p>

<p>When running in an arbitrary thread, such as an I/O queue callback method, drivers must call <a href="https://msdn.microsoft.com/4A109CDF-C5DE-4BAE-AA4E-294EA5CE86C5">IWDFInterrupt::TryToAcquireInterruptLock</a> instead of <b>IWDFInterrupt::AcquireInterruptLock</b>. For example, the driver calls <b>IWDFInterrupt::TryToAcquireInterruptLock</b> from <a href="https://msdn.microsoft.com/library/windows/hardware/ff556875">IQueueCallbackRead::OnRead</a>.</p>

<p>Doing so avoids the possibility of deadlock, as described in the following scenario.</p>

<p>The driver must not attempt to acquire the lock recursively. If connected to the debugger, the framework introduces a breakpoint in this scenario.</p>

<p>For more information about manual interrupt locking, see <a href="wdf.synchronizing_interrupt_code">Synchronizing Interrupt Code</a>.</p>

<p>For more information about handling interrupts in UMDF drivers, see <a href="wdf.accessing_hardware_and_handling_interrupts">Accessing Hardware and Handling Interrupts</a>.</p>

<p>When a driver calls <b>AcquireInterruptLock</b>, the system acquires the framework's interrupt lock.</p>

<p>When the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a>, the system releases the interrupt lock.</p>

<p>You can use <b>AcquireInterruptLock</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a> if your driver must execute a few lines of code without being preempted and with interrupt servicing disabled.</p>

<p>

Your driver cannot call <b>AcquireInterruptLock</b> before the framework has called the driver's <a href="https://msdn.microsoft.com/6C091427-59FF-4101-ACD6-353C959794F6">OnInterruptEnable</a> callback function or after the framework has called the driver's <a href="https://msdn.microsoft.com/3ADBD4C2-075E-4988-BF13-EB0C3E0C02BF">OnInterruptDisable</a> callback function.

After your driver calls <b>AcquireInterruptLock</b>, it must not call the method again for the same interrupt object before calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a>.

</p>

<p>When running in an arbitrary thread, such as an I/O queue callback method, drivers must call <a href="https://msdn.microsoft.com/4A109CDF-C5DE-4BAE-AA4E-294EA5CE86C5">IWDFInterrupt::TryToAcquireInterruptLock</a> instead of <b>IWDFInterrupt::AcquireInterruptLock</b>. For example, the driver calls <b>IWDFInterrupt::TryToAcquireInterruptLock</b> from <a href="https://msdn.microsoft.com/library/windows/hardware/ff556875">IQueueCallbackRead::OnRead</a>.</p>

<p>Doing so avoids the possibility of deadlock, as described in the following scenario.</p>

<p>The driver must not attempt to acquire the lock recursively. If connected to the debugger, the framework introduces a breakpoint in this scenario.</p>

<p>For more information about manual interrupt locking, see <a href="wdf.synchronizing_interrupt_code">Synchronizing Interrupt Code</a>.</p>

<p>For more information about handling interrupts in UMDF drivers, see <a href="wdf.accessing_hardware_and_handling_interrupts">Accessing Hardware and Handling Interrupts</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451283">IWDFInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/55ED21D9-D704-4E38-AFCF-B1D1FDB67DB3">IWDFInterrupt::ReleaseInterruptLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547340">WdfInterruptAcquireLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFInterrupt::AcquireInterruptLock method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
