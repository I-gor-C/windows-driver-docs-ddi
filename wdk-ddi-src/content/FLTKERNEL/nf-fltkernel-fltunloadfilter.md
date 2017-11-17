---
UID: NF.fltkernel.FltUnloadFilter
title: FltUnloadFilter
author: windows-driver-content
description: A minifilter driver that has loaded a supporting minifilter driver by calling FltLoadFilter can unload the minifilter driver by calling FltUnloadFilter.
old-location: ifsk\fltunloadfilter.htm
ms.assetid: 234907d8-d21e-4303-9508-0673afa471a6
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltUnloadFilter
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
req.irql: PASSIVE_LEVEL
ms.keywords: FltUnloadFilter
req.iface: 
---

# FltUnloadFilter function



## -description
<p>A minifilter driver that has loaded a supporting minifilter driver by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543366">FltLoadFilter</a> can unload the minifilter driver by calling <b>FltUnloadFilter</b>. </p>


## -syntax

````
NTSTATUS FltUnloadFilter(
  _In_ PCUNICODE_STRING FilterName
);
````


## -parameters
<dl>

### -param <i>FilterName</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure containing the minifilter driver service name that was passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543366">FltLoadFilter</a>. </p>
</dd>
</dl>

## -returns
<p><b>FltUnloadFilter</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>A matching minifilter driver was found, but it is already being torn down. This is an error code. </p><dl>
<dt><b>STATUS_FLT_FILTER_NOT_FOUND</b></dt>
</dl><p>No matching minifilter driver was found. This is an error code. </p>

<p> </p>

## -remarks
<p>A minifilter driver that has a dependency on another minifilter driver can unload that minifilter driver by calling <b>FltUnloadFilter</b>. This routine searches for a registered minifilter driver whose service name matches the given <i>FilterName</i> and calls that minifilter driver's <i>FilterUnloadCallback</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551085">PFLT_FILTER_UNLOAD_CALLBACK</a>) routine. </p>

<p>If the supporting minifilter driver did not register a <i>FilterUnloadCallback</i> routine, the call to <b>FltUnloadFilter</b> fails. </p>

<p>A minifilter driver cannot call <b>FltUnloadFilter</b> to unload itself. </p>

<p>A minifilter driver that has a dependency on another minifilter driver can unload that minifilter driver by calling <b>FltUnloadFilter</b>. This routine searches for a registered minifilter driver whose service name matches the given <i>FilterName</i> and calls that minifilter driver's <i>FilterUnloadCallback</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551085">PFLT_FILTER_UNLOAD_CALLBACK</a>) routine. </p>

<p>If the supporting minifilter driver did not register a <i>FilterUnloadCallback</i> routine, the call to <b>FltUnloadFilter</b> fails. </p>

<p>A minifilter driver cannot call <b>FltUnloadFilter</b> to unload itself. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543366">FltLoadFilter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551085">PFLT_FILTER_UNLOAD_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltUnloadFilter function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
