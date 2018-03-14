---
UID: NN:prcomoem.IPrintOemDriverUI
title: IPrintOemDriverUI
author: windows-driver-content
description: This section describes the methods defined for the IPrintOemDriverUI COM Interface.
old-location: print\iprintoemdriverui_interface.htm
old-project: print
ms.assetid: 2a885dd5-d328-4aae-8771-613ff93b35ac
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintOemDriverUI, IPrintOemDriverUI interface [Print Devices], IPrintOemDriverUI interface [Print Devices], described, prcomoem/IPrintOemDriverUI, print.iprintoemdriverui_interface, print_unidrv-pscript_ui_af445d30-9f51-4759-867d-d93e9ae0bc34.xml
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
-	IPrintOemDriverUI
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintOemDriverUI interface

This section describes the methods defined for the IPrintOemDriverUI COM Interface.

## Methods

<p>The <b>IPrintOemDriverUI</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintOemDriverUI::DrvGetDriverSetting](nf-prcomoem-iprintoemdriverui-drvgetdriversetting.md) | The IPrintOemDriverUI::DrvGetDriverSetting method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can obtain the current status of printer features and other internal information. |
| [IPrintOemDriverUI::DrvUpdateUISetting](nf-prcomoem-iprintoemdriverui-drvupdateuisetting.md) | The IPrintOemDriverUI::DrvUpdateUISetting method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can notify the driver of a modified user interface option. |
| [IPrintOemDriverUI::DrvUpgradeRegistrySetting](nf-prcomoem-iprintoemdriverui-drvupgraderegistrysetting.md) | The IPrintOemDriverUI::DrvUpdateRegistrySetting method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can update device settings stored in the registry. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |