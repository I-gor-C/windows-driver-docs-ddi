---
UID: NC.wudfinterrupt.WUDF_INTERRUPT_ISR
title: WUDF_INTERRUPT_ISR
author: windows-driver-content
description: A driver's OnInterruptIsr event callback function services a hardware interrupt.
old-location: wdf\oninterruptisr.htm
old-project: wdf
ms.assetid: D4B8182A-67A5-4D64-A95C-5EB6A1C1E4F0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WUDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
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

### -param pInterrupt [in]

<dd>
<p>A pointer to <a href="..\wudfddi\nn-wudfddi-iwdfinterrupt.md">IWDFInterrupt</a> interface.</p>
</dd>

### -param MessageID [in]

<dd>
<p>If the device is using message-signaled interrupts (MSIs), this parameter is the message number that identifies the device's hardware interrupt message. Otherwise, this value is 0.</p>
</dd>

### -param Reserved [in]

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -returns
<p>Returns TRUE if the driver acknowledges ownership of the interrupt, and has stopped and acknowledged the interrupt on its device. Otherwise, returns FALSE.</p>

## -remarks
<p>To register an <i>OnInterruptIsr</i> callback function, your driver must place the callback function's address in a <a href="..\wudfinterrupt\ns-wudfinterrupt--wudf-interrupt-config.md">WUDF_INTERRUPT_CONFIG</a> structure before calling <a href="wdf.iwdfdevice3_createinterrupt">IWDFDevice3::CreateInterrupt</a>.</p>

<p>
The <i>OnInterruptIsr</i> callback function is a UMDF driver's interrupt service routine (ISR), which is called at PASSIVE_LEVEL when a hardware interrupt occurs.</p>

<p>For an edge-triggered interrupt or message-signaled interrupt (MSI), the framework calls <i>OnInterruptIsr</i> outside of the operating system's interrupt dispatch context. This is because UMDF allows only non-shared edge-triggered or MSI interrupts, and the driver does not need to interact with its hardware within this context.</p>

<p>For a level-triggered interrupt, the framework calls <i>OnInterruptIsr</i> in the context of the operating system's interrupt dispatch. As a result, the operating system's interrupt dispatch thread is blocked in kernel-mode waiting for a response from the driver.</p>

<p>Typically, <i>OnInterruptIsr</i> saves any volatile information that might be lost and clears the hardware interrupt. For a level-triggered interrupt, the driver should stop and acknowledge the interrupt on the device and then return TRUE if it owns the interrupt. The driver should do any further processing in an <a href="..\wudfinterrupt\nc-wudfinterrupt-wudf-interrupt-workitem.md">OnInterruptWorkItem</a> callback. To queue a work item, the driver calls the <a href="wdf.iwdfinterrupt_queueworkitemforisr">IWDFInterrupt::QueueWorkItemForIsr</a> method.</p>

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
<a href="..\wudfinterrupt\ns-wudfinterrupt--wudf-interrupt-config.md">WUDF_INTERRUPT_CONFIG</a>
</dt>
<dt>
<a href="wdf.iwdfdevice3_createinterrupt">IWDFDevice3::CreateInterrupt</a>
</dt>
<dt>
<a href="..\wudfinterrupt\nc-wudfinterrupt-wudf-interrupt-workitem.md">OnInterruptWorkItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WUDF_INTERRUPT_ISR callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
