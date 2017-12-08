---
UID: NC.fltkernel.PFLT_CONTEXT_CLEANUP_CALLBACK
title: PFLT_CONTEXT_CLEANUP_CALLBACK
author: windows-driver-content
description: A minifilter driver can register a routine of type PFLT_CONTEXT_CLEANUP_CALLBACK as the minifilter driver's ContextCleanupCallback routine.
old-location: ifsk\pflt_context_cleanup_callback.htm
old-project: ifsk
ms.assetid: f17eb108-58d1-4640-a0cc-ae568b0c844c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IXpsPartIterator, Reset, IXpsPartIterator::Reset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ContextCleanupCallback
req.alt-loc: fltkernel.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=APC_LEVEL
req.iface: IXpsPartIterator
---

# PFLT_CONTEXT_CLEANUP_CALLBACK callback



## -description
<p>A minifilter driver can register a routine of type PFLT_CONTEXT_CLEANUP_CALLBACK as the minifilter driver's <i>ContextCleanupCallback</i> routine. </p>


## -prototype

````
PFLT_CONTEXT_CLEANUP_CALLBACK ContextCleanupCallback;

VOID ContextCleanupCallback(
  _In_ PFLT_CONTEXT     Context,
  _In_ FLT_CONTEXT_TYPE ContextType
)
{ ... }
````


## -parameters
<dl>

### -param Context [in]

<dd>
<p>A pointer to the minifilter driver's portion of the context. </p>
</dd>

### -param ContextType [in]

<dd>
<p>The type of context. Must be one of the following values: </p>
<dl>
<dd>
<p>FLT_FILE_CONTEXT (starting with  Windows Vista)</p>
</dd>
<dd>
<p>FLT_INSTANCE_CONTEXT</p>
</dd>
<dd>
<p>FLT_STREAM_CONTEXT</p>
</dd>
<dd>
<p>FLT_STREAMHANDLE_CONTEXT</p>
</dd>
<dd>
<p>FLT_SECTION_CONTEXT (starting with  Windows 8)</p>
</dd>
<dd>
<p>FLT_TRANSACTION_CONTEXT (starting with  Windows Vista) </p>
</dd>
<dd>
<p>FLT_VOLUME_CONTEXT</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None. </p>

## -remarks
<p>A minifilter driver can optionally specify a routine of type PFLT_CONTEXT_CLEANUP_CALLBACK as the minifilter driver's <i>ContextCleanupCallback</i> routine for each context type that it registers when it calls <a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a> from its <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine. To specify this routine, the minifilter driver stores a pointer to the routine in the <i>ContextCleanupCallback</i> member of the FLT_CONTEXT_REGISTRATION structure for the context type. </p>

<p>If the minifilter driver specifies a <i>ContextCleanupCallback</i> routine for a context type, the filter manager calls this routine before freeing any of the minifilter driver's contexts of that type. In this routine, the minifilter driver performs any needed cleanup, such as freeing additional memory that the minifilter driver allocated inside the context structure. After the <i>ContextCleanupCallback</i> routine returns, the filter manager frees the context. </p>

<p>For more information about context registration, see the reference entry for <a href="..\fltkernel\ns-fltkernel--flt-context-registration.md">FLT_CONTEXT_REGISTRATION</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-context-registration.md">FLT_CONTEXT_REGISTRATION</a>
</dt>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-registration.md">FLT_REGISTRATION</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-context-allocate-callback.md">PFLT_CONTEXT_ALLOCATE_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-context-free-callback.md">PFLT_CONTEXT_FREE_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PFLT_CONTEXT_CLEANUP_CALLBACK routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
