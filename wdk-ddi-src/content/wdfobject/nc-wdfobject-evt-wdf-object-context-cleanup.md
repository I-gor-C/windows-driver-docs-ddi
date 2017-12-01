---
UID: NC.wdfobject.EVT_WDF_OBJECT_CONTEXT_CLEANUP
title: EVT_WDF_OBJECT_CONTEXT_CLEANUP
author: windows-driver-content
description: A driver's EvtCleanupCallback event callback function removes the driver's references on an object so that the object can be deleted.
old-location: wdf\evtcleanupcallback.htm
old-project: wdf
ms.assetid: aba2efca-7d1f-4594-af65-13356f0e3f8b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfDriverMiniportUnload
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfobject.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: EvtCleanupCallback
req.alt-loc: Wdfobject.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_OBJECT_CONTEXT_CLEANUP callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>A driver's <i>EvtCleanupCallback</i> event callback function removes the driver's references on an object so that the object can be deleted.</p>


## -prototype

````
EVT_WDF_OBJECT_CONTEXT_CLEANUP EvtCleanupCallback;

VOID EvtCleanupCallback(
  _In_ WDFOBJECT Object
)
{ ... }
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>A handle to a framework object.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The driver can specify an <i>EvtCleanupCallback</i> callback function in a <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure. This structure is used as input to all of the framework methods that create framework objects, such as <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>. </p>

<p>The framework calls the callback function when either the framework or a driver attempts to delete the object. </p>

<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548758">WdfObjectReference</a> to increase the reference count of an object, the driver must provide an <i>EvtCleanupCallback</i> callback function that calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548739">WdfObjectDereference</a>. This call ensures that the object's reference count is decremented to zero and, as a result, the framework can call the driver's <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-destroy.md">EvtDestroyCallback</a> callback function and then delete the object.</p>

<p>If a driver supplies both an <i>EvtCleanupCallback</i> callback function and an <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-destroy.md">EvtDestroyCallback</a> callback function for a object, the framework calls the <i>EvtCleanupCallback</i> callback function first.</p>

<p>After the framework calls an object's <i>EvtCleanupCallback</i> callback function, the driver can access the object only from its <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-destroy.md">EvtDestroyCallback</a> callback function. However, a driver should not  attempt to call methods on an object from its EvtDestroyCallback.</p>

<p>When a driver creates an object, it sometimes allocates object-specific memory buffers and stores the buffer pointers in the object's <a href="wdf.framework_object_context_space">context space</a>. The driver's <i>EvtCleanupCallback</i> or <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-destroy.md">EvtDestroyCallback</a> callback function can deallocate these memory buffers. </p>

<p>Typically, if your driver does not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548758">WdfObjectReference</a> for an object, the object's <i>EvtCleanupCallback</i> callback function can deallocate object context allocations. In this case, the driver does not need an <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-destroy.md">EvtDestroyCallback</a> callback function for the object.</p>

<p>When an object is deleted, the framework also deletes the object's children. With one exception, the framework calls the <i>EvtCleanupCallback</i> routines of child objects before calling those of their parent objects, so drivers are guaranteed that the parent object still exists when a child's <i>EvtCleanupCallback</i> routine runs.</p>

<p>The exception to this guaranteed ordering applies to I/O requests that the driver completes at DISPATCH_LEVEL. If such an I/O request object has one or more children whose <i>EvtCleanupCallback</i> routines must be called at PASSIVE_LEVEL, the parent request might be deleted before one or more of its children. An object requires cleanup at PASSIVE_LEVEL if it must wait for something to complete or if it accesses paged memory.</p>

<p>If the driver attempts to delete such an object (or the parent of such an object) while it is running at DISPATCH_LEVEL, the framework queues the <i>EvtCleanupCallback</i> to a work item for later processing at PASSIVE_LEVEL and then calls the cleanup callback for the parent object without determining whether the callbacks for the children have run.</p>

<p>To avoid any problems that might result from this behavior, drivers should not set the request object as the parent for any object that requires cleanup at PASSIVE_LEVEL. By default, the parent for most objects is WDFDEVICE, so drivers should just accept the default. Generally, if the WDFDEVICE object is passed as a parameter (either directly or as part of a structure) to the method that creates the object, the WDFDEVICE is the default parent. For a complete list of default parents, see <a href="wdf.summary_of_framework_objects">Summary of Framework Objects</a>.

</p>

<p> If the above exception does not apply, the framework calls the child object's <i>EvtCleanupCallback</i> callback functions before calling the parent object's <i>EvtCleanupCallback</i> callback function. Next, if the child's reference count is zero, the framework calls the child object's <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-destroy.md">EvtDestroyCallback</a> callback function. Finally, if the parent's reference count is zero, the framework calls the parent object's <i>EvtDestroyCallback</i> callback function.</p>

<p>For more information about deleting framework objects, see <a href="wdf.framework_object_life_cycle">Framework Object Life Cycle</a>.</p>

<p>Typically, the framework calls the <i>EvtCleanupCallback</i> callback function at IRQL &lt;= DISPATCH_LEVEL. However, the framework calls the callback function at IRQL = PASSIVE_LEVEL in the following situations:</p>

<p>The object's handle type is WDFDEVICE, WDFDRIVER, WDFDPC, WDFINTERRUPT, WDFIOTARGET, WDFQUEUE, WDFSTRING, WDFTIMER, or WDFWORKITEM.</p>

<p>The object's handle type is WDFMEMORY or WDFLOOKASIDE, and the driver has specified <b>PagedPool</b> for the <i>PoolType</i> parameter to <a href="..\wdfmemory\nf-wdfmemory-wdfmemorycreate.md">WdfMemoryCreate</a> or <a href="..\wdfmemory\nf-wdfmemory-wdflookasidelistcreate.md">WdfLookasideListCreate</a>.</p>

<p>When a work-item object is deleted, either explicitly or because the work item's parent object is being deleted, then before calling the work item's <i>EvtCleanupCallback</i> callback function, the framework waits until all instances of the work item's <a href="wdf.evtworkitem">EvtWorkItem</a> callback function have returned. For more information, see <a href="..\wdfworkitem\nf-wdfworkitem-wdfworkitemenqueue.md">WdfWorkItemEnqueue</a>.</p>

<p>Similarly, when a timer object is deleted, either explicitly or because the timer's parent object is being deleted, then before calling the timer's <i>EvtCleanupCallback</i> callback function, the framework waits until all instances of the timer's <a href="wdf.evttimerfunc">EvtTimerFunc</a> event callback function have returned.</p>

<p>Beginning with version 1.9 of the framework, the <i>wdfroletypes.h</i> header file contains some alternative, object type-specific, function types for the <i>EvtCleanupCallback</i> callback function. These alternative types help verification tools to determine whether the driver is properly using the callback function. Use the following table to determine which function type to use.</p>

<p>Device object</p>

<p>EVT_WDF_DEVICE_CONTEXT_CLEANUP</p>

<p>I/O queue object</p>

<p>EVT_WDF_IO_QUEUE_CONTEXT_CLEANUP_CALLBACK</p>

<p>File object</p>

<p>EVT_WDF_FILE_CONTEXT_CLEANUP_CALLBACK</p>

<p>All other objects</p>

<p>EVT_WDF_OBJECT_CONTEXT_CLEANUP</p>

<p>To define an <i>EvtCleanupCallback</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtCleanupCallback</i> callback function that is named <i>MyCleanupCallback</i>, use the <b>EVT_WDF_OBJECT_CONTEXT_CLEANUP</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_OBJECT_CONTEXT_CLEANUP</b> function type is defined in the Wdfobject.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_OBJECT_CONTEXT_CLEANUP</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks section.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548739">WdfObjectDereference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548758">WdfObjectReference</a>
</dt>
<dt>
<a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-destroy.md">EvtDestroyCallback</a>
</dt>
<dt>
<a href="..\wdfworkitem\nf-wdfworkitem-wdfworkitemflush.md">WdfWorkItemFlush</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_OBJECT_CONTEXT_CLEANUP callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
