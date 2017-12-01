---
UID: NF.printerextension.IPrinterQueueView.SetViewRange
title: IPrinterQueueView::SetViewRange
author: windows-driver-content
description: Sets the range of print jobs being monitored.
old-location: print\iprinterqueueview_setviewrange.htm
old-project: print
ms.assetid: DB3C0439-EB82-4E49-8FEA-003C1B4A9EE0
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrinterQueueView, SetViewRange, IPrinterQueueView::SetViewRange
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: printerextension.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrinterQueueView.SetViewRange
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
req.iface: IPrinterQueueView
req.product: Windows 10 or later.
---

# IPrinterQueueView::SetViewRange method



## -description
<p>Sets the range of print jobs being monitored.</p>


## -syntax

````
HRESULT SetViewRange(
  [in] ULONG ulViewOffset,
  [in] ULONG ulViewSize
);
````


## -parameters
<dl>

### -param <i>ulViewOffset</i> [in]

<dd>
<p>The start of the range of jobs being monitored. Note that the offset value uses a zero-based index.</p>
</dd>

### -param <i>ulViewSize</i> [in]

<dd>
<p>The  size of the range of jobs being monitored.</p>
</dd>
</dl>

## -returns
<p>This method returns the appropriate <b>HRESULT</b> value.</p>

## -remarks
<p>Invoking this method causes the events for status change to the jobs to be fired. The <a href="print.iprinterqueueviewevent_onchanged">IPrinterQueueViewEvent::OnChanged</a> event method returns the live queue in response, using the specified maximum range size.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
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
<dt>
<a href="print.iprinterqueue2_getprinterqueueview">IPrinterQueue2::GetPrinterQueueView</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprinterqueueview.md">IPrinterQueueView</a>
</dt>
<dt>
<a href="print.iprinterqueueviewevent_onchanged">IPrinterQueueViewEvent::OnChanged</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterQueueView::SetViewRange method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
