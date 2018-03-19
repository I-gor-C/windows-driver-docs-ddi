---
UID: NF:ks.KsFreeObjectBag
title: KsFreeObjectBag function
author: windows-driver-content
description: The KsFreeObjectBag function empties and frees an object bag.
old-location: stream\ksfreeobjectbag.htm
old-project: stream
ms.assetid: d0bc4e8b-b173-4568-8c0f-7b87fd84e2cf
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KsFreeObjectBag, KsFreeObjectBag function [Streaming Media Devices], avfunc_f91aca67-5d6c-42f7-9e24-3b15b54c2b69.xml, ks/KsFreeObjectBag, stream.ksfreeobjectbag
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Ks.lib
-	Ks.dll
api_name:
-	KsFreeObjectBag
product: Windows
targetos: Windows
req.typenames: 
---


# KsFreeObjectBag function
The<b> KsFreeObjectBag</b> function empties and frees an object bag.

## Syntax

````
void KsFreeObjectBag(
  _In_ KSOBJECT_BAG ObjectBag
);
````

## Parameters

`ObjectBag`

The KSOBJECT_BAG (equivalent to type PVOID) to be emptied and then freed.


## Return Value

None

## Remarks

For more information, see <a href="https://msdn.microsoft.com/b7ee5756-1c79-4ead-9999-d13be9a0d3d9">Object Bags</a>.

<b>KsFreeObjectBag</b> removes any items present in <i>ObjectBag</i>. In addition, if the reference count for a given object is zero (that is, the object is not present in any other object bag associated with the same device as <i>ObjectBag</i>), then that item is freed.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.  |
| **Target Platform** | Universal |
| **Header** | ks.h (include Ks.h) |
| **Library** | Ks.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\ks\nf-ks-ksallocateobjectbag.md">KsAllocateObjectBag</a>



<a href="..\ks\nf-ks-ksadditemtoobjectbag.md">KsAddItemToObjectBag</a>



<a href="..\ks\nf-ks-kscopyobjectbagitems.md">KsCopyObjectBagItems</a>



<a href="..\ks\nf-ks-ksremoveitemfromobjectbag.md">KsRemoveItemFromObjectBag</a>



<a href="..\ks\nf-ks-ksdiscard.md">KsDiscard</a>