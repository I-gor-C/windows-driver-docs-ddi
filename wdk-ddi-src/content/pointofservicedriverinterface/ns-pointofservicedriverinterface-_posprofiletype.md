---
UID: NS:pointofservicedriverinterface._PosProfileType
title: "_PosProfileType"
author: windows-driver-content
description: This structure describes the number of profile strings in a buffer.
old-location: pos\posprofiletype.htm
old-project: pos
ms.assetid: b0ef1592-f3f3-4ca1-83f8-dc7cb76cda36
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: PosProfileType, pointofservicedriverinterface/PosProfileType, PosProfileType structure, _PosProfileType, pos.posprofiletype
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pointofservicedriverinterface.h
req.include-header: PointOfServiceDriverInterface.h
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
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	PointOfServiceDriverInterface.h
apiname:
-	PosProfileType
product: Windows
targetos: Windows
req.typenames: PosProfileType
---

# _PosProfileType structure
This structure describes the number of profile strings in a buffer.

## Syntax
````
typedef struct _PosProfileType {
  UINT32 EntryCount;
  UINT32 DataLength;
} PosProfileType;
````

## Members


`BufferSize`



`ProfileCount`



## Remarks
The buffer of profile <i>PosStringType</i> strings follows this structure in memory.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include PointOfServiceDriverInterface.h) |