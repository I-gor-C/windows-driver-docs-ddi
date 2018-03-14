---
UID: NN:prcomoem.IPrintOemUni
title: IPrintOemUni
author: windows-driver-content
description: This section describes the methods defined for the IPrintOemUni COM interface.
old-location: print\iprintoemuni_interface.htm
old-project: print
ms.assetid: 097366a0-2ded-435c-9b63-2b736b716032
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintOemUni, IPrintOemUni interface [Print Devices], IPrintOemUni interface [Print Devices], described, prcomoem/IPrintOemUni, print.iprintoemuni_interface, print_unidrv-pscript_rendering_e715c57a-f4a8-4dde-894b-a19761ea0755.xml
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
-	IPrintOemUni
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintOemUni interface

This section describes the methods defined for the IPrintOemUni COM interface.

## Methods

<p>The <b>IPrintOemUni</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintOemUni::CommandCallback](nf-prcomoem-iprintoemuni-commandcallback.md) | The IPrintOemUni::CommandCallback method is used to provide dynamically generated printer commands for Unidrv-supported printers. |
| [IPrintOemUni::Compression](nf-prcomoem-iprintoemuni-compression.md) | The IPrintOemUni::Compression method can be used with Unidrv-supported printers to provide a customized bitmap compression method. |
| [IPrintOemUni::DevMode](nf-prcomoem-iprintoemuni-devmode.md) | The IPrintOemUni::DevMode method, provided by rendering plug-ins for Unidrv, performs operations on private DEVMODEW members. |
| [IPrintOemUni::DisableDriver](nf-prcomoem-iprintoemuni-disabledriver.md) | The IPrintOemuNI::DisableDriver method allows a rendering plug-in for Unidrv to free resources that were allocated by the plug-in's IPrintOemUni::EnableDriver method. |
| [IPrintOemUni::DisablePDEV](nf-prcomoem-iprintoemuni-disablepdev.md) | The IPrintOemUni::DisablePDEV method allows a rendering plug-in for Unidrv to delete the private PDEV structure that was allocated by its IPrintOemUni::EnablePDEV method. |
| [IPrintOemUni::DownloadCharGlyph](nf-prcomoem-iprintoemuni-downloadcharglyph.md) | The IPrintOemUni::DownloadCharGlyph method enables a rendering plug-in for Unidrv to send a character glyph for a specified soft font to the printer. |
| [IPrintOemUni::DownloadFontHeader](nf-prcomoem-iprintoemuni-downloadfontheader.md) | The IPrintOemUni::DownloadFontHeader method allows a rendering plug-in for Unidrv to send a font's header information to a printer. |
| [IPrintOemUni::DriverDMS](nf-prcomoem-iprintoemuni-driverdms.md) | The IPrintOemUni::DriverDMS method allows a rendering plug-in for Unidrv to indicate that it uses a device-managed drawing surface. |
| [IPrintOemUni::EnableDriver](nf-prcomoem-iprintoemuni-enabledriver.md) | The IPrintOemUni::EnableDriver method allows a rendering plug-in for Unidrv to hook out some graphics DDI functions. |
| [IPrintOemUni::EnablePDEV](nf-prcomoem-iprintoemuni-enablepdev.md) | The IPrintOemUni::EnablePDEV method allows a rendering plug-in for Unidrv to create its own PDEV structure. |
| [IPrintOemUni::FilterGraphics](nf-prcomoem-iprintoemuni-filtergraphics.md) | The IPrintOemUni::FilterGraphics method can be used with Unidrv-supported printers to modify scan line data and send it to the spooler. |
| [IPrintOemUni::GetImplementedMethod](nf-prcomoem-iprintoemuni-getimplementedmethod.md) | The IPrintOemUni::GetImplementedMethod method is used by Unidrv to determine which IPrintOemUni interface methods a rendering plug-in has implemented. |
| [IPrintOemUni::GetInfo](nf-prcomoem-iprintoemuni-getinfo.md) | A rendering plug-in's IPrintOemUni::GetInfo method returns identification information. |
| [IPrintOemUni::HalftonePattern](nf-prcomoem-iprintoemuni-halftonepattern.md) | The IPrintOemUni::HalftonePattern method can be used with Unidrv-supported printers to create or modify a halftone pattern before it is used in a halftoning operation. |
| [IPrintOemUni::ImageProcessing](nf-prcomoem-iprintoemuni-imageprocessing.md) | The IPrintOemUni::ImageProcessing method can be used with Unidrv-supported printers to modify image bitmap data, in order to perform color formatting or halftoning. |
| [IPrintOemUni::MemoryUsage](nf-prcomoem-iprintoemuni-memoryusage.md) | The IPrintOemUni::MemoryUsage method can be used with Unidrv-supported printers to specify the amount of memory required for use by a rendering plug-in's IPrintOemUni::ImageProcessing method. |
| [IPrintOemUni::OutputCharStr](nf-prcomoem-iprintoemuni-outputcharstr.md) | The IPrintOemUni::OutputCharStr method enables a rendering plug-in to control the printing of font glyphs. |
| [IPrintOemUni::PublishDriverInterface](nf-prcomoem-iprintoemuni-publishdriverinterface.md) | The IPrintOemUni::PublishDriverInterface method allows a rendering plug-in for Unidrv to obtain the Unidrv driver's IPrintOemDriverUni or IPrintCoreHelperUni interface. |
| [IPrintOemUni::ResetPDEV](nf-prcomoem-iprintoemuni-resetpdev.md) | The IPrintOemUni::ResetPDEV method allows a rendering plug-in for Unidrv to reset its PDEV structure. |
| [IPrintOemUni::SendFontCmd](nf-prcomoem-iprintoemuni-sendfontcmd.md) | The IPrintOemUni::SendFontCmd method enables a rendering plug-in to modify a printer's font selection command and then send it to the printer. |
| [IPrintOemUni::TextOutAsBitmap](nf-prcomoem-iprintoemuni-textoutasbitmap.md) | The IPrintOemUni::TextOutAsBitmap method allows a rendering plug-in to create a bitmap image of a text string, in case a downloadable font is not available. |
| [IPrintOemUni::TTDownloadMethod](nf-prcomoem-iprintoemuni-ttdownloadmethod.md) | The IPrintOemUni::TTDownloadMethod method enables a rendering plug-in to indicate the format that Unidrv should use for a specified TrueType soft font. |
| [IPrintOemUni::TTYGetInfo](nf-prcomoem-iprintoemuni-ttygetinfo.md) | The IPrintOemUni::TTYGetInfo method enables a rendering plug-in to supply Unidrv with information relevant to text-only printers. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |