---
UID: NF.fltkernel.FltIsIoRedirectionAllowed
title: FltIsIoRedirectionAllowed
author: windows-driver-content
description: The FltIsIoRedirectionAllowed routine determines whether I/O can be redirected from the specified source filter instance to another specified filter instance.
old-location: ifsk\fltisioredirectionallowed.htm
old-project: ifsk
ms.assetid: 79a59e86-9ee2-4cfa-b495-5248f227d24b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltIsIoRedirectionAllowed
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltIsIoRedirectionAllowed
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# FltIsIoRedirectionAllowed function



## -description
<p>The <b>FltIsIoRedirectionAllowed</b> routine determines whether I/O can be redirected from the specified source filter instance to another specified filter instance.</p>


## -syntax

````
NTSTATUS FltIsIoRedirectionAllowed(
  _In_  PFLT_INSTANCE SourceInstance,
  _In_  PFLT_INSTANCE TargetInstance,
  _Out_ PBOOLEAN      RedirectionAllowed
);
````


## -parameters
<dl>

### -param <i>SourceInstance</i> [in]

<dd>
<p>The filter instance on the source device stack.</p>
</dd>

### -param <i>TargetInstance</i> [in]

<dd>
<p>The filter instance on the target device stack.</p>
</dd>

### -param <i>RedirectionAllowed</i> [out]

<dd>
<p>A value of <b>TRUE</b> if all I/O to the source device stack can be redirected to the target device stack by changing the filter instance referenced, otherwise <b>FALSE</b>.</p>
</dd>
</dl>

## -returns
<p>An NTSTATUS value of STATUS_SUCCESS for success or STATUS_NOT_SUPPORTED if redirection is not supported.</p>

## -remarks
<p>An I/O operation is associated with a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a> structure. That structure contains a reference to a <b>PFLT_IO_PARAMETER_BLOCK</b> object, which contains a reference to the FLT_INSTANCE of the minifilter associated with the I/O operation. </p>

<p>If <i>RedirectionAllowed</i> is <b>TRUE</b>, the minifilter can redirect I/O by changing that instance to a new target instance.</p>

<p>If <i>RedirectionAllowed</i> is <b>FALSE</b>, the minifilter needs to allocate a new callback data object to issue I/O on the target stack or call <a href="https://msdn.microsoft.com/library/windows/hardware/ff625873">FltAdjustDeviceStackSizeForIoRedirection</a> to increase the size of the source device stack.</p>

<p>An I/O operation is associated with a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a> structure. That structure contains a reference to a <b>PFLT_IO_PARAMETER_BLOCK</b> object, which contains a reference to the FLT_INSTANCE of the minifilter associated with the I/O operation. </p>

<p>If <i>RedirectionAllowed</i> is <b>TRUE</b>, the minifilter can redirect I/O by changing that instance to a new target instance.</p>

<p>If <i>RedirectionAllowed</i> is <b>FALSE</b>, the minifilter needs to allocate a new callback data object to issue I/O on the target stack or call <a href="https://msdn.microsoft.com/library/windows/hardware/ff625873">FltAdjustDeviceStackSizeForIoRedirection</a> to increase the size of the source device stack.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>FltKernel.h (include FltKernel.h)</dt>
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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544638">FLT_IO_PARAMETER_BLOCK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff625873">FltAdjustDeviceStackSizeForIoRedirection</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff625875">FltIsIoRedirectionAllowedForOperation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltIsIoRedirectionAllowed routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
