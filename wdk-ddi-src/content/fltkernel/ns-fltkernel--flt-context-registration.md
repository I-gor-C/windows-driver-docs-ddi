---
UID: NS.fltkernel._FLT_CONTEXT_REGISTRATION
title: FLT_CONTEXT_REGISTRATION
author: windows-driver-content
description: The FLT_CONTEXT_REGISTRATION structure is used to register context types.
old-location: ifsk\flt_context_registration.htm
old-project: ifsk
ms.assetid: 6316acfa-c19c-4705-becb-b89c3feed6a3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FLT_CONTEXT_REGISTRATION, FLT_CONTEXT_REGISTRATION, *PFLT_CONTEXT_REGISTRATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FLT_CONTEXT_REGISTRATION
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FLT_CONTEXT_REGISTRATION structure



## -description
<p>The FLT_CONTEXT_REGISTRATION structure is used to register context types. </p>


## -syntax

````
typedef struct _FLT_CONTEXT_REGISTRATION {
  FLT_CONTEXT_TYPE               ContextType;
  FLT_CONTEXT_REGISTRATION_FLAGS Flags;
  PFLT_CONTEXT_CLEANUP_CALLBACK  ContextCleanupCallback;
  SIZE_T                         Size;
  ULONG                          PoolTag;
  PFLT_CONTEXT_ALLOCATE_CALLBACK ContextAllocateCallback;
  PFLT_CONTEXT_FREE_CALLBACK     ContextFreeCallback;
  PVOID                          Reserved1;
} FLT_CONTEXT_REGISTRATION, *PFLT_CONTEXT_REGISTRATION;
````


## -struct-fields
<dl>

### -field <b>ContextType</b>

<dd>
<p>The type of context. This member is required and must be one of the following values: </p>
<dl>
<dd>
<p>FLT_FILE_CONTEXT (Windows Vista and later only.)</p>
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
<p>FLT_SECTION_CONTEXT (Windows 8 and later only.)</p>
</dd>
<dd>
<p>FLT_TRANSACTION_CONTEXT (Windows Vista and later only.) </p>
</dd>
<dd>
<p>FLT_VOLUME_CONTEXT</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitmask of flags that specify how the filter manager allocates a new context from a lookaside list of fixed-size contexts. This member can be zero or the following value. </p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FLTFL_CONTEXT_REGISTRATION_NO_EXACT_SIZE_MATCH</p>
</td>
<td>
<p>If the minifilter uses fixed-size contexts and this flag is specified, the filter manager allocates a context from the lookaside list if the size of the context in the lookaside list is greater than or equal to the requested size. Otherwise, the filter manager allocates a context from the lookaside list only if the size of the context in the lookaside list is equal to the requested size. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ContextCleanupCallback</b>

<dd>
<p>A pointer to a minifilter-defined <b>ContextCleanupCallback</b> routine of type <a href="..\fltkernel\nc-fltkernel-pflt-context-cleanup-callback.md">PFLT_CONTEXT_CLEANUP_CALLBACK</a>. The filter manager calls this routine immediately before it deletes the context. If the minifilter has no memory or pointers to clean up inside the context, this member is optional and can be <b>NULL</b>. </p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of the minifilter-defined portion of the context, if the minifilter uses fixed-size contexts. Zero is a valid size value. If the minifilter uses variable-size contexts, this member is required and must be set to FLT_VARIABLE_SIZED_CONTEXTS. </p>
</dd>

### -field <b>PoolTag</b>

<dd>
<p>A pool tag value to be used for the context. This tag, which is specified as a string of one to four 7-bit ASCII characters, appears in any crash dump of the system that occurs. If the <b>ContextAllocateCallback</b> member is <b>NULL</b>, this member is required and cannot be zero. </p>
</dd>

### -field <b>ContextAllocateCallback</b>

<dd>
<p>Pointer to a minifilter-defined <b>ContextAllocateCallback</b> routine of type <a href="..\fltkernel\nc-fltkernel-pflt-context-allocate-callback.md">PFLT_CONTEXT_ALLOCATE_CALLBACK</a>. This member is optional and can be <b>NULL</b>. If it is not <b>NULL</b>, the <b>Size</b> and <b>PoolTag</b> members are ignored. </p>
</dd>

### -field <b>ContextFreeCallback</b>

<dd>
<p>A pointer to a minifilter-defined <b>ContextFreeCallback</b> routine of type <a href="..\fltkernel\nc-fltkernel-pflt-context-free-callback.md">PFLT_CONTEXT_FREE_CALLBACK</a>. This member is optional and can be <b>NULL</b>. If it is not <b>NULL</b>, the <b>Size</b> and <b>PoolTag</b> members are ignored. </p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved for system use. Minifilters must set this member to <b>NULL</b>. </p>
</dd>
</dl>

## -remarks
<p>When a minifilter calls <a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a> from its <b>DriverEntry</b> routine, it must register each context type that it uses. </p>

<p>To register these context types, the minifilter creates a variable-length array of FLT_CONTEXT_REGISTRATION structures and stores a pointer to the array in the <b>ContextRegistration</b> member of the <a href="..\fltkernel\ns-fltkernel--flt-registration.md">FLT_REGISTRATION</a> structure that the minifilter passes as the <i>Registration</i> parameter of <a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>. The last element of this array must be {FLT_CONTEXT_END}. </p>

<p>For each context type that the minifilter uses, the minifilter must supply at least one FLT_CONTEXT_REGISTRATION structure, according to the following rules: </p>

<p>If the minifilter supplies an FLT_CONTEXT_REGISTRATION structure with a non-<b>NULL</b><b> ContextAllocateCallback</b> member, it cannot supply any additional FLT_CONTEXT_REGISTRATION structures for that context type. </p>

<p>If the minifilter supplies two or more identical FLT_CONTEXT_REGISTRATION structures, only the first one will be used. The others will be ignored. </p>

<p>Only one FLT_CONTEXT_REGISTRATION structure with a <b>Size</b> member of FLT_VARIABLE_SIZED_CONTEXTS can be supplied for each context type. </p>

<p>No more than three FLT_CONTEXT_REGISTRATION structures with a <b>Size</b> member other than FLT_VARIABLE_SIZED_CONTEXTS can be supplied for each context type. </p>

## -requirements
<table>
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
<a href="..\fltkernel\nc-fltkernel-pflt-context-allocate-callback.md">PFLT_CONTEXT_ALLOCATE_CALLBACK</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FLT_CONTEXT_REGISTRATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
