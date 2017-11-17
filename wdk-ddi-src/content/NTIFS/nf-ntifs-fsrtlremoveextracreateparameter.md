---
UID: NF.ntifs.FsRtlRemoveExtraCreateParameter
title: FsRtlRemoveExtraCreateParameter
author: windows-driver-content
description: The FsRtlRemoveExtraCreateParameter routine searches an ECP list for an ECP context structure and, if found, detaches it from the ECP list.
old-location: ifsk\fsrtlremoveextracreateparameter.htm
ms.assetid: a34845a9-d596-40de-b4d1-0f733818d961
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: FsRtlRemoveExtraCreateParameter routine is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlRemoveExtraCreateParameter
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
ms.keywords: FsRtlRemoveExtraCreateParameter
req.iface: 
---

# FsRtlRemoveExtraCreateParameter function



## -description
<p>The <b>FsRtlRemoveExtraCreateParameter</b> routine searches an ECP list for an ECP context structure and, if found, detaches it from the ECP list.</p>


## -syntax

````
NTSTATUS FsRtlRemoveExtraCreateParameter(
  _Inout_   PECP_LIST EcpList,
  _In_      LPCGUID   EcpType,
  _Out_     PVOID     *EcpContext,
  _Out_opt_ ULONG     *EcpContextSize
);
````


## -parameters
<dl>

### -param <i>EcpList</i> [in, out]

<dd>
<p>Pointer to the extra create parameter (ECP) list that contains the ECP context structure to be detached from the given list.</p>
</dd>

### -param <i>EcpType</i> [in]

<dd>
<p>Pointer to a user-defined GUID that uniquely identifies the ECP context structure to be detached from the list.</p>
</dd>

### -param <i>EcpContext</i> [out]

<dd>
<p>Pointer to the detached ECP context structure.  If the ECP context structure is successfully detached from the given list, this parameter will be set to point to the detached ECP context structure.  If the ECP context structure is not found in the given ECP list, this parameter is set to <b>NULL</b>.</p>
</dd>

### -param <i>EcpContextSize</i> [out, optional]

<dd>
<p>Optional parameter that receives the size of the detached ECP context structure.  If this parameter is present when the routine is called, the parameter will receive the size, in bytes, of the detached ECP context structure.  If the given ECP context structure was not found in the given ECP list, this parameter is undefined. </p>
</dd>
</dl>

## -returns
<p><b>FsRtlRemoveExtraCreateParameter</b> returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The given ECP context structure was successfully detached from the given ECP list.</p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>The given ECP context structure was not found in the given ECP list.</p>

<p> </p>

## -remarks
<p>The <b>FsRtlRemoveExtraCreateParameter</b> routine searches the ECP list given by the <i>EcpList</i> parameter for an ECP context structure given by the <i>EcpType</i> parameter.  If the ECP context structure exists in the list, <b>FsRtlRemoveExtraCreateParameter</b>  detaches the structure from the list, sets the <i>EcpContext</i> parameter to point to the structure, and returns STATUS_SUCCESS. If the ECP context structure does not exist in the list, <b>FsRtlRemoveExtraCreateParameter</b> sets the <i>EcpContext</i> parameter to <b>NULL</b> and returns STATUS_NOT_FOUND.</p>

<p>The <b>FsRtlRemoveExtraCreateParameter</b> routine searches the ECP list given by the <i>EcpList</i> parameter for an ECP context structure given by the <i>EcpType</i> parameter.  If the ECP context structure exists in the list, <b>FsRtlRemoveExtraCreateParameter</b>  detaches the structure from the list, sets the <i>EcpContext</i> parameter to point to the structure, and returns STATUS_SUCCESS. If the ECP context structure does not exist in the list, <b>FsRtlRemoveExtraCreateParameter</b> sets the <i>EcpContext</i> parameter to <b>NULL</b> and returns STATUS_NOT_FOUND.</p>

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
<p>FsRtlRemoveExtraCreateParameter routine is available starting with Windows Vista. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540148">ECP_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541734">FltAllocateExtraCreateParameterFromLookasideList</a>
</dt>
<dt><b>FltAllocateExtraCreateParameterFromLookasideList</b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541939">FltCreateFileEx2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542957">FltFreeExtraCreateParameter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543016">FltGetEcpListFromCallbackData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543305">FltInsertExtraCreateParameter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544339">FltRemoveExtraCreateParameter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544510">FltSetEcpListIntoCallbackData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548283">IoCreateFileEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlRemoveExtraCreateParameter routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
