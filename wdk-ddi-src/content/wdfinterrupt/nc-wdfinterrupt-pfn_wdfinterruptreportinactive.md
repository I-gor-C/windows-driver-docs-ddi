---
UID: NC:wdfinterrupt.PFN_WDFINTERRUPTREPORTINACTIVE
title: PFN_WDFINTERRUPTREPORTINACTIVE function
author: windows-driver-content
description: The WdfInterruptReportInactive method informs the system that the interrupt is no longer active and the driver is not expecting interrupt requests on the associated lines.
old-location: wdf\wdfinterruptreportinactive.htm
old-project: wdf
ms.assetid: 322E70AA-5825-4199-B822-B48B12E62393
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: PFN_WDFINTERRUPTREPORTINACTIVE
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
req.typenames: WDF_COINSTALLER_INSTALL_OPTIONS, *PWDF_COINSTALLER_INSTALL_OPTIONS
req.product: Windows 10 or later.
---

# PFN_WDFINTERRUPTREPORTINACTIVE function



## -description
<p class="CCE_Message">[Applies to KMDF only]


   
  The <b>WdfInterruptReportInactive</b> method informs the system that the interrupt is no longer active and the driver is not expecting interrupt requests on the associated lines.



## -syntax

````
void WdfInterruptReportInactive(
  _In_ WDFINTERRUPT Interrupt
);
````


## -parameters

### -param Interrupt [in]

A handle to a framework interrupt object.


## -returns
This method does not return a value.


## -remarks
Only drivers that implement functional state power management call <b>WdfInterruptReportInactive</b>.

When a driver calls <b>WdfInterruptReportInactive</b>, the power management framework (PoFx) can then  perform related power management tasks.

Typically, a driver calls <b>WdfInterruptReportInactive</b> from either its  <a href="https://msdn.microsoft.com/library/windows/hardware/hh406420">ComponentIdleConditionCallback</a> routine, or from <a href="https://msdn.microsoft.com/library/windows/hardware/hh450931">ComponentIdleStateCallback</a> when <i>State</i> is greater than zero  (indicating a low-power Fx state).

If your driver calls this method on an operating system earlier than Windows 8, <a href="wdf.using_kmdf_verifier">the framework's verifier</a> reports an error.

The following example shows how a driver might call <b>WdfInterruptReportInactive</b> from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450931">ComponentIdleStateCallback</a> routine of a KMDF driver. The driver registers a single component by calling <a href="..\wdfdevice\nf-wdfdevice-wdfdevicewdmassignpowerframeworksettings.md">WdfDeviceWdmAssignPowerFrameworkSettings</a>.


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
Minimum support

</th>
<td width="70%">
Windows 8

</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.11

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
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="https://msdn.microsoft.com/51db6f3c-45cb-46a7-9dd4-2bab67893fea">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;=DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptreportactive.md">WdfInterruptReportActive</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfInterruptReportInactive method%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

