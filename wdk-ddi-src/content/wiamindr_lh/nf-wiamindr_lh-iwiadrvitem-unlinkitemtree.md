---
UID : NF:wiamindr_lh.IWiaDrvItem.UnlinkItemTree
title : IWiaDrvItem::UnlinkItemTree method
author : windows-driver-content
description : The IWiaDrvItem::UnlinkItemTree method unlinks the driver item tree and releases all items in the tree.
old-location : image\iwiadrvitem_unlinkitemtree.htm
old-project : image
ms.assetid : f6fb2929-177b-44cd-a313-8620ba9b2907
ms.author : windowsdriverdev
ms.date : 1/17/2018
ms.keywords : IWiaDrvItem, IWiaDrvItem::UnlinkItemTree, UnlinkItemTree
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : wiamindr_lh.h
req.include-header : Wiamindr.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IWiaDrvItem.UnlinkItemTree
req.alt-loc : wiamindr_lh.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PSCANWINDOW, SCANWINDOW"
req.product : Windows 10 or later.
---


# UnlinkItemTree method
The <b>IWiaDrvItem::UnlinkItemTree</b> method unlinks the driver item tree and releases all items in the tree.

## Syntax

````
HRESULT UnlinkItemTree(
  [in] LONG lFlags
);
````

## Parameters

`__MIDL__IWiaDrvItem0005`




## Return Value

If the method succeeds, it returns S_OK. If the method is called on a nonroot item, it returns E_INVALIDARG. If the method fails for another reason, it returns a standard COM error code.

## Remarks

Minidrivers must call this method on the root item in the driver item tree when they want to invalidate the tree. This is typically done when the driver is being unloaded or when the minidriver needs to rebuild the driver item tree.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wiamindr_lh.h (include Wiamindr.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |