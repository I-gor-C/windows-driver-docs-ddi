---
UID : NS:iddcx.IDARG_IN_COMMITMODES
title : IDARG_IN_COMMITMODES
author : windows-driver-content
description : Gives information about the paths that need to be committed.
old-location : display\idarg_in_commitmodes.htm
old-project : display
ms.assetid : 242b7573-409a-4fdc-8ebf-596b8e6d41c7
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.idarg_in_commitmodes, IDARG_IN_COMMITMODES structure [Display Devices], IDARG_IN_COMMITMODES, iddcx/IDARG_IN_COMMITMODES
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : iddcx.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
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
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : 
---

# IDARG_IN_COMMITMODES structure
Gives information about the paths that need to be committed.

## Syntax
````
typedef struct IDARG_IN_COMMITMODES {
  UINT                                PathCount;
  _Field_size_(PathCount) IDDCX_PATH* pPaths;
} IDARG_IN_COMMITMODES, *IDARG_IN_COMMITMODES;
````

## Members


`PathCount`

[in] The number of paths in the <b>pPaths</b> array

`pPaths`

[in] A pointer to the array of paths that need to be committed.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | iddcx.h |