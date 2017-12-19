---
UID: NF.printerextension.IPrinterQueueViewEvent.OnChanged
title: IPrinterQueueViewEvent::OnChanged method
author: windows-driver-content
description: Provides an IPrintJobCollection object that provides a snapshot of a range of print jobs in the queue.
old-location: print\iprinterqueueviewevent_onchanged.htm
old-project: print
ms.assetid: D964A0C4-041A-47BD-87AB-4AF523939DF0
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IPrinterQueueViewEvent, IPrinterQueueViewEvent::OnChanged, OnChanged
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: printerextension.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrinterQueueViewEvent.OnChanged
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
req.irql: 
req.product: Windows 10 or later.
---

# IPrinterQueueViewEvent::OnChanged method



## -description
Provides an <a href="..\printerextension\nn-printerextension-iprintjobcollection.md">IPrintJobCollection</a> object that provides a snapshot of a range of print jobs in the queue.



## -syntax

````
HRESULT OnChanged(
  [in] IPrintJobCollection *pCollection,
  [in] ULONG               ulViewOffset,
  [in] ULONG               ulViewSize,
  [in] ULONG               ulCountJobsInPrintQueue
);
````


## -parameters

### -param pCollection [in]

An <a href="..\printerextension\nn-printerextension-iprintjobcollection.md">IPrintJobCollection</a> object.


### -param ulViewOffset [in]

The start of the range of jobs being monitored.


### -param ulViewSize [in]

The range of jobs being monitored.


### -param ulCountJobsInPrintQueue [in]

The current number of jobs in the print queue.


## -returns
This method returns the appropriate <b>HRESULT</b> value.


## -remarks
The job range is controlled by the <a href="..\printerextension\nn-printerextension-iprinterqueueview.md">IPrinterQueueView</a> interface. Additionally, this method provides the current number of jobs in the print queue, and the indices of the job range being monitored. Information about the number of jobs, and the indices of the jobs is provided in response to the <a href="print.iprinterqueueview_setviewrange">IPrinterQueueView::SetViewRange</a> method being invoked.


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 8.1

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2012 R2

</td>
</tr>
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
Header

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
<a href="..\printerextension\nn-printerextension-iprinterqueueview.md">IPrinterQueueView</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprinterqueueviewevent.md">IPrinterQueueViewEvent</a>
</dt>
<dt>
<a href="print.iprinterqueueview_setviewrange">IPrinterQueueView::SetViewRange</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprintjobcollection.md">IPrintJobCollection</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterQueueViewEvent::OnChanged method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

