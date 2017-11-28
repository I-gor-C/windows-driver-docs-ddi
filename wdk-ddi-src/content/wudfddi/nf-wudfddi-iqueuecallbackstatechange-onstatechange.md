---
UID: NF.wudfddi.IQueueCallbackStateChange.OnStateChange
title: IQueueCallbackStateChange::OnStateChange
author: windows-driver-content
description: The OnStateChange method is called when the state of the I/O queue object changes.
old-location: wdf\iqueuecallbackstatechange_onstatechange.htm
old-project: wdf
ms.assetid: 69a422a1-b878-496e-b1b9-e04b7c3db121
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IQueueCallbackStateChange, OnStateChange, IQueueCallbackStateChange::OnStateChange
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IQueueCallbackStateChange.OnStateChange
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: IQueueCallbackStateChange
req.product: Windows 10 or later.
---

# IQueueCallbackStateChange::OnStateChange method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OnStateChange</b> method is called when the state of the I/O queue object changes. </p>


## -syntax

````
void OnStateChange(
  [in] IWDFIoQueue        *pWdfQueue,
  [in] WDF_IO_QUEUE_STATE QueueState
);
````


## -parameters
<dl>

### -param <i>pWdfQueue</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558943">IWDFIoQueue</a> interface for the I/O queue object whose state changes. </p>
</dd>

### -param <i>QueueState</i> [in]

<dd>
<p>A valid bitwise OR of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561417">WDF_IO_QUEUE_STATE</a>-typed values that indicates status for the queue.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A driver registers the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556877">IQueueCallbackStateChange</a> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. The driver can optionally register the <b>IQueueCallbackStateChange</b> interface only for a manual queue. The driver must not register <b>IQueueCallbackStateChange</b> for a sequential or a parallel queue.</p>

<p>A driver registers the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556877">IQueueCallbackStateChange</a> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. The driver can optionally register the <b>IQueueCallbackStateChange</b> interface only for a manual queue. The driver must not register <b>IQueueCallbackStateChange</b> for a sequential or a parallel queue.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556877">IQueueCallbackStateChange</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558943">IWDFIoQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561417">WDF_IO_QUEUE_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IQueueCallbackStateChange::OnStateChange method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
