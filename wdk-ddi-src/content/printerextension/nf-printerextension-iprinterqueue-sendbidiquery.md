---
UID: NF.printerextension.IPrinterQueue.SendBidiQuery
title: IPrinterQueue::SendBidiQuery
author: windows-driver-content
description: Performs an asynchronous refresh operation with the specified query, and invokes the IPrinterQueueEvent::OnBidiResponseReceived method.
old-location: print\iprinterqueue_sendbidiquery.htm
old-project: print
ms.assetid: E98A121A-514A-4437-A542-E8629697B7EA
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrinterQueue, SendBidiQuery, IPrinterQueue::SendBidiQuery
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: printerextension.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrinterQueue.SendBidiQuery
req.alt-loc: Printerextension.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: IPrinterQueue
req.product: Windows 10 or later.
---

# IPrinterQueue::SendBidiQuery method



## -description
<p>Performs an asynchronous refresh operation with the specified query, and invokes the <a href="print.iprinterqueueevent_onbidiresponsereceived">IPrinterQueueEvent::OnBidiResponseReceived</a> method.</p>


## -syntax

````
HRESULT SendBidiQuery(
  [in] BSTR bstrBidiQuery
);
````


## -parameters
<dl>

### -param bstrBidiQuery [in]

<dd>
<p>The specified query.</p>
</dd>
</dl>

## -returns
<p>This method returns an <b>HRESULT</b> value.</p>

## -remarks
<p>When the <b>SendBidiQuery</b> method is called, it immediately raises the <a href="print.iprinterqueueevent_onbidiresponsereceived">IPrinterQueueEvent::OnBidiResponseReceived</a> event, if there is a cached response available.  The print system then starts an asynchronous operation to use the <a href="http://msdn.microsoft.com/en-us/library/dd183365(v=vs.85)">Bidi Communication Interfaces</a>. At this point <b>SendBidiQuery</b> returns, thus unblocking the caller.  When the asynchronous operation completes, the print system raises the <b>IPrinterQueueEvent::OnBidiResponseReceived</b> event again. <b>SendBidiQuery</b> is decoupled from its associated response on purpose. The decoupling is done because, in the case where there is no cached data, the resulting latency can be due to many factors and an immediate response cannot be expected.  Additionally the caller may receive multiple responses based on whether there is cached data, and whether there is a response from the device.</p>

<p>Using the <a href="http://msdn.microsoft.com/en-us/library/dd183365(v=vs.85)">Bidi Communication Interfaces</a> causes the port monitor to refresh the underlying requested values. In the case of USB, if a JavaScript component is available, then the JavaScript code is invoked to refresh the requested values.</p>

<p>The cache is also updated in the following situations:</p>

<p><b>At predetermined intervals</b></p>

<p>
<dl>
<dd>For WSD devices the data is updated when the device reports changes via events.</dd>
<dd>For TCP &amp; USB devices the refresh interval is based on where the Bidi value is defined.
All standard Bidi values (as defined by the port monitor’s embedded Bidi files) are refreshed at an interval that is preset by the port monitors. If the specific Bidi Query is part of the IHV Bidi Extension, then the refresh interval is specified in the XML extension file for each individual value.</dd>
</dl>
</p>

<p><b>When printer configuration changes</b></p>

<p>
<dl>
<dd>For example, when a WSD-based device raises an event to let the spooler (WSDMon) know that something about the device has changed. In other words, the printer configuration has changed.</dd>
</dl>
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Printerextension.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><a href="http://msdn.microsoft.com/en-us/library/dd183365(v=vs.85)">Bidi Communication Interfaces</a></dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprinterqueue.md">IPrinterQueue</a>
</dt>
<dt>
<a href="print.iprinterqueueevent_onbidiresponsereceived">IPrinterQueueEvent::OnBidiResponseReceived</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterQueue::SendBidiQuery method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
