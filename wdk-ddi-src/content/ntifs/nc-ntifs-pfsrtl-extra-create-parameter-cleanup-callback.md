---
UID: NC.ntifs.PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK
title: PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK
author: windows-driver-content
description: A file system filter driver (legacy filter) or a minifilter driver can register a PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK-typed routine as the filter driver's CleanupCallback callback routine for an extra create parameter (ECP) context structure.
old-location: ifsk\pfsrtl_extra_create_parameter_cleanup_callback.htm
old-project: ifsk
ms.assetid: 76dc75fa-90ee-4fe7-b8f2-45e1a08a061f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VOLUME_READ_PLEX_INPUT, VOLUME_READ_PLEX_INPUT, *PVOLUME_READ_PLEX_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of all Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK
req.alt-loc: ntifs.h
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

# PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK callback



## -description
<p>A file system filter driver (legacy filter) or a minifilter driver can register a PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK-typed routine as the filter driver's <i>CleanupCallback</i> callback routine for an extra create parameter (ECP) context structure.</p>


## -prototype

````
typedef VOID ( *PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK)(
  _Inout_ PVOID   EcpContext,
  _In_    LPCGUID EcpType
);
````


## -parameters
<dl>

### -param <i>EcpContext</i> [in, out]

<dd>
<p>An ECP context pointer that was returned by the routine that allocated the ECP context structure.</p>
</dd>

### -param <i>EcpType</i> [in]

<dd>
<p>A pointer to a GUID that was passed to the routine that allocated the ECP context structure, that indicates the extra create parameter type.  For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565392">Using GUIDs in Drivers</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>When a file system filter driver (legacy filter) or a minifilter driver allocates an ECP context structure, it can optionally specify a PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK-typed routine as the filter driver's <i>CleanupCallback</i> callback routine.  If the filter driver specifies a <i>CleanupCallback</i> callback routine, the operating system will invoke the <i>CleanupCallback</i> routine (regardless of IRQ level).  This <i>CleanupCallback</i> routine performs any necessary ECP context-related cleanup processing when the ECP context structure is deleted.</p>

<p>To specify a callback routine, a filter driver passes a pointer to the callback routine by using the <i>CleanupCallback</i> parameter of the routine that originally allocated the ECP context structure.  If a callback routine is not needed, a <b>NULL</b> value must be passed to the <i>CleanupCallback</i> parameter. </p>

<p>The following routines support the PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK-typed callback routine:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541728">FltAllocateExtraCreateParameter</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541734">FltAllocateExtraCreateParameterFromLookasideList</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545609">FsRtlAllocateExtraCreateParameter</a>
</p>

<p>When a file system filter driver (legacy filter) or a minifilter driver allocates an ECP context structure, it can optionally specify a PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK-typed routine as the filter driver's <i>CleanupCallback</i> callback routine.  If the filter driver specifies a <i>CleanupCallback</i> callback routine, the operating system will invoke the <i>CleanupCallback</i> routine (regardless of IRQ level).  This <i>CleanupCallback</i> routine performs any necessary ECP context-related cleanup processing when the ECP context structure is deleted.</p>

<p>To specify a callback routine, a filter driver passes a pointer to the callback routine by using the <i>CleanupCallback</i> parameter of the routine that originally allocated the ECP context structure.  If a callback routine is not needed, a <b>NULL</b> value must be passed to the <i>CleanupCallback</i> parameter. </p>

<p>The following routines support the PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK-typed callback routine:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541728">FltAllocateExtraCreateParameter</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541734">FltAllocateExtraCreateParameterFromLookasideList</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545609">FsRtlAllocateExtraCreateParameter</a>
</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of all Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or FltKernel.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540148">ECP_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541728">FltAllocateExtraCreateParameter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541734">FltAllocateExtraCreateParameterFromLookasideList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541741">FltAllocateExtraCreateParameterList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542957">FltFreeExtraCreateParameter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542964">FltFreeExtraCreateParameterList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544339">FltRemoveExtraCreateParameter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK function pointer%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
