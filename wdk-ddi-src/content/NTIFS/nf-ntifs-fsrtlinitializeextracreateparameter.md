---
UID: NF.ntifs.FsRtlInitializeExtraCreateParameter
title: FsRtlInitializeExtraCreateParameter
author: windows-driver-content
description: The FsRtlInitializeExtraCreateParameter routine initializes an extra create parameter (ECP) context structure.
old-location: ifsk\fsrtlinitializeextracreateparameter.htm
ms.assetid: e3be12e4-84f3-4bd5-af9a-26ad89948e50
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: The FsRtlInitializeExtraCreateParameter routine is available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlInitializeExtraCreateParameter
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
ms.keywords: FsRtlInitializeExtraCreateParameter
req.iface: 
---

# FsRtlInitializeExtraCreateParameter function



## -description
<p>The <b>FsRtlInitializeExtraCreateParameter</b> routine initializes an extra create parameter (ECP) context structure. </p>


## -syntax

````
VOID FsRtlInitializeExtraCreateParameter(
  _In_     PECP_HEADER                                    Ecp,
  _In_     ULONG                                          EcpFlags,
  _In_opt_ PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK CleanupCallback,
  _In_     ULONG                                          TotalSize,
  _In_     LPCGUID                                        EcpType,
  _In_opt_ PVOID                                          ListAllocatedFrom
);
````


## -parameters
<dl>

### -param <i>Ecp</i> [in]

<dd>
<p>Pointer to the ECP context structure to initialize. </p>
</dd>

### -param <i>EcpFlags</i> [in]

<dd>
<p>Defines initialization options. Currently, no flags are defined. </p>
</dd>

### -param <i>CleanupCallback</i> [in, optional]

<dd>
<p>Optional pointer to a filter-defined cleanup callback routine of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff551124">PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK</a>. The cleanup callback routine is called when the ECP context structure (created by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545609">FsRtlAllocateExtraCreateParameter</a> routine) is deleted. Set this parameter to <b>NULL</b> if a cleanup callback routine is not applicable. </p>
</dd>

### -param <i>TotalSize</i> [in]

<dd>
<p>The size, in bytes, of the ECP context structure to initialize. </p>
</dd>

### -param <i>EcpType</i> [in]

<dd>
<p>Pointer to a GUID that indicates the type of ECP for which the context structure will be initialized. For more information about ECPs, see <a href="ifsk.using_extra_create_parameters_with_an_irp_mj_create_operation">Using Extra Create Parameters with an IRP_MJ_CREATE Operation</a>. </p>
</dd>

### -param <i>ListAllocatedFrom</i> [in, optional]

<dd>
<p>Optional pointer to the list from which the ECP context structure is allocated. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks


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
<p>The FsRtlInitializeExtraCreateParameter routine is available starting with Windows 7. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545609">FsRtlAllocateExtraCreateParameter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551124">PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlInitializeExtraCreateParameter routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
