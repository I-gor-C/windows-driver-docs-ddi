---
UID: NF.ntifs.FsRtlAllocateExtraCreateParameter
title: FsRtlAllocateExtraCreateParameter
author: windows-driver-content
description: The FsRtlAllocateExtraCreateParameter routine allocates memory for a user-defined extra create parameter (ECP) context structure and generates a pointer to that structure.
old-location: ifsk\fsrtlallocateextracreateparameter.htm
old-project: ifsk
ms.assetid: 644680a9-ec56-4d65-890f-fbc11badf2b7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlAllocateExtraCreateParameter
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: The FsRtlAllocateExtraCreateParameter routine is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlAllocateExtraCreateParameter
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
req.iface: 
---

# FsRtlAllocateExtraCreateParameter function



## -description
<p>The <b>FsRtlAllocateExtraCreateParameter</b> routine allocates memory for a user-defined extra create parameter (ECP) context structure and generates a pointer to that structure.</p>


## -syntax

````
NTSTATUS FsRtlAllocateExtraCreateParameter(
  _In_     LPCGUID                                        EcpType,
  _In_     ULONG                                          SizeOfContext,
  _In_     FSRTL_ALLOCATE_ECP_FLAGS                       Flags,
  _In_opt_ PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK CleanupCallback,
  _In_     ULONG                                          PoolTag,
  _Out_    PVOID                                          *EcpContext
);
````


## -parameters
<dl>

### -param <i>EcpType</i> [in]

<dd>
<p>A pointer to a user-defined GUID that indicates the type of the ECP context structure.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff565392">Using GUIDs in Drivers</a> for more information.</p>
</dd>

### -param <i>SizeOfContext</i> [in]

<dd>
<p>The size, in bytes, of the user-defined context structure.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Defines pool allocation options.  The following describes how pool will be allocated when one or more of the listed flag values are combined with the <i>Flags</i> parameter by using a bitwise OR operation:  </p>
<ul>
<li>
<p>FSRTL_ALLOCATE_ECP_FLAG_NONPAGED_POOL - Non-paged pool will be allocated.  If this flag value is not used, paged pool will be allocated.</p>
</li>
<li>
<p>FSRTL_ALLOCATE_ECPLIST_FLAG_CHARGE_QUOTA - All pool allocated by <b>FsRtlAllocateExtraCreateParameter</b> will be charged against the current process' memory quota.</p>
</li>
</ul>
<p>If more than one flag is used, all of the effects associated with the utilized flag values will occur.</p>
</dd>

### -param <i>CleanupCallback</i> [in, optional]

<dd>
<p>Optional pointer to a filter-defined cleanup callback routine of type <a href="..\ntifs\nc-ntifs-pfsrtl-extra-create-parameter-cleanup-callback.md">PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK</a>.  The cleanup callback routine is called when the ECP structure (created by the <b>FsRtlAllocateExtraCreateParameter</b> routine) is deleted.  Set this parameter to <b>NULL</b> if a cleanup callback routine is not applicable.</p>
</dd>

### -param <i>PoolTag</i> [in]

<dd>
<p>Specifies the pool tag for the allocated memory. For more information, see the <i>Tag</i> parameter of <a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>.</p>
</dd>

### -param <i>EcpContext</i> [out]

<dd>
<p>Receives a pointer to the allocated ECP context structure.  If the routine failed to allocate sufficient pool, the value pointed to by <i>EcpContext </i>will be <b>NULL</b> and <b>FsRtlAllocateExtraCreateParameter</b> will return status code STATUS_INSUFFICIENT_RESOURCES.</p>
</dd>
</dl>

## -returns
<p>FltAllocateExtraCreateParameter can return one of the following values:</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p><b>FsRtlAllocateExtraCreateParameter</b> was unable to allocate sufficient memory for an ECP structure.  In this case, <i>EcpContext </i>is <b>NULL</b>.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The ECP structure was successfully allocated.  In this case, a pointer to the allocated structure is returned in the <i>EcpContext </i> parameter.</p>

<p> </p>

## -remarks
<p>By default, the <b>FsRtlAllocateExtraCreateParameter</b> routine allocates paged memory pool for a user-defined ECP context structure.  If the FSRTL_ALLOCATE_ECP_FLAG_NONPAGED_POOL bitmask is used as described in the <i>Flags</i> parameter, a non-paged memory pool is allocated.  After this pool has been allocated and the ECP context structure has been initialized, the <a href="..\fltkernel\nf-fltkernel-fltinsertextracreateparameter.md">FltInsertExtraCreateParameter</a> routine is used to insert the ECP context structure (ECP list element) into an ECP list structure (<a href="ifsk.ecp_list">ECP_LIST</a>).</p>

<p>If the caller allocates ECP_LIST and one or more ECPs are used in a call to <a href="..\ntddk\nf-ntddk-iocreatefileex.md">IoCreateFileEx</a>, the previous description is correct. In this case, the system does not free any of the ECPs, so the caller can make multiple calls to <b>IoCreateFileEx</b> with the same ECP set. However, if a file system or file system filter driver attaches an ECP to an existing or newly-created ECP_LIST while processing an IRP_MJ_CREATE request, this ECP is automatically cleaned up when the IRP completes. As a result, a filter driver does not have to clean up ECPs that are added dynamically. This allows a filter driver's ECP to be properly propagated across the reparse points--a process that can require multiple IRP_MJ_CREATE requests to be generated.</p>

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
<p>The FsRtlAllocateExtraCreateParameter routine is available starting with Windows Vista. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
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
<a href="ifsk.ecp_list">ECP_LIST</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltallocateextracreateparameterlist.md">FltAllocateExtraCreateParameterList</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltallocateextracreateparameterfromlookasidelist.md">FltAllocateExtraCreateParameterFromLookasideList</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltcreatefileex2.md">FltCreateFileEx2</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltfreeextracreateparameter.md">FltFreeExtraCreateParameter</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltfreeextracreateparameterlist.md">FltFreeExtraCreateParameterList</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetecplistfromcallbackdata.md">FltGetEcpListFromCallbackData</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltinsertextracreateparameter.md">FltInsertExtraCreateParameter</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltremoveextracreateparameter.md">FltRemoveExtraCreateParameter</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltsetecplistintocallbackdata.md">FltSetEcpListIntoCallbackData</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-iocreatefileex.md">IoCreateFileEx</a>
</dt>
<dt>
<a href="..\ntifs\nc-ntifs-pfsrtl-extra-create-parameter-cleanup-callback.md">PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlAllocateExtraCreateParameter routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
