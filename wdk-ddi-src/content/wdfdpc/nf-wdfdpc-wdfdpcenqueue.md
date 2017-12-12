---
UID: NF.wdfdpc.WdfDpcEnqueue
title: WdfDpcEnqueue function
author: windows-driver-content
description: The WdfDpcEnqueue method schedules the execution of a DPC object's EvtDpcFunc callback function.
old-location: wdf\wdfdpcenqueue.htm
old-project: wdf
ms.assetid: 08bc78de-ba04-4845-9d22-c06cd5684f7f
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfDpcEnqueue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdpc.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDpcEnqueue
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: Any level
req.product: Windows 10 or later.
---

# WdfDpcEnqueue function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDpcEnqueue</b> method schedules the execution of a DPC object's <a href="wdf.evtdpcfunc">EvtDpcFunc</a> callback function.



## -syntax

````
BOOLEAN WdfDpcEnqueue(
  _In_ WDFDPC Dpc
);
````


## -parameters

### -param Dpc [in]

A handle to a framework DPC object.


## -returns
<b>WdfDpcEnqueue</b> returns <b>TRUE</b> if it successfully adds the specified DPC object to the system's DPC queue. Otherwise, the method returns <b>FALSE</b>.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
The <b>WdfDpcEnqueue</b> method adds the specified DPC object to the system's DPC queue, if it is not already in the queue. (If the DPC object was already in the queue, the method returns <b>FALSE</b>.) When the system is not executing higher-priority tasks, it removes the DPC object from the queue and calls the object's <a href="wdf.evtdpcfunc">EvtDpcFunc</a> callback function. 

After the callback function executes, a subsequent call to <b>WdfDpcEnqueue</b> will add the DPC object back into the DPC queue.

For more information about using DPC objects, see <a href="wdf.servicing_an_interrupt">Servicing an Interrupt</a>.

The following code example schedules the execution of the callback function that is associated with a DPC object. The example uses the <b>WdfDpcEnqueue</b> method's return value as the containing function's return value. The <a href="wdf.wdfdpccreate">WdfDpcCreate</a> code example shows how the DPC object was created.


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
Header

</th>
<td width="70%">
<dl>
<dt>Wdfdpc.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

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
<a href="wdf.wdfdpccreate">WdfDpcCreate</a>
</dt>
<dt>
<a href="wdf.evtdpcfunc">EvtDpcFunc</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDpcEnqueue method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

