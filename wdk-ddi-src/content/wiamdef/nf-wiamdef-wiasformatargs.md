---
UID : NF:wiamdef.wiasFormatArgs
title : wiasFormatArgs function
author : windows-driver-content
description : The wiasFormatArgs function formats an argument list into a packaged string for logging.
old-location : image\wiasformatargs.htm
old-project : image
ms.assetid : 409c4ff6-3a0e-408a-879d-2875ac245fb8
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : wiasFormatArgs, wiasFormatArgs function [Imaging Devices], wiasFncs_c4e9a1bd-3760-47fb-b828-1f0c521717c5.xml, wiamdef/wiasFormatArgs, image.wiasformatargs
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wiamdef.h
req.include-header : Wiamdef.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.
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
req.lib : Wiaservc.lib
req.dll : Wiaservc.dll
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DEVICEDIALOGDATA2, *PDEVICEDIALOGDATA2, *LPDEVICEDIALOGDATA2
req.product : Windows 10 or later.
---


# wiasFormatArgs function
The <b>wiasFormatArgs</b> function formats an argument list into a packaged string for logging.

## Syntax

````
BSTR __cdecl wiasFormatArgs(
   LPCSTR   lpszFormat, ...
);
````

## Parameters

`lpszFormat`

TBD

``




## Return Value

This function returns a BSTR containing the format string, the arguments following the format string, and a format signature.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wiamdef.h (include Wiamdef.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |