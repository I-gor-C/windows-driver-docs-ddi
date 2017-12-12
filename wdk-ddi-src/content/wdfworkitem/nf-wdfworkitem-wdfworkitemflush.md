---
UID: NF.wdfworkitem.WdfWorkItemFlush
title: WdfWorkItemFlush function
author: windows-driver-content
description: The WdfWorkItemFlush method returns after a specified work item has been serviced.
old-location: wdf\wdfworkitemflush.htm
old-project: wdf
ms.assetid: 5868dd01-17ba-4edf-b665-c90d2b1aa2ba
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfWorkItemFlush
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfworkitem.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfWorkItemFlush
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfWorkItemFlush function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfWorkItemFlush</b> method returns after a specified work item has been serviced.



## -syntax

````
VOID WdfWorkItemFlush(
  _In_ WDFWORKITEM WorkItem
);
````


## -parameters

### -param WorkItem [in]

A handle to a framework work-item object that is obtained from a previous call to <a href="wdf.wdfworkitemcreate">WdfWorkItemCreate</a>.


## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
If your driver calls the <b>WdfWorkItemFlush</b> method, the method does not return until a system worker thread has removed the specified work item from the work-item queue and called the driver's <a href="wdf.evtworkitem">EvtWorkItem</a> callback function, and the <i>EvtWorkItem</i> callback function has subsequently returned after processing the work item.

Most drivers that use work items do not need to call <b>WdfWorkItemFlush</b>. A driver might call <b>WdfWorkItemFlush</b> if it must synchronize completion of work items with the removal of a remote I/O target. In this case, the driver can call <b>WdfWorkItemFlush</b> from within its <a href="..\wdfiotarget\nc-wdfiotarget-evt_wdf_io_target_query_remove.md">EvtIoTargetQueryRemove</a> callback function. 

For more information about work items, see <a href="wdf.using_framework_work_items">Using Framework Work Items</a>.

The following code example is an <a href="..\wdfiotarget\nc-wdfiotarget-evt_wdf_io_target_query_remove.md">EvtIoTargetQueryRemove</a> callback function from the <a href="wdf.sample_kmdf_drivers">Toaster</a> sample driver. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfworkitem.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.evtworkitem">EvtWorkItem</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfWorkItemFlush method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

