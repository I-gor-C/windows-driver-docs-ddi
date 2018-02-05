---
UID : NF:wiamindr_lh.IWiaDrvItem.UnlinkItemTree
title : IWiaDrvItem::UnlinkItemTree method
author : windows-driver-content
description : The IWiaDrvItem::UnlinkItemTree method unlinks the driver item tree and releases all items in the tree.
old-location : image\iwiadrvitem_unlinkitemtree.htm
old-project : image
ms.assetid : f6fb2929-177b-44cd-a313-8620ba9b2907
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : image.iwiadrvitem_unlinkitemtree, DrvItem_70e5eaf0-4115-4207-9ea2-53ca8c210795.xml, UnlinkItemTree method [Imaging Devices], IWiaDrvItem interface, UnlinkItemTree method [Imaging Devices], IWiaDrvItem interface [Imaging Devices], UnlinkItemTree method, IWiaDrvItem, UnlinkItemTree, wiamindr_lh/IWiaDrvItem::UnlinkItemTree, IWiaDrvItem::UnlinkItemTree
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : wiamindr_lh.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : SCANWINDOW, *PSCANWINDOW
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

Minidrivers must call this method on the root item in the driver item tree when they want to invalidate the tree. This is typically done when the driver is being unloaded or when the minidriver needs to rebuild the driver item tree.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Me and in Windows XP and later versions of the Windows operating systems. Available in Windows Me and in Windows XP and later versions of the Windows operating systems. |
| **Target Platform** | Desktop |
| **Header** | wiamindr_lh.h (include Wiamindr.h) |
| **Library** | wiamindr_lh.h |