---
UID: NF:wiamindr_lh.IWiaDrvItem.GetNextSiblingItem
title: IWiaDrvItem::GetNextSiblingItem method
author: windows-driver-content
description: The IWiaDrvItem::GetNextSiblingItem method gets the next sibling of the current item in an IWiaDrvItem folder.
old-location: image\iwiadrvitem_getnextsiblingitem.htm
old-project: image
ms.assetid: bc348f40-aaa4-4cd4-9dee-c02748d7412c
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: DrvItem_659ed27a-dca2-40de-acb7-f057178e9ab7.xml, GetNextSiblingItem method [Imaging Devices], GetNextSiblingItem method [Imaging Devices], IWiaDrvItem interface, GetNextSiblingItem,IWiaDrvItem.GetNextSiblingItem, IWiaDrvItem, IWiaDrvItem interface [Imaging Devices], GetNextSiblingItem method, IWiaDrvItem::GetNextSiblingItem, image.iwiadrvitem_getnextsiblingitem, wiamindr_lh/IWiaDrvItem::GetNextSiblingItem
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	wiamindr_lh.h
api_name:
-	IWiaDrvItem.GetNextSiblingItem
product: Windows
targetos: Windows
req.typenames: SCANWINDOW, *PSCANWINDOW
req.product: Windows 10 or later.
---


# IWiaDrvItem::GetNextSiblingItem method
The <b>IWiaDrvItem::GetNextSiblingItem</b> method gets the next sibling of the current item in an <b>IWiaDrvItem</b> folder.

## Syntax

```
HRESULT GetNextSiblingItem(
  IWiaDrvItem **__MIDL__IWiaDrvItem0014
);
```

## Parameters

`__MIDL__IWiaDrvItem0014`




## Return Value

If the method succeeds, it stores a pointer to the next sibling item in <i>ppISiblingItem</i> and returns S_OK. If there are no more items in the folder, the method returns S_FALSE. If the method fails, it returns a standard COM error code.

## Remarks

Minidrivers obtain a pointer to the first child item in a folder by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543878">IWiaDrvItem::GetFirstChildItem</a>. Minidrivers can then obtain the sibling items of this child item in the folder by making successive calls to <b>IWiaDrvItem::GetNextSiblingItem</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Me and in Windows XP and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | wiamindr_lh.h (include Wiamindr.h) |

## See Also

<a href="https://msdn.microsoft.com/0609e1b2-48df-413c-90bd-d7ddea26510a">IWiaDrvItem</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543878">IWiaDrvItem::GetFirstChildItem</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543892">IWiaDrvItem::GetParentItem</a>