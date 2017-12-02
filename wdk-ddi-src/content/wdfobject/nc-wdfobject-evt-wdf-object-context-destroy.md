---
UID: NC.wdfobject.EVT_WDF_OBJECT_CONTEXT_DESTROY
title: EVT_WDF_OBJECT_CONTEXT_DESTROY
author: windows-driver-content
description: A driver's EvtDestroyCallback event callback function performs operations that are associated with the deletion of a framework object.
old-location: wdf\evtdestroycallback.htm
old-project: wdf
ms.assetid: 4c3b08d2-bb25-40bd-b2fc-1b9ea2d452b3
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: EvtDestroyCallback
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

# EVT_WDF_OBJECT_CONTEXT_DESTROY callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>A driver's <i>EvtDestroyCallback</i> event callback function performs operations that are associated with the deletion of a framework object.</p>


## -prototype

````
EVT_WDF_OBJECT_CONTEXT_DESTROY EvtDestroyCallback;

VOID EvtDestroyCallback(
  _In_ WDFOBJECT Object
)
{ ... }
````


## -parameters
<dl>

### -param Object [in]

<dd>
<p>A handle to a framework object.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The driver can specify an <i>EvtDestroyCallback</i> callback function in a <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure. This structure is used as input to all of the framework methods that create framework objects, such as <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>. </p>

<p>The framework calls the <i>EvtDestroyCallback</i> callback function after the object's reference count has been decremented to zero. The framework deletes the object immediately after the <i>EvtDestroyCallback</i> callback function returns.</p>

<p>The <i>EvtDestroyCallback</i> can access the object context but cannot call any methods on the object.</p>

<p>If a driver supplies both an <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-cleanup.md">EvtCleanupCallback</a> callback function and an <i>EvtDestroyCallback</i> callback function for a object, the framework calls the <i>EvtCleanupCallback</i> callback function first.</p>

<p>When an object is deleted, the framework also deletes the object's children. The framework calls the child objects' <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-cleanup.md">EvtCleanupCallback</a> callback functions before calling the parent object's <i>EvtCleanupCallback</i> callback function. Next, if the child's reference count is zero, the framework calls the child object's <i>EvtDestroyCallback</i> callback function. Finally, if the parent's reference count is zero, the framework calls the parent object's <i>EvtDestroyCallback</i> callback function.</p>

<p>When a driver creates an object, it sometimes allocates object-specific memory buffers and stores the buffer pointers in the object's <a href="wdf.framework_object_context_space">context space</a>. The driver's <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-cleanup.md">EvtCleanupCallback</a> or <i>EvtDestroyCallback</i> callback function can deallocate these memory buffers. </p>

<p>For more information about deleting framework objects, see <a href="wdf.framework_object_life_cycle">Framework Object Life Cycle</a>.</p>

<p>Typically, the framework calls the <i>EvtDestroyCallback</i> callback function at IRQL &lt;= DISPATCH_LEVEL. However, the framework calls the callback function at IRQL = PASSIVE_LEVEL in the following situations:</p>

<p>The object's handle type is WDFDEVICE, WDFDRIVER, WDFDPC, WDFINTERRUPT, WDFIOTARGET, WDFQUEUE, WDFSTRING, WDFTIMER, or WDFWORKITEM.</p>

<p>The object's handle type is WDFMEMORY or WDFLOOKASIDE, and the driver has specified <b>PagedPool</b> for the <i>PoolType</i> parameter to <a href="..\wdfmemory\nf-wdfmemory-wdfmemorycreate.md">WdfMemoryCreate</a> or <a href="..\wdfmemory\nf-wdfmemory-wdflookasidelistcreate.md">WdfLookasideListCreate</a>.</p>

<p>Beginning with version 1.9 of the framework, the <i>wdfroletypes.h</i> header file contains some alternative, object type-specific, function types for the <i>EvtDestroyCallback</i> callback function. These alternative types help verification tools to determine whether the driver is properly using the callback function. Use the following table to determine which function type to use.</p>

<p>Device object</p>

<p>EVT_WDF_DEVICE_CONTEXT_DESTROY</p>

<p>I/O queue object</p>

<p>EVT_WDF_IO_QUEUE_CONTEXT_DESTROY_CALLBACK</p>

<p>File object</p>

<p>EVT_WDF_FILE_CONTEXT_DESTROY_CALLBACK</p>

<p>All other objects</p>

<p>EVT_WDF_OBJECT_CONTEXT_DESTROY</p>

<p>To define an <i>EvtDestroyCallback</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDestroyCallback</i> callback function that is named <i>MyDestroyCallback</i>, use the <b>EVT_WDF_OBJECT_CONTEXT_DESTROY</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_OBJECT_CONTEXT_DESTROY</b> function type is defined in the Wdfobject.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_OBJECT_CONTEXT_DESTROY</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/73a408ba-0219-4fde-8dad-ca330e4e67c3">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-cleanup.md">EvtCleanupCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_OBJECT_CONTEXT_DESTROY callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
