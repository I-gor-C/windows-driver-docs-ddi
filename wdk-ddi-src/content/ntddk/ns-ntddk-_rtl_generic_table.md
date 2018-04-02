---
UID: NS:ntddk._RTL_GENERIC_TABLE
title: "_RTL_GENERIC_TABLE"
author: windows-driver-content
description: The RTL_GENERIC_TABLE structure contains file system-specific data for a splay tree.
old-location: ifsk\rtl_generic_table.htm
old-project: ifsk
ms.assetid: 0e5dba1b-8b0d-470a-8ead-4c022e9da7fe
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PRTL_GENERIC_TABLE, PRTL_GENERIC_TABLE, PRTL_GENERIC_TABLE structure pointer [Installable File System Drivers], RTL_GENERIC_TABLE, RTL_GENERIC_TABLE structure [Installable File System Drivers], _RTL_GENERIC_TABLE, ifsk.rtl_generic_table, ntddk/PRTL_GENERIC_TABLE, ntddk/RTL_GENERIC_TABLE, othersystemstructures_ce9bd546-d224-429d-8835-be3d5ecb1a52.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available on Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddk.h
api_name:
-	RTL_GENERIC_TABLE
product:
- Windows
targetos: Windows
req.typenames: RTL_GENERIC_TABLE
---

# _RTL_GENERIC_TABLE structure
The RTL_GENERIC_TABLE structure contains file system-specific data for a splay tree. 

RTL_GENERIC_TABLE is opaque and not directly manipulated. Drivers must use the support routines that are described in the Remarks section to manipulate RTL_GENERIC_TABLE values.

## Syntax
```
typedef struct _RTL_GENERIC_TABLE {
  PRTL_SPLAY_LINKS              TableRoot;
  LIST_ENTRY                    InsertOrderList;
  PLIST_ENTRY                   OrderedPointer;
  ULONG                         WhichOrderedElement;
  ULONG                         NumberGenericTableElements;
  PRTL_GENERIC_COMPARE_ROUTINE  CompareRoutine;
  PRTL_GENERIC_ALLOCATE_ROUTINE AllocateRoutine;
  PRTL_GENERIC_FREE_ROUTINE     FreeRoutine;
  PVOID                         TableContext;
} RTL_GENERIC_TABLE;
```

## Members


`TableRoot`

Reserved for system use.

`InsertOrderList`

Reserved for system use.

`OrderedPointer`

Reserved for system use.

`WhichOrderedElement`

Reserved for system use.

`NumberGenericTableElements`

Reserved for system use.

`CompareRoutine`

Reserved for system use.

`AllocateRoutine`

Reserved for system use.

`FreeRoutine`

Reserved for system use.

`TableContext`

Reserved for system use.

## Remarks
To initialize a generic table package, you allocate a buffer that is at least <b>sizeof(</b>RTL_GENERIC_TABLE<b>) </b>bytes in size to receive the initialized generic table structure from a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552989">RtlInitializeGenericTable</a> routine. You can use the following routines to manipulate the table:

<ul>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552209">RtlDeleteElementGenericTable</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552243">RtlEnumerateGenericTable</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552247">RtlEnumerateGenericTableWithoutSplaying</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552297">RtlGetElementGenericTable</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553024">RtlInsertElementGenericTable</a>


</li>
<li>

<a href="https://msdn.microsoft.com/c7d346ab-6990-4636-bafd-2e448a937f3b">RtlInsertElementGenericTableFull</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553046">RtlIsGenericTableEmpty</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553091">RtlLookupElementGenericTable</a>


</li>
<li>

<a href="https://msdn.microsoft.com/fddb2e23-ddb3-48bc-a94e-0ca9a8580b78">RtlLookupElementGenericTableFull</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553134">RtlNumberGenericTableElements</a>


</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This structure is available on Windows 2000 and later. This structure is available on Windows 2000 and later. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552209">RtlDeleteElementGenericTable</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552243">RtlEnumerateGenericTable</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552247">RtlEnumerateGenericTableWithoutSplaying</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552297">RtlGetElementGenericTable</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552989">RtlInitializeGenericTable</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553024">RtlInsertElementGenericTable</a>



<a href="https://msdn.microsoft.com/c7d346ab-6990-4636-bafd-2e448a937f3b">RtlInsertElementGenericTableFull</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553046">RtlIsGenericTableEmpty</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553091">RtlLookupElementGenericTable</a>



<a href="https://msdn.microsoft.com/fddb2e23-ddb3-48bc-a94e-0ca9a8580b78">RtlLookupElementGenericTableFull</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553134">RtlNumberGenericTableElements</a>