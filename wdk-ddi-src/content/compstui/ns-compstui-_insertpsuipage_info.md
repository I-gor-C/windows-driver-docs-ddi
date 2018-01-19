---
UID : NS:compstui._INSERTPSUIPAGE_INFO
title : _INSERTPSUIPAGE_INFO
author : windows-driver-content
description : The INSERTPSUIPAGE_INFO structure is used as an input parameter to CPSUI's ComPropSheet function, if the function code is CPSFUNC_INSERT_PSUIPAGE. All member values must be supplied by the ComPropSheet caller.
old-location : print\insertpsuipage_info.htm
old-project : print
ms.assetid : 99ec8cfa-3ec7-4080-b22a-dba0a86b7e4a
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : _INSERTPSUIPAGE_INFO, *PINSERTPSUIPAGE_INFO, INSERTPSUIPAGE_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : compstui.h
req.include-header : Compstui.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : INSERTPSUIPAGE_INFO
req.alt-loc : compstui.h
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
req.typenames : "*PINSERTPSUIPAGE_INFO, INSERTPSUIPAGE_INFO"
---

# _INSERTPSUIPAGE_INFO structure
The INSERTPSUIPAGE_INFO structure is used as an input parameter to CPSUI's <a href="https://msdn.microsoft.com/library/windows/hardware/ff546207">ComPropSheet</a> function, if the function code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff546414">CPSFUNC_INSERT_PSUIPAGE</a>. All member values must be supplied by the <b>ComPropSheet</b> caller.

## Syntax
````
typedef struct _INSERTPSUIPAGE_INFO {
  WORD      cbSize;
  BYTE      Type;
  BYTE      Mode;
  ULONG_PTR dwData1;
  ULONG_PTR dwData2;
  ULONG_PTR dwData3;
} INSERTPSUIPAGE_INFO, *PINSERTPSUIPAGE_INFO;
````

## Members

        
            `cbSize`

            Caller-supplied size, in bytes, of the INSERTPSUIPAGE_INFO structure.
        
            `dwData1`

            
        
            `dwData2`

            
        
            `dwData3`

            Caller-supplied values that depend on the contents of the <b>Type</b> member, as follows:
        
            `Mode`

            Caller-supplied value indicating where CPSUI should insert the new pages. It must be one of the following values:
        
            `Type`

            Caller-supplied integer value indicating the type of insertion being requested. The member can contain one of the following constants:


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | compstui.h (include Compstui.h) |