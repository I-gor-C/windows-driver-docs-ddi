---
UID: NN.wudfddi.IWDFIoQueue
title: IWDFIoQueue
author: windows-driver-content
description: The IWDFIoQueue interface exposes an I/O queue object.
old-location: wdf\iwdfioqueue.htm
ms.assetid: 9a3ec86a-6a1d-4c65-a65a-7cb85bbd1ab8
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
req.umdf-ver: 1.5
req.alt-api: IWDFIoQueue
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

# IWDFIoQueue interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IWDFIoQueue</b> interface exposes an I/O queue object.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFIoQueue</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff560200">IWDFObject</a>. <b>IWDFIoQueue</b> also has these types of members:</p>

<p>The <b>IWDFIoQueue</b> interface has these methods.</p>

<p>The <a href="https://msdn.microsoft.com/376b0cc3-8189-499e-ad7f-5844f8cb4221">ConfigureRequestDispatching</a> method configures the queuing of I/O requests of the given type.</p>

<p>The <a href="https://msdn.microsoft.com/0356e8a7-de44-4b0f-9067-ca3bb04260d8">Drain</a> method directs the queue to reject new incoming I/O requests and allow already-queued requests to be delivered to the driver for processing.</p>

<p>The <a href="https://msdn.microsoft.com/6dc32dd7-e15b-4c93-92d1-5b7206ed98c0">DrainSynchronously</a> method directs the queue to reject new incoming I/O requests and allows already-queued requests to be delivered to the driver for processing. This method returns after all requests are completed or canceled.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451305">GetDevice</a> method retrieves the interface to the device that owns the I/O queue.</p>

<p>The <a href="https://msdn.microsoft.com/42dc9bbe-b00d-4187-ab07-0c268a061298">GetState</a> method retrieves the state of an I/O queue.</p>

<p>The <a href="https://msdn.microsoft.com/c7863713-850f-4516-aec5-9e851c36cf52">Purge</a> method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. </p>

<p>The <a href="https://msdn.microsoft.com/a714dffd-ca88-40cf-95ef-cf15384e0c02">PurgeSynchronously</a> method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. The method returns after all outstanding requests are canceled.</p>

<p>The <a href="https://msdn.microsoft.com/2d9dbfc8-7563-4c47-9b34-27cce2b847b2">RetrieveNextRequest</a> method retrieves the next I/O request from an I/O queue.</p>

<p>The <a href="https://msdn.microsoft.com/136b7582-b974-44fb-8026-e9678ae6623c">RetrieveNextRequestByFileObject</a> method retrieves from an I/O queue the next I/O request whose file object matches the specified file object.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh973223">Start</a> method enables an I/O queue to start receiving new I/O requests and delivering them to a driver.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn927275">Stop</a> method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests.</p>

<p>The <a href="https://msdn.microsoft.com/ea05cb82-8a50-48d8-a15c-b7ab58c01b30">StopSynchronously</a> method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. The method returns after all delivered requests have been canceled or completed.</p>

<p> </p>

## -members
<p>The <b>IWDFIoQueue</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558946">IWDFIoQueue::ConfigureRequestDispatching</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/376b0cc3-8189-499e-ad7f-5844f8cb4221">ConfigureRequestDispatching</a> method configures the queuing of I/O requests of the given type.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558951">IWDFIoQueue::Drain</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/0356e8a7-de44-4b0f-9067-ca3bb04260d8">Drain</a> method directs the queue to reject new incoming I/O requests and allow already-queued requests to be delivered to the driver for processing.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558954">IWDFIoQueue::DrainSynchronously</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/6dc32dd7-e15b-4c93-92d1-5b7206ed98c0">DrainSynchronously</a> method directs the queue to reject new incoming I/O requests and allows already-queued requests to be delivered to the driver for processing. This method returns after all requests are completed or canceled.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558957">IWDFIoQueue::GetDevice</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451305">GetDevice</a> method retrieves the interface to the device that owns the I/O queue.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558959">IWDFIoQueue::GetState</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/42dc9bbe-b00d-4187-ab07-0c268a061298">GetState</a> method retrieves the state of an I/O queue.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558962">IWDFIoQueue::Purge</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/c7863713-850f-4516-aec5-9e851c36cf52">Purge</a> method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558964">IWDFIoQueue::PurgeSynchronously</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/a714dffd-ca88-40cf-95ef-cf15384e0c02">PurgeSynchronously</a> method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. The method returns after all outstanding requests are canceled.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558967">IWDFIoQueue::RetrieveNextRequest</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/2d9dbfc8-7563-4c47-9b34-27cce2b847b2">RetrieveNextRequest</a> method retrieves the next I/O request from an I/O queue.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558971">IWDFIoQueue::RetrieveNextRequestByFileObject</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/136b7582-b974-44fb-8026-e9678ae6623c">RetrieveNextRequestByFileObject</a> method retrieves from an I/O queue the next I/O request whose file object matches the specified file object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558977">IWDFIoQueue::Start</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh973223">Start</a> method enables an I/O queue to start receiving new I/O requests and delivering them to a driver.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558980">IWDFIoQueue::Stop</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn927275">Stop</a> method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558981">IWDFIoQueue::StopSynchronously</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/ea05cb82-8a50-48d8-a15c-b7ab58c01b30">StopSynchronously</a> method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. The method returns after all delivered requests have been canceled or completed.</p>
</td>
</tr>
</table><p>The <a href="https://msdn.microsoft.com/376b0cc3-8189-499e-ad7f-5844f8cb4221">ConfigureRequestDispatching</a> method configures the queuing of I/O requests of the given type.</p>

<p>The <a href="https://msdn.microsoft.com/0356e8a7-de44-4b0f-9067-ca3bb04260d8">Drain</a> method directs the queue to reject new incoming I/O requests and allow already-queued requests to be delivered to the driver for processing.</p>

<p>The <a href="https://msdn.microsoft.com/6dc32dd7-e15b-4c93-92d1-5b7206ed98c0">DrainSynchronously</a> method directs the queue to reject new incoming I/O requests and allows already-queued requests to be delivered to the driver for processing. This method returns after all requests are completed or canceled.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451305">GetDevice</a> method retrieves the interface to the device that owns the I/O queue.</p>

<p>The <a href="https://msdn.microsoft.com/42dc9bbe-b00d-4187-ab07-0c268a061298">GetState</a> method retrieves the state of an I/O queue.</p>

<p>The <a href="https://msdn.microsoft.com/c7863713-850f-4516-aec5-9e851c36cf52">Purge</a> method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. </p>

<p>The <a href="https://msdn.microsoft.com/a714dffd-ca88-40cf-95ef-cf15384e0c02">PurgeSynchronously</a> method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. The method returns after all outstanding requests are canceled.</p>

<p>The <a href="https://msdn.microsoft.com/2d9dbfc8-7563-4c47-9b34-27cce2b847b2">RetrieveNextRequest</a> method retrieves the next I/O request from an I/O queue.</p>

<p>The <a href="https://msdn.microsoft.com/136b7582-b974-44fb-8026-e9678ae6623c">RetrieveNextRequestByFileObject</a> method retrieves from an I/O queue the next I/O request whose file object matches the specified file object.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh973223">Start</a> method enables an I/O queue to start receiving new I/O requests and delivering them to a driver.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn927275">Stop</a> method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests.</p>

<p>The <a href="https://msdn.microsoft.com/ea05cb82-8a50-48d8-a15c-b7ab58c01b30">StopSynchronously</a> method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. The method returns after all delivered requests have been canceled or completed.</p>

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
<p>1.5</p>
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