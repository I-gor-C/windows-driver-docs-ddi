---
UID: NS.wudfinterrupt._WUDF_INTERRUPT_CONFIG
title: WUDF_INTERRUPT_CONFIG
author: windows-driver-content
description: The WUDF_INTERRUPT_CONFIG structure contains configuration information for a device interrupt.
old-location: wdf\wudf_interrupt_config.htm
old-project: wdf
ms.assetid: 7A849A10-2C47-42E2-8BEB-E1D979D3C893
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WUDF_INTERRUPT_CONFIG, WUDF_INTERRUPT_CONFIG, *PWUDF_INTERRUPT_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wudfinterrupt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: WUDF_INTERRUPT_CONFIG
req.alt-loc: Wudfinterrupt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# WUDF_INTERRUPT_CONFIG structure



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>
   The <b>WUDF_INTERRUPT_CONFIG</b> structure contains configuration information for a device interrupt.</p>


## -syntax

````
typedef struct _WUDF_INTERRUPT_CONFIG {
  ULONG                           Size;
  WDF_TRI_STATE                   ShareVector;
  BOOLEAN                         AutomaticSerialization;
  PFN_WUDF_INTERRUPT_ISR          OnInterruptIsr;
  PFN_WUDF_INTERRUPT_ENABLE       OnInterruptEnable;
  PFN_WUDF_INTERRUPT_DISABLE      OnInterruptDisable;
  PFN_WUDF_INTERRUPT_WORKITEM     OnInterruptWorkItem;
  PCM_PARTIAL_RESOURCE_DESCRIPTOR InterruptRaw;
  PCM_PARTIAL_RESOURCE_DESCRIPTOR InterruptTranslated;
} WUDF_INTERRUPT_CONFIG, *PWUDF_INTERRUPT_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>ShareVector</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed value. If this value is <b>WdfTrue</b>, the interrupt vector can be shared. If the value is <b>WdfFalse</b>, the interrupt vector cannot be shared. If the value is <b>WdfDefault</b> and the interrupt is level-triggered,  the Plug and Play manager uses the bus driver's value. If the value is <b>WdfDefault</b> and the interrupt is not level-triggered, the interrupt vector cannot be shared.</p>
</dd>

### -field <b>AutomaticSerialization</b>

<dd>
<p>A Boolean value that, if TRUE, indicates that the framework will synchronize execution of the interrupt object's <a href="..\wudfinterrupt\nc-wudfinterrupt-wudf-interrupt-workitem.md">OnInterruptWorkItem</a> callback function with other callback functions that use the framework's <a href="wdf.specifying_a_callback_synchronization_mode">callback synchronization</a> functionality.  See  Remarks for more information.</p>
</dd>

### -field <b>OnInterruptIsr</b>

<dd>
<p>A pointer to the driver's <a href="..\wudfinterrupt\nc-wudfinterrupt-wudf-interrupt-isr.md">OnInterruptIsr</a> callback function, or NULL.</p>
</dd>

### -field <b>OnInterruptEnable</b>

<dd>
<p>A pointer to the driver's <a href="..\wudfinterrupt\nc-wudfinterrupt-wudf-interrupt-enable.md">OnInterruptEnable</a> callback function, or NULL.</p>
</dd>

### -field <b>OnInterruptDisable</b>

<dd>
<p>A pointer to the driver's <a href="..\wudfinterrupt\nc-wudfinterrupt-wudf-interrupt-disable.md">OnInterruptDisable</a> callback function, or NULL.</p>
</dd>

### -field <b>OnInterruptWorkItem</b>

<dd>
<p>A pointer to the driver's <a href="..\wudfinterrupt\nc-wudfinterrupt-wudf-interrupt-workitem.md">OnInterruptWorkItem</a> callback function, or NULL.</p>
</dd>

### -field <b>InterruptRaw</b>

<dd>
<p>A pointer to the <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure that describes the <a href="wdf.raw_and_translated_resources">raw resources</a> that the system assigned to the interrupt. This member is only used if the interrupt is created in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439734">OnPrepareHardware</a> callback.</p>
</dd>

### -field <b>InterruptTranslated</b>

<dd>
<p>A pointer to the <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure that describes the <a href="wdf.raw_and_translated_resources">translated resources</a> that the system assigned to the interrupt. This member is only used if the interrupt is created in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439734">OnPrepareHardware</a> callback.</p>
</dd>
</dl>

## -remarks
<p>The <b>WUDF_INTERRUPT_CONFIG</b> structure is used as input to <a href="wdf.iwdfdevice3_createinterrupt">IWDFDevice3::CreateInterrupt</a>.</p>

<p>To initialize a <b>WUDF_INTERRUPT_CONFIG</b> structure, your driver should first call <a href="https://msdn.microsoft.com/library/windows/hardware/hh464089">WUDF_INTERRUPT_CONFIG_INIT</a> and then fill in structure members that <b>WUDF_INTERRUPT_CONFIG_INIT</b> does not initialize.</p>

<p>Before setting <b>AutomaticSerialization</b> to TRUE, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff556991">IWDFDeviceInitialize::SetLockingConstraint</a> with the <i>LockType</i> parameter set to <b>WdfDeviceLevel</b>.</p>

<p>Your driver should include Wudfwdm.h, which contains the definition of CM_PARTIAL_RESOURCE_DESCRIPTOR.</p>

<p>
UMDF supports edge-triggered, line-based interrupts and message-signaled interrupts (MSI) on all framework-supported operating systems. Because these types of interrupt resources are not shared, a driver that uses them should set the <b>ShareVector</b> member of this structure to WdfFalse or WdfUseDefault. If the driver specifies an invalid <b>ShareVector</b> value, the driver fails to start.</p>

## -requirements
<table>
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
<dt>Wudfinterrupt.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556991">IWDFDeviceInitialize::SetLockingConstraint</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464089">WUDF_INTERRUPT_CONFIG_INIT</a>
</dt>
<dt>
<a href="wdf.iwdfdevice3_createinterrupt">IWDFDevice3::CreateInterrupt</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WUDF_INTERRUPT_CONFIG structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
