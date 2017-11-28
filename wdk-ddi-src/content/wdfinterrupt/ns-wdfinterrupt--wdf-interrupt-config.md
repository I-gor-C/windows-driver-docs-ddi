---
UID: NS.wdfinterrupt._WDF_INTERRUPT_CONFIG
title: WDF_INTERRUPT_CONFIG
author: windows-driver-content
description: The WDF_INTERRUPT_CONFIG structure contains configuration information for a device interrupt.
old-location: wdf\wdf_interrupt_config.htm
old-project: wdf
ms.assetid: 10eb623d-6778-4ccb-8ed4-9926c13dec5a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_INTERRUPT_CONFIG, WDF_INTERRUPT_CONFIG, *PWDF_INTERRUPT_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_INTERRUPT_CONFIG
req.alt-loc: wdfinterrupt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DIRQL
req.iface: 
req.product: Windows 10 or later.
---

# WDF_INTERRUPT_CONFIG structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_INTERRUPT_CONFIG</b> structure contains configuration information for a device interrupt.</p>


## -syntax

````
typedef struct _WDF_INTERRUPT_CONFIG {
  ULONG                           Size;
  WDFSPINLOCK                     SpinLock;
  WDF_TRI_STATE                   ShareVector;
  BOOLEAN                         FloatingSave;
  BOOLEAN                         AutomaticSerialization;
  PFN_WDF_INTERRUPT_ISR           EvtInterruptIsr;
  PFN_WDF_INTERRUPT_DPC           EvtInterruptDpc;
  PFN_WDF_INTERRUPT_ENABLE        EvtInterruptEnable;
  PFN_WDF_INTERRUPT_DISABLE       EvtInterruptDisable;
  PFN_WDF_INTERRUPT_WORKITEM      EvtInterruptWorkItem;
  PCM_PARTIAL_RESOURCE_DESCRIPTOR InterruptRaw;
  PCM_PARTIAL_RESOURCE_DESCRIPTOR InterruptTranslated;
  WDFWAITLOCK                     WaitLock;
  BOOLEAN                         PassiveHandling;
  WDF_TRI_STATE                   ReportInactiveOnPowerDown;
  BOOLEAN                         CanWakeDevice;
} WDF_INTERRUPT_CONFIG, *PWDF_INTERRUPT_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>SpinLock</b>

<dd>
<p>The handle to a framework spin-lock object, obtained by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff550042">WdfSpinLockCreate</a>, or <b>NULL</b>. If this parameter is <b>NULL</b>, the framework uses an internal spin-lock object. The framework acquires the spin lock before it calls the driver's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-synchronize.md">EvtInterruptSynchronize</a> event callback function and when the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff547340">WdfInterruptAcquireLock</a>. For passive-level interrupt handling, set to NULL.</p>
<p>Starting with UMDF version 2.0, UMDF always uses passive-level interrupt handling. In this case, set this member to NULL.</p>
</dd>

### -field <b>ShareVector</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed value. If this value is <b>WdfTrue</b>, the interrupt vector can be shared. If the value is <b>WdfFalse</b>, the interrupt vector cannot be shared. If the value is <b>WdfDefault</b>, the PnP manager uses the bus driver's value.</p>
</dd>

### -field <b>FloatingSave</b>

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the system will save the processor's floating point and MMX state when the device interrupts. If <b>FALSE</b>, the system does not save the floating point and MMX state. A driver should set this value to <b>TRUE</b> only if its <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a> callback function must use floating point or MMX registers. For more information about saving floating point and MMX state, see <a href="https://msdn.microsoft.com/73414084-4054-466a-b64c-5c81b224be92">Using Floating Point or MMX in a WDM Driver</a>.</p>
<p>This member is ignored starting in UMDF version 2.0.</p>
</dd>

### -field <b>AutomaticSerialization</b>

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the framework will synchronize execution of the interrupt object's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-dpc.md">EvtInterruptDpc</a>    or <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-workitem.md">EvtInterruptWorkItem</a> callback function with callback functions from other objects that are underneath the interrupt's parent  object.  For more information, see the following Remarks section.</p>
</dd>

### -field <b>EvtInterruptIsr</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a> callback function. This pointer cannot be <b>NULL</b>.</p>
</dd>

### -field <b>EvtInterruptDpc</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-dpc.md">EvtInterruptDpc</a> callback function, or <b>NULL</b>. The driver can provide <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-workitem.md">EvtInterruptWorkItem</a> or <i>EvtInterruptDpc</i>, but not both.</p>
</dd>

### -field <b>EvtInterruptEnable</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-enable.md">EvtInterruptEnable</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtInterruptDisable</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-disable.md">EvtInterruptDisable</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtInterruptWorkItem</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-workitem.md">EvtInterruptWorkItem</a> callback function, or <b>NULL</b>. The driver can provide <i>EvtInterruptWorkItem</i> or <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-dpc.md">EvtInterruptDpc</a>, but not both. The <b>EvtInterruptWorkItem</b> member is available in version 1.11 and later versions of KMDF.</p>
</dd>

### -field <b>InterruptRaw</b>

<dd>
<p>A pointer to the <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure that describes the <a href="wdf.raw_and_translated_resources">raw resources</a> that the system assigned to the interrupt. This member is only used if the interrupt is created in the <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> callback. The <b>InterruptRaw</b> member is available in version 1.11 and later versions of KMDF.</p>
</dd>

### -field <b>InterruptTranslated</b>

<dd>
<p>A pointer to the <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure that describes the <a href="wdf.raw_and_translated_resources">translated resources</a> that the system assigned to the interrupt. This member is only used if the interrupt is created in the <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> callback. The <b>InterruptTranslated</b> member is available in version 1.11 and later versions of KMDF.</p>
</dd>

### -field <b>WaitLock</b>

<dd>
<p>A handle to a framework wait-lock object, obtained by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551171">WdfWaitLockCreate</a>, or <b>NULL</b>. If <b>WaitLock</b> is non-<b>NULL</b>, <b>PassiveHandling</b> must be set to <b>TRUE</b>.  The <b>WaitLock</b> member is available in version 1.11 and later versions of KMDF.  For more information about <b>WaitLock</b>, see  <b>Remarks</b>.</p>
</dd>

### -field <b>PassiveHandling</b>

<dd>
<p>Set to <b>FALSE</b> for interrupt handling at the device's IRQL (DIRQL).
Set to <b>TRUE</b> for passive-level interrupt handling.
The <b>PassiveHandling</b> member is available in version 1.11 and later versions of KMDF. Starting in UMDF version 2.0, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552348">WDF_INTERRUPT_CONFIG_INIT</a> always sets this member to TRUE.</p>
</dd>

### -field <b>ReportInactiveOnPowerDown</b>

<dd>
<p>This member applies to KMDF only.</p>
<p> A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed value that applies only if the driver has not called <a href="https://msdn.microsoft.com/library/windows/hardware/ff546147">WdfDeviceInitSetPowerNotPageable</a>.  This member can have one of the following values:</p>
<dl>
<dd>
<p><b>WdfTrue</b> - KMDF reports the interrupt inactive when the device transitions to a low-power (Dx) state.        In operating systems prior to Windows 8, the framework's behavior matches that described for  <b>WdfFalse</b>.</p>
<p>
<div class="alert"><b>Note</b>  If <b>CanWakeDevice</b> is set to <b>TRUE</b> and <b>ReportInactiveOnPowerDown</b> is set to <b>WdfTrue</b>, the framework does not report  the interrupt inactive when the device transitions to a low-power state.</div>
<div> </div>
</p>
</dd>
<dd>
<p><b>WdfFalse</b> - KMDF disconnects the interrupt when the device transitions to a low-power (Dx) state.</p>
</dd>
<dd>
<p><b>WdfDefault</b> - On ARM-based platforms, the framework's behavior matches that described for  <b>WdfTrue</b>. On other platforms, the framework's behavior matches that described for  <b>WdfFalse</b>.</p>
</dd>
</dl>
<p>The <b>ReportInactiveOnPowerDown</b> member is available in version 1.11 and later versions of KMDF. It is not available in UMDF version 2.0.</p>
<p>For more information about reporting an interrupt inactive, see <a href="https://msdn.microsoft.com/library/windows/hardware/jj158878">Making an ISR Active or Inactive</a>.</p>
</dd>

### -field <b>CanWakeDevice</b>

<dd>
<p>A Boolean value that indicates whether the interrupt is used to wake the device from a low-power state.
If <b>FALSE</b>, the interrupt is not used to wake the device. If <b>TRUE</b>, the interrupt is used to wake the device.
The <b>CanWakeDevice</b> member is available starting in KMDF version 1.13 and UMDF version 2.0.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_INTERRUPT_CONFIG</b> structure is used as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547345">WdfInterruptCreate</a>. </p>

<p>To initialize a <b>WDF_INTERRUPT_CONFIG</b> structure, your driver must first call <a href="https://msdn.microsoft.com/library/windows/hardware/ff552348">WDF_INTERRUPT_CONFIG_INIT</a> and then fill in structure members that <b>WDF_INTERRUPT_CONFIG_INIT</b> does not initialize.</p>

<p>If <b>AutomaticSerialization</b> is TRUE, the following rules apply:</p>

<p>The driver can use this structure's <b>WaitLock</b> member to provide its own interrupt lock for <a href="wdf.supporting_passive_level_interrupts">passive-level interrupt handling</a>. If the driver sets <b>PassiveHandling</b> to TRUE but not does provide a <b>WaitLock</b>, the framework creates an interrupt lock internally. The framework acquires the passive-level interrupt lock before calling the following callback functions:<dl>
<dd>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-enable.md">EvtInterruptEnable</a>
</dd>
<dd>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-disable.md">EvtInterruptDisable</a>
</dd>
<dd>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-synchronize.md">EvtInterruptSynchronize</a>
</dd>
<dd>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a>
</dd>
</dl>
</p><dl>
<dd>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-enable.md">EvtInterruptEnable</a>
</dd>
<dd>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-disable.md">EvtInterruptDisable</a>
</dd>
<dd>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-synchronize.md">EvtInterruptSynchronize</a>
</dd>
<dd>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a>
</dd>
</dl><p>For more information about <b>AutomaticSerialization</b> and synchronizing driver callback functions, see <a href="wdf.synchronization_techniques_for_wdf_drivers">Synchronization Techniques for Framework-Based Drivers</a>.</p>

<p>By default, KMDF function drivers are power pageable. A driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff546147">WdfDeviceInitSetPowerNotPageable</a> 
to specify that it is non-power pageable.</p>

<p>In KMDF versions earlier than 1.11, the framework always disconnects interrupts of power pageable drivers when the device transitions into a low-power (Dx) state. Starting in KMDF version 1.11, you can change this behavior by setting the <b>ReportInactiveOnPowerDown</b> member of this structure.  For non-power pageable drivers, interrupts remain connected when Dx state transitions occur, regardless of the value set in <b>ReportInactiveOnPowerDown</b>.</p>

<p>If a UMDF driver sets <b>ReportInactiveOnPowerDown</b>, the value is ignored.</p>

<p>For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.</p>

<p>The driver can use this structure's <b>CanWakeDevice</b> member to create an interrupt that can be used to bring the device from a low-power Dx state back to D0. The driver's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a> callback routine  is scheduled to run at IRQL = PASSIVE_LEVEL after the device enters D0.</p>

<p>For more information, see <a href="wdf.using_an_interrupt_to_wake_a_device">Using an Interrupt to Wake a Device</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546147">WdfDeviceInitSetPowerNotPageable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546766">WdfDeviceInitSetPowerPageable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547345">WdfInterruptCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547371">WdfInterruptQueueDpcForIsr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550042">WdfSpinLockCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552348">WDF_INTERRUPT_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>
</dt>
<dt>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-disable.md">EvtInterruptDisable</a>
</dt>
<dt>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-dpc.md">EvtInterruptDpc</a>
</dt>
<dt>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-enable.md">EvtInterruptEnable</a>
</dt>
<dt>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_INTERRUPT_CONFIG structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
