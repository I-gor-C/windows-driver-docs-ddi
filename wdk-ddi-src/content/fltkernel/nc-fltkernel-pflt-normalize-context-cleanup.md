---
UID: NC.fltkernel.PFLT_NORMALIZE_CONTEXT_CLEANUP
title: PFLT_NORMALIZE_CONTEXT_CLEANUP
author: windows-driver-content
description: A minifilter driver that provides file names for the filter manager's name cache can register a routine of type PFLT_NORMALIZE_CONTEXT_CLEANUP as the minifilter driver's NormalizeContextCleanupCallback routine.
old-location: ifsk\pflt_normalize_context_cleanup.htm
old-project: ifsk
ms.assetid: 968cfc99-4862-41f7-bf7e-d579a3e8061f
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
req.alt-api: NormalizeContextCleanupCallback
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
req.iface: IXpsPartIterator
---

# PFLT_NORMALIZE_CONTEXT_CLEANUP callback



## -description
<p>A minifilter driver that provides file names for the filter manager's name cache can register a routine of type PFLT_NORMALIZE_CONTEXT_CLEANUP as the minifilter driver's <i>NormalizeContextCleanupCallback</i> routine. </p>


## -prototype

````
PFLT_NORMALIZE_CONTEXT_CLEANUP NormalizeContextCleanupCallback;

VOID NormalizeContextCleanupCallback(
  _In_opt_ PVOID *NormalizationContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>NormalizationContext</i> [in, optional]

<dd>
<p>Pointer to minifilter driver-provided context information to be passed in any calls to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551102">PFLT_NORMALIZE_NAME_COMPONENT</a> callback routine that are made to normalize multiple components in the same file name path. </p>
</dd>
</dl>

## -returns
<p>None. </p>

## -remarks
<p>A minifilter driver that provides file names for the filter manager's name cache can register a routine of type PFLT_NORMALIZE_CONTEXT_CLEANUP as the minifilter driver's <i>NormalizeContextCleanupCallback</i> routine. </p>

<p>To register this callback routine, the minifilter driver stores the address of a routine of type PFLT_NORMALIZE_CONTEXT_CLEANUP in the <b>NormalizeContextCleanupCallback</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a> structure that the minifilter driver passes as a parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a>. </p>

<p>The filter manager calls this callback routine to allow the minifilter driver to perform any needed cleanup for the context information passed in the <i>NormalizationContext</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551102">PFLT_NORMALIZE_NAME_COMPONENT</a> callback routine. This context is set by the minifilter driver when its PFLT_NORMALIZE_NAME_COMPONENT callback routine is called. </p>

<p>A minifilter driver that provides file names for the filter manager's name cache can register a routine of type PFLT_NORMALIZE_CONTEXT_CLEANUP as the minifilter driver's <i>NormalizeContextCleanupCallback</i> routine. </p>

<p>To register this callback routine, the minifilter driver stores the address of a routine of type PFLT_NORMALIZE_CONTEXT_CLEANUP in the <b>NormalizeContextCleanupCallback</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a> structure that the minifilter driver passes as a parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a>. </p>

<p>The filter manager calls this callback routine to allow the minifilter driver to perform any needed cleanup for the context information passed in the <i>NormalizationContext</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551102">PFLT_NORMALIZE_NAME_COMPONENT</a> callback routine. This context is set by the minifilter driver when its PFLT_NORMALIZE_NAME_COMPONENT callback routine is called. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551087">PFLT_GENERATE_FILE_NAME</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551102">PFLT_NORMALIZE_NAME_COMPONENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551105">PFLT_NORMALIZE_NAME_COMPONENT_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PFLT_NORMALIZE_CONTEXT_CLEANUP routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
