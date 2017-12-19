---
UID: NF.wdfinterrupt.WdfInterruptSetPolicy
title: WdfInterruptSetPolicy function
author: windows-driver-content
description: The WdfInterruptSetPolicy method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt.
old-location: wdf\wdfinterruptsetpolicy.htm
old-project: wdf
ms.assetid: f61bef13-d9b5-4e6a-8657-995a1fcbf7b1
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfInterruptSetPolicy
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfInterruptSetPolicy
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfInterruptSetPolicy function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfInterruptSetPolicy</b> method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt.



## -syntax

````
VOID WdfInterruptSetPolicy(
  _In_ WDFINTERRUPT           Interrupt,
  _In_ WDF_INTERRUPT_POLICY   Policy,
  _In_ WDF_INTERRUPT_PRIORITY Priority,
  _In_ KAFFINITY              TargetProcessorSet
);
````


## -parameters

### -param Interrupt [in]

A handle to a framework interrupt object.


### -param Policy [in]

A <a href="wdf.wdf_interrupt_policy">WDF_INTERRUPT_POLICY</a>-typed enumerator that specifies a processor affinity policy for the interrupt.


### -param Priority [in]

A <a href="wdf.wdf_interrupt_priority">WDF_INTERRUPT_PRIORITY</a>-typed enumerator that specifies a priority for the interrupt.


### -param TargetProcessorSet [in]

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a>-typed value that specifies a processor affinity for the interrupt, if the <i>Policy</i> parameter is set to <b>WdfIrqPolicySpecifiedProcessors</b>.


## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
Windows Vista and later versions of the operating system allow drivers to specify an interrupt's priority, processor affinity, and affinity policy. For information about how to use the registry to override the values that <b>WdfInterruptSetPolicy</b> sets, see <a href="https://msdn.microsoft.com/e36a52d0-3a94-4017-b4a1-0b41f737523c">Interrupt Affinity and Priority</a>.

If a driver is running on an operating system version that is earlier than Windows Vista, the framework ignores the values that the driver specifies when it calls <b>WdfInterruptSetPolicy</b>.

For more information about registry values and INF sections that specify an interrupt's priority, processor affinity, and affinity policy, see <a href="https://msdn.microsoft.com/e36a52d0-3a94-4017-b4a1-0b41f737523c">Interrupt Affinity and Priority</a>.

If a driver calls <b>WdfInterruptSetPolicy</b>, it typically does so in its <a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a> callback function, after calling <a href="wdf.wdfinterruptcreate">WdfInterruptCreate</a>.

If your driver creates interrupts in <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_prepare_hardware.md">EvtDevicePrepareHardware</a>, do not use <b>WdfInterruptSetPolicy</b> or <a href="wdf.wdfinterruptsetextendedpolicy">WdfInterruptSetExtendedPolicy</a>. Instead, apply policy in <a href="wdf.evtdevicefilteraddresourcerequirements">EvtDeviceFilterAddResourceRequirements</a>, by directly manipulating the interrupt resource requirement that this callback function receives in its <i>IoResourceRequirementsList</i> parameter.

For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.

The following code example assigns a device interrupt to processor 0, with normal priority.


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
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfinterruptcreate">WdfInterruptCreate</a>
</dt>
<dt>
<a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="wdf.wdfinterruptsetextendedpolicy">WdfInterruptSetExtendedPolicy</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfInterruptSetPolicy method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

