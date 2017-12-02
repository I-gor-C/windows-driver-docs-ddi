---
UID: NF.fltkernel.FltLoadFilter
title: FltLoadFilter
author: windows-driver-content
description: The FltLoadFilter routine dynamically loads a minifilter driver into the currently running system.
old-location: ifsk\fltloadfilter.htm
old-project: ifsk
ms.assetid: aecf5f5f-c0b7-487a-9db0-d01212aef094
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltLoadFilter
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
req.alt-api: FltLoadFilter
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
req.iface: 
---

# FltLoadFilter function



## -description
<p>The <b>FltLoadFilter</b> routine dynamically loads a minifilter driver into the currently running system. </p>


## -syntax

````
NTSTATUS FltLoadFilter(
  _In_ PCUNICODE_STRING FilterName
);
````


## -parameters
<dl>

### -param FilterName [in]

<dd>
<p>Pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure containing the service name for the minifilter driver. </p>
</dd>
</dl>

## -returns
<p><b>FltLoadFilter</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as one of the following: </p><dl>
<dt><b>STATUS_DRIVER_FAILED_PRIOR_UNLOAD</b></dt>
</dl><p>The minifilter driver could not be loaded because a previous version of the driver is still in memory. This is an error code. </p><dl>
<dt><b>STATUS_FAILED_DRIVER_ENTRY</b></dt>
</dl><p>The minifilter driver's <b>DriverEntry</b> routine returned an NTSTATUS value that was not a success code. This is an error code. </p><dl>
<dt><b>STATUS_IMAGE_ALREADY_LOADED</b></dt>
</dl><p>The minifilter driver is already running. This is an error code. </p><dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl><p>No matching minifilter driver was found. This is an error code. </p>

<p> </p>

## -remarks
<p>A minifilter driver that has a dependency on another minifilter driver can load that minifilter driver by calling <b>FltLoadFilter</b>. </p>

<p>To unload the supporting minifilter driver, call <a href="..\fltkernel\nf-fltkernel-fltunloadfilter.md">FltUnloadFilter</a>. </p>

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
<a href="..\fltkernel\nf-fltkernel-fltunloadfilter.md">FltUnloadFilter</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltLoadFilter routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
