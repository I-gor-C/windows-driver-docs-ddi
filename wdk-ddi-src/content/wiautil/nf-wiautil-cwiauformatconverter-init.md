---
UID : NF:wiautil.CWiauFormatConverter.Init
title : CWiauFormatConverter::Init method
author : windows-driver-content
description : The CWiauFormatConverter::Init method initializes the CWiauFormatConverter class and GDI+ for converting images. This method should be called only once.
old-location : image\cwiauformatconverter_init.htm
old-project : image
ms.assetid : 342ea1ae-ff8c-429d-bee8-08559fe75b40
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : Init method [Imaging Devices], CWiauFormatConverter interface, Init method [Imaging Devices], CWiauFormatConverter::Init, wiautil/CWiauFormatConverter::Init, CWiauFormatConverter, wiauFncs_d762c597-47d1-446a-b76d-7993ba32f571.xml, image.cwiauformatconverter_init, Init, CWiauFormatConverter interface [Imaging Devices], Init method
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : wiautil.h
req.include-header : Wiautil.h, Wiamindr.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows XP and later.
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
req.lib : wiautil.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : SKIP_AMOUNT
req.product : Windows 10 or later.
---


# Init method
The <b>CWiauFormatConverter::Init</b> method initializes the <b>CWiauFormatConverter</b> class and GDI+ for converting images. This method should be called only once.

## Syntax

````
HRESULT Init();
````

## Parameters

This function has no parameters.

## Return Value

On success, the function returns S_OK. If the function fails, it returns a standard COM error.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wiautil.h (include Wiautil.h, Wiamindr.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |