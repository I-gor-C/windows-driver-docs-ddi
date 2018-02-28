---
UID: NS:d3dkmddi._DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS
title: "_DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS"
author: windows-driver-content
description: A structure containing the set of flags needed to set the VidPN source address.
old-location: display\dxgk_setvidpnsourceaddress_input_flags.htm
old-project: display
ms.assetid: FBC661AA-B028-45AF-8E3C-7C2472652BD5
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS, DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS structure [Display Devices], _DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS, d3dkmddi/DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS, display.dxgk_setvidpnsourceaddress_input_flags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: 
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS
---

# _DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS structure
A structure containing the set of flags needed to set the VidPN source address.

## Syntax
````
typedef struct _DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS {
  union {
    struct {
      UINT FlipStereo  :1;
      UINT FlipStereoTemporaryMono  :1;
      UINT FlipStereoPreferRight   :1;
      UINT RetryAtLowerIrql  :1;
      UINT Reserved  :28;
    };
    UINT Value;
  };
} DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |