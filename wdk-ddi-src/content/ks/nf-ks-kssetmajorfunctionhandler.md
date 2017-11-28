---
UID: NF.ks.KsSetMajorFunctionHandler
title: KsSetMajorFunctionHandler
author: windows-driver-content
description: The KsSetMajorFunctionHandler function sets the handler for a specified major function to use the internal dispatching.
old-location: stream\kssetmajorfunctionhandler.htm
old-project: stream
ms.assetid: 22c1957d-089a-4504-b92c-9268a37ac265
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsSetMajorFunctionHandler
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsSetMajorFunctionHandler
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
req.iface: 
---

# KsSetMajorFunctionHandler function



## -description
<p>The <b>KsSetMajorFunctionHandler</b> function sets the handler for a specified major function to use the internal dispatching. It routes through a KSDISPATCH_TABLE contained in the opaque object header to be the first element within a structure pointed to by an <b>FsContext</b> within a file object. The dispatching assumes the table and <b>FsContext</b> structure are initialized by the device using <b>KsAllocateObjectHeader</b>.</p>


## -syntax

````
NTSTATUS KsSetMajorFunctionHandler(
  _In_ PDRIVER_OBJECT DriverObject,
  _In_ ULONG          MajorFunction
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>Specifies the driver object whose major function is to be handled.</p>
</dd>

### -param <i>MajorFunction</i> [in]

<dd>
<p>Specifies the major function identifier to be handled. This sets the major function pointer in the driver object to an internal function that then dispatches to the <b>KSDISPATCH_TABLE</b> function. The pointer to this table is assumed to be the first element in a structure pointed to by <b>FsContext</b> in the file object of the specific IRP being dispatched. The valid major function identifiers are as listed.</p>
<table>
<tr>
<th>Identifier</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>IRP_MJ_CREATE </p>
</td>
<td>
<p>Create IRP. In this instance, a create request could be used for either creating a new instance of a filter, or for creating some object such as a pin under a filter or a clock under a pin. This assumes that the first element in the driver object's extent contains a KSDEVICE_HEADER structure that is used to find the type of object to create, based on the name passed. If a parent file object is specified, then that object's KSDISPATCH_TABLE.ChildCreateHandlerTable in the <b>FsContext</b> is looked at to determine what handler to use for the create, or use the device object's table.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_MJ_CLOSE </p>
</td>
<td>
<p> Close IRP.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_MJ_DEVICE_CONTROL </p>
</td>
<td>
<p> Device control IRP.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_MJ_READ </p>
</td>
<td>
<p> Read IRP.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_MJ_WRITE </p>
</td>
<td>
<p> Write IRP.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_MJ_FLUSH_BUFFERS </p>
</td>
<td>
<p> Flush IRP.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_MJ_QUERY_SECURITY </p>
</td>
<td>
<p> Query security information.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_MJ_SET_SECURITY </p>
</td>
<td>
<p> Set security information.</p>
</td>
</tr>
<tr>
<td>
<p>KSDISPATCH_FASTIO </p>
</td>
<td>
<p>This flag may be added to the MajorFunction identifier in order to specify that the entry refers to the fast I/O dispatch table, rather than the typical major function entry. This is valid only with IRP_MJ_READ, IRP_MJ_WRITE or IRP_MJ_DEVICE_CONTROL. The driver is responsible for creating the DriverObject-&gt;FastIoDispatch table. As with normal dispatching, if a handler is set for the driver object, all file objects must handle that fast I/O, even if the entry just points to DispatchFastIoDeviceControlFailure or a similar function.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the MajorFunction identifier is valid.</p>

## -remarks
<p>If a major function handler is set for a driver object, all file objects must handle that major function, even if the entry just points to <b>KsDispatchInvalidDeviceRequest</b>.</p>

<p>This flag may be used to specify that the fast I/O entry should be set rather than the IRP-based entry.</p>

<p>If a major function handler is set for a driver object, all file objects must handle that major function, even if the entry just points to <b>KsDispatchInvalidDeviceRequest</b>.</p>

<p>This flag may be used to specify that the fast I/O entry should be set rather than the IRP-based entry.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>