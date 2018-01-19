---
UID : NF:ntddk.RtlInitializeGenericTable
title : RtlInitializeGenericTable function
author : windows-driver-content
description : The RtlInitializeGenericTable routine initializes a generic table.
old-location : ifsk\rtlinitializegenerictable.htm
old-project : ifsk
ms.assetid : 99a91bb4-4fcd-4b49-bd1e-4551027b5d1f
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : RtlInitializeGenericTable
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntddk.h
req.include-header : Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type : Universal
req.target-min-winverclnt : This routine is available on Microsoft Windows 2000 and later versions of all Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RtlInitializeGenericTable
req.alt-loc : NtosKrnl.exe
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe
req.irql : <= DISPATCH_LEVEL (see Remarks section)
req.typenames : WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# RtlInitializeGenericTable function
The <b>RtlInitializeGenericTable</b> routine initializes a generic table.

## Syntax

````
VOID RtlInitializeGenericTable(
  _Out_    PRTL_GENERIC_TABLE            Table,
  _In_     PRTL_GENERIC_COMPARE_ROUTINE  CompareRoutine,
  _In_     PRTL_GENERIC_ALLOCATE_ROUTINE AllocateRoutine,
  _In_     PRTL_GENERIC_FREE_ROUTINE     FreeRoutine,
  _In_opt_ PVOID                         TableContext
);
````

## Parameters

`Table`

A pointer to a caller-allocated buffer, which must be at least <b>sizeof</b>(<a href="..\ntddk\ns-ntddk-_rtl_generic_table.md">RTL_GENERIC_TABLE</a>) bytes in size, to contain the initialized generic table structure.

`CompareRoutine`

An entry point of a comparison callback routine, declared as follows:

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>RTL_GENERIC_COMPARE_RESULTS
(*PRTL_GENERIC_COMPARE_ROUTINE) (
    __in struct _RTL_GENERIC_TABLE  *Table,
    __in PVOID  FirstStruct,
    __in PVOID  SecondStruct
    ); </pre>
</td>
</tr>
</table></span></div>
The <i>CompareRoutine</i> parameters are as follows:

`AllocateRoutine`

An entry point of an allocation callback routine, declared as follows:

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>PVOID
(*PRTL_GENERIC_ALLOCATE_ROUTINE) (
    __in struct _RTL_GENERIC_TABLE  *Table,
    __in CLONG  ByteSize
    );</pre>
</td>
</tr>
</table></span></div>
The <i>AllocateRoutine</i> parameters are as follows:

`FreeRoutine`

An entry point of a deallocation callback routine, declared as follows:

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>VOID
(*PRTL_GENERIC_FREE_ROUTINE) (
    __in struct _RTL_GENERIC_TABLE  *Table,
    __in PVOID  Buffer
    );</pre>
</td>
</tr>
</table></span></div>
The <i>FreeRoutine</i> parameters are as follows:

`TableContext`

An optional pointer to a caller-supplied context for the generic table. This parameter can be <b>NULL</b>.


## Return Value

None

## Remarks

File systems call <b>RtlInitializeGenericTable</b> to initialize a generic table to store file system-specific data, such as name-lookup information for currently open files. The sort order, structure, and contents of the elements are caller-defined. 

File systems must call <b>RtlInitializeGenericTable</b> to initialize the generic table before they use any other <i>Rtl...GenericTable</i> routines on the new generic table. The initialized generic table structure should be considered opaque.

Callers of the <i>Rtl...GenericTable</i> routines are responsible for exclusively synchronizing access to the generic table. An exclusive fast mutex is the most efficient synchronization mechanism to use for this purpose. 

The caller-supplied <i>CompareRoutine</i> is called before the <i>AllocateRoutine</i> to locate an appropriate location at which a new element should be inserted. The <i>CompareRoutine</i> also is called before the <i>FreeRoutine</i> to locate an element to be deleted.

By default, the operating system uses splay trees to implement generic tables. Under some circumstances, operations on a splay tree will make the tree deep and narrow and might even turn it into a straight line. Very deep trees degrade the performance of searches. You can ensure a more balanced, shallower tree implementation of generic tables by using Adelson-Velsky/Landis (AVL) trees. If you want to configure the generic table routines to use AVL trees instead of splay trees in your driver, insert the following define statement in a common header file before including <i>Ntddk.h</i>:

If RTL_USE_AVL_TABLES is not defined, you must use the AVL form of the generic table routines. For example, use the <a href="..\ntddk\nf-ntddk-rtlinitializegenerictableavl.md">RtlInitializeGenericTableAvl</a> routine instead of <b>RtlInitializeGenericTable</b>. <b>RtlInitializeGenericTableAvl</b> returns an initialized <a href="..\ntddk\ns-ntddk-_rtl_avl_table.md">RTL_AVL_TABLE</a> table structure in the buffer to which the <i>Table</i> parameter points. In the call to <b>RtlInitializeGenericTableAvl</b>, the caller must pass a PRTL_AVL_COMPARE_ROUTINE-typed comparison callback routine, a PRTL_AVL_ALLOCATE_ROUTINE-typed allocation callback routine, and a PRTL_AVL_FREE_ROUTINE-typed deallocation callback routine rather than the similar PRTL_GENERIC_<i>Xxx</i>-typed routines.

Callers of <b>RtlInitializeGenericTable</b> must be running at IRQL &lt;= DISPATCH_LEVEL. Note that if <i>Rtl...GenericTable</i> routines are to be used at IRQL DISPATCH_LEVEL, the <i>CompareRoutine</i>, <i>AllocateRoutine</i>, and <i>FreeRoutine</i> must all be nonpageable code, and the <i>AllocateRoutine</i> should allocate memory from nonpaged pool.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h (include Ntddk.h, Ntifs.h, Fltkernel.h) |
| **Library** |  |
| **IRQL** | <= DISPATCH_LEVEL (see Remarks section) |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\wdm\nf-wdm-exinitializefastmutex.md">ExInitializeFastMutex</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtldeleteelementgenerictable.md">RtlDeleteElementGenericTable</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlenumerategenerictable.md">RtlEnumerateGenericTable</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlenumerategenerictablewithoutsplaying.md">RtlEnumerateGenericTableWithoutSplaying</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlgetelementgenerictable.md">RtlGetElementGenericTable</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlinsertelementgenerictable.md">RtlInsertElementGenericTable</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtllookupelementgenerictable.md">RtlLookupElementGenericTable</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlnumbergenerictableelements.md">RtlNumberGenericTableElements</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlInitializeGenericTable routine%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>