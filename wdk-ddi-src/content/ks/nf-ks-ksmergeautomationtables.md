---
UID: NF.ks.KsMergeAutomationTables
title: KsMergeAutomationTables
author: windows-driver-content
description: The KsMergeAutomationTables function merges two automation tables.
old-location: stream\ksmergeautomationtables.htm
old-project: stream
ms.assetid: ef90f9da-3169-4b49-9ba2-2cab058e5d00
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsMergeAutomationTables
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsMergeAutomationTables
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# KsMergeAutomationTables function



## -description
<p>The<b> KsMergeAutomationTables</b> function merges two automation tables.</p>


## -syntax

````
NTSTATUS KsMergeAutomationTables(
  _Out_    PKSAUTOMATION_TABLE *AutomationTableAB,
  _In_opt_ PKSAUTOMATION_TABLE AutomationTableA,
  _In_opt_ PKSAUTOMATION_TABLE AutomationTableB,
  _In_opt_ KSOBJECT_BAG        Bag
);
````


## -parameters
<dl>

### -param <i>AutomationTableAB</i> [out]

<dd>
<p>A pointer to the location at which a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560990">KSAUTOMATION_TABLE</a> is deposited. This structure is the resulting merged automation table.</p>
</dd>

### -param <i>AutomationTableA</i> [in, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560990">KSAUTOMATION_TABLE</a> structure representing the first of the two automation tables to merge. This table is the dominant table with respect to duplicate entries. If <b>NULL</b>, <i>AutomationTableB</i> is copied into <i>AutomationTableAB</i> and optionally placed in <i>Bag</i>.</p>
</dd>

### -param <i>AutomationTableB</i> [in, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560990">KSAUTOMATION_TABLE</a> structure representing the second of the two automation tables to merge. If <b>NULL</b>, <i>AutomationTableA</i> is copied into <i>AutomationTableAB</i> and optionally placed in <i>Bag</i>.</p>
</dd>

### -param <i>Bag</i> [in, optional]

<dd>
<p>The newly created automation table is placed in this KSOBJECT_BAG (equivalent to type PVOID) for later clean up. This parameter is optional.</p>
</dd>
</dl>

## -returns
<p><b>KsMergeAutomationTables</b> returns STATUS_SUCCESS if the merge successfully completes. If unsuccessful, it returns an error code. The most frequent error code is STATUS_INSUFFICIENT_RESOURCES, which indicates that there are insufficient system resources to complete the merge.</p>

## -remarks
<p>If both <i>AutomationTableA</i> and <i>AutomationTableB</i> are <b>NULL</b>, this routine performs no action and returns STATUS_SUCCESS.</p>

<p>The entries in<i> AutomationTableA</i> have priority in the merge<i>.</i> If there is an entry that appears in both <i>AutomationTableA </i>and <i>AutomationTableB</i>, the entry in <i>AutomationTableA</i> is the one that is placed into the merged table. The newly created automation table is placed in the requested object bag if one is provided.</p>

<p>If an input table is in an object bag at call-time, <i>AVStream removes the table from the object bag</i> before <b>KsMergeAutomationTables</b> returns.</p>

<p>If the <i>Bag</i> parameter is not <b>NULL</b>, the minidriver should take the mutex associated with the object bag prior to calling this routine. If the bag is associated with a pin or a filter, then the control mutex must be held. If the bag is associated with a filter factory or a device, then the device mutex should be held. For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

<p>Also see <a href="NULL">Object Bags</a>  and <a href="NULL">Defining Automation Tables</a>.</p>

<p>If both <i>AutomationTableA</i> and <i>AutomationTableB</i> are <b>NULL</b>, this routine performs no action and returns STATUS_SUCCESS.</p>

<p>The entries in<i> AutomationTableA</i> have priority in the merge<i>.</i> If there is an entry that appears in both <i>AutomationTableA </i>and <i>AutomationTableB</i>, the entry in <i>AutomationTableA</i> is the one that is placed into the merged table. The newly created automation table is placed in the requested object bag if one is provided.</p>

<p>If an input table is in an object bag at call-time, <i>AVStream removes the table from the object bag</i> before <b>KsMergeAutomationTables</b> returns.</p>

<p>If the <i>Bag</i> parameter is not <b>NULL</b>, the minidriver should take the mutex associated with the object bag prior to calling this routine. If the bag is associated with a pin or a filter, then the control mutex must be held. If the bag is associated with a filter factory or a device, then the device mutex should be held. For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

<p>Also see <a href="NULL">Object Bags</a>  and <a href="NULL">Defining Automation Tables</a>.</p>

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
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566798">KsRemoveItemFromObjectBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560941">KsAddItemToObjectBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561031">KsCopyObjectBagItems</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsMergeAutomationTables function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
