---
UID: NF:printoem.OEMRealizeBrush
title: OEMRealizeBrush function
author: windows-driver-content
description: The OEMRealizeBrush function requests that the driver realize a specified brush for a specified surface.
old-location: print\oemrealizebrush.htm
old-project: print
ms.assetid: 1c2c103b-41a4-48e8-8232-01719c562d62
ms.author: windowsdriverdev
ms.date: 2/2/2018
ms.keywords: OEMRealizeBrush, OEMRealizeBrush function [Print Devices], print.oemrealizebrush, print_unidrv-pscript_rendering_ab4f8635-9dda-4f08-b4f9-d70681ec532e.xml, printoem/OEMRealizeBrush
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: printoem.h
req.include-header: Printoem.h
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
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	printoem.h
apiname:
-	OEMRealizeBrush
product: Windows
targetos: Windows
req.typenames: STDVARIABLEINDEX
req.product: Windows 10 or later.
---


# OEMRealizeBrush function
The <code>OEMRealizeBrush</code> function requests that the driver realize a specified brush for a specified surface.

## Syntax

````
BOOL APIENTRY OEMRealizeBrush(
   BRUSHOBJ *pbo,
   SURFOBJ  *psoTarget,
   SURFOBJ  *psoPattern,
   SURFOBJ  *psoMask,
   XLATEOBJ *pxlo,
   ULONG    iHatch
);
````

## Parameters

`pbo`



`psoTarget`



`psoPattern`



`psoMask`



`pxlo`



`iHatch`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | printoem.h (include Printoem.h) |
| **Library** | NtosKrnl.exe |