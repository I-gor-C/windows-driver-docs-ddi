---
UID: NF.wdfworkitem.WdfWorkItemCreate
title: WdfWorkItemCreate
author: windows-driver-content
description: The WdfWorkItemCreate method creates a framework work-item object, which can subsequently be added to the system's work-item queue.
old-location: wdf\wdfworkitemcreate.htm
old-project: wdf
ms.assetid: f5bb3af4-c687-47ad-88ce-d56067c78d6d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfWorkItemCreate
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
req.alt-api: WdfWorkItemCreate
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfWorkItemCreate function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfWorkItemCreate</b> method creates a framework work-item object, which can subsequently be added to the system's work-item queue.</p>


## -syntax

````
NTSTATUS WdfWorkItemCreate(
  _In_  PWDF_WORKITEM_CONFIG   Config,
  _In_  PWDF_OBJECT_ATTRIBUTES Attributes,
  _Out_ WDFWORKITEM            *WorkItem
);
````


## -parameters
<dl>

### -param <i>Config</i> [in]

<dd>
<p>A pointer to a caller-allocated <a href="..\wdfworkitem\ns-wdfworkitem--wdf-workitem-config.md">WDF_WORKITEM_CONFIG</a> structure that the driver must have already initialized by calling <a href="..\wdfworkitem\nf-wdfworkitem-wdf-workitem-config-init.md">WDF_WORKITEM_CONFIG_INIT</a>.</p>
</dd>

### -param <i>Attributes</i> [in]

<dd>
<p>A pointer to a caller-allocated <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure that specifies attributes for the work-item object. </p>
</dd>

### -param <i>WorkItem</i> [out]

<dd>
<p>A pointer to a variable that receives a handle to the new work-item object.</p>
</dd>
</dl>

## -returns
<p><b>WdfWorkItemCreate</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was supplied.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The work-item object's parent is not a device object or the ancestor of a device object.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There were insufficient system resources to create a work-item object.</p><dl>
<dt><b>STATUS_WDF_INCOMPATIBLE_EXECUTION_LEVEL</b></dt>
</dl><p>The <b>AutomaticSerialization</b> member in the <a href="..\wdfworkitem\ns-wdfworkitem--wdf-workitem-config.md">WDF_WORKITEM_CONFIG</a> structure that the <i>Config</i> parameter points to is <b>TRUE</b>, but the parent object's execution level is not <b>WdfExecutionLevelPassive</b>.</p><dl>
<dt><b>STATUS_WDF_PARENT_NOT_SPECIFIED</b></dt>
</dl><p>The <i>Attributes</i> parameter was <b>NULL</b>, or the <b>ParentObject</b> member of the <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure that <i>Attributes</i> specifies was <b>NULL</b>.</p>

<p> </p>

## -remarks
<p>After a driver calls <b>WdfWorkItemCreate</b> to create a work item, it typically stores item-specific information in the context memory of the work-item object. The driver's <a href="wdf.evtworkitem">EvtWorkItem</a> callback function, which performs the work item's tasks, can access this information to determine the tasks that it must perform. (For more information about storing information in the context memory, see <a href="wdf.framework_object_context_space">Framework Object Context Space</a>.)</p>

<p>After storing work-item information, the driver must call <a href="..\wdfworkitem\nf-wdfworkitem-wdfworkitemenqueue.md">WdfWorkItemEnqueue</a> to add the work item to the system's work-item queue. When a system worker thread becomes available, the thread removes the work item from the queue and calls the <a href="wdf.evtworkitem">EvtWorkItem</a> callback function.</p>

<p>When the driver creates a work-item object, it must specify a parent object for the work-item object in the <b>ParentObject</b> member of the <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure. The parent object must be a framework device object or any object whose chain of parents leads to a framework device object. The framework will delete the work-item object when it deletes the device object.</p>

<p>To delete the work-item object earlier, the driver can call <a href="..\wdfobject\nf-wdfobject-wdfobjectdelete.md">WdfObjectDelete</a>, as described in <a href="wdf.using_framework_work_items">Using Framework Work Items</a>.</p>

<p>The driver can retrieve a work item's parent object by calling <a href="..\wdfworkitem\nf-wdfworkitem-wdfworkitemgetparentobject.md">WdfWorkItemGetParentObject</a>. </p>

<p>If your driver provides <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-cleanup.md">EvtCleanupCallback</a> or <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-destroy.md">EvtDestroyCallback</a> callback functions for the work-item object, note that the framework calls these callback functions at IRQL = PASSIVE_LEVEL.</p>

<p>For more information about work items, see <a href="wdf.using_framework_work_items">Using Framework Work Items</a>.</p>

<p>The following code example initializes a <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure, initializes a <a href="..\wdfworkitem\ns-wdfworkitem--wdf-workitem-config.md">WDF_WORKITEM_CONFIG</a> structure, and calls <b>WdfWorkItemCreate</b>.</p>

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
<dt>Wdfworkitem.h (include Wdf.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfworkitem\nf-wdfworkitem-wdfworkitemenqueue.md">WdfWorkItemEnqueue</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfWorkItemCreate method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
