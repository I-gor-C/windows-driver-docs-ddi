---
UID: NN:prcomoem.IPrintOemUI
title: IPrintOemUI
author: windows-driver-content
description: This section describes the methods defined for the IPrintOemUI COM interface.
old-location: print\iprintoemui_interface.htm
old-project: print
ms.assetid: 0ef635dd-9598-4356-94fc-7e5237df9bd9
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintOemUI, IPrintOemUI interface [Print Devices], IPrintOemUI interface [Print Devices], described, prcomoem/IPrintOemUI, print.iprintoemui_interface, print_unidrv-pscript_ui_d2e42772-2604-4ef1-a667-70139ac8a62a.xml
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
-	IPrintOemUI
product:
- Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintOemUI interface

This section describes the methods defined for the <b>IPrintOemUI</b> COM interface.

## Methods

<p>The <b>IPrintOemUI</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintOemUI::CommonUIProp](nf-prcomoem-iprintoemui-commonuiprop.md) | The IPrintOemUI::CommonUIProp method allows a user interface plug-in to modify an existing printer property sheet page. |
| [IPrintOemUI::DeviceCapabilities](nf-prcomoem-iprintoemui-devicecapabilities.md) | The IPrintOemUI::DeviceCapabilities method enables a user interface plug-in to specify customized device capabilities. |
| [IPrintOemUI::DevicePropertySheets](nf-prcomoem-iprintoemui-devicepropertysheets.md) | The IPrintOemUI::DevicePropertySheets method allows a user interface plug-in to append a new page to a printer device's printer property sheet. |
| [IPrintOemUI::DevMode](nf-prcomoem-iprintoemui-devmode.md) | The IPrintOemUI::DevMode method, provided by user interface plug-ins, performs operations on the plug-in's private DEVMODEW members. |
| [IPrintOemUI::DevQueryPrintEx](nf-prcomoem-iprintoemui-devqueryprintex.md) | The IPrintOemUI::DevQueryPrintEx method allows a user interface plug-in to help determine if a print job is printable. |
| [IPrintOemUI::DocumentPropertySheets](nf-prcomoem-iprintoemui-documentpropertysheets.md) | The IPrintOemUI::DocumentPropertySheets method allows a user interface plug-in to append a new page to a printer device's document property sheet. |
| [IPrintOemUI::DriverEvent](nf-prcomoem-iprintoemui-driverevent.md) | The printer driver's DrvDriverEvent function calls a user interface plug-in's IPrintOemUI::DriverEvent method for additional processing of printer driver events. |
| [IPrintOemUI::FontInstallerDlgProc](nf-prcomoem-iprintoemui-fontinstallerdlgproc.md) | A user interface plug-in's IPrintOemUI::FontInstallerDlgProc method replaces the Unidrv font installer's user interface. |
| [IPrintOemUI::GetInfo](nf-prcomoem-iprintoemui-getinfo.md) | A user interface plug-in's IPrintOemUI::GetInfo method returns identification information. |
| [IPrintOemUI::PrinterEvent](nf-prcomoem-iprintoemui-printerevent.md) | The IPrintOemUI::PrinterEvent method allows a user interface plug-in to process printer events. |
| [IPrintOemUI::PublishDriverInterface](nf-prcomoem-iprintoemui-publishdriverinterface.md) | The IPrintOemUI::PublishDriverInterface method allows a user interface plug-in to obtain the Unidrv or Pscript5 driver's IPrintOemDriverUI, IPrintCoreUI2, IPrintCoreHelperPS, or IPrintCoreHelperUni interface. |
| [IPrintOemUI::QueryColorProfile](nf-prcomoem-iprintoemui-querycolorprofile.md) | The IPrintOemUI::QueryColorProfile method allows a user interface plug-in to specify an ICC profile to use for color management. |
| [IPrintOemUI::UpdateExternalFonts](nf-prcomoem-iprintoemui-updateexternalfonts.md) | The IPrintOemUI::UpdateExternalFonts method allows a user interface plug-in to update a printer's Unidrv Font Format Files (.uff file). |
| [IPrintOemUI::UpgradePrinter](nf-prcomoem-iprintoemui-upgradeprinter.md) | The IPrintOemUI::UpgradePrinter method allows a user interface plug-in to upgrade device option values that are stored in the registry. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |