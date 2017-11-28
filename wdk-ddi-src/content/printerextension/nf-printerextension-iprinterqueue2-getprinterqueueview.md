---
UID: NF.printerextension.IPrinterQueue2.GetPrinterQueueView
title: IPrinterQueue2::GetPrinterQueueView
author: windows-driver-content
description: Retrieves an IPrinterQueueView object, and initializes the object with the range of jobs to be monitored.
old-location: print\iprinterqueue2_getprinterqueueview.htm
old-project: print
ms.assetid: C565288C-B014-4A92-9F50-1641EAA30D22
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrinterQueue2, GetPrinterQueueView, IPrinterQueue2::GetPrinterQueueView
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
req.alt-api: IPrinterQueue2.GetPrinterQueueView
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
req.iface: IPrinterQueue2
req.product: Windows 10 or later.
---

# IPrinterQueue2::GetPrinterQueueView method



## -description
<p>Retrieves an <a href="https://msdn.microsoft.com/library/windows/hardware/dn265392">IPrinterQueueView</a> object, and initializes the object with the range of jobs to be monitored.</p>
<p>This method allows the user to perform job management tasks from within a UWP  device app for printers.</p>


## -syntax

````
HRESULT GetPrinterQueueView(
  [in]          ULONG              ulViewOffset,
  [in]          ULONG              ulViewSize,
  [out, retval] IPrinterQueueView ** ppJobView 
);
````


## -parameters
<dl>

### -param <i> ulViewOffset</i> [in]

<dd>
<p>Indicates the start of the range of jobs to be monitored.</p>
</dd>

### -param <i> ulViewSize</i> [in]

<dd>
<p>Indicates the size or the range of jobs to be monitored.</p>
</dd>

### -param <i> ppJobView </i> [out, retval]

<dd>
<p>IPrinterQueueView object that shows the range of jobs to be monitored.</p>
</dd>
</dl>

## -returns
<p>If the method call is successful, <b>GetPrinterQueueView</b> returns S_OK.</p>

<p>Otherwise, if a call to <b>GetPrinterQueueView</b> results in an error condition, then one of the following <b>HRESULT</b> values can be returned.
	  <table>
<tr>
<th>HRESULT value</th>
<th>Description</th>
</tr>
<tr>
<td>E_ILLEGAL_METHOD_CALL</td>
<td>Indicates an attempt to retrieve more than one printer queue view object.</td>
</tr>
<tr>
<td>E_INVALIDARG</td>
<td>Indicates an attempt to create a view size larger than the maximum size.</td>
</tr>
</table>
<p> </p>
</p>

<p> </p>

## -remarks
<p>Only one <a href="https://msdn.microsoft.com/library/windows/hardware/dn265392">IPrinterQueueView</a> object can be retrieved per <a href="https://msdn.microsoft.com/library/windows/hardware/dn265389">IPrinterQueue2</a> object.
However it is possible to move around the single view that you retrieve. In other words, it is possible to  change the positions of the monitored jobs by invoking <a href="print.iprinterqueueview_setviewrange">IPrinterQueueView::SetViewRange</a>.</p>

<p>Only one <a href="https://msdn.microsoft.com/library/windows/hardware/dn265392">IPrinterQueueView</a> object can be retrieved per <a href="https://msdn.microsoft.com/library/windows/hardware/dn265389">IPrinterQueue2</a> object.
However it is possible to move around the single view that you retrieve. In other words, it is possible to  change the positions of the monitored jobs by invoking <a href="print.iprinterqueueview_setviewrange">IPrinterQueueView::SetViewRange</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265389">IPrinterQueue2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265392">IPrinterQueueView</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterQueue2::GetPrinterQueueView method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
