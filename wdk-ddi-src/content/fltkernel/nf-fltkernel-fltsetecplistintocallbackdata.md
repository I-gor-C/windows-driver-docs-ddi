---
UID: NF.fltkernel.FltSetEcpListIntoCallbackData
title: FltSetEcpListIntoCallbackData
author: windows-driver-content
description: The FltSetEcpListIntoCallbackData routine attaches an extra create parameter context structure (ECP) list to a create operation callback-data object.
old-location: ifsk\fltsetecplistintocallbackdata.htm
old-project: ifsk
ms.assetid: 91179c1c-fe45-418f-8992-a40e41e3017a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltSetEcpListIntoCallbackData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltSetEcpListIntoCallbackData
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
req.irql: <= APC_LEVEL
req.iface: 
---

# FltSetEcpListIntoCallbackData function



## -description
<p>The <b>FltSetEcpListIntoCallbackData </b>routine attaches an extra create parameter context structure (ECP) list to a create operation callback-data object.</p>


## -syntax

````
NTSTATUS FltSetEcpListIntoCallbackData(
  _In_ PFLT_FILTER        Filter,
  _In_ PFLT_CALLBACK_DATA Data,
  _In_ PECP_LIST          EcpList
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>Opaque filter pointer to the minifilter driver. This pointer uniquely identifies the minifilter driver and remains constant as long as the minifilter driver is loaded.</p>
</dd>

### -param <i>Data</i> [in]

<dd>
<p>Pointer to a callback-data object of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>, which represents the create operation.</p>
</dd>

### -param <i>EcpList</i> [in]

<dd>
<p>Pointer to the ECP list, which contains one or more ECPs, to be attached to the callback-data object.</p>
</dd>
</dl>

## -returns
<p><b>FltSetEcpListIntoCallbackData </b>returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The given ECP list was successfully attached to the given callback-data object.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The given callback data object was not an IRP-based create operation.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_3</b></dt>
</dl><p>An ECP list has already been attached to the given callback-data object.</p>

<p> </p>

## -remarks
<p>The <b>FltSetEcpListIntoCallbackData</b> routine provides a mechanism for passing extra create parameters down the file system filter stack to underlying minifilter and legacy filter drivers.</p>

<p>To retrieve an attached ECP list from a given callback-data object, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543016">FltGetEcpListFromCallbackData</a> routine.</p>

<p>The <b>FltSetEcpListIntoCallbackData</b> routine provides a mechanism for passing extra create parameters down the file system filter stack to underlying minifilter and legacy filter drivers.</p>

<p>To retrieve an attached ECP list from a given callback-data object, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543016">FltGetEcpListFromCallbackData</a> routine.</p>

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
<p>This routine is available starting with Windows Vista. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541661">FltAcknowledgeEcp</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541973">FltDeleteExtraCreateParameterLookasideList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542094">FltFindExtraCreateParameter</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543104">FltGetNextExtraCreateParameter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543261">FltInitExtraCreateParameterLookasideList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543305">FltInsertExtraCreateParameter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543321">FltIsEcpAcknowledged</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543325">FltIsEcpFromUserMode</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544339">FltRemoveExtraCreateParameter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548283">IoCreateFileEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltSetEcpListIntoCallbackData routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
