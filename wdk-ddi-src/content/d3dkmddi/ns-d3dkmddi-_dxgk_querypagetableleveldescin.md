---
UID : NS:d3dkmddi._DXGK_QUERYPAGETABLELEVELDESCIN
title : _DXGK_QUERYPAGETABLELEVELDESCIN
author : windows-driver-content
description : The DXGK_QUERYPAGETABLELEVELDESCIN structure is used to request page level descriptors from the Dxgkrnl Interface.
old-location : display\dxgk_querypagetableleveldescin.htm
old-project : display
ms.assetid : 1B13BBB1-4184-4166-A61F-CC266D0391BF
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_QUERYPAGETABLELEVELDESCIN, DXGK_QUERYPAGETABLELEVELDESCIN
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmddi.h
req.include-header : D3dkmddi.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXGK_QUERYPAGETABLELEVELDESCIN
req.alt-loc : d3dkmddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : DXGK_QUERYPAGETABLELEVELDESCIN
---

# _DXGK_QUERYPAGETABLELEVELDESCIN structure
The <b>DXGK_QUERYPAGETABLELEVELDESCIN</b> structure is used to request page level descriptors from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560940">Dxgkrnl Interface</a>.

## Syntax
````
typedef struct _DXGK_QUERYPAGETABLELEVELDESCIN {
  WORD LevelIndex;
  WORD PhysicalAdapterIndex;
} DXGK_QUERYPAGETABLELEVELDESCIN;
````

## Members

        
            `LevelIndex`

            A zero-based physical adapter index (engine ordinal) for which the data is queried.
        
            `PhysicalAdapterIndex`

            A zero-based page table level index for the information requested.

    ## Remarks
        To get page table level descriptors Dxgkrnl calls <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_queryadapterinfo.md">DxgkDdiQueryAdapterInfo</a> with the following parameters:</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |