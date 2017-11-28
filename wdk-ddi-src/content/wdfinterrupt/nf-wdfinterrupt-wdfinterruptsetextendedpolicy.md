---
UID: NF.wdfinterrupt.WdfInterruptSetExtendedPolicy
title: WdfInterruptSetExtendedPolicy
author: windows-driver-content
description: The WdfInterruptSetExtendedPolicy method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt.
old-location: wdf\wdfinterruptsetextendedpolicy.htm
old-project: wdf
ms.assetid: 043c15dc-ebd7-4d91-8f65-d89d6064cc7c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfInterruptSetExtendedPolicy
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.9
req.umdf-ver: 2.0
req.alt-api: WdfInterruptSetExtendedPolicy
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfInterruptSetExtendedPolicy function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfInterruptSetExtendedPolicy</b> method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt.</p>


## -syntax

````
VOID WdfInterruptSetExtendedPolicy(
  _In_ WDFINTERRUPT                   Interrupt,
  _In_ PWDF_INTERRUPT_EXTENDED_POLICY PolicyAndGroup
);
````


## -parameters
<dl>

### -param <i>Interrupt</i> [in]

<dd>
<p>A handle to a framework interrupt object.</p>
</dd>

### -param <i>PolicyAndGroup</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552349">WDF_INTERRUPT_EXTENDED_POLICY</a> structure that the caller allocates and initializes.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Windows Vista and later versions of the operating system allow drivers to use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547387">WdfInterruptSetPolicy</a> method to specify an interrupt's priority, processor affinity, and affinity policy. In addition, versions 1.9 and later of KMDF allow drivers to use the <b>WdfInterruptSetExtendedPolicy</b> method to specify an interrupt's priority, processor affinity, affinity policy, and processor group.</p>

<p>For information about how to use the registry to override the values that <b>WdfInterruptSetExtendedPolicy</b> sets, see <a href="https://msdn.microsoft.com/e36a52d0-3a94-4017-b4a1-0b41f737523c">Interrupt Affinity and Priority</a>.</p>

<p>If a driver is running on an operating system version that is earlier than Windows 7, the framework ignores the value that the driver specifies for the processor group number when it calls <b>WdfInterruptSetExtendedPolicy</b>.</p>

<p>If a driver is running on an operating system version that is earlier than Windows Vista, the framework ignores all values that the driver specifies when it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff547387">WdfInterruptSetPolicy</a> or <b>WdfInterruptSetExtendedPolicy</b>.</p>

<p>For more information about registry values and INF sections that specify an interrupt's priority, processor affinity, and affinity policy, see <a href="https://msdn.microsoft.com/e36a52d0-3a94-4017-b4a1-0b41f737523c">Interrupt Affinity and Priority</a>.</p>

<p>If a driver calls <b>WdfInterruptSetExtendedPolicy</b>, it typically does so in its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function, after calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547345">WdfInterruptCreate</a>.</p>

<p>If your driver creates interrupts in <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a>, do not use <a href="https://msdn.microsoft.com/library/windows/hardware/ff547387">WdfInterruptSetPolicy</a> or <b>WdfInterruptSetExtendedPolicy</b>. Instead, you can instead apply policy in <a href="wdf.evtdevicefilteraddresourcerequirements">EvtDeviceFilterAddResourceRequirements</a>, by directly manipulating the interrupt resource requirement that this callback function receives in its <i>IoResourceRequirementsList</i> parameter.</p>

<p>For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.</p>

<p>The following code example calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff552350">WDF_INTERRUPT_EXTENDED_POLICY_INIT</a> to initialize a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552349">WDF_INTERRUPT_EXTENDED_POLICY</a> structure; sets values for the policy, priority, and target processor set; and calls <b>WdfInterruptSetExtendedPolicy</b>. The example sets normal priority for the interrupt and assigns the interrupt to processor 0 in processor group 2. </p>

<p>Windows Vista and later versions of the operating system allow drivers to use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547387">WdfInterruptSetPolicy</a> method to specify an interrupt's priority, processor affinity, and affinity policy. In addition, versions 1.9 and later of KMDF allow drivers to use the <b>WdfInterruptSetExtendedPolicy</b> method to specify an interrupt's priority, processor affinity, affinity policy, and processor group.</p>

<p>For information about how to use the registry to override the values that <b>WdfInterruptSetExtendedPolicy</b> sets, see <a href="https://msdn.microsoft.com/e36a52d0-3a94-4017-b4a1-0b41f737523c">Interrupt Affinity and Priority</a>.</p>

<p>If a driver is running on an operating system version that is earlier than Windows 7, the framework ignores the value that the driver specifies for the processor group number when it calls <b>WdfInterruptSetExtendedPolicy</b>.</p>

<p>If a driver is running on an operating system version that is earlier than Windows Vista, the framework ignores all values that the driver specifies when it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff547387">WdfInterruptSetPolicy</a> or <b>WdfInterruptSetExtendedPolicy</b>.</p>

<p>For more information about registry values and INF sections that specify an interrupt's priority, processor affinity, and affinity policy, see <a href="https://msdn.microsoft.com/e36a52d0-3a94-4017-b4a1-0b41f737523c">Interrupt Affinity and Priority</a>.</p>

<p>If a driver calls <b>WdfInterruptSetExtendedPolicy</b>, it typically does so in its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function, after calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547345">WdfInterruptCreate</a>.</p>

<p>If your driver creates interrupts in <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a>, do not use <a href="https://msdn.microsoft.com/library/windows/hardware/ff547387">WdfInterruptSetPolicy</a> or <b>WdfInterruptSetExtendedPolicy</b>. Instead, you can instead apply policy in <a href="wdf.evtdevicefilteraddresourcerequirements">EvtDeviceFilterAddResourceRequirements</a>, by directly manipulating the interrupt resource requirement that this callback function receives in its <i>IoResourceRequirementsList</i> parameter.</p>

<p>For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.</p>

<p>The following code example calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff552350">WDF_INTERRUPT_EXTENDED_POLICY_INIT</a> to initialize a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552349">WDF_INTERRUPT_EXTENDED_POLICY</a> structure; sets values for the policy, priority, and target processor set; and calls <b>WdfInterruptSetExtendedPolicy</b>. The example sets normal priority for the interrupt and assigns the interrupt to processor 0 in processor group 2. </p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
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
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547387">WdfInterruptSetPolicy</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfInterruptSetExtendedPolicy method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
