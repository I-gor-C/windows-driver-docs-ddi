---
UID: NF:wiautil.CWiauPropertyList.SetAccessSubType
title: CWiauPropertyList::SetAccessSubType method
author: windows-driver-content
description: The CWiauPropertyList::SetAccessSubType method resets a property's access and subtype.
old-location: image\cwiaupropertylist_setaccesssubtype.htm
old-project: image
ms.assetid: 207125d3-0833-4c5d-b66f-aa49c96a6a2d
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: CWiauPropertyList, CWiauPropertyList interface [Imaging Devices], SetAccessSubType method, CWiauPropertyList::SetAccessSubType, SetAccessSubType method [Imaging Devices], SetAccessSubType method [Imaging Devices], CWiauPropertyList interface, SetAccessSubType,CWiauPropertyList.SetAccessSubType, image.cwiaupropertylist_setaccesssubtype, wiauFncs_ab4b792f-54f0-4efa-bb13-5b71d94e03e0.xml, wiautil/CWiauPropertyList::SetAccessSubType
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wiautil.h
req.include-header: Wiautil.h, Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
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
-	Wiautil.h
api_name:
-	CWiauPropertyList.SetAccessSubType
product: Windows
targetos: Windows
req.typenames: SKIP_AMOUNT
req.product: Windows 10 or later.
---


# CWiauPropertyList::SetAccessSubType method
The <b>CWiauPropertyList::SetAccessSubType</b> method resets a property's access and subtype.

## Syntax

```
void SetAccessSubType(
  INT   index,
  ULONG Access,
  ULONG SubType
);
```

## Parameters

`index`

Specifies the property's index in the property list.

`Access`

Specifies the type of access for the property, usually either WIA_PROP_READ (read-only) or WIA_PROP_RW (read/write).

`SubType`

Specifies the property subtype, one of WIA_PROP_FLAG, WIA_PROP_LIST, WIA_PROP_RANGE, or WIA_PROP_NONE. The first three constants indicate, respectively, that a property is a set of flag values, a list of values, or a range of values. The fourth constant indicates that a property is none of these.


## Return Value

This method does not return a value.

## Remarks

The WIA_PROP_<i>XXX</i> constants are defined in the Microsoft Windows SDK documentation.

A property's access and subtype are set originally in a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540391">CWiauPropertyList::DefineProperty</a> method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows XP and later.  |
| **Target Platform** | Desktop |
| **Header** | wiautil.h (include Wiautil.h, Wiamindr.h) |

## See Also

<a href="https://msdn.microsoft.com/4f11bec0-8ff4-4fa0-824c-71ce9774d5d1">CWiauPropertyList</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540391">CWiauPropertyList::DefineProperty</a>