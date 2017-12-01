---
UID: NS.ntddk._RTL_AVL_TABLE
title: RTL_AVL_TABLE
author: windows-driver-content
description: The RTL_AVL_TABLE structure contains file system-specific data for an Adelson-Velsky/Landis (AVL) tree.
old-location: ifsk\rtl_avl_table.htm
old-project: ifsk
ms.assetid: 115d9489-f9f5-4dd2-bf09-33e8fd640743
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RTL_AVL_TABLE,
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
<p>The RTL_AVL_TABLE structure contains file system-specific data for an Adelson-Velsky/Landis (AVL) tree. An AVL tree ensures a more balanced, shallower tree implementation than a splay tree implementation of a generic table (<a href="..\ntddk\ns-ntddk--rtl-generic-table.md">RTL_GENERIC_TABLE</a>). </p>
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
<p>To initialize an AVL table package, you allocate a buffer that is at least <b>sizeof(</b>RTL_AVL_TABLE<b>) </b>bytes in size. You can then use this buffer to receive the initialized AVL table structure from a call to the <a href="..\ntddk\nf-ntddk-rtlinitializegenerictable.md">RtlInitializeGenericTableAvl</a> routine. Use the following routines to manipulate the table:</p>

<p>
<a href="..\ntddk\nf-ntddk-rtldeleteelementgenerictable.md">RtlDeleteElementGenericTableAvl</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-rtlenumerategenerictable.md">RtlEnumerateGenericTableAvl</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-rtlenumerategenerictablelikeadirectory.md">RtlEnumerateGenericTableLikeADirectory</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-rtlenumerategenerictablewithoutsplaying.md">RtlEnumerateGenericTableWithoutSplayingAvl</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-rtlgetelementgenerictableavl.md">RtlGetElementGenericTableAvl</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-rtlinsertelementgenerictable.md">RtlInsertElementGenericTableAvl</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-rtlinsertelementgenerictablefullavl.md">RtlInsertElementGenericTableFullAvl</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-rtlisgenerictableempty.md">RtlIsGenericTableEmptyAvl</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-rtllookupelementgenerictable.md">RtlLookupElementGenericTableAvl</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-rtllookupelementgenerictablefullavl.md">RtlLookupElementGenericTableFullAvl</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-rtllookupfirstmatchingelementgenerictableavl.md">RtlLookupFirstMatchingElementGenericTableAvl</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-rtlnumbergenerictableelements.md">RtlNumberGenericTableElementsAvl</a>
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
<a href="..\ntddk\ns-ntddk--rtl-generic-table.md">RTL_GENERIC_TABLE</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtldeleteelementgenerictable.md">RtlDeleteElementGenericTableAvl</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlenumerategenerictable.md">RtlEnumerateGenericTableAvl</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlenumerategenerictablelikeadirectory.md">RtlEnumerateGenericTableLikeADirectory</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlenumerategenerictablewithoutsplaying.md">RtlEnumerateGenericTableWithoutSplayingAvl</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlgetelementgenerictableavl.md">RtlGetElementGenericTableAvl</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlinitializegenerictable.md">RtlInitializeGenericTableAvl</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlinsertelementgenerictable.md">RtlInsertElementGenericTableAvl</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlinsertelementgenerictablefullavl.md">RtlInsertElementGenericTableFullAvl</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlisgenerictableempty.md">RtlIsGenericTableEmptyAvl</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtllookupelementgenerictable.md">RtlLookupElementGenericTableAvl</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtllookupelementgenerictablefullavl.md">RtlLookupElementGenericTableFullAvl</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtllookupfirstmatchingelementgenerictableavl.md">RtlLookupFirstMatchingElementGenericTableAvl</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlnumbergenerictableelements.md">RtlNumberGenericTableElementsAvl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RTL_AVL_TABLE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
