---
UID: NC.wudfinterrupt.WUDF_INTERRUPT_ISR
title: WUDF_INTERRUPT_ISR
author: windows-driver-content
description: A driver's OnInterruptIsr event callback function services a hardware interrupt.
old-location: wdf\oninterruptisr.htm
ms.assetid: D4B8182A-67A5-4D64-A95C-5EB6A1C1E4F0
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfinterrupt.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: OnInterruptIsr
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
ms.keywords: WUDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT
req.iface: 
req.product: Windows 10 or later.
---

# WUDF_INTERRUPT_ISR callback



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>A driver's <i>OnInterruptIsr</i> event callback function services a hardware interrupt.</p>


## -prototype

````
WUDF_INTERRUPT_ISR OnInterruptIsr;

BOOLEAN OnInterruptIsr(
  _In_ IWDFInterrupt *pInterrupt,
  _In_ ULONG         MessageID,
  _In_ ULONG         Reserved
)
{ ... }
````


## -parameters
<dl>

### -param <i>pInterrupt</i> [in]

<dd>
<p>A pointer to <a href="https://msdn.microsoft.com/library/windows/hardware/hh451283">IWDFInterrupt</a> interface.</p>
</dd>

### -param <i>MessageID</i> [in]

<dd>
<p>If the device is using message-signaled interrupts (MSIs), this parameter is the message number that identifies the device's hardware interrupt message. Otherwise, this value is 0.</p>
</dd>

### -param <i>Reserved</i> [in]

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -returns
<p>Returns TRUE if the driver acknowledges ownership of the interrupt, and has stopped and acknowledged the interrupt on its device. Otherwise, returns FALSE.</p>

## -remarks
<p>To register an <i>OnInterruptIsr</i> callback function, your driver must place the callback function's address in a <a href="https://msdn.microsoft.com/library/windows/hardware/hh464084">WUDF_INTERRUPT_CONFIG</a> structure before calling <a href="https://msdn.microsoft.com/EE68BED8-5FDC-4590-8E95-B228F1DFD32D">IWDFDevice3::CreateInterrupt</a>.</p>

<p>
The <i>OnInterruptIsr</i> callback function is a UMDF driver's interrupt service routine (ISR), which is called at PASSIVE_LEVEL when a hardware interrupt occurs.</p>

<p>For an edge-triggered interrupt or message-signaled interrupt (MSI), the framework calls <i>OnInterruptIsr</i> outside of the operating system's interrupt dispatch context. This is because UMDF allows only non-shared edge-triggered or MSI interrupts, and the driver does not need to interact with its hardware within this context.</p>

<p>For a level-triggered interrupt, the framework calls <i>OnInterruptIsr</i> in the context of the operating system's interrupt dispatch. As a result, the operating system's interrupt dispatch thread is blocked in kernel-mode waiting for a response from the driver.</p>

<p>Typically, <i>OnInterruptIsr</i> saves any volatile information that might be lost and clears the hardware interrupt. For a level-triggered interrupt, the driver should stop and acknowledge the interrupt on the device and then return TRUE if it owns the interrupt. The driver should do any further processing in an <a href="https://msdn.microsoft.com/10677BC2-2A98-41C8-BAE9-1FA3689ACD93">OnInterruptWorkItem</a> callback. To queue a work item, the driver calls the <a href="https://msdn.microsoft.com/5C6DC011-4032-4DB6-AE17-88E510DF9A3A">IWDFInterrupt::QueueWorkItemForIsr</a> method.</p>

<p>
For more information about handling interrupts in UMDF drivers, see <a href="wdf.accessing_hardware_and_handling_interrupts">Accessing Hardware and Handling Interrupts</a>.</p>

<p>The function type is declared in <i>Wudfinterrupt.h</i>, as follows.</p>

<p>To define an <i>OnInterruptIsr</i> callback function that is named <i>MyInterruptIsr</i>, you must first provide a function declaration that SDV and other verification tools require, as follows:</p>

<p>Then, implement your callback function as follows:</p>

<p>To register an <i>OnInterruptIsr</i> callback function, your driver must place the callback function's address in a <a href="https://msdn.microsoft.com/library/windows/hardware/hh464084">WUDF_INTERRUPT_CONFIG</a> structure before calling <a href="https://msdn.microsoft.com/EE68BED8-5FDC-4590-8E95-B228F1DFD32D">IWDFDevice3::CreateInterrupt</a>.</p>

<p>
The <i>OnInterruptIsr</i> callback function is a UMDF driver's interrupt service routine (ISR), which is called at PASSIVE_LEVEL when a hardware interrupt occurs.</p>

<p>For an edge-triggered interrupt or message-signaled interrupt (MSI), the framework calls <i>OnInterruptIsr</i> outside of the operating system's interrupt dispatch context. This is because UMDF allows only non-shared edge-triggered or MSI interrupts, and the driver does not need to interact with its hardware within this context.</p>

<p>For a level-triggered interrupt, the framework calls <i>OnInterruptIsr</i> in the context of the operating system's interrupt dispatch. As a result, the operating system's interrupt dispatch thread is blocked in kernel-mode waiting for a response from the driver.</p>

<p>Typically, <i>OnInterruptIsr</i> saves any volatile information that might be lost and clears the hardware interrupt. For a level-triggered interrupt, the driver should stop and acknowledge the interrupt on the device and then return TRUE if it owns the interrupt. The driver should do any further processing in an <a href="https://msdn.microsoft.com/10677BC2-2A98-41C8-BAE9-1FA3689ACD93">OnInterruptWorkItem</a> callback. To queue a work item, the driver calls the <a href="https://msdn.microsoft.com/5C6DC011-4032-4DB6-AE17-88E510DF9A3A">IWDFInterrupt::QueueWorkItemForIsr</a> method.</p>

<p>
For more information about handling interrupts in UMDF drivers, see <a href="wdf.accessing_hardware_and_handling_interrupts">Accessing Hardware and Handling Interrupts</a>.</p>

<p>The function type is declared in <i>Wudfinterrupt.h</i>, as follows.</p>

<p>To define an <i>OnInterruptIsr</i> callback function that is named <i>MyInterruptIsr</i>, you must first provide a function declaration that SDV and other verification tools require, as follows:</p>

<p>Then, implement your callback function as follows:</p>

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
<dt>Wudfinterrupt.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464084">WUDF_INTERRUPT_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/EE68BED8-5FDC-4590-8E95-B228F1DFD32D">IWDFDevice3::CreateInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/10677BC2-2A98-41C8-BAE9-1FA3689ACD93">OnInterruptWorkItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WUDF_INTERRUPT_ISR callback function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
