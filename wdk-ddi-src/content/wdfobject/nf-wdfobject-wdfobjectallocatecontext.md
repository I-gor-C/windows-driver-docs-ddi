---
UID: NF.wdfobject.WdfObjectAllocateContext
title: WdfObjectAllocateContext
author: windows-driver-content
description: The WdfObjectAllocateContext method allocates context space for a specified framework object.
old-location: wdf\wdfobjectallocatecontext.htm
old-project: wdf
ms.assetid: dbabd045-4f18-4103-b3c0-5405173628d6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfObjectAllocateContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfobject.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfObjectAllocateContext
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfObjectAllocateContext function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfObjectAllocateContext</b> method allocates context space for a specified framework object.</p>


## -syntax

````
NTSTATUS WdfObjectAllocateContext(
  _In_  WDFOBJECT              Handle,
  _In_  PWDF_OBJECT_ATTRIBUTES ContextAttributes,
  _Out_ PVOID                  *Context
);
````


## -parameters
<dl>

### -param Handle [in]

<dd>
<p>A handle to a framework object.</p>
</dd>

### -param ContextAttributes [in]

<dd>
<p>A pointer to a caller-supplied <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure that describes the context space.</p>
</dd>

### -param Context [out]

<dd>
<p>A pointer to a location that receives a pointer to the allocated context space.</p>
</dd>
</dl>

## -returns
<p><b>WdfObjectAllocateContext</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.</p><dl>
<dt><b>STATUS_OBJECT_NAME_INVALID</b></dt>
</dl><p>The <b>ContextTypeInfo</b> member of the WDF_OBJECT_ATTRIBUTES structure that the <i>ContextAttributes</i> parameter specified was invalid.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Context space could not be allocated.</p><dl>
<dt><b>STATUS_OBJECT_NAME_EXISTS</b></dt>
</dl><p>The driver has already allocated context space that matches the <b>ContextTypeInfo</b> member of the WDF_OBJECT_ATTRIBUTES structure that <i>ContextAttributes</i> specifies. In this situation, the pointer in the <i>Context</i> parameter receives a pointer to the existing context space and does not allocate duplicate context space.</p><dl>
<dt><b>STATUS_DELETE_PENDING</b></dt>
</dl><p>The object that the <i>Handle</i> parameter specifies is being deleted. In this situation, the framework does not allocate context space.</p>

<p> </p>

<p>This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>Typically, drivers create object context space by specifying a <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure when they call a framework object's creation method, such as <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>. </p>

<p>If you want your driver to allocate more than one type of context space to some of its objects, the driver can call <b>WdfObjectAllocateContext</b> one or more times after it has called an object's creation method. Each call to <b>WdfObjectAllocateContext</b> must specify a different context type. (The <b>ContextTypeInfo</b> member of the WDF_OBJECT_ATTRIBUTES structure identifies the context type.) </p>

<p>If your driver calls <b>WdfObjectAllocateContext</b> more than once for a given object, you can provide separate <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-cleanup.md">EvtCleanupCallback</a> and <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-destroy.md">EvtDestroyCallback</a> callback functions for each context.</p>

<p>When calling <b>WdfObjectAllocateContext</b>, do not specify a <b>ParentObject</b> in the <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure.</p>

<p>When the framework allocates context space for an object, it also zero-initializes the context space.</p>

<p>For more information about object context space, see <a href="wdf.framework_object_context_space">Framework Object Context Space</a>.</p>

<p>The following code example creates context space for a request object. The context space is based on the example's REQUEST_CONTEXT structure.</p>

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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552404">WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE</a>
</dt>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfObjectAllocateContext method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
