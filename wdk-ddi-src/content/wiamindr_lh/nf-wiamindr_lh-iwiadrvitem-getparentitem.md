---
UID : NF:wiamindr_lh.IWiaDrvItem.GetParentItem
title : IWiaDrvItem::GetParentItem method
author : windows-driver-content
description : The IWiaDrvItem::GetParentItem gets the parent item of the current item.
old-location : image\iwiadrvitem_getparentitem.htm
old-project : image
ms.assetid : e6197993-b998-424e-ab5d-a91a57c7398c
ms.author : windowsdriverdev
ms.date : 1/17/2018
ms.keywords : IWiaDrvItem, IWiaDrvItem::GetParentItem, GetParentItem
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
req.alt-api : IWiaDrvItem.GetParentItem
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


# GetParentItem method
The <b>IWiaDrvItem::GetParentItem</b> gets the parent item of the current item.

## Syntax

````
HRESULT GetParentItem(
  [out, optional] IWiaDrvItem **ppIParentItem
);
````

## Parameters

`__MIDL__IWiaDrvItem0012`




## Return Value

If the method succeeds, it stores a pointer to the parent item in <i>pplParentItem</i> and returns S_OK. If the parent item is the root item, the method returns S_FALSE. If the method fails, it returns a standard COM error code.

## Remarks

Minidrivers typically use this method to obtain a pointer to the nonroot parent item of the current item.

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

<dl>
<dt>
<a href="..\wiamindr_lh\nn-wiamindr_lh-iwiadrvitem.md">IWiaDrvItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543878">IWiaDrvItem::GetFirstChildItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543889">IWiaDrvItem::GetNextSiblingItem</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IWiaDrvItem::GetParentItem method%20 RELEASE:%20(1/17/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>