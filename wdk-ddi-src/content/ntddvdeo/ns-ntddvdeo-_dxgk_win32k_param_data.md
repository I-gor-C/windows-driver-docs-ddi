---
UID : NS:ntddvdeo._DXGK_WIN32K_PARAM_DATA
title : "_DXGK_WIN32K_PARAM_DATA"
author : windows-driver-content
description : The DXGK_WIN32K_PARAM_DATA structure is reserved for system use.
old-location : display\dxgk_win32k_param_data.htm
old-project : display
ms.assetid : a6bb2127-64f7-402d-906e-199d5ec1b313
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : "*PDXGK_WIN32K_PARAM_DATA, ntddvdeo/PDXGK_WIN32K_PARAM_DATA, DXGK_WIN32K_PARAM_DATA, Video_Structs_40ff171a-ad28-44ae-bcad-bf93aba4ad6e.xml, display.dxgk_win32k_param_data, ntddvdeo/DXGK_WIN32K_PARAM_DATA, PDXGK_WIN32K_PARAM_DATA structure pointer [Display Devices], _DXGK_WIN32K_PARAM_DATA, PDXGK_WIN32K_PARAM_DATA, DXGK_WIN32K_PARAM_DATA structure [Display Devices]"
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddvdeo.h
req.include-header : Ntddvdeo.h
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
req.typenames : "*PDXGK_WIN32K_PARAM_DATA, DXGK_WIN32K_PARAM_DATA"
---

# _DXGK_WIN32K_PARAM_DATA structure
The DXGK_WIN32K_PARAM_DATA structure is reserved for system use.

## Syntax
````
typedef struct _DXGK_WIN32K_PARAM_DATA {
  PVOID PathsArray;
  PVOID ModesArray;
  ULONG NumPathArrayElements;
  ULONG NumModeArrayElements;
  ULONG SDCFlags;
} DXGK_WIN32K_PARAM_DATA, *PDXGK_WIN32K_PARAM_DATA;
````

## Members


`ModesArray`

Reserved for system use.

`NumModeArrayElements`

Reserved for system use.

`NumPathArrayElements`

Reserved for system use.

`PathsArray`

Reserved for system use.

`SDCFlags`

Reserved for system use.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddvdeo.h (include Ntddvdeo.h) |