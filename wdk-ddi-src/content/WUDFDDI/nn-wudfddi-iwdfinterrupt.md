---
UID: NN.wudfddi.IWDFInterrupt
title: IWDFInterrupt
author: windows-driver-content
description: This interface exposes an interrupt object.
old-location: wdf\iwdfinterrupt.htm
ms.assetid: 729A2361-6FE1-4096-AC8B-3D042326EE5C
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IWDFInterrupt
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
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IWDFInterrupt interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>This interface exposes an interrupt object.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFInterrupt</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff560200">IWDFObject</a>. <b>IWDFInterrupt</b> also has these types of members:</p>

<p>The <b>IWDFInterrupt</b> interface has these methods.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451289">AcquireInterruptLock</a> method begins a code sequence that executes while holding an interrupt object's lock.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh450971">Disable</a> method disables a specified device interrupt by calling the driver's <a href="https://msdn.microsoft.com/3ADBD4C2-075E-4988-BF13-EB0C3E0C02BF">OnInterruptDisable</a> callback function.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451004">Enable</a> method enables a specified device interrupt by calling the driver's <a href="https://msdn.microsoft.com/6C091427-59FF-4101-ACD6-353C959794F6">OnInterruptEnable</a> callback function.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451305">GetDevice</a> method returns the framework device object interface for this interrupt object.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451309">GetInfo</a> method retrieves information about a specified interrupt.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451314">QueueWorkItemForIsr</a> method queues a work item to process interrupt-related work outside of the interrupt service routine.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a> method ends a code sequence that executes while holding an interrupt object's lock.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451324">SetExtendedPolicy</a> method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt.
  </p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451328">SetPolicy</a> method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451332">TryToAcquireInterruptLock</a> method acquires the interrupt lock if no other thread has already acquired it.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFInterrupt</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff560200">IWDFObject</a>. <b>IWDFInterrupt</b> also has these types of members:</p>

<p>The <b>IWDFInterrupt</b> interface has these methods.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451289">AcquireInterruptLock</a> method begins a code sequence that executes while holding an interrupt object's lock.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh450971">Disable</a> method disables a specified device interrupt by calling the driver's <a href="https://msdn.microsoft.com/3ADBD4C2-075E-4988-BF13-EB0C3E0C02BF">OnInterruptDisable</a> callback function.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451004">Enable</a> method enables a specified device interrupt by calling the driver's <a href="https://msdn.microsoft.com/6C091427-59FF-4101-ACD6-353C959794F6">OnInterruptEnable</a> callback function.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451305">GetDevice</a> method returns the framework device object interface for this interrupt object.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451309">GetInfo</a> method retrieves information about a specified interrupt.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451314">QueueWorkItemForIsr</a> method queues a work item to process interrupt-related work outside of the interrupt service routine.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a> method ends a code sequence that executes while holding an interrupt object's lock.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451324">SetExtendedPolicy</a> method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt.
  </p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451328">SetPolicy</a> method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451332">TryToAcquireInterruptLock</a> method acquires the interrupt lock if no other thread has already acquired it.</p>

<p> </p>

## -members
<p>The <b>IWDFInterrupt</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451289">AcquireInterruptLock</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451289">AcquireInterruptLock</a> method begins a code sequence that executes while holding an interrupt object's lock.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450971">Disable</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh450971">Disable</a> method disables a specified device interrupt by calling the driver's <a href="https://msdn.microsoft.com/3ADBD4C2-075E-4988-BF13-EB0C3E0C02BF">OnInterruptDisable</a> callback function.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451004">Enable</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451004">Enable</a> method enables a specified device interrupt by calling the driver's <a href="https://msdn.microsoft.com/6C091427-59FF-4101-ACD6-353C959794F6">OnInterruptEnable</a> callback function.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451305">GetDevice</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451305">GetDevice</a> method returns the framework device object interface for this interrupt object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451309">GetInfo</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451309">GetInfo</a> method retrieves information about a specified interrupt.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451314">QueueWorkItemForIsr</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451314">QueueWorkItemForIsr</a> method queues a work item to process interrupt-related work outside of the interrupt service routine.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a> method ends a code sequence that executes while holding an interrupt object's lock.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451324">SetExtendedPolicy</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451324">SetExtendedPolicy</a> method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt.
  </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451328">SetPolicy</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451328">SetPolicy</a> method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451332">TryToAcquireInterruptLock</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451332">TryToAcquireInterruptLock</a> method acquires the interrupt lock if no other thread has already acquired it.</p>
</td>
</tr>
</table><p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451289">AcquireInterruptLock</a> method begins a code sequence that executes while holding an interrupt object's lock.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh450971">Disable</a> method disables a specified device interrupt by calling the driver's <a href="https://msdn.microsoft.com/3ADBD4C2-075E-4988-BF13-EB0C3E0C02BF">OnInterruptDisable</a> callback function.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451004">Enable</a> method enables a specified device interrupt by calling the driver's <a href="https://msdn.microsoft.com/6C091427-59FF-4101-ACD6-353C959794F6">OnInterruptEnable</a> callback function.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451305">GetDevice</a> method returns the framework device object interface for this interrupt object.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451309">GetInfo</a> method retrieves information about a specified interrupt.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451314">QueueWorkItemForIsr</a> method queues a work item to process interrupt-related work outside of the interrupt service routine.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451319">ReleaseInterruptLock</a> method ends a code sequence that executes while holding an interrupt object's lock.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451324">SetExtendedPolicy</a> method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt.
  </p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451328">SetPolicy</a> method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451332">TryToAcquireInterruptLock</a> method acquires the interrupt lock if no other thread has already acquired it.</p>

<p> </p>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560200">IWDFObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFInterrupt interface%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
