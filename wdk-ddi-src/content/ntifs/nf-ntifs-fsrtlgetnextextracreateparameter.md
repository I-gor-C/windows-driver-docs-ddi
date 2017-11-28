---
UID: NF.ntifs.FsRtlGetNextExtraCreateParameter
title: FsRtlGetNextExtraCreateParameter
author: windows-driver-content
description: The FsRtlGetNextExtraCreateParameter routine returns a pointer to the next (or first) extra create parameter (ECP) context structure in a given ECP list.
old-location: ifsk\fsrtlgetnextextracreateparameter.htm
old-project: ifsk
ms.assetid: b9dd2890-4b2d-4fe1-88bb-30d94ff36c44
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlGetNextExtraCreateParameter
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: The FsRtlGetNextExtraCreateParameter routine is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlGetNextExtraCreateParameter
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

# FsRtlGetNextExtraCreateParameter function



## -description
<p>The <b>FsRtlGetNextExtraCreateParameter</b> routine returns a pointer to the next (or first) extra create parameter (ECP) context structure  in a given ECP list.</p>


## -syntax

````
NTSTATUS FsRtlGetNextExtraCreateParameter(
  _In_      PECP_LIST EcpList,
  _In_opt_  PVOID     CurrentEcpContext,
  _Out_opt_ LPGUID    NextEcpType,
  _Out_     PVOID     *NextEcpContext,
  _Out_opt_ ULONG     *NextEcpContextSize
);
````


## -parameters
<dl>

### -param <i>EcpList</i> [in]

<dd>
<p>Pointer to the ECP list to examine.</p>
</dd>

### -param <i>CurrentEcpContext</i> [in, optional]

<dd>
<p>Optional pointer to an ECP context structure in the given ECP list.  If present, <b>FsRtlGetNextExtraCreateParameter</b> returns a pointer to the ECP after the <i>CurrentEcpContext</i> ECP context structure.  If <i>CurrentEcpContext</i> is <b>NULL</b>, <b>FsRtlGetNextExtraCreateParameter</b> returns the first ECP context structure in the list.</p>
</dd>

### -param <i>NextEcpType</i> [out, optional]

<dd>
<p>Optional parameter that receives a pointer to the GUID of the returned ECP context structure.</p>
</dd>

### -param <i>NextEcpContext</i> [out]

<dd>
<p>Optional parameter that receives a pointer to the returned ECP context structure.</p>
</dd>

### -param <i>NextEcpContextSize</i> [out, optional]

<dd>
<p>Optional parameter that receives the size, in bytes, of the returned ECP context structure.</p>
</dd>
</dl>

## -returns
<p><b>FsRtlGetNextExtraCreateParameter</b> returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p><b>FsRtlGetNextExtraCreateParameter </b>found an ECP context structure in the <i>EcpList</i> ECP list.</p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>The <i>EcpList</i> ECP list is empty or <i>CurrentEcpContext</i> is the last ECP in the list (that is, there is no next ECP list element).  Additionally, <i>NextEcpContext</i> is set to <b>NULL</b> and <i>NextEcpContextSize</i> is set to zero.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>EcpList</i> parameter is <b>NULL</b>.</p>

<p> </p>

## -remarks
<p>The<b>FsRtlGetNextExtraCreateParameter</b> routine processes an ECP list in a non-circular manner.  That is, if the ECP context structure pointed to by the <i>CurrentEcpContext</i> parameter is the last element in the ECP list, there is no "next" ECP in the list and the routine returns STATUS_NOT_FOUND.</p>

<p>The<b>FsRtlGetNextExtraCreateParameter</b> routine processes an ECP list in a non-circular manner.  That is, if the ECP context structure pointed to by the <i>CurrentEcpContext</i> parameter is the last element in the ECP list, there is no "next" ECP in the list and the routine returns STATUS_NOT_FOUND.</p>

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
<p>The FsRtlGetNextExtraCreateParameter routine is available starting with Windows Vista. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541728">FltAllocateExtraCreateParameter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541734">FltAllocateExtraCreateParameterFromLookasideList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541741">FltAllocateExtraCreateParameterList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541939">FltCreateFileEx2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542957">FltFreeExtraCreateParameter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542964">FltFreeExtraCreateParameterList</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlGetNextExtraCreateParameter routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
