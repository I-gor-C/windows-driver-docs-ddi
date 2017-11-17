---
UID: NF.wdfobject.WdfObjectDelete
title: WdfObjectDelete
author: windows-driver-content
description: The WdfObjectDelete method deletes a framework object and its child objects.
old-location: wdf\wdfobjectdelete.htm
ms.assetid: 09eceeb4-8501-48c4-84f5-aa747914f9dd
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfobject.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfObjectDelete
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: AddPdoToStaticChildList, ControlDeviceDeleted, CtlDeviceFinishInitDeviceAdd, CtlDeviceFinishInitDrEntry, DriverCreate, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2, MemAfterReqCompletedIntIoctlA, MemAfterReqCompletedIoctlA, MemAfterReqCompletedReadA, MemAfterReqCompletedWriteA, ReqDelete, ReqSendFail
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: See Remarks section.
ms.keywords: WdfObjectDelete
req.iface: 
req.product: Windows 10 or later.
---

# WdfObjectDelete function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfObjectDelete</b> method deletes a framework object and its child objects.</p>


## -syntax

````
VOID WdfObjectDelete(
  _In_ WDFOBJECT Object
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>A handle to framework object.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>After a driver calls <b>WdfObjectDelete</b>, the specified object is deleted after its reference count becomes zero.</p>

<p>Drivers cannot call <b>WdfObjectDelete</b> to delete the following framework objects, because the framework always handles deletion of these objects:</p>

<p>Framework child-list objects (WDFCHILDLIST)</p>

<p>Framework device objects  (WDFDEVICE), unless the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff545841">WdfControlDeviceInitAllocate</a> and created a <a href="wdf.using_control_device_objects">control device object</a>, which the driver must sometimes delete</p>

<p>Framework driver objects (WDFDRIVER)</p>

<p>Framework file objects (WDFFILEOBJECT)</p>

<p>Framework interrupt objects (WDFINTERRUPT)</p>

<p>Framework queue objects (WDFQUEUE), if an object represents a <a href="wdf.creating_i_o_queues">default I/O queue</a> or if the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff545920">WdfDeviceConfigureRequestDispatching</a> to set up the queue to receive all I/O requests of a particular type</p>

<p>Framework USB pipe objects (WDFUSBPIPE)</p>

<p>Framework USB interface objects (WDFUSBINTERFACE)</p>

<p>Framework WMI provider objects (WDFWMIPROVIDER)</p>

<p>Resource range list object
(WDFIORESLIST)</p>

<p>Resource list object
(WDFCMRESLIST)</p>

<p>Resource requirements list object
(WDFIORESREQLIST)</p>

<p>See <a href="wdf.summary_of_framework_objects">Summary of Framework Objects</a> for a complete list of framework objects.</p>

<p>The <b>WdfObjectDelete</b> method can return before the framework has deleted the object and its child objects. The order in which the framework deletes child objects is not predictable.</p>

<p>For more information about <b>WdfObjectDelete</b>, see <a href="wdf.framework_object_life_cycle">Framework Object Life Cycle</a>.</p>

<p>The <b>WdfObjectDelete</b> method must be called at IRQL &lt;= DISPATCH_LEVEL. If your driver is deleting a control device object, <b>WdfObjectDelete</b> must be called at IRQL = PASSIVE_LEVEL. Similarly, if your driver is deleting a common buffer, <b>WdfObjectDelete</b> must be called at IRQL = PASSIVE_LEVEL.</p>

<p>The following code example deletes a framework object and its child objects.</p>

<p>After a driver calls <b>WdfObjectDelete</b>, the specified object is deleted after its reference count becomes zero.</p>

<p>Drivers cannot call <b>WdfObjectDelete</b> to delete the following framework objects, because the framework always handles deletion of these objects:</p>

<p>Framework child-list objects (WDFCHILDLIST)</p>

<p>Framework device objects  (WDFDEVICE), unless the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff545841">WdfControlDeviceInitAllocate</a> and created a <a href="wdf.using_control_device_objects">control device object</a>, which the driver must sometimes delete</p>

<p>Framework driver objects (WDFDRIVER)</p>

<p>Framework file objects (WDFFILEOBJECT)</p>

<p>Framework interrupt objects (WDFINTERRUPT)</p>

<p>Framework queue objects (WDFQUEUE), if an object represents a <a href="wdf.creating_i_o_queues">default I/O queue</a> or if the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff545920">WdfDeviceConfigureRequestDispatching</a> to set up the queue to receive all I/O requests of a particular type</p>

<p>Framework USB pipe objects (WDFUSBPIPE)</p>

<p>Framework USB interface objects (WDFUSBINTERFACE)</p>

<p>Framework WMI provider objects (WDFWMIPROVIDER)</p>

<p>Resource range list object
(WDFIORESLIST)</p>

<p>Resource list object
(WDFCMRESLIST)</p>

<p>Resource requirements list object
(WDFIORESREQLIST)</p>

<p>See <a href="wdf.summary_of_framework_objects">Summary of Framework Objects</a> for a complete list of framework objects.</p>

<p>The <b>WdfObjectDelete</b> method can return before the framework has deleted the object and its child objects. The order in which the framework deletes child objects is not predictable.</p>

<p>For more information about <b>WdfObjectDelete</b>, see <a href="wdf.framework_object_life_cycle">Framework Object Life Cycle</a>.</p>

<p>The <b>WdfObjectDelete</b> method must be called at IRQL &lt;= DISPATCH_LEVEL. If your driver is deleting a control device object, <b>WdfObjectDelete</b> must be called at IRQL = PASSIVE_LEVEL. Similarly, if your driver is deleting a common buffer, <b>WdfObjectDelete</b> must be called at IRQL = PASSIVE_LEVEL.</p>

<p>The following code example deletes a framework object and its child objects.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfobject.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks section.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975064">AddPdoToStaticChildList</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543528">ControlDeviceDeleted</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543607">CtlDeviceFinishInitDeviceAdd</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543610">CtlDeviceFinishInitDrEntry</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547267">InvalidReqAccessLocal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549090">MemAfterReqCompletedIntIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549106">MemAfterReqCompletedIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549116">MemAfterReqCompletedReadA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549125">MemAfterReqCompletedWriteA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551583">ReqDelete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551599">ReqSendFail</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545841">WdfControlDeviceInitAllocate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548730">WdfObjectCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfObjectDelete method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
