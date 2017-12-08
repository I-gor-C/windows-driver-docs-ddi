---
UID: NS.printoem._OEMUIPSPARAM
title: OEMUIPSPARAM
author: windows-driver-content
description: The OEMUIPSPARAM structure is passed to a user interface plug-in's IPrintOemUI::DevicePropertySheets and IPrintOemUI::DocumentPropertySheets methods.
old-location: print\oemuipsparam.htm
old-project: print
ms.assetid: e7708b33-b032-41b9-84f9-6c5b38044f9c
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: OEMUIPSPARAM, OEMUIPSPARAM, *POEMUIPSPARAM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: printoem.h
req.include-header: Printoem.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OEMUIPSPARAM
req.alt-loc: printoem.h
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
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# OEMUIPSPARAM structure



## -description
<p>The OEMUIPSPARAM structure is passed to a user interface plug-in's <a href="print.iprintoemui_devicepropertysheets">IPrintOemUI::DevicePropertySheets</a> and <a href="print.iprintoemui_documentpropertysheets">IPrintOemUI::DocumentPropertySheets</a> methods.</p>


## -syntax

````
typedef struct _OEMUIPSPARAM {
  DWORD     cbSize;
  POEMUIOBJ poemuiobj;
  HANDLE    hPrinter;
  PWSTR     pPrinterName;
  HANDLE    hModule;
  HANDLE    hOEMHeap;
  PDEVMODE  pPublicDM;
  PVOID     pOEMDM;
  PVOID     pOEMUserData;
  DWORD     dwFlags;
  PVOID     pOemEntry;
} OEMUIPSPARAM, *POEMUIPSPARAM;
````


## -struct-fields
<dl>

### -field cbSize

<dd>
<p>Size of the OEMUIPSPARAM structure. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field poemuiobj

<dd>
<p>Not used.</p>
</dd>

### -field hPrinter

<dd>
<p>Handle to the printer. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field pPrinterName

<dd>
<p>String containing the printer name. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field hModule

<dd>
<p>Handle to the user interface plug-in. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field hOEMHeap

<dd>
<p>Handle to a heap from which space can be allocated by calling the Microsoft Windows SDK <b>HeapAlloc</b> function. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field pPublicDM

<dd>
<p></p>
<dl>

### -field For calls to IPrintOemUI::DocumentPropertySheets:

<dd>
<p>Caller-supplied pointer to the printer's public DEVMODEW structure.</p>
</dd>

### -field For calls to IPrintOemUI::DevicePropertySheets:

<dd>
<p>Not used.</p>
</dd>
</dl>
</dd>

### -field pOEMDM

<dd>
<p></p>
<dl>

### -field For calls to IPrintOemUI::DocumentPropertySheets:

<dd>
<p>Caller-supplied pointer to the user interface plug-in's private DEVMODEW members.</p>
</dd>

### -field For calls to IPrintOemUI::DevicePropertySheets:

<dd>
<p>Not used.</p>
</dd>
</dl>
</dd>

### -field pOEMUserData

<dd>
<p>Pointer, supplied by user interface plug-in, to a location containing private information. This pointer is returned to the plug-in's <a href="..\compstui\nc-compstui--cpsuicallback.md">_CPSUICALLBACK</a>-typed callback function when a property sheet item has changed.</p>
</dd>

### -field dwFlags

<dd>
<p></p>
<dl>

### -field For calls to IPrintOemUI::DocumentPropertySheets:

<dd>
<p>Contains the contents of the <b>fMode</b> member of the DOCUMENTPROPERTYHEADER structure received by the printer driver's <a href="..\winddiui\nf-winddiui-drvdocumentpropertysheets.md">DrvDocumentPropertySheets</a> function.</p>
</dd>

### -field For calls to IPrintOemUI::DevicePropertySheets:

<dd>
<p>Contains the contents of the <b>Flags</b> member of the DEVICEPROPERTYHEADER structure received by the printer driver's <a href="..\winddiui\nf-winddiui-drvdevicepropertysheets.md">DrvDevicePropertySheets</a> function.</p>
</dd>
</dl>
</dd>

### -field pOemEntry

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Printoem.h (include Printoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="print.iprintoemui_devicepropertysheets">IPrintOemUI::DevicePropertySheets</a>
</dt>
<dt>
<a href="print.iprintoemui_documentpropertysheets">IPrintOemUI::DocumentPropertySheets</a>
</dt>
<dt>
<a href="..\compstui\nc-compstui--cpsuicallback.md">_CPSUICALLBACK</a>
</dt>
<dt>
<a href="..\winddiui\nf-winddiui-drvdocumentpropertysheets.md">DrvDocumentPropertySheets</a>
</dt>
<dt>
<a href="..\winddiui\nf-winddiui-drvdevicepropertysheets.md">DrvDevicePropertySheets</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20OEMUIPSPARAM structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
