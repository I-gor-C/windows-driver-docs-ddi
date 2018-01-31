---
UID : NF:wiamindr_lh.IWiaDrvItem.RemoveItemFromFolder
title : IWiaDrvItem::RemoveItemFromFolder method
author : windows-driver-content
description : The IWiaDrvItem::RemoveItemFromFolder method removes an item from a parent folder.
old-location : image\iwiadrvitem_removeitemfromfolder.htm
old-project : image
ms.assetid : f800427e-d6b6-4f4c-aee7-4b2b0d0aa0c4
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : wiamindr_lh/IWiaDrvItem::RemoveItemFromFolder, image.iwiadrvitem_removeitemfromfolder, IWiaDrvItem::RemoveItemFromFolder, RemoveItemFromFolder method [Imaging Devices], IWiaDrvItem, RemoveItemFromFolder, RemoveItemFromFolder method [Imaging Devices], IWiaDrvItem interface, DrvItem_240e14a4-36bd-4a72-b143-6f8f5c220682.xml, IWiaDrvItem interface [Imaging Devices], RemoveItemFromFolder method
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
req.typenames : "*PSCANWINDOW, SCANWINDOW"
req.product : Windows 10 or later.
---


# RemoveItemFromFolder method
The <b>IWiaDrvItem::RemoveItemFromFolder</b> method removes an item from a parent folder.

## Syntax

````
HRESULT RemoveItemFromFolder(
  [in] LONG lReason
);
````

## Parameters

`__MIDL__IWiaDrvItem0006`




## Return Value

If the method succeeds, it returns S_OK. If the item to be removed is a folder and the folder is not empty, the method returns E_INVALIDARG. If <i>lReason</i> contains an invalid reason, the method returns E_INVALIDARG. If the method fails for another reason, it returns a standard COM error code.

## Remarks

After the item has been removed from the folder, it can no longer be used for device access.

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

## See Also

<a href="..\wiamindr_lh\nn-wiamindr_lh-iwiadrvitem.md">IWiaDrvItem</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543856">IWiaDrvItem::AddItemToFolder</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IWiaDrvItem::RemoveItemFromFolder method%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>