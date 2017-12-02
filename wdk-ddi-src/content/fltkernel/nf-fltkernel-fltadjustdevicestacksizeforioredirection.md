---
UID: NF.fltkernel.FltAdjustDeviceStackSizeForIoRedirection
title: FltAdjustDeviceStackSizeForIoRedirection
author: windows-driver-content
description: The FltAdjustDeviceStackSizeForIoRedirection routine increases the size of the source device stack to allow a minifilter to redirect I/O from a specified source instance to a specified target instance when the target stack is deeper than the source stack.
old-location: ifsk\fltadjustdevicestacksizeforioredirection.htm
old-project: ifsk
ms.assetid: 48ca0f39-e870-4f9b-92d5-1226972bf2d5
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltAdjustDeviceStackSizeForIoRedirection
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
req.alt-api: FltAdjustDeviceStackSizeForIoRedirection
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# FltAdjustDeviceStackSizeForIoRedirection function



## -description
<p>The <b>FltAdjustDeviceStackSizeForIoRedirection</b> routine increases the size of the source device stack to allow a minifilter to redirect I/O from a specified source instance to a specified target instance when the target stack is deeper than the source stack.</p>


## -syntax

````
NTSTATUS FltAdjustDeviceStackSizeForIoRedirection(
  _In_      PFLT_INSTANCE SourceInstance,
  _In_      PFLT_INSTANCE TargetInstance,
  _Out_opt_ PBOOLEAN      SourceDeviceStackSizeModified
);
````


## -parameters
<dl>

### -param SourceInstance [in]

<dd>
<p>The filter instance on the source device stack.</p>
</dd>

### -param TargetInstance [in]

<dd>
<p>The filter instance on the target device stack.</p>
</dd>

### -param SourceDeviceStackSizeModified [out, optional]

<dd>
<p>This optional parameter has a value of <b>TRUE</b> if the <b>FltAdjustDeviceStackSizeForIoRedirection</b> routine modified the size of the source device stack, <b>FALSE</b> otherwise.</p>
</dd>
</dl>

## -returns
<dl>
<dt>STATUS_SUCCESS</dt>
</dl><p>Success.</p><dl>
<dt>STATUS_NOT_SUPPORTED</dt>
</dl><p>The redirection is not supported.</p><dl>
<dt>STATUS_INVALID_PARAMETER</dt>
</dl><p>The source device stack would be too large after calling this routine.</p>

<p> </p>

## -remarks
<p>Using <b>FltAdjustDeviceStackSizeForIoRedirection</b> does not guarantee that every IRP that the minifilter encounters will be sufficient in size to be redirected to the target stack. IRPs that were allocated and issued before the call to <b>FltAdjustDeviceStackSizeForIoRedirection</b> would still have been allocated based on the old stack size. </p>

<p>A minifilter can adjust the stack size during instance setup if the filter knows which stack the I/O will be redirected to. </p>

<p>The filter can issue its own create operation down the new stack using <a href="..\fltkernel\nf-fltkernel-fltcreatefile.md">FltCreateFile</a>. Before completing the create operation, the filter can adjust the stack size to account for the target stack. Doing that adjustment ensures that the stack size will be adjusted before the create action is completed. All IRPs allocated for that file object will have a large enough stack to support redirection.</p>

<p>During instance-setup or during post-create callback for a redirected file object, use <a href="..\fltkernel\nf-fltkernel-fltisioredirectionallowed.md">FltIsIoRedirectionAllowed</a> to determine if redirection is possible without modifying the source stack. If necessary, use <b>FltAdjustDeviceStackSizeForIoRedirection</b> to adjust the source stack.</p>

<p>In the pre-operation callback for every operation that needs redirection, use <a href="..\fltkernel\nf-fltkernel-fltisioredirectionallowedforoperation.md">FltIsIoRedirectionAllowedForOperation</a> to determine if redirection is possible without modifying the source stack. If necessary, use <b>FltAdjustDeviceStackSizeForIoRedirection</b> to adjust the source stack.</p>

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
<a href="..\fltkernel\ns-fltkernel--flt-callback-data.md">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-io-parameter-block.md">FLT_IO_PARAMETER_BLOCK</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltisioredirectionallowed.md">FltIsIoRedirectionAllowed</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltisioredirectionallowedforoperation.md">FltIsIoRedirectionAllowedForOperation</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md">PFLT_PRE_OPERATION_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltAdjustDeviceStackSizeForIoRedirection routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
