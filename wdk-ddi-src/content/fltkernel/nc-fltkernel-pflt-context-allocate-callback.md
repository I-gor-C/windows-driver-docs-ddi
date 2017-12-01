---
UID: NC.fltkernel.PFLT_CONTEXT_ALLOCATE_CALLBACK
title: PFLT_CONTEXT_ALLOCATE_CALLBACK
author: windows-driver-content
description: A minifilter driver can register a routine of type PFLT_CONTEXT_ALLOCATE_CALLBACK as the minifilter driver's ContextAllocateCallback routine.
old-location: ifsk\pflt_context_allocate_callback.htm
old-project: ifsk
ms.assetid: ca737e84-5b03-4fcd-b715-3344d8bbaaf3
ms.author: windowsdriverdev
ms.date: 11/14/2017
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
req.alt-api: ContextAllocateCallback
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

# PFLT_CONTEXT_ALLOCATE_CALLBACK callback



## -description
<p>A minifilter driver can register a routine of type PFLT_CONTEXT_ALLOCATE_CALLBACK as the minifilter driver's <i>ContextAllocateCallback</i> routine. </p>


## -prototype

````
PFLT_CONTEXT_ALLOCATE_CALLBACK ContextAllocateCallback;

PVOID ContextAllocateCallback(
  _In_ POOL_TYPE        PoolType,
  _In_ SIZE_T           Size,
  _In_ FLT_CONTEXT_TYPE ContextType
)
{ ... }
````


## -parameters
<dl>

### -param <i>PoolType</i> [in]

<dd>
<p>The type of pool to allocate. This parameter is required and must be one of the following: </p>
<dl>
<dd>
<p><b>NonPagedPool</b></p>
</dd>
<dd>
<p><b>PagedPool</b></p>
</dd>
</dl>
<p>Must be <b>NonPagedPool</b> if the <i>ContextType</i> parameter is FLT_VOLUME_CONTEXT. </p>
</dd>

### -param <i>Size</i> [in]

<dd>
<p>The size, in bytes, of the entire context, including both the portion defined by the filter manager and the portion defined by the minifilter driver. </p>
</dd>

### -param <i>ContextType</i> [in]

<dd>
<p>The type of context. This parameter is required and must be one of the following values: </p>
<dl>
<dd>
<p>FLT_FILE_CONTEXT (starting with Windows Vista)</p>
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
<p>FLT_SECTION_CONTEXT (starting with Windows 8)</p>
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
<p>If not enough free pool is available to satisfy the request, this routine returns a <b>NULL</b> pointer. Otherwise, it returns a pointer to the newly allocated context. </p>

## -remarks
<p>For the rare cases that a minifilter driver must perform its own context allocation, it can specify a routine of type PFLT_CONTEXT_ALLOCATE_CALLBACK as the <i>ContextAllocateCallback</i> routine for each context type that it registers when it calls <a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a> from its <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine. To specify this routine, the minifilter driver stores a pointer to the routine in the <i>ContextAllocateCallback</i> member of the FLT_CONTEXT_REGISTRATION structure for the context type. </p>

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
<a href="..\fltkernel\nc-fltkernel-pflt-context-cleanup-callback.md">PFLT_CONTEXT_CLEANUP_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-context-free-callback.md">PFLT_CONTEXT_FREE_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PFLT_CONTEXT_ALLOCATE_CALLBACK routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
