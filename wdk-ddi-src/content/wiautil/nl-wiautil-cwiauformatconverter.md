---
UID: NL:wiautil.CWiauFormatConverter
title: CWiauFormatConverter
author: windows-driver-content
description: The CWiauFormatConverter class is a helper class for converting images to BMP format.
old-location: image\cwiauformatconverter_class.htm
old-project: image
ms.assetid: b30c3336-ddc6-459d-97c4-244ca0b50cfc
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: image.cwiauformatconverter_class, CWiauFormatConverter interface [Imaging Devices], CWiauFormatConverter interface [Imaging Devices], described, CWiauFormatConverter, wiautil/CWiauFormatConverter, wiauFncs_8d01dc38-ef09-425a-ade6-d06bd0e1e08a.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: class
req.header: wiautil.h
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
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	wiautil.h
apiname:
-	CWiauFormatConverter
product: Windows
targetos: Windows
req.typenames: SKIP_AMOUNT
req.product: Windows 10 or later.
---

# CWiauFormatConverter Class
The <b>CWiauFormatConverter</b> class is a helper class for converting images to BMP format.

## Methods

<p>The <b>CWiauFormatConverter</b> class has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wiautil.CWiauFormatConverter.~CWiauFormatConverter](nf-wiautil-cwiauformatconverter-~cwiauformatconverter.md) | The CWiauFormatConverter::~CWiauFormatConverter method is the destructor for the CWiauFormatConverter class. |
| [wiautil.CWiauFormatConverter.ConvertToBmp](nf-wiautil-cwiauformatconverter-converttobmp.md) | The CWiauFormatConverter::ConvertToBmp method converts an image to BMP format. |
| [wiautil.CWiauFormatConverter.CWiauFormatConverter](nf-wiautil-cwiauformatconverter-cwiauformatconverter.md) | The CWiauFormatConverter::CWiauFormatConverter method is the constructor for the CWiauFormatConverter class. |
| [wiautil.CWiauFormatConverter.Init](nf-wiautil-cwiauformatconverter-init.md) | The CWiauFormatConverter::Init method initializes the CWiauFormatConverter class and GDI+ for converting images. This method should be called only once. |
| [wiautil.CWiauFormatConverter.IsFormatSupported](nf-wiautil-cwiauformatconverter-isformatsupported.md) | The CWiauFormatConverter::IsFormatSupported method verifies that GDI+ supports the image format that is to be converted. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wiautil.h |