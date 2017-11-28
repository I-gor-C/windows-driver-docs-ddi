---
UID: NF.wdfinterrupt.WdfInterruptReportInactive
title: WdfInterruptReportInactive
author: windows-driver-content
description: The WdfInterruptReportInactive method informs the system that the interrupt is no longer active and the driver is not expecting interrupt requests on the associated lines.
old-location: wdf\wdfinterruptreportinactive.htm
old-project: wdf
ms.assetid: 322E70AA-5825-4199-B822-B48B12E62393
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfInterruptReportInactive
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WdfInterruptReportInactive
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfInterruptReportInactive function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>
   
  The <b>WdfInterruptReportInactive</b> method informs the system that the interrupt is no longer active and the driver is not expecting interrupt requests on the associated lines.</p>


## -syntax

````
void WdfInterruptReportInactive(
  _In_ WDFINTERRUPT Interrupt
);
````


## -parameters
<dl>

### -param <i>Interrupt</i> [in]

<dd>
<p>A handle to a framework interrupt object.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>Only drivers that implement functional state power management call <b>WdfInterruptReportInactive</b>.</p>

<p>When a driver calls <b>WdfInterruptReportInactive</b>, the power management framework (PoFx) can then  perform related power management tasks.</p>

<p>Typically, a driver calls <b>WdfInterruptReportInactive</b> from either its  <a href="https://msdn.microsoft.com/library/windows/hardware/hh406420">ComponentIdleConditionCallback</a> routine, or from <a href="https://msdn.microsoft.com/library/windows/hardware/hh450931">ComponentIdleStateCallback</a> when <i>State</i> is greater than zero  (indicating a low-power Fx state).</p>

<p>If your driver calls this method on an operating system earlier than Windows 8, <a href="wdf.using_kmdf_verifier">the framework's verifier</a> reports an error.</p>

<p>The following example shows how a driver might call <b>WdfInterruptReportInactive</b> from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450931">ComponentIdleStateCallback</a> routine of a KMDF driver. The driver registers a single component by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451097">WdfDeviceWdmAssignPowerFrameworkSettings</a>.</p>

<p>Only drivers that implement functional state power management call <b>WdfInterruptReportInactive</b>.</p>

<p>When a driver calls <b>WdfInterruptReportInactive</b>, the power management framework (PoFx) can then  perform related power management tasks.</p>

<p>Typically, a driver calls <b>WdfInterruptReportInactive</b> from either its  <a href="https://msdn.microsoft.com/library/windows/hardware/hh406420">ComponentIdleConditionCallback</a> routine, or from <a href="https://msdn.microsoft.com/library/windows/hardware/hh450931">ComponentIdleStateCallback</a> when <i>State</i> is greater than zero  (indicating a low-power Fx state).</p>

<p>If your driver calls this method on an operating system earlier than Windows 8, <a href="wdf.using_kmdf_verifier">the framework's verifier</a> reports an error.</p>

<p>The following example shows how a driver might call <b>WdfInterruptReportInactive</b> from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450931">ComponentIdleStateCallback</a> routine of a KMDF driver. The driver registers a single component by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451097">WdfDeviceWdmAssignPowerFrameworkSettings</a>.</p>

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
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
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
<dt>Wdfinterrupt.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439273">WdfInterruptReportActive</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfInterruptReportInactive method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
