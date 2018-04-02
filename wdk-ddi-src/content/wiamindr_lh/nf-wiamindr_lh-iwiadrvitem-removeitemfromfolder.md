---
UID: NF:wiamindr_lh.IWiaDrvItem.RemoveItemFromFolder
title: IWiaDrvItem::RemoveItemFromFolder method
author: windows-driver-content
description: The IWiaDrvItem::RemoveItemFromFolder method removes an item from a parent folder.
old-location: image\iwiadrvitem_removeitemfromfolder.htm
old-project: image
ms.assetid: f800427e-d6b6-4f4c-aee7-4b2b0d0aa0c4
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: DrvItem_240e14a4-36bd-4a72-b143-6f8f5c220682.xml, IWiaDrvItem, IWiaDrvItem interface [Imaging Devices], RemoveItemFromFolder method, IWiaDrvItem::RemoveItemFromFolder, RemoveItemFromFolder method [Imaging Devices], RemoveItemFromFolder method [Imaging Devices], IWiaDrvItem interface, RemoveItemFromFolder,IWiaDrvItem.RemoveItemFromFolder, image.iwiadrvitem_removeitemfromfolder, wiamindr_lh/IWiaDrvItem::RemoveItemFromFolder
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
-	IWiaDrvItem.RemoveItemFromFolder
product:
- Windows
targetos: Windows
req.typenames: SCANWINDOW, *PSCANWINDOW
req.product: Windows 10 or later.
---


# IWiaDrvItem::RemoveItemFromFolder method
The <b>IWiaDrvItem::RemoveItemFromFolder</b> method removes an item from a parent folder.

## Syntax

```
HRESULT RemoveItemFromFolder(
  LONG __MIDL__IWiaDrvItem0006
);
```

## Parameters

`__MIDL__IWiaDrvItem0006`




## Return Value

If the method succeeds, it returns S_OK. If the item to be removed is a folder and the folder is not empty, the method returns E_INVALIDARG. If <i>lReason</i> contains an invalid reason, the method returns E_INVALIDARG. If the method fails for another reason, it returns a standard COM error code.

## Remarks

After the item has been removed from the folder, it can no longer be used for device access.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Me and in Windows XP and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | wiamindr_lh.h (include Wiamindr.h) |

## See Also

<a href="https://msdn.microsoft.com/0609e1b2-48df-413c-90bd-d7ddea26510a">IWiaDrvItem</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543856">IWiaDrvItem::AddItemToFolder</a>