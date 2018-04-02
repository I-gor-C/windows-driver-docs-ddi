---
UID: NN:prcomoem.IPrintCorePS2
title: IPrintCorePS2
author: windows-driver-content
description: This section describes the methods defined for the IPrintCorePS2 COM Interface. Method prototypes are defined in prcomoem.h.
old-location: print\iprintcoreps2_interface.htm
old-project: print
ms.assetid: bf7e15df-49ba-4850-acf6-dab5dc137f48
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintCorePS2, IPrintCorePS2 interface [Print Devices], IPrintCorePS2 interface [Print Devices], described, prcomoem/IPrintCorePS2, print.iprintcoreps2_interface, print_unidrv-pscript_rendering_ee16e348-6dec-4820-ab6c-d41adecf8c74.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: prcomoem.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	prcomoem.h
api_name:
-	IPrintCorePS2
product:
- Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintCorePS2 interface

This section describes the methods defined for the <a href="https://msdn.microsoft.com/d5eb6962-2201-405f-9a22-2b11fb6d0360">IPrintCorePS2 COM Interface</a>. Method prototypes are defined in prcomoem.h.

## Methods

<p>The <b>IPrintCorePS2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintCorePS2::DrvWriteSpoolBuf](nf-prcomoem-iprintcoreps2-drvwritespoolbuf.md) | The IPrintCorePS2::DrvWriteSpoolBuf method is provided by the Pscript5 driver so that a rendering plug-in can send printer data to the spooler. |
| [IPrintCorePS2::EnumFeatures](nf-prcomoem-iprintcoreps2-enumfeatures.md) | The IPrintCorePS2::EnumFeatures method enumerates a printer's available features. |
| [IPrintCorePS2::EnumOptions](nf-prcomoem-iprintcoreps2-enumoptions.md) | The IPrintCorePS2::EnumOptions method enumerates the available options of a specific feature. |
| [IPrintCorePS2::GetFeatureAttribute](nf-prcomoem-iprintcoreps2-getfeatureattribute.md) | The IPrintCorePS2::GetFeatureAttribute method retrieves the feature attribute list or the value of a specific feature attribute. |
| [IPrintCorePS2::GetGlobalAttribute](nf-prcomoem-iprintcoreps2-getglobalattribute.md) | The IPrintCorePS2::GetGlobalAttribute method retrieves the global attribute list or the value of a specific global attribute. |
| [IPrintCorePS2::GetOptionAttribute](nf-prcomoem-iprintcoreps2-getoptionattribute.md) | The IPrintCorePS2::GetOptionAttribute method retrieves the option attribute list or the value of a specific option attribute. |
| [IPrintCorePS2::GetOptions](nf-prcomoem-iprintcoreps2-getoptions.md) | The IPrintCorePS2::GetOptions method retrieves the driver's current feature settings in the format of a list of feature/option keyword pairs. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |