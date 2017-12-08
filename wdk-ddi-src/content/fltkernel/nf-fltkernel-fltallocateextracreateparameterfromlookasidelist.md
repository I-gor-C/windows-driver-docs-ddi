---
UID: NF.fltkernel.FltAllocateExtraCreateParameterFromLookasideList
title: FltAllocateExtraCreateParameterFromLookasideList function
author: windows-driver-content
description: The FltAllocateExtraCreateParameterFromLookasideList routine allocates memory pool from a given lookaside list for an extra create parameter (ECP) context structure and generates a pointer to that structure.
old-location: ifsk\fltallocateextracreateparameterfromlookasidelist.htm
old-project: ifsk
ms.assetid: 33ab7ff3-d9b0-43ad-9971-62735f3240df
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltAllocateExtraCreateParameterFromLookasideList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltAllocateExtraCreateParameterFromLookasideList
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: <= APC_LEVEL
---

# FltAllocateExtraCreateParameterFromLookasideList function



## -description
The <b>FltAllocateExtraCreateParameterFromLookasideList </b>routine allocates memory pool from a given lookaside list for an extra create parameter (ECP) context structure and generates a pointer to that structure.


## -syntax

````
NTSTATUS FltAllocateExtraCreateParameterFromLookasideList(
  _In_     PFLT_FILTER                                    Filter,
  _In_     LPCGUID                                        EcpType,
  _In_     ULONG                                          SizeOfContext,
  _In_     FSRTL_ALLOCATE_ECP_FLAGS                       Flags,
  _In_opt_ PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK CleanupCallback,
  _Inout_  PVOID                                          LookasideList,
  _Out_    PVOID                                          *EcpContext
);
````


## -parameters

### -param Filter [in]

Opaque filter pointer to the minifilter driver. This pointer uniquely identifies the minifilter driver and remains constant as long as the minifilter driver is loaded.

### -param EcpType [in]

Pointer to a GUID that indicates the type of the ECP context structure.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff565392">Using GUIDs in Drivers</a> for more information.

### -param SizeOfContext [in]

The size, in bytes, of the ECP context structure.

### -param Flags [in]

Defines pool allocation options.  If the value of the <i>SizeOfContext</i> parameter is larger than the size, in bytes, of the given lookaside list, the ECP context structure will be allocated from system pool instead of the lookaside list.  In this case, if the <i>Flags</i> parameter contains the FSRTL_ALLOCATE_ECP_FLAG_CHARGE_QUOTA bit flag value, system pool allocated by the routine will be charged against the current process' memory quota. See the <i>Flags</i> parameter of <a href="ifsk.fltallocateextracreateparameter">FltAllocateExtraCreateParameter</a> for more information.  In the more typical case when memory for the ECP context structure is allocated from the lookaside list, the FSRTL_ALLOCATE_ECP_FLAG_CHARGE_QUOTA bit flag is not used by the routine.

### -param CleanupCallback [in, optional]

Optional pointer to a minifilter-defined cleanup callback routine of type <a href="..\ntifs\nc-ntifs-pfsrtl_extra_create_parameter_cleanup_callback.md">PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK</a>.  The cleanup callback routine is called when the ECP context structure is deleted.  Set this parameter to <b>NULL</b> if a cleanup callback routine is not applicable.

### -param LookasideList [in, out]


      Pointer to an initialized lookaside list in which to attempt to allocate pool from (for the ECP context structure).  To initialize the lookaside list, use the <a href="ifsk.fltinitextracreateparameterlookasidelist">FltInitExtraCreateParameterLookasideList</a> routine.
     

### -param EcpContext [out]

Receives a pointer to the allocated ECP context structure.  If the routine failed to allocate sufficient pool for the ECP context structure, <i>EcpContext </i>will be <b>NULL</b> and the routine will return status code STATUS_INSUFFICIENT_RESOURCES.

## -returns
The <b>FltAllocateExtraCreateParameterFromLookasideList</b> routine can return one of the following values:
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>The <b>FltAllocateExtraCreateParameterFromLookasideList</b> routine was unable to allocate sufficient memory for an ECP context structure.  In this case, <i>EcpContext</i> will be <b>NULL</b>.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The ECP context structure was successfully allocated.  In this case, a pointer to the allocated structure is returned by the <i>EcpContext </i>parameter.

 

## -remarks
This routine is available starting with Windows Vista. 

The <b>FltAllocateExtraCreateParameterFromLookasideList</b> routine allocates memory pool for an ECP context structure from the given initialized paged or non-paged lookaside list.  However, if the size of the ECP context structure (as defined by the <i>SizeOfContext</i>  parameter) is larger than the lookaside list, the routine analogously allocates memory from paged or non-paged system pool.

Use the <a href="ifsk.fltinitextracreateparameterlookasidelist">FltInitExtraCreateParameterLookasideList</a> routine to initialize a paged or non-paged pool lookaside list. Use the <b>FltAllocateExtraCreateParameterFromLookasideList</b> routine to allocate an ECP context structure from the lookaside list, and the <a href="ifsk.fltfreeextracreateparameter">FltFreeExtraCreateParameter</a> routine to deallocate the ECP context structure.

Use the <a href="ifsk.fltdeleteextracreateparameterlookasidelist">FltDeleteExtraCreateParameterLookasideList</a> routine to free a lookaside list.

Drivers must free all ECP context structures and lookaside lists they create before unloading.

For more information on using lookaside lists with drivers, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565416">Using Lookaside Lists</a>.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= APC_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.ecp_list">ECP_LIST</a>
</dt>
<dt>
<a href="ifsk.fltallocateextracreateparameter">FltAllocateExtraCreateParameter</a>
</dt>
<dt>
<a href="ifsk.fltallocateextracreateparameterlist">FltAllocateExtraCreateParameterList</a>
</dt>
<dt>
<a href="ifsk.fltcreatefileex2">FltCreateFileEx2</a>
</dt>
<dt>
<a href="ifsk.fltdeleteextracreateparameterlookasidelist">FltDeleteExtraCreateParameterLookasideList</a>
</dt>
<dt>
<a href="ifsk.fltfreeextracreateparameter">FltFreeExtraCreateParameter</a>
</dt>
<dt>
<a href="ifsk.fltfreeextracreateparameterlist">FltFreeExtraCreateParameterList</a>
</dt>
<dt>
<a href="ifsk.fltgetecplistfromcallbackdata">FltGetEcpListFromCallbackData</a>
</dt>
<dt>
<a href="ifsk.fltinitextracreateparameterlookasidelist">FltInitExtraCreateParameterLookasideList</a>
</dt>
<dt>
<a href="ifsk.fltinsertextracreateparameter">FltInsertExtraCreateParameter</a>
</dt>
<dt>
<a href="ifsk.fltremoveextracreateparameter">FltRemoveExtraCreateParameter</a>
</dt>
<dt>
<a href="ifsk.fltsetecplistintocallbackdata">FltSetEcpListIntoCallbackData</a>
</dt>
<dt>
<a href="ifsk.iocreatefileex">IoCreateFileEx</a>
</dt>
<dt>
<a href="..\ntifs\nc-ntifs-pfsrtl_extra_create_parameter_cleanup_callback.md">PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltAllocateExtraCreateParameterFromLookasideList routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
