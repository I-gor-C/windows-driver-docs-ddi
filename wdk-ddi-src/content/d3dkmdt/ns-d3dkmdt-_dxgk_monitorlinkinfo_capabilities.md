---
UID : NS:d3dkmdt._DXGK_MONITORLINKINFO_CAPABILITIES
title : _DXGK_MONITORLINKINFO_CAPABILITIES
author : windows-driver-content
description : Flags which describe the capabilities for driving the monitor.
old-location : display\dxgk_monitorlinkinfo_capabilities.htm
old-project : display
ms.assetid : 9838DF74-6561-40DB-A745-A15005B97AAC
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_MONITORLINKINFO_CAPABILITIES, DXGK_MONITORLINKINFO_CAPABILITIES, *PDXGK_MONITORLINKINFO_CAPABILITIES
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmdt.h
req.include-header : D3dkmddi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXGK_MONITORLINKINFO_CAPABILITIES
req.alt-loc : d3dkmdt.h
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
req.typenames : DXGK_MONITORLINKINFO_CAPABILITIES, *PDXGK_MONITORLINKINFO_CAPABILITIES
---

# _DXGK_MONITORLINKINFO_CAPABILITIES structure
Flags which describe the capabilities for driving the monitor.

## Syntax
````
typedef union _DXGK_MONITORLINKINFO_CAPABILITIES {
  struct {
    UINT Stereo  :1;
    UINT WideColorSpace  :1;
    UINT HighColorSpace  :1;
    UINT DynamicColorSpace  :1;
    UINT DynamicBitsPerColorChannel  :1;
    UINT DynamicColorEncodingFormat  :1;
    UINT DedicatedTimingGeneration  :1;
  };
  UINT Reserved  :25;
} DXGK_MONITORLINKINFO_CAPABILITIES, *PDXGK_MONITORLINKINFO_CAPABILITIES;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmdt.h (include D3dkmddi.h) |