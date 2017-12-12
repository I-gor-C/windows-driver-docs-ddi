---
UID: NN.wudfddi.IWDFIoQueue
title: IWDFIoQueue
author: windows-driver-content
description: The IWDFIoQueue interface exposes an I/O queue object.
old-location: wdf\iwdfioqueue.htm
old-project: wdf
ms.assetid: 9a3ec86a-6a1d-4c65-a65a-7cb85bbd1ab8
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, POWER_ACTION, *PPOWER_ACTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
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
req.product: Windows 10 or later.
---

# IWDFIoQueue interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFIoQueue</b> interface exposes an I/O queue object.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFIoQueue</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a>. <b>IWDFIoQueue</b> also has these types of members:

The <b>IWDFIoQueue</b> interface has these methods.

The <a href="wdf.iwdfioqueue_configurerequestdispatching">ConfigureRequestDispatching</a> method configures the queuing of I/O requests of the given type.

The <a href="wdf.iwdfioqueue_drain">Drain</a> method directs the queue to reject new incoming I/O requests and allow already-queued requests to be delivered to the driver for processing.

The <a href="wdf.iwdfioqueue_drainsynchronously">DrainSynchronously</a> method directs the queue to reject new incoming I/O requests and allows already-queued requests to be delivered to the driver for processing. This method returns after all requests are completed or canceled.

The <a href="wdf.iwdfioqueue_getdevice">GetDevice</a> method retrieves the interface to the device that owns the I/O queue.

The <a href="wdf.iwdfioqueue_getstate">GetState</a> method retrieves the state of an I/O queue.

The <a href="wdf.iwdfioqueue_purge">Purge</a> method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. 

The <a href="wdf.iwdfioqueue_purgesynchronously">PurgeSynchronously</a> method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. The method returns after all outstanding requests are canceled.

The <a href="wdf.iwdfioqueue_retrievenextrequest">RetrieveNextRequest</a> method retrieves the next I/O request from an I/O queue.

The <a href="wdf.iwdfioqueue_retrievenextrequestbyfileobject">RetrieveNextRequestByFileObject</a> method retrieves from an I/O queue the next I/O request whose file object matches the specified file object.

The <a href="wdf.iwdfioqueue_start">Start</a> method enables an I/O queue to start receiving new I/O requests and delivering them to a driver.

The <a href="wdf.iwdfioqueue_stop">Stop</a> method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests.

The <a href="wdf.iwdfioqueue_stopsynchronously">StopSynchronously</a> method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. The method returns after all delivered requests have been canceled or completed.

 


## -members
The <b>IWDFIoQueue</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfioqueue_configurerequestdispatching">IWDFIoQueue::ConfigureRequestDispatching</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfioqueue_configurerequestdispatching">ConfigureRequestDispatching</a> method configures the queuing of I/O requests of the given type.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfioqueue_drain">IWDFIoQueue::Drain</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfioqueue_drain">Drain</a> method directs the queue to reject new incoming I/O requests and allow already-queued requests to be delivered to the driver for processing.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfioqueue_drainsynchronously">IWDFIoQueue::DrainSynchronously</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfioqueue_drainsynchronously">DrainSynchronously</a> method directs the queue to reject new incoming I/O requests and allows already-queued requests to be delivered to the driver for processing. This method returns after all requests are completed or canceled.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfioqueue_getdevice">IWDFIoQueue::GetDevice</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfioqueue_getdevice">GetDevice</a> method retrieves the interface to the device that owns the I/O queue.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfioqueue_getstate">IWDFIoQueue::GetState</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfioqueue_getstate">GetState</a> method retrieves the state of an I/O queue.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfioqueue_purge">IWDFIoQueue::Purge</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfioqueue_purge">Purge</a> method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. 

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfioqueue_purgesynchronously">IWDFIoQueue::PurgeSynchronously</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfioqueue_purgesynchronously">PurgeSynchronously</a> method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. The method returns after all outstanding requests are canceled.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfioqueue_retrievenextrequest">IWDFIoQueue::RetrieveNextRequest</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfioqueue_retrievenextrequest">RetrieveNextRequest</a> method retrieves the next I/O request from an I/O queue.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfioqueue_retrievenextrequestbyfileobject">IWDFIoQueue::RetrieveNextRequestByFileObject</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfioqueue_retrievenextrequestbyfileobject">RetrieveNextRequestByFileObject</a> method retrieves from an I/O queue the next I/O request whose file object matches the specified file object.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfioqueue_start">IWDFIoQueue::Start</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfioqueue_start">Start</a> method enables an I/O queue to start receiving new I/O requests and delivering them to a driver.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfioqueue_stop">IWDFIoQueue::Stop</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfioqueue_stop">Stop</a> method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfioqueue_stopsynchronously">IWDFIoQueue::StopSynchronously</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfioqueue_stopsynchronously">StopSynchronously</a> method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. The method returns after all delivered requests have been canceled or completed.

</td>
</tr>
</table>The <a href="wdf.iwdfioqueue_configurerequestdispatching">ConfigureRequestDispatching</a> method configures the queuing of I/O requests of the given type.

The <a href="wdf.iwdfioqueue_drain">Drain</a> method directs the queue to reject new incoming I/O requests and allow already-queued requests to be delivered to the driver for processing.

The <a href="wdf.iwdfioqueue_drainsynchronously">DrainSynchronously</a> method directs the queue to reject new incoming I/O requests and allows already-queued requests to be delivered to the driver for processing. This method returns after all requests are completed or canceled.

The <a href="wdf.iwdfioqueue_getdevice">GetDevice</a> method retrieves the interface to the device that owns the I/O queue.

The <a href="wdf.iwdfioqueue_getstate">GetState</a> method retrieves the state of an I/O queue.

The <a href="wdf.iwdfioqueue_purge">Purge</a> method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. 

The <a href="wdf.iwdfioqueue_purgesynchronously">PurgeSynchronously</a> method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. The method returns after all outstanding requests are canceled.

The <a href="wdf.iwdfioqueue_retrievenextrequest">RetrieveNextRequest</a> method retrieves the next I/O request from an I/O queue.

The <a href="wdf.iwdfioqueue_retrievenextrequestbyfileobject">RetrieveNextRequestByFileObject</a> method retrieves from an I/O queue the next I/O request whose file object matches the specified file object.

The <a href="wdf.iwdfioqueue_start">Start</a> method enables an I/O queue to start receiving new I/O requests and delivering them to a driver.

The <a href="wdf.iwdfioqueue_stop">Stop</a> method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests.

The <a href="wdf.iwdfioqueue_stopsynchronously">StopSynchronously</a> method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. The method returns after all delivered requests have been canceled or completed.

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.5

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>