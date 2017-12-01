---
UID: NE.wudfinterrupt._WDF_INTERRUPT_PRIORITY
title: WDF_INTERRUPT_PRIORITY
author: windows-driver-content
description: The WDF_INTERRUPT_PRIORITY enumeration type identifies relative priorities for device interrupts.
old-location: wdf\wdf_interrupt_priority_umdf.htm
old-project: wdf
ms.assetid: ECAB84B8-1C39-473C-A6AE-41D1EBDB1FF4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WUDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wudfinterrupt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: WDF_INTERRUPT_PRIORITY
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

# WDF_INTERRUPT_PRIORITY enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>
      The <a href="..\wudfinterrupt\ne-wudfinterrupt--wdf-interrupt-priority.md">WDF_INTERRUPT_PRIORITY</a> enumeration type identifies relative priorities for device interrupts.</p>


## -syntax

````
typedef enum _WDF_INTERRUPT_PRIORITY { 
  WdfIrqPriorityUndefined  = 0,
  WdfIrqPriorityLow        = 1,
  WdfIrqPriorityNormal     = 2,
  WdfIrqPriorityHigh       = 3
} WDF_INTERRUPT_PRIORITY, *PWDF_INTERRUPT_PRIORITY;
````


## -enum-fields
<dl>

### -field <a id="WdfIrqPriorityUndefined"></a><a id="wdfirqpriorityundefined"></a><a id="WDFIRQPRIORITYUNDEFINED"></a><b>WdfIrqPriorityUndefined</b>

<dd>
<p>The relative priority of a device's interrupt is undefined.</p>
</dd>

### -field <a id="WdfIrqPriorityLow"></a><a id="wdfirqprioritylow"></a><a id="WDFIRQPRIORITYLOW"></a><b>WdfIrqPriorityLow</b>

<dd>
<p>The device's interrupt has a relatively low priority, typically because the interrupt does not have to be serviced immediately.</p>
</dd>

### -field <a id="WdfIrqPriorityNormal"></a><a id="wdfirqprioritynormal"></a><a id="WDFIRQPRIORITYNORMAL"></a><b>WdfIrqPriorityNormal</b>

<dd>
<p>The device's interrupt priority is neither relatively low nor relatively high.</p>
</dd>

### -field <a id="WdfIrqPriorityHigh"></a><a id="wdfirqpriorityhigh"></a><a id="WDFIRQPRIORITYHIGH"></a><b>WdfIrqPriorityHigh</b>

<dd>
<p>The device's interrupt has a relatively high priority, typically because the interrupt must be serviced immediately.</p>
</dd>
</dl>

## -remarks
<p>The <a href="..\wudfinterrupt\ne-wudfinterrupt--wdf-interrupt-priority.md">WDF_INTERRUPT_PRIORITY</a> enumeration type is used as input to the <a href="wdf.iwdfinterrupt_setpolicy">IWDFInterrupt::SetPolicy</a> method.</p>

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
<a href="wdf.iwdfinterrupt_setpolicy">IWDFInterrupt::SetPolicy</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_INTERRUPT_PRIORITY enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
