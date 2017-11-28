---
UID: NS.ntddk._RTL_AVL_TABLE~r1
title: RTL_AVL_TABLE
author: windows-driver-content
description: The RTL_AVL_TABLE structure contains file system-specific data for an Adelson-Velsky/Landis (AVL) tree.
old-location: ifsk\rtl_avl_table.htm
old-project: ifsk
ms.assetid: 115d9489-f9f5-4dd2-bf09-33e8fd640743
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RTL_AVL_TABLE, RTL_AVL_TABLE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available on Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RTL_AVL_TABLE
req.alt-loc: ntddk.h
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

# RTL_AVL_TABLE structure



## -description
<p>The RTL_AVL_TABLE structure contains file system-specific data for an Adelson-Velsky/Landis (AVL) tree. An AVL tree ensures a more balanced, shallower tree implementation than a splay tree implementation of a generic table (<a href="https://msdn.microsoft.com/library/windows/hardware/ff553345">RTL_GENERIC_TABLE</a>). </p>
<p>RTL_AVL_TABLE is opaque, so cannot be directly manipulated. Drivers must use the support routines that are described in the Remarks section to manipulate RTL_AVL_TABLE values. </p>


## -syntax

````
typedef struct _RTL_AVL_TABLE {
  RTL_BALANCED_LINKS        BalancedRoot;
  PVOID                     OrderedPointer;
  ULONG                     WhichOrderedElement;
  ULONG                     NumberGenericTableElements;
  ULONG                     DepthOfTree;
  PRTL_BALANCED_LINKS       RestartKey;
  ULONG                     DeleteCount;
  PRTL_AVL_COMPARE_ROUTINE  CompareRoutine;
  PRTL_AVL_ALLOCATE_ROUTINE AllocateRoutine;
  PRTL_AVL_FREE_ROUTINE     FreeRoutine;
  PVOID                     TableContext;
} RTL_AVL_TABLE, *PRTL_AVL_TABLE;
````


## -struct-fields
<dl>

### -field <b>BalancedRoot</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>OrderedPointer</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>WhichOrderedElement</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>NumberGenericTableElements</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>DepthOfTree</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>RestartKey</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>DeleteCount</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>CompareRoutine</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>AllocateRoutine</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>FreeRoutine</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>TableContext</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>To initialize an AVL table package, you allocate a buffer that is at least <b>sizeof(</b>RTL_AVL_TABLE<b>) </b>bytes in size. You can then use this buffer to receive the initialized AVL table structure from a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406465">RtlInitializeGenericTableAvl</a> routine. Use the following routines to manipulate the table:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439514">RtlDeleteElementGenericTableAvl</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406458">RtlEnumerateGenericTableAvl</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552245">RtlEnumerateGenericTableLikeADirectory</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406462">RtlEnumerateGenericTableWithoutSplayingAvl</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552301">RtlGetElementGenericTableAvl</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406468">RtlInsertElementGenericTableAvl</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553030">RtlInsertElementGenericTableFullAvl</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406472">RtlIsGenericTableEmptyAvl</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406476">RtlLookupElementGenericTableAvl</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553092">RtlLookupElementGenericTableFullAvl</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553106">RtlLookupFirstMatchingElementGenericTableAvl</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406522">RtlNumberGenericTableElementsAvl</a>
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure is available on Windows XP and later. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553345">RTL_GENERIC_TABLE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439514">RtlDeleteElementGenericTableAvl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406458">RtlEnumerateGenericTableAvl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552245">RtlEnumerateGenericTableLikeADirectory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406462">RtlEnumerateGenericTableWithoutSplayingAvl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552301">RtlGetElementGenericTableAvl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406465">RtlInitializeGenericTableAvl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406468">RtlInsertElementGenericTableAvl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553030">RtlInsertElementGenericTableFullAvl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406472">RtlIsGenericTableEmptyAvl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406476">RtlLookupElementGenericTableAvl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553092">RtlLookupElementGenericTableFullAvl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553106">RtlLookupFirstMatchingElementGenericTableAvl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406522">RtlNumberGenericTableElementsAvl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RTL_AVL_TABLE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
