---
UID: NF.wiamindr_lh.IWiaDrvItem.UnlinkItemTree
title: IWiaDrvItem::UnlinkItemTree
author: windows-driver-content
description: The IWiaDrvItem::UnlinkItemTree method unlinks the driver item tree and releases all items in the tree.
old-location: image\iwiadrvitem_unlinkitemtree.htm
old-project: image
ms.assetid: f6fb2929-177b-44cd-a313-8620ba9b2907
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWiaDrvItem, UnlinkItemTree, IWiaDrvItem::UnlinkItemTree
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaDrvItem.UnlinkItemTree
req.alt-loc: wiamindr_lh.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IWiaDrvItem
req.product: Windows 10 or later.
---

# IWiaDrvItem::UnlinkItemTree method



## -description
<p>The <b>IWiaDrvItem::UnlinkItemTree</b> method unlinks the driver item tree and releases all items in the tree.</p>


## -syntax

````
HRESULT UnlinkItemTree(
  [in] LONG lFlags
);
````


## -parameters
<dl>

### -param <i>lFlags</i> [in]

<dd>
<p>Indicates how the driver item tree should be unlinked. This parameter must be set to one of the following values. See the Microsoft Windows SDK documentation for a description of the WIA item type flags.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WiaItemTypeDeleted</p>
</td>
<td>
<p>The item is marked as deleted from the tree.</p>
</td>
</tr>
<tr>
<td>
<p>WiaItemTypeDisconnected</p>
</td>
<td>
<p>The item represents a disconnected device.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>If the method succeeds, it returns S_OK. If the method is called on a nonroot item, it returns E_INVALIDARG. If the method fails for another reason, it returns a standard COM error code.</p>

## -remarks
<p>Minidrivers must call this method on the root item in the driver item tree when they want to invalidate the tree. This is typically done when the driver is being unloaded or when the minidriver needs to rebuild the driver item tree.</p>

<p>Minidrivers must call this method on the root item in the driver item tree when they want to invalidate the tree. This is typically done when the driver is being unloaded or when the minidriver needs to rebuild the driver item tree.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamindr_lh.h (include Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>