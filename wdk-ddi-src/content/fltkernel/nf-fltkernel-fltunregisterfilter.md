---
UID: NF.fltkernel.FltUnregisterFilter
title: FltUnregisterFilter
author: windows-driver-content
description: A registered minifilter driver calls FltUnregisterFilter to unregister itself so that the Filter Manager no longer calls it to process I/O operations.
old-location: ifsk\fltunregisterfilter.htm
old-project: ifsk
ms.assetid: 5369566b-fa64-4aec-ad3e-1a129bcefdd6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltUnregisterFilter
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltUnregisterFilter
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
req.iface: 
---

# FltUnregisterFilter function



## -description
<p>A registered minifilter driver calls <b>FltUnregisterFilter</b> to unregister itself so that the Filter Manager no longer calls it to process I/O operations. </p>


## -syntax

````
VOID FltUnregisterFilter(
  _In_ PFLT_FILTER Filter
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>Opaque filter pointer returned by <a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p><b>FltUnregisterFilter</b> unregisters the minifilter driver's callback routines and removes any contexts that the minifilter driver has set on files, volumes, instances, streams, or stream handles. It also calls the minifilter driver's <i>InstanceTeardownStartCallback</i> and <i>InstanceTeardownCompleteCallback</i> (<a href="..\fltkernel\nc-fltkernel-pflt-instance-teardown-callback.md">PFLT_INSTANCE_TEARDOWN_CALLBACK</a>) routines for each minifilter driver instance. </p>

<p>A minifilter driver typically calls <b>FltUnregisterFilter</b> from its unload routine when it is about to be unloaded. </p>

<p>A minifilter driver can only call <b>FltUnregisterFilter</b> to unregister itself, not another minifilter driver. </p>

<p>To register a minifilter driver, call <a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>. </p>

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
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-registration.md">FLT_REGISTRATION</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-filter-unload-callback.md">PFLT_FILTER_UNLOAD_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-instance-teardown-callback.md">PFLT_INSTANCE_TEARDOWN_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltUnregisterFilter function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
