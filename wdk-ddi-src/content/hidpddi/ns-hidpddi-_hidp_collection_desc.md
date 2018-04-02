---
UID: NS:hidpddi._HIDP_COLLECTION_DESC
title: "_HIDP_COLLECTION_DESC"
author: windows-driver-content
description: Contains the information of a top-level-collection. This structure is used in the HidP_GetCollectionDescription call.
old-location: hid\hidp_collection_desc.htm
old-project: hid
ms.assetid: 4B044635-1088-4CED-87C7-4385E565A54A
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*PHIDP_COLLECTION_DESC, HIDP_COLLECTION_DESC, HIDP_COLLECTION_DESC structure [Human Input Devices], PHIDP_COLLECTION_DESC, PHIDP_COLLECTION_DESC structure pointer [Human Input Devices], _HIDP_COLLECTION_DESC, hid.hidp_collection_desc, hidpddi/HIDP_COLLECTION_DESC, hidpddi/PHIDP_COLLECTION_DESC"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hidpddi.h
req.include-header: Hidpddi.h
req.target-type: Windows
req.target-min-winverclnt: 
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
req.irql: "<= DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Hidpddi.h
api_name:
-	HIDP_COLLECTION_DESC
product:
- Windows
targetos: Windows
req.typenames: HIDP_COLLECTION_DESC, *PHIDP_COLLECTION_DESC
---

# _HIDP_COLLECTION_DESC structure
Contains the information of a top-level-collection. This structure is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt740164">HidP_GetCollectionDescription</a> call.

## Syntax
```
typedef struct _HIDP_COLLECTION_DESC {
  USAGE                UsagePage;
  USAGE                Usage;
  UCHAR                CollectionNumber;
  UCHAR                Reserved[15];
  USHORT               InputLength;
  USHORT               OutputLength;
  USHORT               FeatureLength;
  USHORT               PreparsedDataLength;
  PHIDP_PREPARSED_DATA PreparsedData;
} HIDP_COLLECTION_DESC, *PHIDP_COLLECTION_DESC;
```

## Members


`UsagePage`

Specifies the usage page of the usage ID specified by <b>Usage</b>.

`Usage`

Indicates a usage ID.

`CollectionNumber`

The index of the collection in the array of  <b>HIDP_COLLECTION_DESC</b> structure. This is a 1-based value.

`Reserved`

Reserved for internal system use. Must be 0.

`InputLength`

The maximum length of an input report of this collection.

`OutputLength`

The maximum length of an output report of this collection.

`FeatureLength`

The maximum length of a feature report of this collection.

`PreparsedDataLength`

The length of the preparsed data pointed to by <i>PreparsedData</i>.

`PreparsedData`

A pointer to a <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff539679">_HIDP_PREPARSED_DATA</a> structure that contains a top-level collection's preparsed data.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | hidpddi.h (include Hidpddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt740164">HidP_GetCollectionDescription</a>