---
UID: NS.NTDDK._RTL_AVL_TABLE
title: _RTL_AVL_TABLE
author: windows-driver-content
description: The RTL_AVL_TABLE structure contains file system-specific data for an Adelson-Velsky/Landis (AVL) tree.
old-location: ifsk\rtl_avl_table.htm
old-project: ifsk
ms.assetid: 115d9489-f9f5-4dd2-bf09-33e8fd640743
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: _RTL_AVL_TABLE, RTL_AVL_TABLE
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
---

# _RTL_AVL_TABLE structure



## -description
The RTL_AVL_TABLE structure contains file system-specific data for an Adelson-Velsky/Landis (AVL) tree. An AVL tree ensures a more balanced, shallower tree implementation than a splay tree implementation of a generic table (<a href="ifsk.rtl_generic_table">RTL_GENERIC_TABLE</a>). 

RTL_AVL_TABLE is opaque, so cannot be directly manipulated. Drivers must use the support routines that are described in the Remarks section to manipulate RTL_AVL_TABLE values. 



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

### -field BalancedRoot

Reserved for system use.


### -field OrderedPointer

Reserved for system use.


### -field WhichOrderedElement

Reserved for system use.


### -field NumberGenericTableElements

Reserved for system use.


### -field DepthOfTree

Reserved for system use.


### -field RestartKey

Reserved for system use.


### -field DeleteCount

Reserved for system use.


### -field CompareRoutine

Reserved for system use.


### -field AllocateRoutine

Reserved for system use.


### -field FreeRoutine

Reserved for system use.


### -field TableContext

Reserved for system use.


## -remarks
To initialize an AVL table package, you allocate a buffer that is at least <b>sizeof(</b>RTL_AVL_TABLE<b>) </b>bytes in size. You can then use this buffer to receive the initialized AVL table structure from a call to the <a href="ifsk.rtlinitializegenerictable">RtlInitializeGenericTableAvl</a> routine. Use the following routines to manipulate the table:


<a href="ifsk.rtldeleteelementgenerictable">RtlDeleteElementGenericTableAvl</a>



<a href="ifsk.rtlenumerategenerictable">RtlEnumerateGenericTableAvl</a>



<a href="ifsk.rtlenumerategenerictablelikeadirectory">RtlEnumerateGenericTableLikeADirectory</a>



<a href="ifsk.rtlenumerategenerictablewithoutsplaying">RtlEnumerateGenericTableWithoutSplayingAvl</a>



<a href="ifsk.rtlgetelementgenerictableavl">RtlGetElementGenericTableAvl</a>



<a href="ifsk.rtlinsertelementgenerictable">RtlInsertElementGenericTableAvl</a>



<a href="ifsk.rtlinsertelementgenerictablefullavl">RtlInsertElementGenericTableFullAvl</a>



<a href="ifsk.rtlisgenerictableempty">RtlIsGenericTableEmptyAvl</a>



<a href="ifsk.rtllookupelementgenerictable">RtlLookupElementGenericTableAvl</a>



<a href="ifsk.rtllookupelementgenerictablefullavl">RtlLookupElementGenericTableFullAvl</a>



<a href="ifsk.rtllookupfirstmatchingelementgenerictableavl">RtlLookupFirstMatchingElementGenericTableAvl</a>



<a href="ifsk.rtlnumbergenerictableelements">RtlNumberGenericTableElementsAvl</a>



## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
This structure is available on Windows XP and later. 

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="ifsk.rtl_generic_table">RTL_GENERIC_TABLE</a>
</dt>
<dt>
<a href="ifsk.rtldeleteelementgenerictable">RtlDeleteElementGenericTableAvl</a>
</dt>
<dt>
<a href="ifsk.rtlenumerategenerictable">RtlEnumerateGenericTableAvl</a>
</dt>
<dt>
<a href="ifsk.rtlenumerategenerictablelikeadirectory">RtlEnumerateGenericTableLikeADirectory</a>
</dt>
<dt>
<a href="ifsk.rtlenumerategenerictablewithoutsplaying">RtlEnumerateGenericTableWithoutSplayingAvl</a>
</dt>
<dt>
<a href="ifsk.rtlgetelementgenerictableavl">RtlGetElementGenericTableAvl</a>
</dt>
<dt>
<a href="ifsk.rtlinitializegenerictable">RtlInitializeGenericTableAvl</a>
</dt>
<dt>
<a href="ifsk.rtlinsertelementgenerictable">RtlInsertElementGenericTableAvl</a>
</dt>
<dt>
<a href="ifsk.rtlinsertelementgenerictablefullavl">RtlInsertElementGenericTableFullAvl</a>
</dt>
<dt>
<a href="ifsk.rtlisgenerictableempty">RtlIsGenericTableEmptyAvl</a>
</dt>
<dt>
<a href="ifsk.rtllookupelementgenerictable">RtlLookupElementGenericTableAvl</a>
</dt>
<dt>
<a href="ifsk.rtllookupelementgenerictablefullavl">RtlLookupElementGenericTableFullAvl</a>
</dt>
<dt>
<a href="ifsk.rtllookupfirstmatchingelementgenerictableavl">RtlLookupFirstMatchingElementGenericTableAvl</a>
</dt>
<dt>
<a href="ifsk.rtlnumbergenerictableelements">RtlNumberGenericTableElementsAvl</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RTL_AVL_TABLE structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

